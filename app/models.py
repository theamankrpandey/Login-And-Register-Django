from django.db import models
# Create your models here.
class Employee(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.EmailField()
    Password=models.CharField(max_length=20)
    Cpassword=models.CharField(max_length=20)
    Profile=models.ImageField(null=True)
    Audio=models.FileField(upload_to='audio')
    Video=models.FileField(upload_to='video')
    Resume=models.FileField(upload_to='document')
    Qualification=models.CharField(max_length=50)
    Gender=models.CharField(max_length=20)
    State=models.CharField(max_length=50)
    def __str__(self):
        return str (self.Name)