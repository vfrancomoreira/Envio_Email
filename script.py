import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from segredos import email, senha

# Email emissor
fromaddr = email

# Email receptor
toaddr = 'seu_email@email.com.br', 'outro_email@email.com'

# Instancia do MIMEMultipart
msg = MIMEMultipart()

msg['From'] = fromaddr

msg['To'] = toaddr

msg['Subject'] = 'Assunto'

body = """
E-mail enviado do nosso robo.\n
Olá sou o robô automatico enviado pelo python."""

# Colocando a variável body(mensagem) no corpo do e-mail
msg.attach(MIMEText(body, 'plain'))

# Servidor SMTP
s = smtplib.SMTP('smtp.gmail.com', 587) # Usar porta de servidor do email selecionado

# Segurança 
s.starttls()

s.login(fromaddr, senha)

# Converte para String
text = msg.as_string()

# Inserindo as 3 variáveis, emitente, receptor e a conversão para strings
s.sendmail(fromaddr, toaddr, text)

s.quit()

# Problema talvez com a porta do servidor'