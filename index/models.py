from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.forms import CharField

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=100, null=False)
    email=models.EmailField()
    subject=models.CharField(max_length=100, null=False)
    message=models.CharField(max_length=1000, null=False)
    def __str__(self):
        return self.name,self.email,self.subject,self.message



class Testimonial(models.Model):
    name=models.CharField(max_length=100,null=False)
    passion=models.CharField(max_length=200,null=False)
    graduation=models.TextField()
    testimonial_image =models.ImageField(upload_to="myimage")

    def __str___(self):
        return self.name,self.passion,self.graduation,self.testimonial_image




class Teacher(models.Model):
    name=models.CharField(max_length=100, null=False)
    new_image=models.ImageField(upload_to="myimage")

    def __str__(self):
        return "%s %s" %(self.name,self.new_image)

class Passout(models.Model):
    name=models.CharField(max_length=100,null=False)
    passion=models.CharField(max_length=300,null=False)
    twitter=models.CharField(max_length=300,null=False)
    facebook=models.CharField(max_length=300,null=False)
    insta=models.CharField(max_length=300,null=False)
    linked=models.CharField(max_length=300,null=False)
    passout_image=models.ImageField(upload_to="image")

    def __str__(self):    
        return "%s %s %s" %(self.name,self.passion,self.passout_image)

class Student10(models.Model):
    name=models.CharField(max_length=100,null=False)
    percent=models.CharField(max_length=100,null=False)
    img10=models.ImageField(upload_to="image")

    def __str__(self):
        return "%s %s %s" %(self.name,self.percent,self.img10)


class Student12(models.Model):
    name=models.CharField(max_length=100,null=False)
    percent=models.CharField(max_length=100,null=False)
    s_image=models.ImageField(upload_to="image")

    def __str__(self):
        return "%s %s %s" %(self.name,self.percent,self.s_image)
