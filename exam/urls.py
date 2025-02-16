from django.urls import path   
from .views import RetreveExam, QuestionViewSet, RetreveTestRequest, UpdateTestRequest

 
urlpatterns = [
    path('exams/<int:pk>/', RetreveExam.as_view(), name='get_exam_by_id'),
    path('questions/', QuestionViewSet.as_view(), name="questions"),


    path('test_request/<int:id_user>/', RetreveTestRequest.as_view(), name="test_request"),
    path('test_request/<int:pk>/update/', UpdateTestRequest.as_view(), name='test_request_update'),

]
