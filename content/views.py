from django.shortcuts import render
from rest_framework.views import APIView
from .models import Feed
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.response import Response

# sns/main.html 파일을 보이게 하기 위해선  veiw라는 파일을 만들어서 연결해줘야한다.
class Main(APIView): # 메인이라는 클래스를 만들고 그 메인 클래스는 APIView를 작동한다는 의미 /APIView는 클라이언트와 서버가 데이터를 주고받을 수 있도록 도와주는 역할을 한다
    def get(self, request): # get과 post가 있는데 일반적으로 홈페이지를 조회하는 데는 get방식을 사용하고 특정 작업을 요청할 때는 post를 사용한다. 페이지 조회를 위해 나는 get을 사용
        feed_list = Feed.objects.all().order_by('-id')#   # 모델 안의 데이터가 여러개라면 리스트로 작성되기 때문에 feed_list라고 이름을 붙힘 /모델을 활용하는 코드이고 모델명 +.object를 뒤에 붙여서 뒤에 데이터를 다룰 수 있다/ 즉 모델안에 있는 모든 데이터를 말한다
        for feed in feed_list:
            print(feed)

        return render(request, 'sns/main.html',context=dict(feeds=feed_list))