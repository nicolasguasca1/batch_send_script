import os
import csv
import argparse
from time import sleep
from utils import create_message3, get_gmail_service, create_message2, message2bytes, press_Yn_to_continue
from config import gmail_address, subject_line_all, scopes, credenciales, port, max_emails, txt_violative_content, subject_line_VIOLATIVE
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def main():
    parser = argparse.ArgumentParser(description="Send generated CSV files to corresponding emails.")
    parser.add_argument("--source_folder", type=str, required=True,
                        help="Folder containing the CSV files generated for each Tenant ID.")
    parser.add_argument("--email_mapping_path", type=str, required=True,
                        help="Path to the CSV file containing Tenant ID and email mapping.")
    parser.add_argument("--max_image_size", type=int, default=1024,
                        help="Maximum size of the image to send.")
    args = parser.parse_args()

    if not os.path.exists(args.source_folder):
        print(f"Directory {args.source_folder} does not exist.")

    if os.access(args.source_folder, os.W_OK):
        print(f"Directory '{args.source_folder}' has write permission.")
    else:
        print(f"Directory '{args.source_folder}' does not have write permission.")


    # -- (i) Set up the service connection -- #
    # Note, this will open a browser window to authenticate
    service = get_gmail_service(
        scopes=scopes, credentials=credenciales, port=port)

    email_user_mapping = {}
    
    # Force the user to confirm they would like to continue after seeing the details
    press_Yn_to_continue()

    # Read the mapping from Tenant ID to email
    with open(args.email_mapping_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if len(row) == 2:
                tenant_id, email = row
                email_user_mapping[tenant_id] = email

    # Loop through each Tenant ID and send the corresponding CSV file
    for tenant_id, email in email_user_mapping.items():
        path_to_send = os.path.join(args.source_folder, f"{tenant_id}.csv")
        file_to_send = os.path.join(f"{tenant_id}.csv")
        
        if os.path.exists(path_to_send):
            print(f"Sending {file_to_send} to {email}...")
            
            # # Create the message
            # message = create_message2(
            #     message=txt_violative_content, 
            #     email_from=gmail_address, 
            #     email_to=email, 
            #     subject=subject_line_all,
            #     folder_attachments=args.source_folder, 
            #     attachment_suffix=tenant_id, 
            #     max_image_size=args.max_image_size
            # )

            message = create_message3(
                message=txt_violative_content,
                email_from=gmail_address,
                email_to=email,
                subject=subject_line_VIOLATIVE,
                folder_attachments=args.source_folder, 
                attachment_suffix=file_to_send
        )
            
            # Convert the message to a raw byte
            raw_message = message2bytes(message)
            
            # Send the message
            try:
                send_message = (service.users().messages().send(
                    userId="me", body=raw_message).execute())
                if 'SENT' in send_message.get('labelIds', []):
                    print(f"Email sent successfully to {email}")
                else:
                    print(f"Failed to send email to {email}")
            except HttpError as error:
                print(f'An error occurred while sending email to {email}: {error}')
            
            # Pause if the number of sent emails hits the maximum limit before continuing
            if (list(email_user_mapping.keys()).index(tenant_id) + 1) % max_emails == 0:
                print(f"Pausing for 1 minute after sending {max_emails} emails")
                sleep(60)
        else:
            print(f"No file found for Tenant ID {tenant_id} to send to {email}")

    print('~~~ End of CSV sending script ~~~')

if __name__ == '__main__':
    main()
