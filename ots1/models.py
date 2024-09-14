from django.db import models

class Candidate(models.Model):
    username=models.CharField(primary_key=True,max_length=20)
    password=models.CharField(null=False, max_length=20)
    name=models.CharField(null=False,max_length=30)
    test_attempted=models.IntegerField(default=0)
    points=models.FloatField(default=0.0)

class Question(models.Model):
    qid=models.BigAutoField(primary_key=True,auto_created=True)
    ques=models.TextField(255)
    a=models.CharField(max_length=255)
    b=models.CharField(max_length=255)
    c=models.CharField(max_length=255)
    d=models.CharField(max_length=255)
    ans=models.CharField(max_length=20)

class Result(models.Model):
    resultid=models.BigAutoField(primary_key=True,auto_created=True)
    username=models.ForeignKey(Candidate,on_delete=models.CASCADE)
    date=models.DateField(auto_now=True)
    time=models.TimeField(auto_now=True)
    attempt=models.IntegerField(default=0)
    right=models.IntegerField(default=0)
    wrong=models.IntegerField(default=0)
    points=models.FloatField(default=0.0) 