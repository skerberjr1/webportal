from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

from syspro_web import views
from syspro_web.views import *

urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^index/orders_table$', Index.get_recent_orders, name='orders_table'),
    url(r'^index/customers_table$', Index.get_recent_customers, name='customers_table'),
    url(r'^customer/(?P<pk>\d+)/$', CustomerDetailView.as_view(), name='customer_detail'),
    url(r'^customer/search$', views.customer_search),
    url(r'^customer/search/results$', views.customer_search_results),
    url(r'^customer/advanced_search$', CustomerSearchView.as_view(), name='customer_advanced_search'),
    url(r'^customer/advanced_search/results$', CustomerSearchResults.as_view(), name='customer_advanced_search_results'),
    url(r'^order/(?P<pk>\d+)/$', OrderDetailView.as_view(), name='order_detail'),
    url(r'^order/search$', views.order_search),
    url(r'^order/search/results$', views.order_search_results),
    url(r'^order/advanced_search$', OrderSearchView.as_view(), name='order_advanced_search'),
    url(r'^order/advanced_search/results$', OrderSearchResults.as_view(), name='order_advanced_search_results'),
    url(
        r'^logout/',
        auth_views.logout_then_login,
        {
            'extra_context': {'next': '/syspro_web/'},
            'login_url': '/syspro_web/login',
            'current_app': 'syspro_web'
        },
        name='logout'
    ),
    url(
        r'^login/',
        auth_views.login,
        {
            'extra_context': {'next': '/syspro_web/'},
            'current_app': 'syspro_web'
        },
        name='login'
    ),
]