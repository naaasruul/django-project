from django.db import models

# Create your models here.
class Mentor(models.Model):
    mentorId = models.CharField(max_length=5, unique=True)
    mentorName = models.TextField(max_length=200)
    password = models.CharField(max_length=128)  # Add password field for Mentor

class Student(models.Model):
    studentId = models.CharField(max_length=5, unique=True)
    studentName = models.TextField(max_length=200)
    password = models.CharField(max_length=128)  # Add password field for Student
    

class Admin(models.Model):
    adminId = models.CharField(max_length=5, unique=True)
    adminName = models.TextField(max_length=200)
    password = models.CharField(max_length=128)  # Add password field for Admin

class Appointment(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    appointmentDate = models.DateField()
    # Add any other fields relevant to the appointment
    
class Report(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    reportCategory = models.TextField()
    reportText = models.TextField()
    # Add any other fields relevant to the report