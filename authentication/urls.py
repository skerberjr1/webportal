from django.conf.urls import url

from authentication.views import *

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', AccountProfileView.as_view(), name='account_profile'),
    url(r'^list/$', AccountListView.as_view(), name='account_list'),
    url(r'^list/(?P<pk>\d+)/$', AccountDetailView.as_view(template_name='authentication/account_list_detail.html'), name='account_list_detail'),
]