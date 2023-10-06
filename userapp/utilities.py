
import requests
import smtplib
from email.mime.text import MIMEText


def send_whatsApp_message(mobile,message):
    x = requests.get(f'https://bookmyotservice.pythonanywhere.com/sendWhatsAppMessage?number={mobile}&message={message}')
    return  str(x.text)


def send_email(subject, message_body, recipient_email):
    try:
        sender_email = "Crm@perennialcode.in"
        password = "P3r3nni@l"
        smtp_server = "smtp.hostinger.com"
        smtp_port = 465
        message = MIMEText(message_body)
        message["Subject"] = subject
        message["From"] = sender_email
        message["To"] = recipient_email
         # Establish a secure SMTP connection 
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
             server.login(sender_email, password)
             server.sendmail(sender_email, recipient_email, message.as_string())
             print("Email sent successfully")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# send_email("Test Subject 001", "This is a test message.", "chaitanya.vinay16@gmail.com" )




