import EmailSending
import Bot
def EnteringEmailofUser():
    EmailofUser = input("Enter your email to send the password and login")
    return(EmailofUser)

def RegisterCheck():
    countCheck =1
    while countCheck >0:
        RegisterCheck = input("Have you register already?")
        if RegisterCheck == "Yes":
          countCheck=- 1
        elif RegisterCheck == "No":
          EnteringEmailofUser()
          EmailSending.emailandpassword()
          objecttt = str(EmailSending.emailandpassword.objecttt)
          msgg = str(EmailSending.emailandpassword.msgg)
          Bot.send_email(objecttt,msgg)
          print("message sent")

          countCheck =-1


