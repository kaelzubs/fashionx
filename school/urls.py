from django.urls import path
from . import views

app_name = 'school'

urlpatterns = [
    path('', views.home, name='home'),
    path('programs/', views.program_list, name='program_list'),
    path('programs/<slug:slug>/', views.program_detail, name='program_detail'),
    path('courses/<slug:slug>/', views.course_detail, name='course_detail'),
    path('instructors/', views.instructor_list, name='instructor_list'),
    path('portfolio/', views.project_list, name='project_list'),
    path('events/', views.event_list, name='event_list'),
    path('events/<slug:slug>/', views.event_detail, name='event_detail'),
    path('contact/', views.contact, name='contact'),
]