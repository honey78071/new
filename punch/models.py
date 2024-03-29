from django.db import models

# Create your models here.
class contactus(models.Model):
    username=models.CharField(max_length=233)
    useremail=models.EmailField(max_length=231)
    phonenumber=models.IntegerField()
    message=models.TextField()
    myimage=models.ImageField(upload_to="userprofile",null=True,blank=True)