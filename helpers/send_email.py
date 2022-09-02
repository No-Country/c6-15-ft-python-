from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from gc import get_objects
from django.template.loader import render_to_string
from doggy import settings
import smtplib
from django.contrib.auth.models import User
from reservations.models import Reservations
from django.shortcuts import render, redirect, get_object_or_404

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
    mensaje['Subject']="Reservaron tu publicacion de DOGGY"

    # detail = get_object_or_404(Reservations, id = id)
    payment_type = request.POST.get('payment_type')
    payments = {1:'Efectivo',2:'Tarjeta de credito',3:'Tarjeta de debito',4:'Paypal'}
    pay_type = payments[int(payment_type)]
        
    content = render_to_string('email_sitter_templates.html', {'user': request.user, 'detalle': request.POST, 'pay_type': pay_type})
    mensaje.attach(MIMEText(content, 'html'))
    
        # Envio del mensaje
    mailServer.sendmail(settings.EMAIL_HOST_USER,
                    email,
                    mensaje.as_string())
    mailServer.close()


def send_email_owner(request,email):
    
    mailServer = smtplib.SMTP(settings.EMAIL_HOST,settings.EMAIL_PORT)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.login(settings.EMAIL_HOST_USER,settings.EMAIL_HOST_PASSWORD)
    print("Mail server started successfully")

        # Construimos el mensaje simple
    mensaje = MIMEMultipart()
    mensaje['From']=settings.EMAIL_HOST_USER
    mensaje['To']=email
    mensaje['Subject']="Haz hecho una reservacion en DOGGY"

    # detail = get_object_or_404(Reservations, id = id)
    payment_type = request.POST.get('payment_type')
    payments = {1:'Efectivo',2:'Tarjeta de credito',3:'Tarjeta de debito',4:'Paypal'}
    pay_type = payments[int(payment_type)]
        
    content = render_to_string('email_owner_templates.html', {'user': request.user, 'detalle': request.POST, 'pay_type': pay_type})
    mensaje.attach(MIMEText(content, 'html'))
    
        # Envio del mensaje
    mailServer.sendmail(settings.EMAIL_HOST_USER,
                    email,
                    mensaje.as_string())
    mailServer.close()                    