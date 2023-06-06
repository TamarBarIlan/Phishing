import smtplib, ssl
from getpass import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, receiver_email, password, username, mail_service_name, title, job_title, personal_status, kids_status):
    message = MIMEMultipart("alternative")
    message["Subject"] = "Hello " + username
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the HTML version of your message
    html = """\
<html>
  <head>
    <meta charset="utf-8">
    <style>
      .container {
        max-width: 600px;
        margin: 0 auto;
        font-family: Arial, sans-serif;
      }
      .header {
        background-color: #E53238;
        padding: 20px;
        color: #FFFFFF;
        text-align: center;
      }
      .content {
        padding: 20px;
        background-color: #F9F9F9;
        font-size: 16px;
        line-height: 1.5;
        text-align: left;
      }
      .button {
        display: inline-block;
        background-color: #0066CC;
        color: #FFFFFF;
        padding: 10px 20px;
        text-decoration: none;
        border-radius: 4px;
        margin-top: 20px;
        font-size: 16px;
      }
      .footer {
        background-color: #E53238;
        padding: 20px;
        color: #FFFFFF;
        text-align: center;
      }
      .ebay-logo {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
      }
      .ebay-logo img {
        max-width: 150px;
        height: auto;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <div class="header">
        <h1>Special Offer!</h1>
      </div>
      <div class="content">
        <p>Hi,<br>
          How are you?<br>
          Check out this great deal on eBay:
        </p>
        <a class="button" href="https://www.ebay.com/some-product">View Deal</a>
      </div>
      <div class="footer">
        <p>© 2023 eBay Inc. All rights reserved.</p>
      </div>
      <div class="ebay-logo">
        <img src="https://ir.ebaystatic.com/rs/v/fxxj3ttftm5ltcqnto1o4baovyl.png" alt="eBay Logo">
      </div>
    </div>
  </body>
</html>
"""

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    message.attach(part1)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP("smtp.office365.com", 587) as server:
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

# Usage:
send_email("tam1362001@outlook.com", "tamarbarilan.4@gmail.com", 'tam123456', 'Username', 'Mail Service Name', 'Title', 'Job Title', 'Personal Status', 'Kids Status')
