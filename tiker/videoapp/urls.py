from django.urls import path
from . import views

urlpatterns = [
    path('generate/', views.generate_video_view, name='generate'),
]