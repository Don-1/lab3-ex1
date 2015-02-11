import smtplib

fromaddr = 'don-saynomre@hotmail.com'

toaddr = 'don-saynomore@hotmail.com'

message = """From: {} <{}>

To: {} <{}>

Subject: {}

{}

"""

fromname = 'don'
toname = 'don'
subject = 'lab3'
msg = 'dfasfsdfsdafsd'

messagetosend = message.format(

 fromname,

 fromaddr,

 toname,

 toaddr,

 subject,

 msg)

# Credentials (if needed)

username = 'jaypaisley13@gmail.com'

password = 'gobiyusnsamkowvq'

# The actual mail send

server = smtplib.SMTP('smtp.gmail.com:587')

server.starttls()

server.login(username,password)

server.sendmail(fromaddr, toaddr, messagetosend)

server.quit()