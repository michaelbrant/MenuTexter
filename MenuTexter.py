import pullMenu
import myHTMLParser
import smtplib
import sys
import configparser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

configParser = configparser.RawConfigParser()
configFilePath = '/home/ec2-user/MenuTexter/config.cfg'
configParser.read(configFilePath)
USERNAME = str(configParser.get('email-login', 'username'))
PASSWORD = str(configParser.get('email-login', 'password'))

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == 'L':
            url = pullMenu.getLunchURL()
            menuList = myHTMLParser.parse(url)
            sendMail(menuList, "Lunch")
        if sys.argv[1] == 'D':
            url = pullMenu.getDinnerURL()
            menuList = myHTMLParser.parse(url)
            sendMail(menuList, "Dinner")

def getRecipients():
    #Read the file containing phone numbers
    readReceivers = open("emailList.txt", "r")
    receiverString = readReceivers.read()
    receiverList = receiverString.splitlines(receiverString.count('\n'))
    readReceivers.close()
    return receiverList

def sendMail(menuList, DorL):
    recipients = getRecipients()
    msg = MIMEMultipart()
    msg['From'] = 'Cafe Menu'
    msg['Subject'] = 'The ' +DorL +' Menu for today:'
    for item in menuList:
        msg.attach(MIMEText(item))
    for recipient in recipients:
        try:
            mailserver = smtplib.SMTP('smtp.gmail.com',587)
            # identify ourselves to smtp gmail client
            mailserver.ehlo()
            # secure our email with tls encryption
            mailserver.starttls()
            # re-identify ourselves as an encrypted connection
            mailserver.ehlo()
            mailserver.login(USERNAME, PASSWORD)
            mailserver.sendmail(USERNAME,recipient,msg.as_string())
            mailserver.quit()
            print("Emailing:" + recipient)
        except:
            print( "ERROR")

def sendHello(receiver):
    msg = MIMEMultipart()
    msg['From'] = 'Cafe Menu'
    #msg['To'] = ', '.join(recipients)
    msg['Subject'] = 'Welcome to the Cafeteria Menu Texter'
    menuList = []
    menuList.append("\nA text of the daily lunch menu will be sent to you Monday - Friday before lunch\nReply 'Stop' to stop receiving texts \n\n Developed by M.D.B ")
    for item in menuList:
        msg.attach(MIMEText(item))
    mailserver = smtplib.SMTP('smtp.gmail.com',587)
    # identify ourselves to smtp gmail client
    mailserver.ehlo()
    # secure our email with tls encryption
    mailserver.starttls()
    # re-identify ourselves as an encrypted connection
    mailserver.ehlo()
    mailserver.login(USERNAME, PASSWORD)
    mailserver.sendmail(USERNAME,receiver,msg.as_string())
    mailserver.quit()

def sendOneLunchMenu(receiver):
    url = pullMenu.getLunchURL()
    sendOneMenu(receiver,"Lunch",url)

def sendOneDinnerMenu(receiver):
    url = pullMenu.getDinnerURL()
    sendOneMenu(receiver,"Dinner",url)

def sendOneMenu(OneReceiver, DorL, url):
    menuList = myHTMLParser.parse(url)

    msg = MIMEMultipart()
    msg['From'] = 'Cafe Menu'
    #msg['To'] = ', '.join(recipients)
    msg['Subject'] = 'The '+ DorL +' Menu for today:'
    for item in menuList:
        msg.attach(MIMEText(item))
    mailserver = smtplib.SMTP('smtp.gmail.com',587)
    # identify ourselves to smtp gmail client
    mailserver.ehlo()
    # secure our email with tls encryption
    mailserver.starttls()
    # re-identify ourselves as an encrypted connection
    mailserver.ehlo()
    mailserver.login(USERNAME, PASSWORD)
    mailserver.sendmail(USERNAME,OneReceiver,msg.as_string())
    mailserver.quit()

main()
