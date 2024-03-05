from django.db import models
from accounts.models import CustomUser
from datetime import datetime

class CalcHistory(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    expression = models.CharField(max_length=2048)
    saved_time = models.DateTimeField(default = datetime.now)