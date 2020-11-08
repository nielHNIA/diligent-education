from django.urls import path

app_name = 'jobs'

from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('topics/<int:topic_id>/', views.detail ,name = 'detail'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name ='about'),
    path('counselling/', views.counselling, name = 'counselling')
]
