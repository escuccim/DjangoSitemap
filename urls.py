from django.conf.urls import url
from . import views

app_name = "sitemap"

urlpatterns = [
    url(r'^$', views.Index, name='index'),
    url(r'^pages$', views.Pages, name='pages'),
]
