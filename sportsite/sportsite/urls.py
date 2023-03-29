from django.contrib import admin
from django.urls import path, include
from news import views
from django.conf.urls.static import static
from sportsite import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = views.handler404
