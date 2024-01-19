from django.urls import path
from . import views

urlpatterns = [
    path('operations/<str:accountId>', views.OperationsAPIView.as_view()),
]
