from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('student/', views.student, name = 'student'),
    path('student/data', views.student_data, name = 'student_data'),
    path('student/data/add/$', views.student_add, name = 'student_add'),
]
