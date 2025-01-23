from django.shortcuts import render
from post.models import Post  # Post 모델을 가져옴

# 홈 페이지 뷰
def home(request):
    posts = Post.objects.all()  # 모든 게시글을 가져옴
    return render(request, 'home/home.html', {'posts': posts})  # 템플릿에 전달
