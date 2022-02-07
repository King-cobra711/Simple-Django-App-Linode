from django.urls import path
from .views import HomeView, ThankYou, ContactFormView, TeacherCreateView, TeacherListView, TeacherDetailView, TeacherUpdateView, TeacherDeleteView

app_name = 'classroom'

# domain.com/classroom/
# path expects a function
# name is used for linking pages (<a>)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('thank_you/', ThankYou.as_view(), name='thank_you'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('create_teacher/', TeacherCreateView.as_view(), name='create_teacher'),
    path('teacher_list/', TeacherListView.as_view(), name='teacher_list'),
    path('teacher_detail/<int:pk>', TeacherDetailView.as_view(), name='teacher_detail'),
    path('teacher_update/<int:pk>', TeacherUpdateView.as_view(), name='teacher_update'),
    path('teacher_delete/<int:pk>', TeacherDeleteView.as_view(), name='teacher_delete'),
]