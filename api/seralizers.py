from datetime import timedelta
from rest_framework import serializers
from .models import User, Schedule


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'

    def validate_taking_time(self, value):
        """Rounds taking_time to the nearest 15 minutes."""

        minutes = value.minute
        rounded = (minutes + 14) // 15 * 15
        if rounded == 60:
            value = value.replace(minute=0, second=0, microsecond=0) + timedelta(hours=1)
        else:
            value = value.replace(minute=rounded, second=0, microsecond=0)
        return value
