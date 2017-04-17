import email
import time
import imaplib
import mailbox
import emailListRemover
import MenuTexter
import configparser

configParser = configparser.RawConfigParser()
configFilePath = '/home/ec2-user/MenuTexter/config.cfg'
configParser.read(configFilePath)
EMAIL_ACCOUNT = str(configParser.get('email-login', 'username'))
PASSWORD = str(configParser.get('email-login', 'password'))


mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(EMAIL_ACCOUNT, PASSWORD)
mail.list()
mail.select('inbox')
result, data = mail.uid('search', None, "UNSEEN") # (ALL/UNSEEN)
i = len(data[0].split())


#For every unread email, x, look at the text body for keywords "Start", "start", "START, or "Stop"
for x in range(i):
    mail.select('inbox')
    latest_email_uid = data[0].split()[x]
    result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
    raw_email = email_data[0][1]
    raw_email_string = raw_email.decode('utf-8')
    email_message = email.message_from_string(raw_email_string)
    email_from = str(email.header.make_header(email.header.decode_header(email_message['From'])))

    # Look at Email Body
    for part in email_message.walk():
	    #if part.get_content_type() == "text/plain":
	    body = part.get_payload(decode=True)
	    if(isinstance(body, str)):
		    if body.find("Start") >= 0 or body.find("start") >= 0 or body.find("START") >= 0:
			    print("NEW SUBSCRIBER")
			    MenuTexter.sendHello(email_from)
			    with open("emailList.txt", "a") as myfile:
				    myfile.write(email_from)
				    myfile.write("\n")
		    if body.find("Stop") >= 0 or body.find("STOP") >= 0:
			    print("UNSUBSCRIBED")
			    emailListRemover.remove(email_from)
		    if body.find("Dinner") >= 0 or body.find("dinner") >=0 or body.find("DINNER") >=0:
			    MenuTexter.sendOneDinnerMenu(email_from)
			    print("REQUESTED DINNER MENU")
		    if body.find("Lunch") >= 0 or body.find("lunch") >= 0 or body.find("LUNCH") >=0:
			    MenuTexter.sendOneLunchMenu(email_from)
			    print("REQUESTED LUNCH MENU")
    mail.close()
