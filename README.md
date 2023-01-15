# Send emails with the Gmail API for python

This repo provides a one-line python functionality to send the same email to a list of recipients using the [Gmail API](https://developers.google.com/gmail/api/guides). This readme provides step-by-step instructions on how to configure the files in this repo so that the email message is tailored to your needs. 

This repo was tested on Mac Venture 13.1 (22C65) and Python 3.10.8.  

There are four files in this repo that will need to be updated by the user:

* `credentials.json` (see (1))
* `config.py` (see (3))
* `emails/example1.txt` (see (4))
* `attachments/file1.png` (see (5)) 

The ones found in this repo are meant for demonstrative purposes only. An example of the structure of this repo is shown below, when there are two attachments files (file1.png, file2.jpg) and two email lists (list1.txt, list2.txt):

```
├── .gitignore
├── README.md
├── attachments
│   ├── file1.png
│   ├── file2.jpg
│   └── readme.md
├── config.py
├── credentials.json
├── emails
│   ├── list1.txt
│   ├── list2.txt
│   └── readme.md
├── environment.yml
├── send_emails.py
└── utils.py
```

To sure you don't commit any private changes to your branch, you'll probably want to stop tracking the template files:

```
git update-index --skip-worktree credentials.json
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

The contents of the email and subject line are controlled by the `config.py` script. The config script found in this repo contains empty strings so that different users/clones can have different set-ups. This file is included in the .gitignore, so it won't be pushed with any changes.

1. `txt_message`: Put your main message here.
2. `gmail_address`: Put your gmail address here.
3. `subject_line`: Put your subject line here.
4. There are four other parameters: `scopes`, `credentials`, `port`, and `max_emails`, but only adjust these ify ou know.

<br>

## (4) Set up email list

Users can add email lists in an unstructured format to the `emails` folder. For example, an `emails/emails1.txt` may look like:

```
jack@hotmail.com;    jazz@outlook.com

jim@gmail.com
```

Any spaces, semi-colons, or line-breaks will treated a possible separators. Angle brackets will be removed as well. For example `John Doe <john.doe@email.com>` will just become `john.doe@email.com`. For a "valid" email to be considered, it must contain an ampersand. Users can add as many *.txt files to this folder, and all emails will combined for the final list (e.g. emails/emails2.txt, ..., emails/moreemails.txt). 

<br>

## (5) Set up attachments (if any)

Users can also include attachments in the email by dropping files in the `attachments` folder. If the attachment is an email, the maximum image size rule will kick in upon upload (see below). For example, of file1.png is a 1500x2000 image, and there is a max_image_size=1000, when the email will be shrunken by 50%.

<br>

## (6) Send emails

After the `config.py` has been set up, email lists have been added to the `emails/*.txt` folder, and attachments (optional) have been added to the `attachment/*` folder, the main script can be run. An example of the script call can be found below. When running this from the user command line, a broswer window should open for authentication to give the app access to send emails from your gmail account. If it doesn't happen automatically, you can copy the link that will be printed to the console. Additionally, after the email list is printed out, users will need to confirm they want to go ahead with sending the email by typing "Y" into the console when prompted. If you type "n" the script will exit and no emails will send. If you type in anything else, you will be re-prompted to type in either "Y" or "n".

```python
conda activate gmailAPI
python3 send_emails.py --attachment_suffix png jpg --email_suffix txt --max_image_size 1024
```
