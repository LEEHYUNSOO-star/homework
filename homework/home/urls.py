from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # 기본 경로에 대한 처리
]
