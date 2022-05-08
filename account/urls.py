from django.urls import path

from account import views

urlpatterns = [
    path('get-user/', views.UserInfo.as_view()),
]
