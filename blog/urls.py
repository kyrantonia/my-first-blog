from django.conf.urls import include, url , re_path
from . import views
urlpatterns=[
    re_path(r'^$', views.post_list)
]