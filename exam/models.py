from django.db import models
import os
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.contrib.auth.models import User  # Import Django's User model



class Exam(models.Model):
    test_name = models.CharField(max_length=255)
    timerQuestion = models.IntegerField(default=0)
 
    def __str__(self):
        return f"Exam ID: {self.id}, Type: {self.test_name}"


class Question(models.Model):
    question_level  = models.CharField(max_length=255, default="")
    exam_id = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='questions', null=True, blank=True)
    question_text = models.CharField(max_length=255)

    def __str__(self):
        return f"level: {self.question_level},  "


class Answer(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers', null=True, blank=True)
    answer_text = models.CharField(max_length=255)
    score = models.IntegerField(default=0)   
    next_question =  models.ForeignKey(
        Question, 
        on_delete=models.CASCADE, 
        related_name='next_question_level', 
        null=True, blank=True
    )

    def __str__(self):
        return f"ID: {self.id}, score: {self.score}"



class TestRequest(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)   
    id_exam = models.ForeignKey(Exam,  on_delete=models.SET_NULL, null=True, blank=True)   
    
    is_completed = models.BooleanField(default=False)   
    time_limit = models.DateField(null=True, blank=True)
    total_score = models.IntegerField(default=0)
 
    def __str__(self):
        return f"Exam ID: {self.id}, exam_id: {self.time_limit}"
