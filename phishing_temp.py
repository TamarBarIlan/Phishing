import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "itizik_bitizk@outlook.com"
receiver_email = " tamarbarilan.4@gmail.com"
password = "CYBERlab123"

message = MIMEMultipart("alternative")
message["Subject"] = "eBay-style email"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
text = """\
Hi,
How are you?
Check out this great deal on eBay:
https://www.ebay.com/some-product"""
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
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp-mail.outlook.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
