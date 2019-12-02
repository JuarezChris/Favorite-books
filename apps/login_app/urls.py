# Login urls

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^success$', views.success),
    url(r'^register_user$', views.register_users),
    url(r'^login_user$', views.login_user),
    url(r'^clear$', views.clear),
    url(r'^admin_only$', views.admin),

]