from datetime import timedelta, time
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError

from .models import Schedule, User
from .seralizers import ScheduleSerializer


class ScheduleCreateView(APIView):
    """Handles creation of new medication schedule."""

    def post(self, request):
        serializer = ScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"schedule_id": serializer.instance.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ScheduleListView(APIView):
    """Returns list of schedule IDs for a specific user."""

    def get(self, request):
        user_id = request.query_params.get('user_id')
        if not user_id:
            return Response({"error": "user_id is required"}, status=status.HTTP_400_BAD_REQUEST)

        schedules = Schedule.objects.filter(user_id=user_id).values_list('id', flat=True)
        return Response({"schedules": list(schedules)}, status=status.HTTP_200_OK)


class ScheduleDetailView(APIView):
    """Returns detailed information about a schedule, including today's takings."""

    def get(self, request):
        user_id = request.query_params.get('user_id')
        schedule_id = request.query_params.get('schedule_id')

        if not user_id or not schedule_id:
            return Response({"error": "user_id and schedule_id are required"}, status=status.HTTP_400_BAD_REQUEST)

        schedule = get_object_or_404(Schedule, user_id=user_id, id=schedule_id)

        times = []
        day_start = time(hour=8, minute=0)
        current_time = schedule.taking_time

        if current_time.time() < day_start:
            current_time = current_time.replace(hour=8, minute=0, second=0)

        end_of_day = current_time.replace(hour=22, minute=0, second=0)

        while current_time <= end_of_day:
            times.append(current_time.strftime("%H:%M"))
            current_time += timedelta(hours=schedule.frequency)

        serializer = ScheduleSerializer(schedule)
        return Response({
            "schedule": serializer.data,
            "takings_for_today": times
        }, status=status.HTTP_200_OK)


class NextTakingsView(APIView):
    """Returns next scheduled takings for a user within the next hour."""

    def get(self, request):
        user_id = request.query_params.get('user_id')
        if not user_id:
            raise ValidationError("user_id is required")

        user = get_object_or_404(User, user_id=user_id)
        current_time = timezone.now()
        end_of_day = current_time.replace(hour=22, minute=0, second=0)

        next_hour = current_time + timedelta(hours=1)
        if next_hour > end_of_day:
            next_hour = end_of_day

        queryset = Schedule.objects.filter(
            user=user,
            taking_time__gte=current_time,
            taking_time__lte=next_hour
        ).order_by('taking_time')[:5]

        serializer = ScheduleSerializer(queryset, many=True)
        return Response(serializer.data)
