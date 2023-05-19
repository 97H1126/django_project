# Create your views here.
# sns/main.html 파일을 보이게 하기 위해선  veiw라는 파일을 만들어서 연결해줘야한다.
# sns/main.html 파일을 보이게 하기 위해선  veiw라는 파일을 만들어서 연결해줘야한다.
from django.shortcuts import render
from rest_framework.views import APIView #APIView는 djangorestframework라는 패키지를 설치해야 사용할 수 있는 기능/ pip install djangorestframework
from content.models import Feed
from rest_framework.response import Response
import os
from .settings import MEDIA_ROOT
from uuid import uuid4
from datetime import datetime


class Main(APIView): # 메인이라는 클래스를 만들고 그 메인 클래스는 APIView를 작동한다는 의미 /APIView는 클라이언트와 서버가 데이터를 주고받을 수 있도록 도와주는 역할을 한다
    def get(self, request): # get과 post가 있는데 일반적으로 홈페이지를 조회하는 데는 get방식을 사용하고 특정 작업을 요청할 때는 post를 사용한다. 페이지 조회를 위해 나는 get을 사용
        print("get 으로 호출")
        feed_list = Feed.objects.all().order_by('-id')#   # 모델 안의 데이터가 여러개라면 리스트로 작성되기 때문에 feed_list라고 이름을 붙힘 /모델을 활용하는 코드이고 모델명 +.object를 뒤에 붙여서 뒤에 데이터를 다룰 수 있다/ 즉 모델안에 있는 모든 데이터를 말한다
        return render(request, 'sns/main.html', context={'feed_list': feed_list})
    def post(self, request):
        print("post 로 호출")
        feed_list = Feed.objects.all().order_by('-id')#   # 모델 안의 데이터가 여러개라면 리스트로 작성되기 때문에 feed_list라고 이름을 붙힘 /모델을 활용하는 코드이고 모델명 +.object를 뒤에 붙여서 뒤에 데이터를 다룰 수 있다/ 즉 모델안에 있는 모든 데이터를 말한다
        return render(request, 'sns/main.html', context={'feed_list': feed_list})


# return render(request, 'jinstagram/main.html')은 get으로 실행하면 render이란 기능을 사용한다는 의미 render을 사용하면 내가 만든 html을 브라우저를 통해 보여줄수 있다
# 그리고 리스트로 담긴 feed_list를 context 안에 딕셔너리 형태로 집어넣어주었다 , 그리고 내가 만든 html 파일로 넘어간다./ 즉 render에 우리가 이동하고 싶은 html과 데이터를 각각 넣으면 데이터가 이동한다

class UploadFeed(APIView):
    def post(self, request):
        file = request.FILES['file']  #file을 처리하기 위해서는 request.FILES를 통해서 파일을 읽어와야한다 / 서버에서는 올라온 파일이름 그대로를 저장하지 않고 특정 id값을 만들어 저장한다 한글이나 특수문자를 막기위해서
        uuid_name = uuid4().hex # uuid라는 값을 랜덤으로 만들어서 해당파일의 고유 id 값을으로 사용한다
        save_path = os.path.join(MEDIA_ROOT,uuid_name) # 이부분은 sns/settings.py에서 설정한 부분이다
        with open(save_path,'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        content = request.data.get('content') # 파일을 제외한 데이터는 request.data.get을 통해 가져온다
        image = uuid_name
        profile_image = request.data.get('profile_image')
        user_id = request.data.get('user_id')

        Feed.objects.create(content=content, image=image, profile_image=profile_image, user_id=user_id, like_count=0)
        #request.data.get을 통해가져온 데이터들로 Feed.object.create를 통해서 새로운 Feed를 만들어준다 / 좋아요는 처음올리면 0이기때문에 0으로 고정한다

        return Response({'message': '업로드가 완료되었습니다.'}, status=200)

    # view.py에 함수를 만들면 urls.py에서 함수에 url을 할당해줘야한다/ 사용자들이 업로드한 이미지를 사용할 수 있도록 media에 대한 url도 추가해줘야한다

