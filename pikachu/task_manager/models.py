from django.db import models
from django.contrib.auth.models import User
from .constants import *

# Create your models here.


class Task(models.Model):
    TASK_STATES = (
        (SUCCESS, 'success'),
        (FAILURE, 'failure'),
        (IN_PROGRESS, 'in_progress')
    )
    deadline = models.DateTimeField(null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    time_estimated = models.IntegerField(null=True)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    state = models.CharField(max_length=20, choices=TASK_STATES, default=IN_PROGRESS)
    notes = models.CharField(max_length=100, null=True)