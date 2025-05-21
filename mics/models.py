from django.db import models

# Create your models here.

class OpenMicEvent(models.Model):
    name = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    description = models.TextField(blank=True)
    day = models.CharField(max_length=20, blank=True, null=True)
    start_time = models.CharField(max_length=20, blank=True, null=True)
    latest_end_time = models.CharField(max_length=20, blank=True, null=True)
    borough = models.CharField(max_length=50, blank=True, null=True)
    neighborhood = models.CharField(max_length=100, blank=True, null=True)
    venue_type = models.CharField(max_length=50, blank=True, null=True)
    cost = models.CharField(max_length=100, blank=True, null=True)
    stage_time = models.CharField(max_length=50, blank=True, null=True)
    signup_instructions = models.TextField(blank=True, null=True)
    hosts = models.CharField(max_length=255, blank=True, null=True)
    changes_updates = models.TextField(blank=True, null=True)
    last_verified = models.CharField(max_length=100, blank=True, null=True)
    other_rules = models.TextField(blank=True, null=True)
    reviews = models.TextField(blank=True, null=True)
    unique_identifier = models.CharField(max_length=100, blank=True, null=True)
    verification_status = models.CharField(
        max_length=20,
        choices=[
            ("verified", "Verified"),
            ("verified tediously", "Verified Tediously"),
            ("unverified", "Unverified"),
        ],
        default="unverified",
    )

    def __str__(self):
        return f"{self.name} at {self.venue} on {self.date}"
