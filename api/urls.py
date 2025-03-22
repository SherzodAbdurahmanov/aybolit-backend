from django.urls import path
from .views import ScheduleCreateView, ScheduleListView, ScheduleDetailView, NextTakingsView

app_name = 'api'

urlpatterns = [
    path('schedule/', ScheduleCreateView.as_view(), name='create_schedule'),
    path('schedules/', ScheduleListView.as_view(), name='schedule_list'),
    path('schedule-detail/', ScheduleDetailView.as_view(), name='schedule_detail'),
    path('next-takings/', NextTakingsView.as_view(), name='next_takings'),
]