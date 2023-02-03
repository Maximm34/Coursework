import time
import datetime
import UploadingtoMInio
import DownloadingFromMinio







def choiceofoption():
#Choice of option and fololowing downloading data
    listoftopics = ["power rule", "differentiation from first principles",
                    "stationary point", "tangents and normals to the curve",
                    "practice applications of differentiation",
                    "chain rule", "quotient rule", "implicit differentiation",
                    "connected rates of change"]
    a=1
    while a>0:
        choice = input("Please insert the topic you want to work on")
        if choice == any(listoftopics):
            print("sucess")
            a=-1
        else:
            print("try again")

        if choice == listoftopics[0]:
            DownloadingFromMinio.downloadingmaths1()
        if choice == listoftopics[1]:
            DownloadingFromMinio.downloadingmaths2()
        if choice == listoftopics[2]:
            DownloadingFromMinio.downloadingmaths3()
        if choice == listoftopics[3]:
            DownloadingFromMinio.downloadingmaths4()
        if choice == listoftopics[4]:
            DownloadingFromMinio.downloadingmaths5()
        if choice == listoftopics[5]:
            DownloadingFromMinio.downloadingmaths6()
        if choice == listoftopics[6]:
            DownloadingFromMinio.downloadingmaths7()
        if choice == listoftopics[7]:
            DownloadingFromMinio.downloadingmaths8()
        if choice == listoftopics[8]:
            DownloadingFromMinio.downloadingmaths9()

def practicerequest():
    a=1
    while a>0:
        ready=input("Are you ready to start the practice?")
        if ready == "Yes":
            a =-1
            print("Success")

        else:
            print("Try again")




#imports practice papers
def startfortest():
    #imports test papers
    DownloadingFromMinio.downloadingtests()

    count = 1
    while count >0:
        Starting = input("Are you ready to start the test? Yes/no")
        if Starting == "yes":
          print("The Enter the parameters")
          H=int(input("enter the number of hours you need"))
          M=int(input("Enter the number of minutes you need"))
          S=int(input("Enter the number of seconds you need"))
          count = -1
          countdown(H, M, S)

        elif Starting == "No":
          count=-1
          choiceofoption()



def countdown(H,M,S):
    #startingtheexamconditionsfortest
    allseconds = H*3600+M*60+S
    while allseconds >0:
        timer = datetime.timedelta(seconds=allseconds)
        print(timer, end="r")
        time.sleep(1)
        allseconds -=1
        print("the time is over, put your pen down")

def AnswerSubmissionForPractice():
    #exportofanswers
    Answer1 = input("Input your answer for question 1 if such exists")
    Answer2 = input("Input your answer for question 2 if such exists")
    Answer3 = input("Input your answer for question 3 if such exists")
    Answer4 = input("Input your answer for question 4 if such exists")
    Answer5 = input("Input your answer for question 5 if such exists")
    Answer6 = input("Input your answer for question 6 if such exists")
    Answer7 = input("Input your answer for question 7 if such exists")
    Answer8 = input("Input your answer for question 8 if such exists")
    Answer9 = input("Input your answer for question 9 if such exists")
    Answer10 = input("Input your answer for question 10 if such exists")



    lines1 = [Answer1, Answer2, Answer3, Answer4, Answer5, Answer6, Answer7, Answer8, Answer9, Answer10]
    with open('AnswersPractice.txt', 'w') as f:
        f.writelines(lines1)
    document = sr.Document("AnswersPractice.txt")
    document.save("OutputP.doc")

    UploadingtoMInio.UploadingAnswersPractice()
    #export and save in minio

    print("now, open your browser and you will be able to find your answers submitted there;"
          "once done, you will recieve your answer for practice paper")
    #import answers
    DownloadingFromMinio.downloadinganswersfortests()

def answersfortest():
    Answer1 = input("Input your answer for question 1 if such exists")
    Answer2 = input("Input your answer for question 2 if such exists")
    Answer3 = input("Input your answer for question 3 if such exists")
    Answer4 = input("Input your answer for question 4 if such exists")
    Answer5 = input("Input your answer for question 5 if such exists")
    Answer6 = input("Input your answer for question 6 if such exists")
    Answer7 = input("Input your answer for question 7 if such exists")
    Answer8 = input("Input your answer for question 8 if such exists")
    Answer9 = input("Input your answer for question 9 if such exists")
    Answer10 = input("Input your answer for question 10 if such exists")
    lines1 = [Answer1, Answer2, Answer3, Answer4, Answer5, Answer6, Answer7, Answer8, Answer9, Answer10]
    with open('AnswersTest.txt', 'w') as f:
        f.writelines(lines1)
    document = f.Document("AnswersTest.txt")
    document.save("OutputT.doc")

    UploadingtoMInio.UploadingAnswersTest()


















