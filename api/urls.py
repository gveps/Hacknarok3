from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from api import views

urlpatterns = [
    path('easy', views.easy),
    path('upload/', views.upload),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


