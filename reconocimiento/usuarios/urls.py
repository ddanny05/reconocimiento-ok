from django.urls import path
from . import views

urlpatterns = [
    path('reconocer/', views.reconocer_rostro, name='reconocer_rostro'),
]
