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

html_file = "email.html"

with open(html_file, "w") as file:
    file.write(html)

print("HTML file saved as:", html_file)
