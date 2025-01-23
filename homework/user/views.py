# views.py
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# 회원가입 뷰: 사용자가 새로운 계정을 생성하는 기능
def signup(request):
    if request.method == 'POST':  # POST 요청 시 (폼 제출 시)
        form = UserCreationForm(request.POST)  # 사용자 가입 폼
        if form.is_valid():  # 폼이 유효하면
            form.save()  # 새로운 사용자 저장
            return redirect('login')  # 로그인 페이지로 리디렉션
    else:  # GET 요청 시 (회원가입 폼을 띄울 때)
        form = UserCreationForm()
    return render(request, 'user/signup.html', {'form': form})

# 로그인 뷰: 사용자가 로그인하는 기능
def login_view(request):
    if request.method == 'POST':  # POST 요청 시 (폼 제출 시)
        form = AuthenticationForm(request, data=request.POST)  # 로그인 폼
        if form.is_valid():  # 폼이 유효하면
            user = form.get_user()  # 사용자 객체 가져오기
            login(request, user)  # 세션에 사용자 로그인
            return redirect('home')  # 홈페이지로 리디렉션
    else:  # GET 요청 시 (로그인 폼을 띄울 때)
        form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form})

# 로그아웃 뷰: 사용자가 로그아웃하는 기능
def logout_view(request):
    logout(request)  # 세션에서 로그아웃 처리
    return redirect('home')  # 홈페이지로 리디렉션

# views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# 사용자 프로필 페이지: 로그인한 사용자의 프로필을 보여주는 페이지
@login_required  # 로그인한 사용자만 접근 가능
def user_profile(request):
    return render(request, 'user/profile.html')  # 'user/profile.html' 템플릿 렌더링

# post/urls.py
from django.urls import path
from . import views  # 현재 디렉토리(post) 내의 views.py 파일을 임포트
# 또는
# from post import views  # post 앱에서 views 임포트

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('create/', views.PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]
