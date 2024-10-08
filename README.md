-> SCROLL TO THE BOTTOM FOR CUSTOM INSTRUCTIONS:

# Send emails with the Gmail API for python

This repo provides a one-line python functionality to send the same email to a list of recipients using the [Gmail API](https://developers.google.com/gmail/api/guides). This readme provides step-by-step instructions on how to configure the files in this repo so that the email message is tailored to your needs.

This repo was tested on Mac Venture 13.1 (22C65) and Python 3.10.8.

There are four files in this repo that will need to be updated by the user:

- `credenciales.json` (see (1))
- `config.py` (see (3))
- `emails/example1.txt` (see (4))
- `attachments/` (see (5))

The ones found in this repo are meant for demonstrative purposes only. An example of the structure of this repo is shown below, when there are two attachments files (file1.png, file2.jpg) and two email lists (list1.txt, list2.txt):

```
├── .gitignore
├── README.md
├── attachments
│   ├── file1.png
│   ├── file2.jpg
│   └── readme.md
├── config.py
├── credenciales.json
├── emails
│   ├── list1.txt
│   ├── list2.txt
│   └── readme.md
├── environment.yml
├── send_emails.py
└── utils.py
```

To ensure you don't commit any private changes to your branch, you'll probably want to stop tracking the template files:

```
git update-index --skip-worktree credenciales.json
git update-index --skip-worktree config.py
git update-index --skip-worktree attachments/file1.png
git update-index --skip-worktree attachments/file2.jpg
git update-index --skip-worktree emails/list1.txt
git update-index --skip-worktree emails/list2.txt
```

<br>

## (1) Configuring the gmail API

For a step-by-step guide on how to set up the gmail API see [this post](https://bioeconometrician.github.io/gmail_api/).

<br>

## (2) Setting up conda environment

The python scripts in this repo call in packages that may not be installed on your environment. If you don't conda installed on your machine, [do so first](https://docs.conda.io/en/latest/miniconda.html), and then set up an environment that has been tested to work with this repo: `conda env create --file environment.yml`.

If the environment build doens't work (I find this often happens for different OS, particularly windows), you can manually re-create it yourself:

1. `conda create -n gmailAPI python=3.10`
2. `conda activate gmailAPI`
3. `conda install -c conda-forge numpy pandas opencv google-auth-oauthlib google-api-python-client`

<br>

## (3) Setting up the email parameters

The contents of the email and subject line are controlled by the `config.py` script. The config script found in this repo contains empty strings so that different users/clones can have different set-ups.

1. `txt_message`: Put your main message here.
2. `gmail_address`: Put your gmail address here.
3. `subject_line`: Put your subject line here.
4. There are four other parameters: `scopes`, `credenciales`, `port`, and `max_emails`, but only adjust these if you know what you are doing.

<br>

## (4) Set up email list

Users can add email lists in an unstructured format to the `emails` folder. For example, an `emails/emails1.txt` may look like:

```
jack@hotmail.com;    jazz@outlook.com

jim@gmail.com
```

Any spaces, semi-colons, or line-breaks will treated a possible separators. Angle brackets will be removed as well. For example `John Doe <john.doe@email.com>` will just become `john.doe@email.com`. For a "valid" email to be considered, it must contain an ampersand. Users can add as many \*.txt files to this folder, and all emails will combined for the final list (e.g. emails/emails2.txt, ..., emails/moreemails.txt).

Remove the toy list1.txt and list2.txt files before sending your email.

<br>

## (5) Set up attachments (if any)

Users can also include attachments in the email by dropping files in the `attachments` folder. If the attachment is an email, the maximum image size rule will kick in upon upload (see below). For example, of file1.png is a 1500x2000 image, and there is a max_image_size=1000, when the email will be shrunken by 50%.

Remove the toy file1.png and file2.jpg files before sending your email.

<br>

## (6) Send emails

After the `config.py` has been set up, email lists have been added to the `emails/*.txt` folder, and attachments (optional) have been added to the `attachment/*` folder, the main script can be run. An example of the script call can be found below. When running this from the user command line, a broswer window should open for authentication to give the app access to send emails from your gmail account. If it doesn't happen automatically, you can copy the link that will be printed to the console. Additionally, after the email list is printed out, users will need to confirm they want to go ahead with sending the email by typing "Y" into the console when prompted. If you type "n" the script will exit and no emails will send. If you type in anything else, you will be re-prompted to type in either "Y" or "n".

<!-- CUSTOM INSTRUCTIONS -->

<!-- LEGACY INFO -->

NOTE:If the interpreter you are using is 3.10 and .zshrc for shell profile use:
`python send_simple_template_email.py --csv_file_path possible_delays_sep_2023_royalty_run_to_export.csv`

9. Make a copy of the logged activity after running the script and save it under Logs folder with the convention existing already

<!-- STEP BY STEP TO SEND THE EMAILS WITH FILES TO CUSTOMERS -->

1. Process the files to obtain information about assets above/below the 1k threshold (10k for Tiktok) as well as breakdown of clients with the most AS Streams.

--> Paste the folder containing the AS Reports into this repository and run the command `python dataframe_cell.py --folder_to_filter [ABS_PATH_TO_THE_FOLDER]`

2. After the config.py has been set up, email lists have been added to the emails/_.txt folder, and attachments (optional) have been added to the attachment/_ folder, the main script can be run. An example of the script call can be found below. When running this from the user command line, a browser window should open for authentication to give the app access to send emails from your gmail account. If it doesn't happen automatically, you can copy the link that will be printed to the console. Additionally, after the email list is printed out, users will need to confirm they want to go ahead with sending the email by typing "Y" into the console when prompted. If you type "n" the script will exit and no emails will send. If you type in anything else, you will be re-prompted to type in either "Y" or "n".

-> Make sure the amount below and above match the number of folders analyzed in total

3. There will be a document created called 'enterprises_analyzed.txt' with the EntIds of the companies we need to contact. You can choose to select those or copy directories_above_1000.txt/below_1000.txt to populate a google sheet with the email addresses you will send to based on the report that uses the EntID of the company. Use the instructions available on the example sheet on the most recent doc from this folder: https://drive.google.com/drive/folders/11vDTkFzpenaQTOrcAk4zfmol8CKu-iMH

4. Follow the instruction in order to get a file like To_Export_All.csv to trigger the script.

5. Remove the additional commas and the first line on each csv so the script grabs the emails accurately

6. Change the contents of the text to send as message as well as the recipients in CC and subject and make sure it is being used by the script used (send_emails_violative_content_by_file.py the latest)

7. Make a test sending an above and a below email to two different sample email addresses to see the attachments went well

-> Run the script with:

<!-- LEGACY COMMANDS: -->

`python3 send_emails_above.py --folder_attachments <ABS_PATH_TO_THE_FOLDER> --csv_file_path To_Export_ABOVE.csv`

`python3 send_emails_below.py --folder_attachments <ABS_PATH_TO_THE_FOLDER> --csv_file_path To_Export_BELOW.csv`

<!-- Latest script ran: -->

`python send_emails_AS_by_folder.py --folder_attachments /Users/nicolasguascasantamaria/Desktop/RevAPIS/extRepo/gmailAPI/attachments/march_27th_processing  --csv_file_path To_Export_All.csv`

->It sends a folder with both Spotify + Tiktok reports and two files with the rows above 1k for Spo and rows above 10k for tiktok. It was sent to the customer and Support.

Make a copy of the logged activity after running the script and save it under Logs folder with the convention existing already
Stop sending emails to clients with 0 rows. There is already an additional script ruling these out.

Save the compiled folder into a drive link that we can share instead of the file itself

Test sending with 'bcc' to 420184@bcc.hbs.com

Work also on the sum per ISRC

For the Spo folder: Make sure the folder containing all the folders coming from opsscripting is in place to run include_pot_penalized script to add a detailed file with relevant information like so `python include_pot_penalized.py <RELATIVE_PATH_TO_ENTIRE_REPORT_TO_AFFECT> <RELATIVE_PATH_TO_SEGREGATED_REPORT_OBTAINED_WITH_PROBLEMATIC_ROWS>`

Reports for Violative content: Prepare a folder coming from Opsscripting repo to process with send_emails_violative_content_by_file.py: `python send_emails_violative_content_by_file.py --source_folder /Users/nicolasguascasantamaria/Desktop/RevAPIS/extRepo/gmailAPI/attachments/violative_content_files --email_mapping_path To_Export_All.csv`

<!-- FUTURE IMPROVEMENT -->

1. Stop sending emails to clients with 0 rows. There is already an additional script ruling these out.

2. Save the compiled folder into a drive link that we can share instead of the file itself

3. Work also on the sum per ISRC
