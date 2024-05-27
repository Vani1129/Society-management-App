from django.db import models

from societies.models import Unit
from users.models import User

# Create your models here.
class Maintenance(models.Model):
	STATUS_CHOICES = (
    	('pending', 'Pending'),
    	('in_progress', 'In Progress'),
    	('completed', 'Completed'),
	)
	unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	description = models.TextField()
	status = models.CharField(max_length=20, choices=STATUS_CHOICES)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
