from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<report_id>[0-9]+)/$', views.report_detail, name='report_detail'),
]
