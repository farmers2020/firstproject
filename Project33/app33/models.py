from django.db import models

class CourseModel(models.Model):
    cid =models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    fee = models.FloatField()

    def __str__(self):
        return self.name

class StudentModel(models.Model):
    sid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    contact = models.IntegerField()
    courseid = models.ManyToManyField(CourseModel)