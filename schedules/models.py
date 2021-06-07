from django.db import models


# Create your models here.

class schedules(models.Model):
    Nschedule = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.Nschedule