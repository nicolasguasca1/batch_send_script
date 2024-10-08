"""
Utility scripts for sending emails and other tasks
"""

# External modules
import array
import mimetypes
import os
import sys
import io
# import cv2
# import numpy as np
import pandas as pd
import email.message
import googleapiclient.discovery


import os
import shutil
import tempfile
import zipfile


from base64 import urlsafe_b64encode
from email.message import EmailMessage
from google_auth_oauthlib.flow import InstalledAppFlow
from typing import List, Optional



def get_gmail_service(scopes: str or list, credentials: str, port: int = 0) -> googleapiclient.discovery:
    """
    Using the googleapiclient.discovery.build method to get a service connection to the gmail API

    Parameters
    ----------
    credentials : str
        Path to the credenciales.json file
    port : int, optional
        Port to use for the local server, by default 0

    Returns
    -------
    googleapiclient.discovery
        Service connection to the gmail API
    """
    # Input checks
    scopes = str2list(scopes)
    assert isinstance(
        scopes, list), f"Scopes should be a list, not {type(scopes)}"
    assert os.path.exists(
        credentials), f"credenciales file {credentials} does not exist"
    # Use the local and secret
    flow = InstalledAppFlow.from_client_secrets_file(
        client_secrets_file=credentials, scopes=scopes)
    creds = flow.run_local_server(port=port)
    service = googleapiclient.discovery.build('gmail', 'v1', credentials=creds)
    return service


def get_email_from_(identifier, folder_path):
    for filename in os.listdir(folder_path):
        file_identifier = os.path.splitext(filename)[0]
        if file_identifier == identifier:
            with open(os.path.join(folder_path, filename), 'r') as file:
                email = file.read().strip()
                return email
    return None  # Identifier not found


def create_message(message: str, email_from: str, email_to: str, subject: str, max_image_size: int = 1024) -> email.message:
    """
    Use the email.message.EmailMessage class to create a message and return its raw base64 encoded version in a dictionary

    Parameters
    ----------
    message : str
        Message to send
    email_from : str
        Email address to send from
    email_to : str
        Email address to send to
    subject : str
        Subject line
    folder_attachments : str
        Path to the folder containing the attachments
    attachment_suffix : str or list
        Suffix of the attachment to send

    Returns
    -------
    dict
        Dictionary with the raw base64 encoded message
    """
    # Input checks
    assert isinstance(
        message, str), f"Message should be a string, not {type(message)}"
    assert isinstance(
        email_from, str), f"Email_from should be a string, not {type(email_from)}"
    assert isinstance(
        email_to, str), f"Email_to should be a string, not {type(email_to)}"
    assert isinstance(
        subject, str), f"Subject should be a string, not {type(subject)}"
    msg = EmailMessage()
    msg.set_content(message, subtype='html')
    msg['To'] = email_to
    msg['From'] = 'Nicolás Guasca'
    msg['Subject'] = subject
    # msg['Cc'] = 'naomi@revelator.com'
    # msg['Cc'] = 'nicolas.guasca@gmail.com', 'nicolas.g@revelator.com'
    # msg['Bcc'] = '420184@bcc.hubspot.com'
    temp_dir = tempfile.mkdtemp()
    # Clean up the temporary directory
    shutil.rmtree(temp_dir)
    return msg

