"""
Adjust the contents of the message and other parameters used by the API
"""

import os

# Set up the email message
txt_message = """[YOUR MESSAGE HERE]"""

# gmail address
gmail_address = '[YOUR GMAIL]@gmail.com'

# Subject line
subject_line = '[SUBJECT LINE]'


# The gmail API can be used to send emails
scopes = ['https://www.googleapis.com/auth/gmail.send']

# Path to the credentials file
credentials = 'credentials.json'
# Check that the credentials file exists
assert os.path.exists(credentials), f"Credentials file {credentials} does not exist"

# Port 
port = 0

# Maximum number of emails to send before pause (see https://developers.google.com/gmail/api/reference/quota)
max_emails = 100