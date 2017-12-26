"""webportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.urls import *
from django.contrib.auth import views as auth_views
from django.conf import settings

from rest_framework_nested import routers

from django.views.generic import TemplateView
from orders import views as orders_views
from authentication.views import AccountViewSet


router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

urlpatterns = [
    url(r'^$', orders_views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^orders/', include('orders.urls')),
    url(r'^reports/', include('reports.urls')),
    url(r'^authentication/', include('authentication.urls')),
    url(r'^syspro_web/', include('syspro_web.urls')),
    url(
        r'^login/',
        auth_views.login,
        {'template_name': 'login.html'},
        name='login'
    ),
    url(r'^passwordreset/', auth_views.password_reset, name='password_reset'),
    url(
        r'^logout/',
        auth_views.logout_then_login,
        {'extra_context': {'next': '/orders/'}},
        name='logout'
    ),
    url(
        r'^packer_logout/',
        auth_views.logout,
        {'next_page': '/warehouse_login'},
        name='packer_logout'
    ),
    url(r'^api/v1/', include(router.urls)),
    url(r'^warehouse_login/', auth_views.login, {'template_name': 'packer_login.html'}, name='packer_login')
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
