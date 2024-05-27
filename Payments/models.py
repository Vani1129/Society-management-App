from django.db import models

from users.models import User

# Create your models here.
class Payment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	amount = models.DecimalField(max_digits=10, decimal_places=2)
	payment_date = models.DateField()
	payment_method = models.CharField(max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
