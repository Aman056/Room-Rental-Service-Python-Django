from django.db import models
from django.contrib.auth.models import User

class Signup(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20,null=True)
    image = models.FileField(null=True)
    gender = models.CharField(max_length=20, null=True)
    dob = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=50, null=True)
    def _str_(self):
        return self.user.username


class Contact(models.Model):
    full_name = models.CharField(max_length=20,null=True)
    email = models.CharField(max_length=20, null=True)
    mobile = models.CharField(max_length=50, null=True)
    comment = models.CharField(max_length=50, null=True)

class Feedback(models.Model):
    full_name = models.CharField(max_length=20,null=True)
    email = models.CharField(max_length=20, null=True)
    mobile = models.CharField(max_length=50, null=True)
    feedback = models.CharField(max_length=50, null=True)


class Room(models.Model):
    room_no = models.CharField(max_length=20,null=True,unique=True)
    price = models.CharField(max_length=50, null=True)
    r_type = models.CharField(max_length=50, null=True)
    r_image = models.FileField(max_length=50, null=True)
    status = models.CharField(max_length=50, null=True)