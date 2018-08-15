from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^end/$', views.end, name='end'),
    url(r'^start/$', views.GamePlay.as_view(), name='start'),
    url(r'^won/(?P<score>\d+)$', views.won, name='won'),
]