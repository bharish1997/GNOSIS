from django.core.validators import RegexValidator
from djongo import models
from django.contrib.auth.models import User


class Instructor(models.Model):
    first_name = models.CharField(max_length=50, validators=[
        RegexValidator('^[A-Z_]*$', 'Only uppercase letters and underscores allowed.')])
    last_name = models.CharField(max_length=50, validators=[
        RegexValidator('^[A-Z_]*$', 'Only uppercase letters and underscores allowed.')])
    age = models.IntegerField()
    gender_select = (("male", "MALE"),
                     ("female", "FEMALE"))
    gender = models.CharField(max_length=10, choices=gender_select)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

    class Meta:
        unique_together = ('first_name', 'last_name')

    def __str__(self):
        return self.first_name + " " + self.last_name


class Category(models.Model):
    title = models.CharField(max_length=100, primary_key=True)
    description = models.TextField()

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

#
# class Video(models.Model):
#     upload = models.TextField()
#     url = models.TextField(blank=True, null=True)
#
#     class Meta:
#         abstract = True


class Course(models.Model):
    instructor = models.ForeignKey(Instructor, related_name="course_creator", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, primary_key=True)
    video = models.FileField(upload_to='video/')
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class Student(models.Model):
    first_name = models.CharField(max_length=50, validators=[
        RegexValidator('^[A-Z_]*$', 'Only uppercase letters and underscores allowed.')])
    last_name = models.CharField(max_length=50, validators=[
        RegexValidator('^[A-Z_]*$', 'Only uppercase letters and underscores allowed.')])
    age = models.IntegerField()
    gender_select = (("male", "MALE"),
                     ("female", "FEMALE"))
    gender = models.CharField(max_length=10, choices=gender_select)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

    class Meta:
        unique_together = ('first_name', 'last_name')

    def __str__(self):
        return self.first_name + " " + self.last_name
