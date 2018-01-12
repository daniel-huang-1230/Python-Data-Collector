import smtplib
from email.mime.text import MIMEText
def send_email(email, height):
        from_email = "dahdeveloper@gmail.com"
        from_password= "dahpythondev"
        to_email = email

        subject = "Height data"

        message = "Hey there, your height is <strong>%s</strong>." %height

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