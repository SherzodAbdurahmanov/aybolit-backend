from rest_framework import serializers
from .models import User, Schedule

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id']


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['id', 'user', 'medication_name', 'frequency', 'duration', 'created_at']
