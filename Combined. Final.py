import UploadingtoMInio
import DownloadingFromMinio
import aspose.words as sr
from countdown import Countdown
from minio import Minio
import credentials
import yaml
from yaml import SafeLoader
import sqlite3
import datetime
from tkinter import Tk, Label, Button, mainloop
from threading import Thread
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from platform import python_version
import random

global test_is_over
test_is_over = False


class Countdown(Tk):
    def __init__(self):
        super().__init__()
        self.title("Time left")
        self.geometry("250x100")
        self.attributes("-topmost", True)
        self.label = Label(self, text="", font=("Arial Bold", 30))
        self.label.pack()

    def start(self, H, M, S):
        def thread():
            # starting the exam conditions for test
            allseconds = H * 3600 + M * 60 + S
            while allseconds > 0:
                timer = datetime.timedelta(seconds=allseconds)
                self.label.configure(text=str(timer))
                time.sleep(1)
                allseconds -= 1
            print("The time is over, put your pen down\nPress Enter to send results")
            self.stop()
        Thread(target=thread).start()
        return True

    def stop(self):
        self.destroy()



class Database:


    def __init__(self):
        try:
            self.sqlite_connection = sqlite3.connect('sqlite_python.db')
            cur = self.sqlite_connection.cursor()

            res = cur.execute("SELECT name FROM sqlite_master WHERE name='users'")
            if res.fetchone() is None:
                cur.execute("CREATE TABLE users(user TEXT PRIMARY KEY, pwd TEXT NOT NULL UNIQUE)")
                self.sqlite_connection.commit()

        except sqlite3.Error as error:
            print("Error connecting sqlite", error)

        finally:
            cur.close()

    def check_user(self, user, pwd):
        try:
            cur = self.sqlite_connection.cursor()

            res = cur.execute(f"SELECT user, pwd FROM users WHERE user = '{user}' AND pwd = '{pwd}'")
            if res.fetchone() is None:
                print("User or password invalid")
                return False
            else:
                print("User successfully logged in")
                return True

        except sqlite3.Error as error:
            print("Error connecting sqlite", error)
            return False

        finally:
            cur.close()

    def create_user(self, user, pwd):
        try:
            cur = self.sqlite_connection.cursor()
            res = cur.execute(f"INSERT INTO users (user, pwd) VALUES ({user}, {pwd})")
            self.sqlite_connection.commit()
            return True

        except sqlite3.Error as error:
            print("Error connecting sqlite", error)
            return False

        finally:
            cur.close()

def read():
    file = "credentials.yaml"
    try:
        with open(file) as f:
            config = yaml.load(f, Loader=SafeLoader)
        return config
    except:
        print(f'Error reading file: {file}\n return False')
        return False



def UploadingAnswers(doc_to_upload):
    config = credentials.read()
    Bucketname = "uploadeddocks"
    doc_to_upload = doc_to_upload

    try:
        minioClient = Minio('%s:%s' % (config['minioHostUri'], config["minioPort"]),
                            access_key=config['minioAccessKey'],
                            secret_key=config['minioSecretKey'],
                            secure=config['minioSecure'])

        if not minioClient.bucket_exists(Bucketname):
            minioClient.make_bucket(Bucketname)

        uploaded_doc = minioClient.fput_object(
            bucket_name=Bucketname, object_name=doc_to_upload, file_path="./%s" % doc_to_upload
        )
        print(f"Answers are saved in minio: {uploaded_doc[0]}")


    except Exception as ex:
        print(f"Answer saving error: {ex}")


def downloading_bucket(bucket_name):
    config = credentials.read()
    client = Minio(
        '%s:%s' % (config['minioHostUri'], config["minioPort"]),
        secure=config['minioSecure'],
        access_key=config['minioAccessKey'],
        secret_key=config['minioSecretKey'],
    )

    for item in client.list_objects(bucket_name, recursive=True):
        client.fget_object(bucket_name, item.object_name, item.object_name)

def downloadingmaths1():
    client = Minio(
          "127.0.0.1:9000",
          secure=False,
          access_key="minio1",
          secret_key="minio12345",
    )


    for item in client.list_objects("maths1",recursive=True):
        client.fget_object("maths1",item.object_name,item.object_name)


