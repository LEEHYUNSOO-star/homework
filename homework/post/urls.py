# post/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),  # 게시글 목록 보기
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),  # 게시글 상세 보기
    path('create/', views.PostCreateView.as_view(), name='post_create'),  # 게시글 작성
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),  # 게시글 수정
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),  # 게시글 삭제
]
