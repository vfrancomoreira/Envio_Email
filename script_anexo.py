import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from segredos import email, senha

fromaddr = email

toaddr = 'seu_email@email.com.br', 'outro_email@email.com'

msg = MIMEMultipart()

msg['From'] = fromaddr

msg['To'] = toaddr

msg['Subject'] = 'Documento anexado'

body = """
Carta enviada pelo nosso robo.\n
Olá sou o robô automatico enviado pelo python. 
TESTE 2"""

msg.attach(MIMEText(body, 'plain'))

# Anexo
# Definir o nome do arquivo
filename = "cartaemanexo.pdf"

# Abrir arquivo
anexo = open('curriculo.pdf', 'rb')

p = MIMEBase('application', 'octet-stream')

# Upload do arquivo para a memória
p.set_payload((anexo).read())

# encode em base64
encoders.encode_base64(p)

p.add_header('Content-Disposition', 'attachment; filename= %s' % filename)

msg.attach(p)

s = smtplib.SMTP('smtp.gmail.com', 587) # Usar porta de servidor do email selecionado

s.starttls()

s.login(fromaddr, senha)

text = msg.as_string()

s.sendmail(fromaddr, toaddr, text)

s.quit()
