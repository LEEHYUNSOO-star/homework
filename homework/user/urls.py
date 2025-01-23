# user/urls.py

from django.urls import path
from . import views  # 현재 디렉토리(user) 내의 views.py 파일을 임포트

urlpatterns = [
    path('signup/', views.signup, name='signup'),  # views.signup을 호출
    path('login/', views.login_view, name='login'),  # views.login_view를 호출
    path('logout/', views.logout_view, name='logout'),  # views.logout_view를 호출
    path('profile/', views.user_profile, name='user_profile'),  # views.user_profile을 호출
]
