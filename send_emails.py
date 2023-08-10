"""
Main script used to send emails. Allows user to specify the attachment suffix, email suffix, and maximum image size. The contents of the email are specified in the config.py file.

For more information on script parameter run: python3 send_emails.py --help. An example of running the script is: 

python3 send_emails.py --attachment_suffix png jpg --email_suffix txt --max_image_size 1024
"""

# Arguments to specify the attachment and email suffix, as well as the maximum image size
from utils import get_gmail_service, create_message, message2bytes, press_Yn_to_continue, process_email_list
from config import txt_message, txt_message2, gmail_address, subject_line, scopes, credenciales, port, max_emails
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

    # -- (iii) Get the list of emails -- #
    emails = process_email_list(folder='emails'
                                # , file_suffix=args.email_suffix
                                )
    emails.sort()
    print('The following emails will be reached:\n')
    print('\n'.join(emails))
    print('\n')

    email_user_mapping = {
        "28877": "obtomb@gmail.com",
        "79": "info@adigoldstein.com",
        "8": "asher@asherbitansky.com",
        "39553": "alejandro@cdirecords.com",
        "92490": "adamofficialmusic@outlook.dk",
        "66031": "yehezkel.raz@gmail.com",
        "126905": "wesleycarter86@gmail.com.sd",
        "126877": "label-pub-ops@artlist.io",
        "127198": "gt@greggterrence.com",
        "141686": "yuel@ellatv.co.uk",
        "141017": "info@luzonic.net",
        "134365": "julian@immrecords.com",
        "144639": "contact@dibsteur.com",
        "142804": "keakong1225@gmail.com",
        "142507": "alex.kumar@familyinmusic.com",
        "142395": "info@nxzsound.com ",
        "145439": "burak@coverz.com",
        "222115": "shantelbankonit@gmail.com",
        "283693": "payments@luzonic.net",
        "283159": "carlos@unitesync.com",
        "282821": "claudiopairot@puntilla.us",
        "285597": "finance@session-42.com",
        "284397": "payam.shams@tunepays.com",
        "288647": "brunkowrecordingfactory@bluewin.ch",
        "289229": "service@tdmusic.cn",
        "290004": "allenwang@sparklingrecreation.com",
        "289337": "copyright@kamirecords.co",
        "299070": "network@alkabits.com.br",
        "297796": "yen@indiehay.com",
        "297148": "mathias@highvibesdistribution.com",
        "302247": "julius.grimm@yourv.id",
        "301300": "marcodreamz@gmail.com",
        "300410": "todor@unleashlab.com",
        "305759": "sid@dropzik.com",
        "304822": "yonnyf@mentamusic.com",
        "303709": "alicia@acemusica.com",
        "311690": "support@redstar.media",
        "310198": "music.admin@soundstripe.com",
        "309079": "manager@vexdistroportal.com",
        "313641": "admin@daomusic.vn",
        "321531": "nickpacay@gmail.com",
        "320759": "levani.javakhadze@kingsmen.group",
        "320034": "support@majesticdistributions.com",
        "323214": "dw.lamusic@gmail.com",
        "322719": "info@g30music.com",
        "322260": "contact@fivesound.es",
        "327572": "info@tupartner.co",
        "324855": "info@brilliantmusic.net",
        "324562": "adam@carpentercreate.com",
        "329158": "mersel@nextfly.me",
        "329156": "info@musicbusinessartists.com",
        "328657": "audiotunemediagroup@gmail.com",
        "330804": "karan@bull18.com",
        "330498": "skmusic@aol.com",
        "329161": "accadm@strm.com.br ",
        "332591": "go@0to8.us",
        "331942": "flavaceo@gmail.com",
        "331675": "m4apublishing@gmail.com",
        "333084": "admin@bitaran.digital ",
        "332935": "christaylorbrown@icloud.com",
        "339227": "soura.bd@gmail.com",
        "338653": "omer@indieflow.me",
        "336086": "content@vibeable.io",
        "339231": "noud-roemer@wearemarqeters.com",
        "344773": "info@sharplinemusicgroup.com",
        "341580": "Philipp Börsig",
        "339631": "analytics@calientalomedia.com",
        "345817": "avish@avidz.co",
        "345588": "distros.music@gmail.com",
        "345031": "arman2musicgroup@gmail.com",
        "347444": "smaung@contentgateway.org",
        "346841": "info@apprisemusic.com",
        "346588": "info@1337battle.com",
        "348746": "dan@putumayodigital.com",
        "348249": "CEO@TLMUSICENT.COM",
        "359638": "wldyck01@163.com",
        "350172": "criativaproducoesartisticas@gmail.com",
        "349146": "cosminanton@manelementolate.com",
        "366869": "contact@oceandistribution.tech",
        "366141": "kobzx2z.perso@gmail.com",
        "365918": "rory@hitpiece.com",
        "370633": "integralsilence.pvt.ltd@gmail.com",
        "369884": "guillaume@parabelrecords.com",
        "369718": "diz.mgmt@hotmail.com",
        "373759": "starmakersdistribution@gmail.com",
    }

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

                message = create_message(message=txt_message2, email_from=gmail_address, email_to=gmail_address, subject=subject_line,
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
