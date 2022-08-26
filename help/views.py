import email
from django.shortcuts import render
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
# Create your views here.

def send_email(email):
    context = {'email':email}

    template = get_template('mail.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        
    )

#user contact with us
def user_help(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            email = request.POST.get('email')
            message = request.POST.get('message')
            print(email)
            print(message)
        
    return render(request,'help.html')

