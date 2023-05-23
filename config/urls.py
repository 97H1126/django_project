from django.contrib import admin
from django.urls import path, include
from .views import Sub
from content.views import Main, UploadFeed
from .settings import MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', Main.as_view()), # 그냥 실행시키면 뷰에 있는 Main 클래스를 실행시키겠다
    path('content/', include('content.urls')),
    path('user/', include('user.urls')),

]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)


