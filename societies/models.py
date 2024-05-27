from django.db import models

# Create your models here.

class Society(models.Model):
    TYPE_CHOICES = [
        ('Bungalow', 'Bungalow'),
        ('Building', 'Building'),
        ('Both', 'Both'),
    ]
    
    
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField()
    city = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.CharField(max_length=10,blank=True, null=True)
    state = models.CharField(max_length=100,blank=True, null=True)
    country = models.CharField(max_length=100, default='India')
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='Building')
    registration_number = models.CharField(max_length=50, unique=True)
    total_bungalows = models.PositiveIntegerField(blank=True, null=True)
    total_buildings = models.PositiveIntegerField(blank=True, null=True)
    total_flats = models.PositiveIntegerField(blank=True, null=True)
    amenities = models.TextField(blank=True, null=True)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.name
    
    class Meta:
        verbose_name_plural = "Societies"


class Building(models.Model):
    name = models.CharField(max_length=100)
    society = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return f" {self.name}"

class Unit(models.Model):
	building = models.ForeignKey(Building, on_delete=models.SET_NULL, blank=True, null=True)
	unit_name = models.CharField(max_length=10)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

   