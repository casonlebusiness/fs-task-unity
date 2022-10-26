from django.views import View
from rest_framework.views import APIView
from .pagination import CommonPagination
from .serializers import EmailSerializer
from .models import Email
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from rest_framework.generics import ListAPIView

class EmailAPI(ListAPIView):
    pagination_class = CommonPagination
    serializer_class = EmailSerializer
    queryset = Email.objects.all().order_by('id')

    def get(self, request, format=None):
        queryset = self.get_queryset()
        serializer = EmailSerializer(queryset, many=True)
        page = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(page)

    def post(self, request, format=None):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def reports(request):
    template = loader.get_template('email-report.html')
    today = datetime.today()
    current_month = datetime.now().month
    snippets = Email.objects.all().order_by('id')
    serializer = EmailSerializer(snippets, many=True)

    # Get count of emails this month
    thisMonthEmails = Email.objects.filter(timestamp__month=current_month)

    context = {
        'totalEmail': snippets.count(),
        'thisMonthEmails': thisMonthEmails.count(),
        'currentTime': today.strftime('%B %Y'),
        'listEmails': serializer.data
    }
    return HttpResponse(template.render(context, request))
