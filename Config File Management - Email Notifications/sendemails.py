#Sending the differences via email
#Defining the e-mail parameters
fromaddr = 'mihai.python3@gmail.com'
toaddr = 'mihai.python3@gmail.com'
 
#More on MIME and multipart: https://en.wikipedia.org/wiki/MIME#Multipart_messages
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'Daily Configuration Management Report'
msg.attach(MIMEText(difference, 'html'))
 
#Sending the email via Gmail's SMTP server on port 587
server = smtplib.SMTP('smtp.gmail.com', 587)
 
#SMTP connection is in TLS (Transport Layer Security) mode. All SMTP commands that follow will be encrypted.
server.starttls()
 
#Logging in to Gmail and sending the e-mail
server.login('mihai.python3', 'python3.7')
server.sendmail(fromaddr, toaddr, msg.as_string())
server.quit()