def downloadingmaths2():
    client = Minio(
         "127.0.0.1:9000",
         access_key="minio",
         secret_key="minio12345",
         secure=False,
    )

    for item in client.list_objects("maths2", recursive=True):
        client.fget_object("maths2", item.object_name, item.object_name)


def downloadingmaths3():
    client = Minio(
         "127.0.0.1:9000",
         access_key="minio",
         secret_key="minio12345",
         secure=False,
    )

    for item in client.list_objects("maths3", recursive=True):
        client.fget_object("maths3", item.object_name, item.object_name)


def downloadingmaths4():
    client = Minio(
         "127.0.0.1:9000",
         access_key="minio",
         secret_key="minio12345",
         secure=False,
    )

    for item in client.list_objects("maths4", recursive=True):
        client.fget_object("maths4", item.object_name, item.object_name)


def downloadingmaths5():
    client = Minio(
         "127.0.0.1:9000",
         access_key="minio",
         secret_key="minio12345",
         secure=False,
    )

    for item in client.list_objects("maths5", recursive=True):
        client.fget_object("maths5", item.object_name, item.object_name)


def downloadingmaths6():
    client = Minio(
         "127.0.0.1:9000",
         access_key="minio",
         secret_key="minio12345",
         secure=False,
    )

    for item in client.list_objects("maths6", recursive=True):
        client.fget_object("maths6", item.object_name, item.object_name)


def downloadingmaths7():
    client = Minio(
         "127.0.0.1:9000",
         access_key="minio",
         secret_key="minio12345",
         secure=False,
    )

    for item in client.list_objects("maths7", recursive=True):
        client.fget_object("maths7", item.object_name, item.object_name)


def downloadingmaths8():
     client = Minio(
         "127.0.0.1:9000",
         access_key="minio",
         secret_key="minio12345",
         secure=False,
     )

     for item in client.list_objects("maths8", recursive=True):
         client.fget_object("maths8", item.object_name, item.object_name)


def downloadingmaths9():
     client = Minio(
         "127.0.0.1:9000",
         access_key="minio",
         secret_key="minio12345",
         secure=False,
     )

     for item in client.list_objects("maths9", recursive=True):
         client.fget_object("maths9", item.object_name, item.object_name)

def downloadingtests():
    client = Minio(
         "127.0.0.1:9000",
         access_key="minio",
         secret_key="minio12345",
         secure=False,
    )

    for item in client.list_objects("tests", recursive=True):
        client.fget_object("test", item.object_name, item.object_name)


def downloadingpractice():
    client = Minio(
         "127.0.0.1:9000",
         access_key="minio",
         secret_key="minio12345",
         secure=False,
    )

    for item in client.list_objects("practices", recursive=True):
        client.fget_object("practices", item.object_name, item.object_name)

def downloadinganswersfortests():
    client = Minio(
         "127.0.0.1:9000",
         access_key="minio1",
         secret_key="minio12345",
         secure=False,
    )

    for item in client.list_objects("answers_for_tests", recursive=True):
        client.fget_object("answersfortests", item.object_name, item.object_name)



def choice_of_option():
#Choice of option and following downloading data
    list_of_topics = {"power rule": "maths1",
                      "differentiation from first principles": "maths2",
                      "stationary point": "maths3",
                      "tangents and normals to the curve": "maths4",
                      "practice applications of differentiation": "maths5",
                      "chain rule": "maths6",
                      "quotient rule": "maths7",
                      "implicit differentiation": "maths8",
                      "connected rates of change": "maths9"
                      }
    print(f"\nTopics:\n{list(list_of_topics.keys())}")
    while True:
        choice = input("Please insert the topic you want to work on:\n")
        if choice in list_of_topics:
            print(f"Your topic is: {list_of_topics.get(choice)}")
            DownloadingFromMinio.downloading_bucket(list_of_topics.get(choice))
            break
        else:
            print("Try again")


def practice_request():
    while True:
        ready = input("Are you ready to start the practice? (yes/no):\n")
        if ready.lower() == "yes":
            print("Success")
            break
        else:
            print("Try again")


