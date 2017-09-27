from django.conf.urls import url
from . import views

app_name = "sitemap"

urlpatterns = [
    url(r'^$', views.Index, name='index'),
    url(r'^pages$', views.Pages, name='pages'),
    url(r'^blog$', views.Blog, name='blogs'),
    url(r'^labels$', views.Label, name='labels'),
    url(r'^records$', views.Records, name='records'),
]
