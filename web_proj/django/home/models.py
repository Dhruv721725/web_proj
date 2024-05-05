from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Recipies(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    name=models.CharField(max_length=20)
    desc=models.CharField(max_length=500)
    img=models.ImageField(upload_to='recpimg')
    def __str__(self):
        return self.name


class Department(models.Model):
    department=models.CharField(max_length=20)
    date_of_establishment='26/1/2023'
    def __str__(self):
        return self.department
    class Meta:
        ordering=['department']

class StudentId(models.Model):
    st_id=models.CharField(max_length=20)
    def __str__(self):
        return self.st_id

class Student(models.Model):
    department=models.ForeignKey(Department,related_name='depart',on_delete=models.CASCADE)
    st_id=models.OneToOneField(StudentId,related_name='studentid',on_delete=models.CASCADE)
    st_name=models.CharField(max_length=20)
    st_email=models.EmailField(unique=True)
    st_age=models.IntegerField(default=18)
    st_address=models.TextField()
    def __str__(self):
        return self.st_name
    
    class Meta:
        ordering=['st_name']
        verbose_name='student'

class Sub(models.Model):
    sub_name=models.CharField(max_length=20)
    def __str__(self):
        return self.sub_name

class Sub_marks(models.Model):
    st_name=models.ForeignKey(Student,related_name='st_marks',on_delete=models.CASCADE)
    sub_name=models.ForeignKey(Sub,on_delete=models.CASCADE)
    marks=models.IntegerField()

    def __str__(self):
        return f'{self.st_name.st_name} {self.sub_name.sub_name}'
    class Meta:
        unique_together=['st_name','sub_name']
        ordering=['st_name']