def create_message2(message: str, email_from: str, email_to: str, subject: str, folder_attachments: str, attachment_suffix: str or list, max_image_size: int = 1024) -> email.message:
    """
    Use the email.message.EmailMessage class to create a message and return its raw base64 encoded version in a dictionary

    Parameters
    ----------
    message : str
        Message to send
    email_from : str
        Email address to send from
    email_to : str
        Email address to send to
    subject : str
        Subject line
    folder_attachments : str
        Path to the folder containing the attachments
    attachment_suffix : str or list
        Suffix of the attachment to send

    Returns
    -------
    dict
        Dictionary with the raw base64 encoded message
    """
    # Input checks
    assert isinstance(
        message, str), f"Message should be a string, not {type(message)}"
    assert isinstance(
        email_from, str), f"Email_from should be a string, not {type(email_from)}"
    assert isinstance(
        email_to, str), f"Email_to should be a string, not {type(email_to)}"
    assert isinstance(
        subject, str), f"Subject should be a string, not {type(subject)}"
    assert os.path.exists(
        folder_attachments), f"Folder {folder_attachments} does not exist"
    # attachment_suffix = str2list(attachment_suffix)
    # assert isinstance(
    #     attachment_suffix, list), f"Attachment_suffix should be a list, not {type(attachment_suffix)}"
    # Create the message
    msg = EmailMessage()
    msg.set_content(message, subtype='html')
    msg['To'] = email_to
    msg['From'] = 'Nicolás Guasca'
    msg['Subject'] = subject
    # msg['Cc'] = 'nicolas.guasca@gmail.com', 'nicolas.g@revelator.com'
    msg['Bcc'] = ['420184@bcc.hubspot.com']

    # _____________________________________________________________________________

    # # Find the folders
    # folders = find_files_with_suffix(folder_attachments, attachment_suffix)
    # print(f"Found {len(folders)} folders with suffix {attachment_suffix} in folder {folder_attachments}: {folders}")

    # Create a temporary directory to store the zip files
    temp_dir = tempfile.mkdtemp()

    # Add the attachments
    # for folder in folders:
    folder_name = folder_attachments+'/'+attachment_suffix
    # folder_name = attachment_suffix
    zip_path = os.path.join(temp_dir, f"{folder_name}.zip")

    # Check directory permissions
    permissions = os.access(folder_name, os.W_OK)
    print(f"Directory '{folder_name}' has write permission: {permissions}")

    with io.BytesIO() as zip_buffer:
        with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
            for file in os.listdir(folder_name):
                if file.endswith(".csv"):
                    file_path = os.path.join(folder_name, file)
                    relative_path = os.path.relpath(file_path, folder_name)
                    zip_file.write(file_path, arcname=relative_path)

        # Get the bytes of the zip file
        zip_data = zip_buffer.getvalue()
    # MOMENTANOUESLY

    # Add the attachment to the email
    msg.add_attachment(zip_data, maintype='application',
                       subtype='zip', filename=f"{attachment_suffix}.zip")

    # Clean up the temporary directory
    shutil.rmtree(temp_dir)
    return msg

def create_message3(message: str, email_from: str, email_to: str, subject: str, folder_attachments: str, attachment_suffix: str, max_image_size: int = 1024) -> EmailMessage:
    """
    Use the EmailMessage class to create a message and return it.

    Parameters
    ----------
    message : str
        Message to send.
    email_from : str
        Email address to send from.
    email_to : str
        Email address to send to.
    subject : str
        Subject line.
    folder_attachments : str
        Path to the folder containing the attachments.
    attachment_suffix : str
        Name or identifier of the specific attachment to send.
    max_image_size : int
        Maximum size of the image to send (not used in this implementation).

    Returns
    -------
    EmailMessage
        The constructed email message with the attachment.
    """
    # Input checks
    assert isinstance(message, str), f"Message should be a string, not {type(message)}"
    assert isinstance(email_from, str), f"Email_from should be a string, not {type(email_from)}"
    assert isinstance(email_to, str), f"Email_to should be a string, not {type(email_to)}"
    assert isinstance(subject, str), f"Subject should be a string, not {type(subject)}"
    assert os.path.exists(folder_attachments), f"Folder {folder_attachments} does not exist"

    # Create the email message
    msg = EmailMessage()
    msg.set_content(message, subtype='html')
    msg['To'] = email_to
    msg['From'] = email_from
    msg['Subject'] = subject
    msg['Bcc'] = ['420184@bcc.hubspot.com','infringement@revelator.com']

    # Construct the full path to the attachment
    file_to_send = os.path.join(folder_attachments, attachment_suffix)

    # Ensure the file exists
    if not os.path.isfile(file_to_send):
        raise FileNotFoundError(f"No such file: '{file_to_send}'")

    # Determine the content type based on the file's extension
    ctype, encoding = mimetypes.guess_type(file_to_send)
    if ctype is None or encoding is not None:
        ctype = 'application/octet-stream'
    maintype, subtype = ctype.split('/', 1)

    # Add the file as an attachment to the email
    with open(file_to_send, 'rb') as fp:
        msg.add_attachment(fp.read(), maintype='application', subtype=subtype, filename=os.path.basename(file_to_send))

    return msg

