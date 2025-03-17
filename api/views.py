from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from api.models import Schedule
from api.seralizers import ScheduleSerializer


class ScheduleCreateView(APIView):

    def post(self, request: Request) -> Response:
        user_data = request.data
        serializer = ScheduleSerializer(data=user_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"schedule_id": serializer.instance.id}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ScheduleListView(ListAPIView):
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        user = self.request.user
        return Schedule.objects.filter(user=user)


class ScheduleDetailView(RetrieveAPIView):
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        user = self.request.user
        return Schedule.objects.filter(user=user)
