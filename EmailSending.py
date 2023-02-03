import random


#setting the error emails and storing it
def ErrorEmail():
    erorrLogins = []
    erorrPasswords =[]
    count =1
    while count >0:
        login = random.randint(1, 9999999)
        password = random.randint(1, 9999999)
        if login not in erorrLogins and password not in erorrPasswords:
            emailandpassword().subject = str("Your login is:",
                                     login
                                     )
            emailandpassword().msg = str("password is:",

                                 password)
            erorrLogins.append(login)
            erorrPasswords.append(password)
            count =-1
        else:
            continue




    return


#the code describing the email and setting the login details n
def emailandpassword():
    logins =[]
    passwords=[]
    count = 1
    while count >0:
        login =random.randint(1,9999999)
        password = random.randint(1,9999999)
        if login not in logins and password not in passwords:
            emailandpassword().subject=str("Your login is:",
                                   login
                                   )
            emailandpassword().msg=str("password is:",

                                   password )
            logins.append(login)
            passwords.append(password)
            count=-1
        else:
            continue


    return



