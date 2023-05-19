from django.db import models # 장고에 있는 models를 쓸 것이다

class Feed(models.Model): # 원래 이런 형식으로 작성한다 / 모델즈에서 모델에 상속하여 Feed라는 클래스를 사용한다
    objects = None
    content = models.TextField() # 글
    image = models.TextField() # 피드 이미지
    profile_image = models.TextField() # 프로필 이미지
    user_id = models.TextField() # 글쓴이
    like_count = models.IntegerField() # 좋아요 수

# 파일을 저장하는것이 아니라 주소를 저장해놓고 불러오는 방식이다 그래서 텍스트필드로 넣어주었고 좋아요만 숫자를 세는것이기 때문에 integerfield를 넣어줬다.


# settings.py에서 INSTALLED_APPS에 content를 주가해야함 이유는 장고프로그램에 내가 만든 앱을 사용하겠다고 명시해야되기 때문
#python manage.py makemigrations를 터미널에 작성하면
#python manage.py migrate