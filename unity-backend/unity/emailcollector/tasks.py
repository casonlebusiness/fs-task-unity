import string
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from .serializers import EmailSerializer
from .models import Email
from celery import shared_task
from datetime import datetime

@shared_task
def print_new_emails():
    current_month = datetime.now().month
    thisMonthEmails = Email.objects.filter(timestamp__month=current_month)
    serializer = EmailSerializer(thisMonthEmails, many=True)
    print(serializer.data)