# EMAIL CHECKER / Verifier By Mohammed Ouedrhiri

# Using Python

## Private University Of Fez

> (It's A University Project)

> Follow Me On Github For More Projects

> Mohammed Ouedrhiri &copy;

#### Linkedin Account [Linkedin](https://www.linkedin.com/in/mohammed-ouedrhiri-512183187 “Linkedin”)

# Lets Begin The explanation

## The Progress Bar :

### I've Creted The Progress Bar Using THE Tqdm (تقدم) and Import it

`from tqdm import tqdm`

### Then Imported The Sleep Library To Control The Time Flow

`from time import sleep`

### The I Used The Library Imaplib To Give Me Acces To Gmail Account

`import imaplib`

### I've Made a Function For The Progress Bar Like That :

Give it Argument To Make it Relative To The Searching

    def progress(listofmessages):
    for i in tqdm(listofmessages, desc ="Progress : "):
        sleep(.1)

### I Defined Here The Email Protocol (Gmail) with safety Protocol 993

    mail = imaplib.IMAP4_SSL('imap.gmail.com',993)

### The Library Attribute Needs Email Adress To Login Without Any Aythentication or Captcha(You Need a No Captcha and No Authentication Gmail with less secure apps Allow)

    address = 'youreemail@gmail.com'
    mypassword = 'password'

### The Fucntion Login Makes The Login

    mail.login(address, mypassword)

---

## I've Created The Function Inbox To Call it later

    def Inbox():

### Here I've Selected The Desired Folder Which is Ibox For This Case

        mail.select('Inbox')

### I've Looked Only For the Unseen Messages in The First Page Which Is Today's Emails

        typ,messageIds = mail.search(None,"UNSEEN")

### Every Email in The Web Version has an Id and Index So I Transformed it to string to make it easy to count

        messageIdsString = str(messageIds[0],encoding='utf-8')

### Then I Split it to a List To Count How Many Ids We Have So We Can Count The Number Of email We Have

        listofmessages = messageIdsString.split(" ")

### The Number Of Emails Here is the length of The List (Listofmessages)

        nbr = len(listofmessages)
        if len(listofmessages)== 0:

### I Repeated That Twice Because I've Found That the List Of Messages Take One Argument which is "b" or "ok" who goes with the string from html

            progress(listofmessages)
            print("You Have No Mails On Inbox")
        elif len(listofmessages)== 0:
            progress(listofmessages)
            print("You Have No Mails On Inbox")
        else :
            progress(listofmessages)
            print("You Have ",nbr,"New Emails Inbox")

---

## I've Created Also Functions For Spam and Sent Messages :

### Spam Function :

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

### Sent Function :

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

---

## Defined A Function Chceking To Reduce The Lines Of Codes When I Want To Loop The Program Again

    def checking():

### Give The User The CHoice of What he is planning To Check

        print("what Are you planning To Check ? ")
        print("Here is the List : ")
        print("I : Inbox")
        print("S : Spam")
        print("E : Sent")

### Get The Answer From The User

        an = input("Enter here : ")

### Make it Lower in Case He Enntered in a uppercase

        answer = an.lower()
        print("We've Got your Answer Please Hold on !")

### Every Answer Now Will Call a Function Depends On What The User is Planning To Use

        if answer == 'i':
            Inbox()
        elif answer == 's':
            Spam()
        elif answer == 'e':
            Sent()

---

### Calling Our Function For The First Time

### (If There is a Do While Loop In Python we Can Avoid all this and Start it From HERE)

```
checking()
an = input("Still wanna Check (press any key) : ")
answer = an.lower()
```

---

## I've Used A While Loop Because I Want to Loop All this Again

    while(answer != 'n'):

### Call The Function again

        checking()
        print("Thank You For Using Our Program Want To Check Again ?")
        print('Y for yes / N for no')

### Here Wher The Function Will Get LOOPED

        answer = input()

Thanks For Using My Code If You Have Any Problem Contact Me On email : mouedrhiri492@gmail.com

> Mohammed Ouedrhiri &copy;

![logo](https://www.laformation.ma/images/contenu/24214a91e4.png)
