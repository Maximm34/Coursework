import smtplib
import configuration
import RegistrationProcess





#Bot sending emails with confirming registration
def send_email(objecttt, msgg):
    try:
        servers = smtplib.SMTP('smtp.gmail.com:587')
        servers.ehlo()
        servers.starttls()
        servers.login(configuration.email_adress, configuration.password)
        messaging = 'Subject: {}\n\n{}'.format(objecttt, msgg)
        servers.sendmail(RegistrationProcess.EnteringEmailofUser(), RegistrationProcess.EnteringEmailofUser(), messaging)

        servers.quit()
        print("Success")
    except:
        print("Failure")
