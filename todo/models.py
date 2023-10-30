from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=20, null=False, blank=False)
    start_date = models.DateField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=True)

