# models.py
from django.db import models
from django.contrib.auth import get_user_model

# Post 모델: 게시글을 저장하는 모델
class Post(models.Model):
    title = models.CharField(max_length=200)  # 게시글 제목
    content = models.TextField()  # 게시글 내용
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)  # 작성자 (사용자 모델과 관계)
    created_at = models.DateTimeField(auto_now_add=True)  # 작성일
    updated_at = models.DateTimeField(auto_now=True)  # 수정일

    def __str__(self):
        return self.title  # 제목을 문자열로 반환
