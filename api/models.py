from django.db import models


class User(models.Model):
    """User model representing a patient or animal receiving medication."""

    user_id = models.CharField(max_length=50, primary_key=True, unique=True)

    def __str__(self):
        return f"User {self.user_id}"


class Schedule(models.Model):
    """Schedule model representing medication intake schedule."""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="schedules", to_field="user_id")
    medication_name = models.CharField(max_length=255)
    frequency = models.PositiveIntegerField(help_text="Frequency of intake in hours")
    duration = models.PositiveIntegerField(null=True, blank=True, help_text="Duration in days")
    taking_time = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.medication_name} for {self.user.user_id}"
