from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.template.loader import render_to_string
from doggy import settings
import smtplib
from django.contrib.auth.models import User

def send_email(request,email):
    
    mailServer = smtplib.SMTP(settings.EMAIL_HOST,settings.EMAIL_PORT)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.login(settings.EMAIL_HOST_USER,settings.EMAIL_HOST_PASSWORD)
    print("Mail server started successfully")

        # Construimos el mensaje simple
    mensaje = MIMEMultipart()
    mensaje['From']=settings.EMAIL_HOST_USER
    mensaje['To']=email
    mensaje['Subject']="alguien reservo tu publicacion de DOGGY"

    
    content = render_to_string('email_sitter_templates.html', {'user': request.user})
    mensaje.attach(MIMEText(content, 'html'))
    
        # Envio del mensaje
    mailServer.sendmail(settings.EMAIL_HOST_USER,
                    email,
                    mensaje.as_string())
