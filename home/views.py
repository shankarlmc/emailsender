from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from home.forms import NotificationForm

# Create your views here.


def home(request):
    return render(request, 'home/main.html')


def sendMail(request):
    form = NotificationForm()
    if request.method == 'POST':
        receiver = request.POST.get('receiver')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if receiver == '':
            messages.error(request, 'Please enter receiver email address')
            return HttpResponseRedirect('/')

        if subject == '':
            messages.error(request, 'Please enter subject')
            return HttpResponseRedirect('/')

        if message == '':
            messages.error(request, 'Please enter message')
            return HttpResponseRedirect('/')

        sender = settings.EMAIL_HOST_USER
        email = send_mail(subject, message, sender, [
                          receiver], fail_silently=False)

        if email:
            messages.success(request, 'Mail has been sent successfully.')
            return HttpResponseRedirect('/')
        else:
            messages.error(request, 'There was an error sending an email.')
            return HttpResponseRedirect('/')
    context = {
        'form': form
    }
    return render(request, 'home/main.html', context)
