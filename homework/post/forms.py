from django import forms
from .models import Post

# 게시글 폼
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']  # 제목과 내용만 입력 받기
