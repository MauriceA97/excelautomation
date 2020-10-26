from __future__ import annotations
import smtplib
from excel_reader import read_spreadsheet
from email.message import EmailMessage
from zip_reader import pdf_names
from agents import set_agent_type
import os
import time
import sys

# ! Missing
''' 
    TODO: 
    1. Missing body/subject for other agents
'''
body = ''
message = None
password = None
sender = None
subject = ''
webserver = None
SMTP_NAME = 'outlook.office365.com'
SMTP_PORT = 587

def forward_to_agents():
    pdf_files = pdf_names() # Full path name
    spreadsheet = read_spreadsheet(6)

    found_names = []

    # Get the agent email
    for agent, email in list(spreadsheet.items()):
        for pdf_name in pdf_files[1]:
            if agent in pdf_name.split('/')[1].split('.pdf')[0]:
                send_mass(email, pdf_name)
                found_names.append(agent)
                break
    print('Messages sent!')

    # Shows missing names from excel sheet
    for missing_agent in sorted(list(set(found_names).symmetric_difference(list(spreadsheet.keys())))):
        print('Missing:', missing_agent)


def initialize_email(sender:str, recipient:str, file:str) -> bool:
    """Composes the message."""

    if not sender:
        return True

    global message
    message = EmailMessage()
    message['From'] = sender
    message['To'] = recipient

    message['Subject'] = subject
    message.set_content(body)


    # Make a function

    with open(os.path.join(os.getcwd(), file), 'rb') as pdf_file:
        file_data = pdf_file.read()
        pdf_name = file
    
    message.add_attachment(
            file_data, maintype='application', subtype='octet-stream', filename=pdf_name
    )

    with open(os.path.join(os.getcwd(), 'attachment', 'Oscar_Broker Recon. Report.xlsx'), 'rb') as excel_file:
        file_data = excel_file.read()
        spreadsheet_name = 'Oscar_Broker Recon. Report.xlsx'
    
    message.add_attachment(
            file_data, maintype='application', subtype='octet-stream', filename=spreadsheet_name
    )

    
    return False


def initialize_server() -> None:
    """Setups up the webserver for sending emails."""

    global webserver
    webserver = smtplib.SMTP(SMTP_NAME, SMTP_PORT)
    webserver.ehlo()
    webserver.starttls()


def send_email(sender: str, password: str) -> None:
    """Sends an email to a user."""

    # Check for a email and password
    if not sender or not password:
        print('A recipent or password was not supplied')
        exit(1)
    
    initialize_server()

    webserver.login(sender, password)
    webserver.send_message(message)
    webserver.quit()
    

def send_mass(email, file=''):
    global sender
    initialize_email(sender, email, file)
    send_email(sender, password)



if __name__ == "__main__":
    print('=== PLEASE INCLUDE ZIP, EXCEL SHEET, AND ADD ATTACHMENT XLSX INTO ATTACHMENT FOLDER ===\n')

    if len(os.listdir()) < 4:
        print('You are missing a file')
        exit(1)

    sender = input('Please enter your email: ')
    password = input('Please enter your password: ')
    agent_type = set_agent_type(int(input('''\nSelect an agent type: 
    AMBETTER      = (1) 
    AVMED         = (2)
    BRIGHT_HEALTH = (3)
    CIGNA         = (4)
    MOLINA        = (5)
    OSCAR         = (6)
    WORKAGENTS    = (7)
    \nNumber: ''')))

    

    print('\nExtracting zip...')
    syms = ['\\', '|', '/', '-']
    bs = '\b'

    for _ in range(5):
        for sym in syms:
            sys.stdout.write("\b%s" % sym)
            sys.stdout.flush()
            time.sleep(.5)
    
    sys.stdout.write("\b%s" % '')

    subject = agent_type['subject']  
    body = agent_type['body']
    forward_to_agents()

    
    os.system('pause')