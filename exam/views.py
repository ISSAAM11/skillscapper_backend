from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .models import Exam, Question, TestRequest
from .serializers import ExamSerializer, QuestionSerializer, TestRequestSerializer, TestRequestUpdateSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

 

 
class RetreveExam(generics.RetrieveAPIView):
    queryset = Exam.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ExamSerializer
    lookup_field = "pk"

 



class RetreveTestRequest(generics.ListAPIView):
    queryset = TestRequest.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = TestRequestSerializer
    lookup_field = "id"  

    def get_queryset(self):
        user_id = self.kwargs.get("id")  
        return TestRequest.objects.filter(id_user=user_id)


class UpdateTestRequest(generics.UpdateAPIView):
    queryset = TestRequest.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = TestRequestUpdateSerializer
    lookup_field = "pk"  

