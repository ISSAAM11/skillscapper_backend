from rest_framework import serializers
from .models import Exam, Question, TestRequest, Answer
import base64


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ['id', 'question_id', 'answer_text', 'score', 'next_question','video_timing' ]

class QuestionSerializer(serializers.ModelSerializer):
    # video_base64 = serializers.SerializerMethodField()

    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'question_level', 'exam_id', 'question_text', 'answers', ] # 'video_base64', 'video_file',

    # def get_video_base64(self, obj):
    #     if obj.video_file:
    #         with open(obj.video_file.path, "rb") as video_file:
    #             return base64.b64encode(video_file.read()).decode('utf-8')
    #     return None

class ExamSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Exam
        fields = ['id', 'timerQuestion', 'test_name', 'questions', 'video_file_exam', ]
 




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