from rest_framework import serializers
from .models import Exam, Question, TestRequest, Answer



class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ['id', 'question_id', 'answer_text', 'score', 'next_question']

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'question_level', 'exam_id', 'question_text', 'answers']

class ExamSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Exam
        fields = ['id', 'timerQuestion', 'test_name', 'questions']
 




class ExamOnlySerializer(serializers.ModelSerializer):

    class Meta:
        model = Exam
        fields = ['id', 'test_name', 'timerQuestion']

 
class TestRequestSerializer(serializers.ModelSerializer):
    
     class Meta:
        model = TestRequest
        fields = ['id', 'id_user','id_exam','is_completed','time_limit', 'total_score', ]
        depth=1


class TestRequestUpdateSerializer(serializers.ModelSerializer):
    
     class Meta:
        model = TestRequest
        fields = ['id', 'id_user','id_exam','is_completed','time_limit', 'total_score', ]
        depth=1