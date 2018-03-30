import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_user = 'Your email'
password = 'Your password'
email_receiver = 'Receiver Email'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_receiver
msg['Subject'] = 'Python'
body = 'Hi there, sending this email from Python!'
msg.attach(MIMEText(body, 'plain'))
# text = msg.as_string()

filename = 'Document.txt'
attachment = open(filename, 'rb')
part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)

part.add_header('Content-Disposition', "attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()
# server = smtplib.SMTP('smtp.gmail.com', 587)
server = smtplib.SMTP('smtp-mail.outlook.com', 587)
server.starttls()
server.login(email_user, password)

# message = 'Hi there, sending this email from Python!'

server.sendmail(email_user, email_receiver, text)
server.quit()