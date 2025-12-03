import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def enviar_email(smtp_server, smtp_port, remetente, destinatario, assunto, corpo):
    msg = MIMEMultipart()
    msg["From"] = remetente
    msg["To"] = destinatario
    msg["Subject"] = assunto
    msg.attach(MIMEText(corpo, "plain"))

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(remetente, "password")
    texto = msg.as_string()
    server.sendmail(remetente, destinatario, texto)
    server.quit()
