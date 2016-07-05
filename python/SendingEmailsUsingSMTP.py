import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

GMAIL_USERNAME = 'example@gmail.com'
GMAIL_PASSWORD = ''
FROM_EMAIL = ''  # email-sender
TO_EMAIL = ''  # email-recipient
EMAIL_SUBJECT = ''  # subject for your email alert, name of the metric for example


def send_email_with_gmail(from_addr, to_addr, username, password, email_subject, message):
    """Send an email using Gmail and SMTP protocol
    Sends an email with your 'message' passed as a paramentr
    Args:
         from_addr (str): email-sender
         to_addr (str): email-recipient
         username (str): Gmail username
         password (str): password for Gmail account
         email_subject (str): subject of an email message
         message (str): message included in a body of an email
    Returns:
         -1 if an error was encountered
    """
    server = smtplib.SMTP('smtp.gmail.com:587')  # Gmail
    # Sending an email alert
    try:
        # forming the content of the email alert
        content = MIMEMultipart()
        content['From'] = from_addr
        content['To'] = to_addr
        content['Subject'] = email_subject
        content.attach(MIMEText(message, 'plain'))  # email body

        server.starttls()
        server.login(username, password)
        server.send_message(content,from_addr,to_addr)
    except Exception as e:
        print(e)
        return -1
    finally:
        server.quit()


if __name__ == '__main__':
    send_email_with_gmail(FROM_EMAIL, TO_EMAIL, GMAIL_USERNAME, GMAIL_PASSWORD, EMAIL_SUBJECT, 'YOUR MESSAGE')