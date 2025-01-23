# urls.py
# homework/urls.py (프로젝트의 최상위 urls.py)

from django.contrib import admin
from django.urls import path, include  # include를 사용하여 앱별 urls.py 포함

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),  # 'user' 앱의 urls.py 파일 포함
    path('post/', include('post.urls')),  # 'post' 앱의 urls.py 파일 포함
]
