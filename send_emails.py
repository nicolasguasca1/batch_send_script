"""
Main script used to send emails. Allows user to specify the attachment suffix, email suffix, and maximum image size. The contents of the email are specified in the config.py file.

For more information on script parameter run: python3 send_emails.py --help. An example of running the script is: 

python3 send_emails.py --attachment_suffix png jpg --email_suffix txt --max_image_size 1024
"""

# Arguments to specify the attachment and email suffix, as well as the maximum image size
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--attachment_suffix', nargs='+', default=['png','jpg'], help='Suffix of the attachment to send (default: ["png", "jpg"])')
parser.add_argument('--email_suffix', nargs='+', default='txt', help='Suffix of the email to send (default: "txt")')
parser.add_argument('--max_image_size', type=int, default=1024, help='Maximum size of the image to send')
args = parser.parse_args()

# External libraries
import numpy as np
from time import sleep
# Internal config and utility files
from config import txt_message, gmail_address, subject_line, scopes, credentials, port, max_emails
from utils import get_gmail_service, create_message, message2bytes, press_Yn_to_continue, process_email_list

if __name__ == '__main__':
    # -- (i) Set up the service connection -- #
    # Note, this will open a browser window to authenticate
    service = get_gmail_service(scopes=scopes, credentials=credentials, port=port)

    # -- (ii) Create the message -- #
    message = create_message(message=txt_message, email_from=gmail_address, email_to=gmail_address, subject=subject_line, folder_attachents='attachments', attachment_suffix=args.attachment_suffix, max_image_size=args.max_image_size)

    # -- (iii) Get the list of emails -- # 
    emails = process_email_list(folder='emails', file_suffix=args.email_suffix)
    emails.sort()
    print('The following emails will sent:\n')
    print('\n'.join(emails))
    print('\n')
    
    # Force the user to confirm they would like to continue after
    press_Yn_to_continue()

    # -- (iv) Loop over each recipient, and send message -- #
    for i, email in enumerate(emails):
        # Update the recipient email
        del message['To']
        message['To'] = email
        # Convert the message to a raw byte
        raw_message = message2bytes(message)
        # Send the message
        send_message = (service.users().messages().send(userId="me", body=raw_message).execute())
        if not 'SENT' in send_message['labelIds']:
            print(f'Email not sent to {email}')
        if (i+1) % max_emails == 0:
            print(f'Pausing for 1 second after sending {i+1} emails')
            sleep(1)
    
    print('~~~ End of send_emails.py ~~~')
