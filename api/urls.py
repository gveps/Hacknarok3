from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from api import views

urlpatterns = [
    path('easy', views.easy),
    path('task/add_new_task', views.new_task, name='api_new_task'),
    path('upload/', views.upload),
    path('task/', views.task, name='api_task'),
    path('account/', views.account, name='api_account'),
    path('competition/', views.competition, name='api_competition'),
    path('daily/', views.daily, name='api_daily'),
    path('', views.home, name='api_home'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


