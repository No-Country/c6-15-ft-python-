from django.conf import settings
from django.shortcuts import render
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
# Create your views here.

def send_email(mail):
    context = {'mail':mail}

    template = get_template('mail.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        'nuevo contacto',
        'solicitu de ayuda',
        settings.EMAIL_HOST_USER,
        [mail]
    )

    email.attach_alternative(content, 'text,html')
    email.send()



#user contact with us
def user_help(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            mail = request.POST.get('mail')
            #message = request.POST.get('message')

            send_email(mail)

    return render(request,'help.html', {})

