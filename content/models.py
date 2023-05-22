from django.db import models # 장고에 있는 models를 쓸 것이다

class Feed(models.Model): # 원래 이런 형식으로 작성한다 / 모델즈에서 모델에 상속하여 Feed라는 클래스를 사용한다

    content = models.TextField() # 글
    image = models.TextField() # 피드 이미지
    user_id = models.TextField() # 글쓴이



# settings.py에서 INSTALLED_APPS에 content를 주가해야함 이유는 장고프로그램에 내가 만든 앱을 사용하겠다고 명시해야되기 때문
#python manage.py makemigrations를 터미널에 작성하면
#python manage.py migrate

class Like(models.Model):
    feed_id = models.IntegerField(default=0)
    email = models.EmailField(default='')
    is_like = models.BooleanField(default=True)


class Reply(models.Model):
    feed_id = models.IntegerField(default=0)
    email = models.EmailField(default='')
    reply_content = models.TextField()


class Bookmark(models.Model):
    feed_id = models.IntegerField(default=0)
    email = models.EmailField(default='')
    is_marked = models.BooleanField(default=True)
