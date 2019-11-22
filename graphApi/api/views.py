from django.shortcuts import render
from django.core.mail import send_mail
from sendsms.message import SmsMessage
from .models import EmailSubscriber
from django.utils import timezone
from datetime import timedelta
import random

# Create your views here.
def home(request):
    # for i in range(0, 100):
    #     EmailSubscriber.objects.create(email=f"user_{i}@email.com", created_at=timezone.now() - timedelta(days=random.randint(0, 100)))

    
    return render(request,'home.html')

def index(request):
    send_mail(
        'Test Pentest send Mail',
        'Bonjour a tous juste un test ',
        'patrick.dagouagauvci.edu.ci',
        ['patrick.dagouagagmail.com'],
        fail_silently=False,
    )
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~MESSAGES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")
    
    message = SmsMessage(body='Bonjour a tous ', from_phone='+41791111111', to=['+79962642'])
    message.send()
    return render(request,'pages/index.html')

def cat(request,pk):
    data={
        'pk':pk
    }
    return render(request,'pages/ingrediant.html',data)

def detail(request):
    return render(request,'pages/detail.html')