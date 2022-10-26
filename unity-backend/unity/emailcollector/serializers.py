from rest_framework import serializers
from .models import Email
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
import humanfriendly


class EmailSerializer(serializers.ModelSerializer):
    timestampDiffNow = serializers.SerializerMethodField()

    class Meta:
        model = Email
        fields = ('id', 'email', 'timestamp', 'timestampDiffNow', 'status') 
        read_only_fields = ('timestamp', 'status')

    def get_timestampDiffNow(self, obj):
        now = timezone.now()
        originalEmailTimestamp = obj.timestamp
        return f'{humanfriendly.format_timespan(now - originalEmailTimestamp)} ago'

    