from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # polls라는 url로 시작하면 앱 폴더의 polls.py와 연결
    path('polls/', include('polls.urls')),
]
