from django.contrib import admin
from .models import Exam, Question, Answer,TestRequest

# Register your models here.
admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(TestRequest)
