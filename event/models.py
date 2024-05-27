from django.db import models

from societies.models import Society


# Create your models here.
class Event(models.Model):
	society = models.ForeignKey(Society, on_delete=models.CASCADE)
	Event_name = models.CharField(max_length=100)
	description = models.TextField()
	date = models.DateField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
 
class Notice(models.Model):
	society = models.ForeignKey(Society, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	description = models.TextField()
	posted_date = models.DateField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

