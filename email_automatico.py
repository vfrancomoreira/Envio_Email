import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from segredos import email, senha
from corpo_email import corpo_email

fromaddr = email

toaddr = 'seu_email@email.com.br', 'outro_email@email.com'

msg = MIMEMultipart()

msg['From'] = fromaddr

msg['To'] = toaddr 

msg['Subject'] = 'E-mail Automático'

html = corpo_email

part1 = MIMEText(html, 'html')

msg.attach(part1)

s = smtplib.SMTP('smtp.gmail.com', 587) 

s.starttls()

s.login(fromaddr, senha)

text = msg.as_string()

s.sendmail(fromaddr, toaddr, text)

s.quit()
