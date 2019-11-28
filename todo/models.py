from django.db import models


class Todo(models.Model):
    "Generated Model"
    description = models.CharField(max_length=256,)
    due_date = models.DateField(auto_now=False, auto_now_add=False,)


# Create your models here.
