#I've Used tqdm library to make the progress Bar
from tqdm import tqdm
#I used Time Library to Control The Speed and The Progress
from time import sleep
#I Used The Imaplib Library to Access The SMTP Gmail Protocol 
import imaplib
#The Progression Bar is Related in real time to The Search Of Emails
def progress(listofmessages):
    for i in tqdm(listofmessages, desc ="Progress : "):
        sleep(.1)
#I Defined Here The Email Protocol (Gmail) with safety Protocol 993
mail = imaplib.IMAP4_SSL('imap.gmail.com',993)
#The Library Attribute Needs Email Adress To Login Without Any Aythentication or Captcha
address = 'email@gmail.com'
mypassword = 'password'
#The Fucntion Login Makes The Login
mail.login(address, mypassword)
#I've Created The Function Inbox To Call it later
def Inbox():
    #Here I've Selected The Desired Folder Which is Ibox For This Case
    mail.select('Inbox')
    #I've Looked Only For the Unseen Messages in The First Page Which Is Today's Emails
    typ,messageIds = mail.search(None,"UNSEEN")
    #Every Email in The Web Version has an Id and Index So I Transformed it to string to make it easy to count
    messageIdsString = str(messageIds[0],encoding='utf-8')
    #Then I Split it to a List To Count How Many Ids We Have So We Can Count The Number Of email We Have
    listofmessages = messageIdsString.split(" ")
    #The Number Of Emails Here is the length of The List (Listofmessages)
    nbr = len(listofmessages)
    if len(listofmessages)== 0:
        #I Repeated That Twice Because I've Found That the List Of Messages Take One Argument which is "b" or "ok" who goes with the string from html
        progress(listofmessages)
        print("You Have No Mails On Inbox")
    elif len(listofmessages)== 0:
        progress(listofmessages)
        print("You Have No Mails On Inbox")
    else :
        progress(listofmessages)
        print("You Have ",nbr,"New Emails Inbox")

#The Same explanation For The Next Functions
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
#Defined A Function Chceking To Reduce The Lines Of Codes When I Want To Loop The Program Again
def checking():
    #Give The User The CHoice of What he is planning To Check
    print("what Are you planning To Check ? ")
    print("Here is the List : ")
    print("I : Inbox")
    print("S : Spam")
    print("E : Sent")
    #Get The Answer From The User
    an = input("Enter here : ")
    #Make it Lower in Case He Enntered in a uppercase
    answer = an.lower()
    print("We've Got your Answer Please Hold on !")
    #Every Answer Now Will Call a Function Depends On What The User is Planning To Use
    if answer == 'i':
        Inbox()
    elif answer == 's':
        Spam()
    elif answer == 'e':
        Sent()
#Calling Our Function For The First Time
#(If There is a Do While Loop In Python we Can Avoid all this and Start it From HERE)
checking()
an = input("Still wanna Check (press any key) : ")
answer = an.lower()
#I've Used A While Loop Because I Want to Loop All this Again
while(answer != 'n'):
    #Call The Function again
    checking()
    print("Thank You For Using Our Program Want To Check Again ?")
    print('Y for yes / N for no')
    #Here Wher The Function Will Get LOOPED
    answer = input()
print('Hope you enjoyed our Program See You Next Time ')
