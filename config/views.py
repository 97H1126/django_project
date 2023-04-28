# sns/main.html 파일을 보이게 하기 위해선  veiw라는 파일을 만들어서 연결해줘야한다.
from django.shortcuts import render
from rest_framework.views import APIView


class Main(APIView):
    def get(self, request):
        return render(request, 'sns/main.html')

# 메인이라는 클래스를 만들고 그 메인 클래스는 APIView를 작동한다는 의미
# APIView는 클라이언트와 서버가 데이터를 주고받을 수 있도록 도와주는 역할을 한다
# get과 post가 있는데 일반적으로 홈페이지를 조회하는 데는 get방식을 사용하고 특정 작업을 요청할 때는 post를 사용한다. 페이지 조회를 위해 나는 get을 사용
# return render(request, 'jinstagram/main.html')은 get으로 실행하면 render이란 기능을 사용한다는 의미 render을 사용하면 내가 만든 html을 브라우저를 통해 보여줄수 있다
