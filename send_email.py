import smtplib
from email.mime.text import MIMEText
def send_email(email, height, average_height, count):
        from_email = "dahdeveloper@gmail.com"
        from_password= "dahpythondev"
        to_email = email

        subject = "Height data"

        message = "Hey there, your height is <strong>%s</strong>. <br>" \
                  "The average height of all is <strong>%s</strong> out of <strong>%s</strong>" \
                  " people in the survey pool. <br> Thanks!" %(height, average_height, count)

        msg = MIMEText(message, 'html')

        msg['Subject'] = subject

        msg['To'] = to_email

        msg['From'] = from_email

        #use smtplib to sent from my gmail account(temp developer account)
        gmail = smtplib.SMTP('smtp.gmail.com', 587)
        gmail.ehlo()
        gmail.starttls()
        gmail.login(from_email,from_password)
        gmail.send_message(msg)