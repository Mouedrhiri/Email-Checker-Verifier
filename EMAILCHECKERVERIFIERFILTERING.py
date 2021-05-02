from tqdm import tqdm
from time import sleep
import imaplib
def progress(listofmessages):
    for i in tqdm(listofmessages, desc ="Progress : "):
        sleep(.1)

mail = imaplib.IMAP4_SSL('imap.gmail.com',993)
address = 'uness6.test@gmail.com'
mypassword = 'lgxnotewin8'
mail.login(address, mypassword)
def Inbox():
    mail.select('Inbox')
    typ,messageIds = mail.search(None,"UNSEEN")
    messageIdsString = str(messageIds[0],encoding='utf-8')
    listofmessages = messageIdsString.split(" ")
    nbr = len(listofmessages)
    if len(listofmessages)== 0:
        progress(listofmessages)
        print("You Have No Mails On Inbox")
    elif len(listofmessages)== 0:
        progress(listofmessages)
        print("You Have No Mails On Inbox")
    else :
        progress(listofmessages)
        print("You Have ",nbr,"New Emails Inbox")

def Spam():
    mail.select('[Gmail]/Spam')
    typ,messageIds = mail.search(None,"UNSEEN")
    messageIdsString = str(messageIds[0],encoding='utf-8')
    listofmessages = messageIdsString.split(" ")
    nbr = len(listofmessages)
    if len(listofmessages)== 0:
        progress(listofmessages)
        print("You Have No Mails On Spam")
    elif len(listofmessages)== 0:
        progress(listofmessages)
        print("You Have No Mails On Spam")
    else :
        progress(listofmessages)
        print("You Have ",nbr,"New Emails Spam")



def Sent():
    mail.select('"[Gmail]/Messages envoy&AOk-s"')
    typ,messageIds = mail.search(None,"SEEN")
    messageIdsString = str(messageIds[0],encoding='utf-8')
    listofmessages = messageIdsString.split(" ")
    nbr = len(listofmessages)
    if len(listofmessages)== 0:
        progress(listofmessages)
        print("You Have Sent No Email")
    else :
        progress(listofmessages)
        print("You Have Sent ",nbr,"Emails")

print("Welcome to E-mail Checker !!")
def checking():
    print("what Are you planning To Check ? ")
    print("Here is the List : ")
    print("I : Inbox")
    print("S : Spam")
    print("E : Sent")
    an = input("Enter here : ")
    answer = an.lower()
    print("We've Got your Answer Please Hold on !")
    if answer == 'i':
        Inbox()
    elif answer == 's':
        Spam()
    elif answer == 'e':
        Sent()
checking()
an = input("Still wanna Check (press any key) : ")
answer = an.lower()
while(answer != 'n'):
    checking()
    print("Thank You For Using Our Program Want To Check Again ?")
    print('Y for yes / N for no')
    answer = input()
print('Hope you enjoyed our Program See You Next Time ')
