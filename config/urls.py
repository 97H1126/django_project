"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import Main, UploadFeed
from user.views import Login, Join
from django.conf import settings
from django.conf.urls.static import static


#127.0.0.1 뒤에 붙는애들
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Main.as_view()), #메인 페이지 실행된다
    path('main/', Main.as_view()),#main/ URL 패턴을 추가 / 이부분이 있어야 로그인을 하면 나의 메인 페이지로 이동할 수 있다
    path('content/upload', UploadFeed.as_view()),  #'content/upload'로 접속할 경우 UploadFeed를 실행
    path('user/login', Login.as_view(), name='login'), #로그인으로 가는 페이지
    path('user/join', Join.as_view(), name='join'), #회원가입으로 가는 페이지

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#media 경로에 url을 포함하는 코드이다 이걸 해야만 파일을 올리면 ~/media/{파일이름}으로 조회가 가능하다
