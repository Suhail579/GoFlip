from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import CharField
from django.conf import settings


from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


# Create your models here.

# Coustom User



from django.db import models
from django.contrib.auth.models import AbstractUser


class CoustomUser(AbstractUser):

    username = models.CharField(
        max_length=150,
        unique=True
    )

    email = models.EmailField(
        blank=True,
        null=True


    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    address = models.CharField(
        null=True,
        blank=True,
        max_length=100
    )

    pincode = models.IntegerField(
        null=True,
        blank=True
    )

    profile_image = models.ImageField(
        upload_to="profile/",
        null=True,
        blank=True
    )

    otp = models.IntegerField(
        null=True,
        blank=True
    )

    verified = models.BooleanField(
        default=False
    )

    phone = models.CharField(
        max_length=15,
        null=True,
        blank=True
    )

    Location = models.CharField(
        null=True,
        blank=True,
        max_length=100
    )
# Car Adding model

class Cars(models.Model):
    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True)
    Brand = models.CharField(max_length=100,null=True)
    Model = models.CharField(max_length=100,null=True)
    year = models.IntegerField(null=True)
    Fuel = models.CharField(max_length=50,null=True)
    Transmission = models.CharField(null=True,max_length=100)
    KM_drive = models.IntegerField(null=True)
    Title = models.CharField(max_length=200,null=True)
    Description = models.CharField(max_length=500,null=True)
    Price = models.IntegerField(null=True)
    Images = models.ImageField(upload_to="cars/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)


# Bike adding Model

class Bikes(models.Model):
    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True)
    Brand = models.CharField(max_length=100)
    Model = models.CharField(max_length=100)
    year = models.IntegerField()
    Fuel = models.CharField(max_length=100)
    KM_drive = models.IntegerField()
    Title = models.CharField(null=True,max_length=100)
    Ownership = models.CharField(null=True,max_length=100)
    Description = models.CharField(max_length=100)
    Price = models.IntegerField()
    Images = models.ImageField(upload_to="books/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)


# Mobile adding Model

class Mobiles(models.Model):
    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True)
    Brand = models.CharField(max_length=100)
    Model = models.CharField(max_length=100)
    year = models.IntegerField()
    Title = models.CharField(max_length=20)
    Description = models.CharField(max_length=100)
    Price = models.IntegerField()
    Images = models.ImageField(upload_to="books/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)


# Electronics adding Model

class Electronicss(models.Model):
    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True)
    Items = models.CharField(null=True,max_length=100)
    Brand  = models.CharField(null=True,max_length=100)
    year  = models.IntegerField()
    Title = models.CharField(null=True, max_length=20)
    Description = models.CharField(max_length=100)
    Price = models.IntegerField()
    Images = models.ImageField(upload_to="books/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)


# Book adding Model

class Bookss(models.Model):
    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True)
    Book_name = models.CharField(max_length=100)
    Author = models.CharField(max_length=100)
    year = models.IntegerField()
    Title = models.CharField(max_length=20)
    Description = models.CharField(max_length=100)
    Price = models.IntegerField()
    Images = models.ImageField(upload_to="books/",null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)


# Furniture adding model

class Furniture(models.Model):
    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True)
    Item = models.CharField(max_length=100)
    Brand = models.CharField(max_length=100, blank=True, null=True)
    Material = models.CharField(max_length=100)
    Condition = models.CharField(max_length=50)
    Title = models.CharField(max_length=20)
    Description = models.CharField(max_length=100)
    Price = models.IntegerField()
    Images = models.ImageField(upload_to="furniture/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

# Book adding Model

class Book_Detail(models.Model):
    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True)
    Book_name = models.CharField(max_length=100)
    Author = models.CharField(max_length=100)
    year = models.IntegerField()
    Title = models.CharField(max_length=100)
    Description = models.CharField(max_length=100)
    Price = models.IntegerField()
    Images = models.ImageField(null=True, blank=True)



# Gadgets adding Model

class Gadgets(models.Model):
    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True)
    Brand = models.CharField(max_length=100)
    Item = models.CharField(max_length=100)
    year = models.IntegerField()
    Title = models.CharField(max_length=20)
    Description = models.CharField()
    Price = models.IntegerField()
    Images = models.ImageField(upload_to="books/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