def message2bytes(msg) -> dict:
    # Encode the message and save it in a dictionary
    encoded_msg = urlsafe_b64encode(msg.as_bytes()).decode()
    di_msg = {'raw': encoded_msg}
    return di_msg


def find_files_with_identifier(directory: str, identifier: str) -> Optional[str]:
    """
    Find files within a directory that match a specific identifier.

    Parameters
    ----------
    directory : str
        Path to the directory containing the files
    identifier : str
        Identifier to match in the file names

    Returns
    -------
    List[str]
        List of file names that match the identifier
    """
    matching_files = [file for file in os.listdir(directory) if file.endswith('.csv') and identifier == file.split('-')[0]]

    if matching_files:
        return matching_files[0]
    else:
        print(f"No CSV file found with identifier '{identifier}'.")
        return None

def find_files_with_suffix(folder: str, suffix: str or list) -> list:
    """
    Search a folder for all files with a certain suffix

    Parameters
    ----------
    folder : str
        Path to the folder to search
    suffix : str or list, optional
        Suffix of the files to search for, by default 'txt'

    Returns
    -------
    pd.Series
        Series of all files with the correct suffix in the folder

    Example
    -------
    >>> find_files_with_suffix('data','txt')
    0    file1.txt
    1    file2.txt
    dtype: object
    """
    # Input checks
    assert os.path.exists(folder), f"Folder {folder} does not exist"
    # suffix = str2list(suffix)
    # Find all files in the folder
    files = pd.Series(os.listdir(folder))
    file_suffixes = files.str.split('.', regex=False).apply(
        lambda x: x[-1], 1).to_list()
    # Find all files with the correct suffix
    idx_suffix = [file_suffix in suffix for file_suffix in file_suffixes]
    files_suffix = files[idx_suffix].to_list()
    return files_suffix
# Find all files in the folder
    # files = os.listdir(folder)

    return files


def str2list(string: str or list):
    """
    Check if a string is a list, if not, make it a list

    Parameters
    ----------
    string : str or list
        String to check

    Returns
    -------
    list
        List of the string
    """
    if isinstance(string, str):
        return [string]
    else:
        return string


def extract_values(tuple_set: array):
    values = []
    for tuple_item in tuple_set:
        values.append(tuple_item[0])
    return values


def press_Yn_to_continue():
    """
    Force the user to press Y to continue, n to break, or repeat options
    """
    inp = input('Press Y to continue, or n to break\n')
    print('You pressed', inp)
    while (inp != 'Y') and (inp != 'n'):        # Loop until it is a blank line
        print('You did not press Y or n, try again')
        inp = input()
        print('You pressed', inp)
    if inp == 'n':
        sys.exit('You pressed n, breaking')


def is_file_image(path: str) -> bool:
    """Check whether a file is an image"""
    # Input checks
    assert os.path.exists(path), f"{path} does not exist"
    check = path.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))
    return check


# def image2bytes(path: str, max_size: int = 1024) -> bytes:
#     """
#     Convert an image to bytes

#     Parameters
#     ----------
#     path : str
#         Path to the image
#     max_size : int, optional
#         Maximum size of the image, by default 1024

#     Returns
#     -------
#     bytes
#         Bytes of the image
#     """
#     # Check the image exists
#     assert os.path.exists(path), f"{path} does not exist"
#     # Check the image is an image
#     assert is_file_image(path), f"{path} is not an image"
#     # Read the image
#     img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
#     # Resize the image if it exceeds the maximum size
#     dim_max = np.argmax(img.shape[:2])
#     pixels_max = img.shape[dim_max]
#     if pixels_max > max_size:
#         scale = max_size / pixels_max
#         img = cv2.resize(img, None, fx=scale, fy=scale)
#     # Convert to bytes
#     suffix = path.split('.')[-1]
#     raw = cv2.imencode(f'.{suffix}', img)[1].tobytes()
#     assert isinstance(raw, bytes), f"Data should be bytes, not {type(raw)}"
#     return raw
