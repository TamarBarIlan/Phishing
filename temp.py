import smtplib, ssl
from getpass import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "tam1362001@outlook.com"
receiver_email = "tamarbarilan.4@gmail.com"
password = 'tam123456'  # Please do not expose your password in the script. Use getpass to ask it when needed

message = MIMEMultipart("alternative")
message["Subject"] = "Hello"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
text = """\
Hii"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")

# Add HTML/plain-text parts to MIMEMultipart message
message.attach(part1)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP("smtp.office365.com", 587) as server:
    server.starttls(context=context)
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
