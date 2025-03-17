from django.urls import path
from .views import ScheduleCreateView, ScheduleListView, ScheduleDetailView

app_name = 'api'


urlpatterns = [
    path('schedule-create/', ScheduleCreateView.as_view(), name='create_schedule'),
    path('schedule-list/', ScheduleListView.as_view(), name='schedule_list'),
    path('schedule-detail/<int:pk>/', ScheduleDetailView.as_view(), name='schedule_detail'),
    # path('next_takings/', NextTakingsView.as_view(), name='next_takings'),
]
