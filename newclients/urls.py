from django.urls import path
from newclients import views

urlpatterns = [
    path('client/', views.new_client_view, name='new_client'),
    path('about/', views.about, name='about'),
    path('appointment/', views.appointment, name='appointment'),
    path('contact/', views.contact, name='contact'),
    path('news/', views.NewsListView.as_view(), name='news'),
    path('service/', views.service, name='service'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('', views.home, name='home'),
]
