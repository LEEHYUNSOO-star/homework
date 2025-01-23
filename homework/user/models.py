# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

# CustomUser 모델: 기본 User 모델을 확장하여 프로필 이미지와 소개글을 추가
class CustomUser(AbstractUser):
    # 프로필 이미지를 저장할 필드
    profile_image = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    # 사용자 소개글을 저장할 필드
    bio = models.TextField(blank=True, null=True)

# settings.py에서 기본 User 모델 대신 CustomUser를 사용하도록 지정
# AUTH_USER_MODEL = 'user.CustomUser'