def answer_submission_for_practice():
    print("Practice\n")
    lines = []
    for i in range(10):
        answer = input(f"Input your answer for question {i + 1} if such exists:\n")
        lines.append(answer)

    with open('AnswersPractice.txt', 'w') as f:
        for i, line in enumerate(lines):
            f.writelines(f"{i}:{line}\n")
    document = sr.Document("AnswersPractice.txt")
    document.save("OutputP.doc")

    UploadingtoMInio.UploadingAnswers("OutputP.doc")
    #export and save in minio

    print("now, open your browser and you will be able to find your answers submitted there;"
          "once done, you will recieve your answer for practice paper")
    #import answers
    DownloadingFromMinio.downloading_bucket("answersfortests")


#imports practice papers
def start_for_test():

    #imports test papers
    DownloadingFromMinio.downloading_bucket("tests")

    while True:
        Starting = input("Are you ready to start the test? yes/no\n")
        if Starting.lower() == "yes":
            print("The Enter the parameters")
            H=int(input("Enter the number of HOURS you need\n"))
            M=int(input("Enter the number of MINUTES you need\n"))
            S=int(input("Enter the number of SECONDS you need\n"))

            th = Thread(target=countdown, name="countdown", args=(H, M, S))
            th.start()
            answers_for_test()
            break
        elif Starting.lower() == "no":
            choice_of_option()
            break
        else:
            print("Try again")


def countdown(H, M, S):
    countdown_counter = Countdown()
    result = countdown_counter.start(H, M, S)
    countdown_counter.mainloop()
    global test_is_over
    test_is_over = result


def answers_for_test():
    print("\nTest\n")

    lines = []

    for i in range(10):
        answer = input(f"Input your answer for question {i + 1} if such exists:\n")
        if test_is_over:
            break
        lines.append(answer)

    with open('AnswersTest.txt', 'w') as f:
        for i, line in enumerate(lines):
            f.writelines(f"{i}:{line}\n")
    document = sr.Document("AnswersTest.txt")
    document.save("OutputT.doc")
    UploadingtoMInio.UploadingAnswers("OutputT.doc")

    another_topic = input(f"Practice another topic (yes/no):\n")
    if another_topic.lower() == "yes":
        choice_of_option()

# Bot sending emails with confirming registration
def send_email(email_user, object, msg):
    config = credentials.read()

    server = config['mailServer']
    user = config['mailUser']  # login
    password = config['mailPassword']  # password (you need to create a password for an external application)

    recipients = [email_user]  # mail recipient
    sender = config['mailSender']  # mail sender
    subject = "Exam assistant registration"
    text = f"{object}\n{msg}"

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = f'Python script <{sender}>'
    msg['To'] = ', '.join(recipients)
    msg['Reply-To'] = sender
    msg['Return-Path'] = sender
    msg['X-Mailer'] = 'Python/' + (python_version())
    part_text = MIMEText(text, 'plain')

    msg.attach(part_text)

    try:
        mail = smtplib.SMTP_SSL(server)
        mail.login(user, password)
        mail.sendmail(sender, recipients, msg.as_string())
        mail.quit()
    except Exception as ex:
        print(f"Error: {ex}")


print("Welcome to the new era of eam preparation!"
      "Your greatest, favourite, the only one exam assistant. lets get started.")
count = False
while not count:
    InitialCheck = input("Are you registered already?")
    if InitialCheck == "yes":
        login = input("enter your login")
        password = input("enter your password")
        Database.check_user(login, password) #help me please
        count = True
    elif InitialCheck == "no":
        emailofuser =input("enter the email to send the login and password to")
        username = random.randint(111, 999)
        pswrd = random.randint(111111, 999999)
        send_email(emailofuser, username, pswrd) #help me please

        Database.create_user(username, pswrd) #help me please
    else:
        continue


for i in range (0, 99999999999):
    choice_of_option()
    practice_request()
    answer_submission_for_practice()
    start_for_test()
    answers_for_test()
    choiceOfLife = input("Are you sure you want to continue")
    if choiceOfLife.lower() == "yes":
        continue
    else:
        print("I WILL BE BACK")
        break








