from django.db import models


class User(models.Model):
    """Модель пользователя (зверя)"""
    user_id = models.CharField(max_length=50, primary_key=True, unique=True)

    def __str__(self):
        return f"User {self.user_id}"


class Schedule(models.Model):
    """Расписание приёма лекарства"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="scheludes", to_field="user_id")
    medication_name = models.CharField(max_length=255)
    frequency = models.PositiveIntegerField()
    duration = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.medication_name} for {self.user.user_id}"
