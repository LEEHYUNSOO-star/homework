# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

# 게시글 목록 보기: 모든 게시글을 리스트 형식으로 보여주는 뷰
class PostListView(ListView):
    model = Post
    template_name = 'post/post_list.html'

# 게시글 상세 보기: 개별 게시글을 상세히 보여주는 뷰
class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post_detail.html'

# 게시글 작성: 새로운 게시글을 작성하는 뷰
class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']  # 제목과 내용만 입력받음
    template_name = 'post/post_form.html'
    success_url = reverse_lazy('post_list')  # 작성 후 게시글 목록으로 리디렉션

# 게시글 수정: 기존 게시글을 수정하는 뷰
class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']  # 제목과 내용만 수정 가능
    template_name = 'post/post_form.html'
    success_url = reverse_lazy('post_list')  # 수정 후 게시글 목록으로 리디렉션

# 게시글 삭제: 게시글을 삭제하는 뷰
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post/post_confirm_delete.html'  # 삭제 확인 페이지
    success_url = reverse_lazy('post_list')  # 삭제 후 게시글 목록으로 리디렉션
