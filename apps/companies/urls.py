from django.urls import path
from . import views

urlpatterns = [
    path('companies/', views.CompaniesAPIView.as_view()),
]
