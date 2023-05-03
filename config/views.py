# sns/main.html 파일을 보이게 하기 위해선  veiw라는 파일을 만들어서 연결해줘야한다.
from django.shortcuts import render
from rest_framework.views import APIView
from content.models import Feed


class Main(APIView): # 메인이라는 클래스를 만들고 그 메인 클래스는 APIView를 작동한다는 의미 /APIView는 클라이언트와 서버가 데이터를 주고받을 수 있도록 도와주는 역할을 한다
    def get(self, request): # get과 post가 있는데 일반적으로 홈페이지를 조회하는 데는 get방식을 사용하고 특정 작업을 요청할 때는 post를 사용한다. 페이지 조회를 위해 나는 get을 사용
        feed_list = Feed.objects.all() #   # 모델 안의 데이터가 여러개라면 리스트로 작성되기 때문에 feed_list라고 이름을 붙힘 /모델을 활용하는 코드이고 모델명 +.object를 뒤에 붙여서 뒤에 데이터를 다룰 수 있다/ 즉 모델안에 있는 모든 데이터를 말한다
        return render(request, 'sns/main.html', context=dict(feed_list=feed_list))
# return render(request, 'jinstagram/main.html')은 get으로 실행하면 render이란 기능을 사용한다는 의미 render을 사용하면 내가 만든 html을 브라우저를 통해 보여줄수 있다
# 그리고 리스트로 담긴 feed_list를 context 안에 딕셔너리 형태로 집어넣어주었다 , 그리고 내가 만든 html 파일로 넘어간다./ 즉 render에 우리가 이동하고 싶은 html과 데이터를 각각 넣으면 데이터가 이동한다


