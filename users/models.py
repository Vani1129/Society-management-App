from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from societies.models import Society, Building


# Create your models here.
class MyUserManager(BaseUserManager):
    
    
    def create_user(self, full_name, phone, email=None, password=None, is_active=False):
        if not full_name:
            raise ValueError("Full name is required")
        if not email:
            raise ValueError("Email is required")
       
        user = self.model(
            full_name=full_name, phone=phone, email=email, password=password
        )
        
        user.is_admin= True
        user.set_password(password)
        user.is_active = is_active
        user.save(using=self._db)
        return user
    
    
    def create_superuser(self, full_name, phone, email=None, password=None):
        user = self.create_user(
            full_name=full_name, email=email, phone=phone, password=password
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user
    
    
    
class User(AbstractBaseUser):
    ROLE_CHOICES = (
        ('super_admin', 'Super Admin'),
        ('sub_admin', 'Sub Admin'),
        ('member', 'Member'),
    )

    MEMBER_TYPE_CHOICES = (
        ('owner', 'Owner'),
        ('tenant', 'Tenant'),
    )
    
    
    full_name = models.CharField(max_length=250)
    email = models.EmailField(null=True, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='member')
    phone = models.CharField(unique=True, max_length=15, )
    profile_pic = models.ImageField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    otp_code = models.CharField(max_length=8, blank=True, null=True)
    member_type = models.CharField(max_length=10, choices=MEMBER_TYPE_CHOICES, null=True, blank=True, default='owner')
    society = models.ForeignKey(Building, related_name='society_name_buildings', on_delete=models.CASCADE)
    building = models.ForeignKey(Building, related_name='buildings', on_delete=models.CASCADE)
    
    # required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["full_name"]

    class Meta:
        verbose_name_plural = "Users"
        
    def __str__(self):
        return self.full_name