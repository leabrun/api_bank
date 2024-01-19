from django.urls import path
from . import views

urlpatterns = [
    path('accounts/<str:companyId>', views.AccountsAPIView.as_view()),
]
