from django.shortcuts import render, redirect
from django.core.mail import send_mail

# Create your views here.


def index(request):
    return render(request, 'MyPortafolio/index.html')


def send_email(request):
    if request.method != 'POST':
        context = {
            'fail': 'Unable to send Email...!!! Please try later.'
        }
        return render(request, 'MyPortafolio/index.html', context)

    name = request.POST['Name']
    email = request.POST['Email']
    subject = request.POST['Subject']
    message = request.POST['Message']

    send_mail(
        subject,
        f"{email} send you an email. {message}",
        email,
        ['santiago.codeapp@gmail.com'],
        fail_silently=False,
    )

    context = {
        'success': 'message'
    }
    # return redirect('index', context)
    return render(request, 'MyPortafolio/index.html', context)