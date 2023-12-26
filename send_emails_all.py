"""
Main script used to send emails to all customer available in the output folder. Allows user to specify the attachment suffix, email suffix, and maximum image size. The contents of the email are specified in the config.py file.

For more information on script parameter run: python3 send_emails.py --help. An example of running the script is: 

python3 send_emails.py --attachment_suffix png jpg --email_suffix txt --max_image_size 1024
"""

# Arguments to specify the attachment and email suffix, as well as the maximum image size
from utils import get_gmail_service, create_message2, message2bytes, press_Yn_to_continue
from config import txt_message_below, gmail_address, subject_line_below, scopes, credenciales, port, max_emails
from time import sleep

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


import os.path
import csv

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--folder_attachments', type=str,
                    help='Folder name of the attachments to send')
# parser.add_argument('--email_suffix', nargs='+', default='txt',
#                     help='Suffix of the email to send (default: "txt")')
parser.add_argument('--max_image_size', type=int, default=1024,
                    help='Maximum size of the image to send')
parser.add_argument("--csv_file_path", type=str,
                    help="Path to the CSV file containing email-identifier mapping.")
args = parser.parse_args()

# External libraries
# Internal config and utility files

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credenciales available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credenciales.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credenciales for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        # Call the Gmail API
        service = build('gmail', 'v1', credentials=creds)
        results = service.users().labels().list(userId='me').execute()
        labels = results.get('labels', [])

        if not labels:
            print('No labels found.')
            return
        print('Labels:')
        for label in labels:
            print(label['name'])

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'An error occurred: {error}')


if __name__ == '__main__':
    # -- (i) Set up the service connection -- #
    # Note, this will open a browser window to authenticate
    service = get_gmail_service(
        scopes=scopes, credentials=credenciales, port=port)

    email_user_mapping2 = {}
    # Force the user to confirm they would like to continue after
    press_Yn_to_continue()

    # -- (iv) Loop over each recipient, and send message -- #
    # for i, email in enumerate(emails):
    with open(args.csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for i, row in enumerate(csv_reader):
            # identifier = ""
            # email = ""
            if len(row) == 2:
                identifier, email = row
                print(f'Identifier is {identifier}')
                print(f'Email is {email}')
                email_user_mapping2[identifier] = email
                # -- (ii) Create the message -- #

                message = create_message2(message=txt_message_below, email_from=gmail_address, email_to=gmail_address, subject=subject_line_below,
                folder_attachments=args.folder_attachments, attachment_suffix=identifier, max_image_size=args.max_image_size)
                # Update the recipient email
                del message['To']
                message['To'] = {email}
                print(f'Sending to {email}')
                print(f'Sending attachment number {identifier}')
                # Convert the message to a raw byte
                raw_message = message2bytes(message)
                # Send the message
                send_message = (service.users().messages().send(
                    userId="me", body=raw_message).execute())
                if not 'SENT' in send_message['labelIds']:
                    print(f'Email not sent to {email}')
                if (i+1) % max_emails == 0:
                    print(f'Pausing for 1 minute after sending {i+1} emails')
                    sleep(60)

    print('~~~ End of send_emails.py ~~~')