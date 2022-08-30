from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

def send_email(subject, content, email ,*args):
   
            msg = EmailMultiAlternatives(subject, content, email, [email])
            msg.attach_alternative(content ,'text/html')
            msg.send()
            

def send_email_help(request):

    if request.method == 'POST':
            user = User.objects.get(username=request.user.username)
            subject = f'Nueva solicitud de ayuda desde Doggy del usuario {user}'
            text_content = request.POST.get('message')
            email='apdoggy27@gmail.com'
            context = {
                'user':user,
                'text_content':text_content,
                'email':email
            }
            template = get_template('mail.html')
            content = template.render(context)

            send_email(subject,content, email,[email])
            return render(request, 'homepage/index.html')
        
    return render(request, 'help.html')
    
