from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^fav_book$', views.index),
    url(r'^log_out$', views.log_out),
    url(r'^add_fav_book$', views.add_fav_book),
    # url(r'^liked_book/(?P<num>\d+)$', views.liked_book),
    url(r'^update/(?P<num>\d+)$', views.update),
    url(r'^unfav/(?P<num>\d+)$', views.unfav),
    url(r'^book_info/(?P<num>\d+)$', views.book_info),
   
   
]