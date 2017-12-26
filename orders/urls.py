from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from orders import views
from orders.views import *

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^denied/$', views.denied, name='denied'),
    url(r'^(?P<order_id>\d+)/$', views.detail, name='detail'),
    url(r'^open_orders/$', views.open_orders, name='open_orders'),
    url(r'^hour/$', views.orders_for_hour, name='orders_for_hour'),
    url(r'^status/$', views.orders_for_status, name='orders_for_status'),
    url(r'^charts/(?P<d>\d+.\d+.\d+)/$', views.orders_charts, name='orders_charts'),
    url(r'^charts/status_chart$', views.status_chart, name='status_chart'),
    url(r'^charts/hour_chart$', views.hour_chart, name='hour_chart'),
    url(r'^order_search/$', views.search_orders, name='order_search'),
    url(r'^order_search/search_results$', views.search_results, name='search_results'),
    url(r'^warehouse_orders/$', views.warehouse_orders, name='warehouse_orders'),
    url(r'^warehouse_orders/chart$', views.warehouse_chart, name='warehouse_chart'),
    url(r'^warehouse_orders/transfers_chart/(?P<begin_date>\d+.\d+.\d+)/(?P<end_date>\d+.\d+.\d+)/(?P<interval>\w+)/$', views.transfer_orders_chart, name='transfer_orders_chart'),
    url(r'^warehouse_orders/transfers_table$', views.transfer_orders_table, name='transfer_orders_table'),
    url(r'^backorder_orders/$', views.backorder_orders, name='backorder_orders'),
    url(r'^customer/(?P<customer>\d+)/$', views.customer_detail, name='customer_detail'),
    url(r'^completed_boxes/$', login_required(TemplateView.as_view(template_name='orders/completed_boxes/completed_boxes.html')), name='completed_boxes'),
    url(r'^completed_boxes/chart$', views.boxes_chart, name='boxes_chart'),
    url(r'^packer_overview$', login_required(TemplateView.as_view(template_name='orders/packer_overview/packer_overview.html')), name='packer_overview'),
    url(r'^packer_overview/chart$', views.packer_chart, name='packer_chart'),
    url(r'^item_sales$', views.item_sales, name='item_sales'),
    url(r'^item_sales/table$', views.item_sales_table, name='item_sales_table'),
    url(r'^item_sales/selection_table$', item_sales_selection_table, name='item_sales_selection_table'),
]
