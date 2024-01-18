from django.urls import path
from . import views

urlpatterns = [
    path('operations/', views.OperationsAPIView.as_view()),
]
