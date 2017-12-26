import django_tables2 as tables
from .models import SorMaster, SorMasterRep, ArCustomer
import datetime
from django.utils.safestring import mark_safe

class IndexOrderTable(tables.Table):

    def render_salesorder(self, value):
        return value.lstrip('0')

    class Meta:
        model = SorMaster
        fields = ['salesorder', 'customerponumber', 'shipaddress1', 'orderstatus', 'order_time']
        attrs = {'class': 'table table-responsive', 'data-type': 'order'}
        row_attrs = {'class': 'clickable-row'}
        orderable = False

class IndexCustomerTable(tables.Table):

    def render_customer(self, value):
        return value.lstrip('0')

    class Meta:
        model = ArCustomer
        fields = ['customer', 'name', 'email']
        attrs = {'class': 'table table-responsive', 'data-type': 'customer'}
        row_attrs = {'class': 'clickable-row'}
        orderable = False

class CustomerOrderTable(tables.Table):

    def render_salesorder(self, value):
        return mark_safe('<a href="/syspro_web/order/' + value.lstrip('0') + '">' + value.lstrip('0') + '</a>')

    def render_orderdate(self, value):
        return value.strftime('%b %-d, %Y')

    class Meta:
        fields = ['salesorder', 'customerponumber', 'orderstatus', 'documenttype', 'orderdate', 'salesperson']
        model = SorMaster
        attrs = {'class': 'table table-responsive', 'data-type': 'order'}
        verbose_name = 'Sales Orders'
        row_attrs = {'class': 'clickable-row'}

class CustomerReprintTable(tables.Table):

    def render_salesorder(self, value):
        return value.lstrip('0')

    def render_orderdate(self, value):
        return value.strftime('%b %-d, %Y')

    class Meta:
        fields = ['salesorder', 'customerponumber', 'documenttype', 'orderdate', 'salesperson']
        model = SorMasterRep
        attrs = {'class': 'table table-responsive', 'data-type': 'order'}

class CustomerSearchTable(tables.Table):
    container = 'search_table'

    def render_customer(self, value):
        return value.lstrip('0')

    def render_datecustadded(self, value):
        if value:
            return value.strftime('%b %-d, %Y')
        return value

    class Meta:
        model = ArCustomer
        fields = ['customer', 'name', 'email', 'datecustadded']
        attrs = {'class': 'table table-responsive', 'data-type': 'customer'}
        row_attrs = {'class': 'clickable-row'}


class OrderSearchTable(tables.Table):
    container = 'search_table'

    def render_salesorder(self, value):
        return mark_safe('<a href="/syspro_web/order/' + value.lstrip('0') + '">' + value.lstrip('0') + '</a>')

    def render_orderdate(self, value):
        return value.strftime('%b %-d, %Y')

    class Meta:
        model = SorMaster
        fields = ['salesorder', 'orderstatus', 'customerponumber', 'customer.name', 'salesperson', 'orderdate']
        attrs = {'class': 'table table-responsive', 'data-type': 'order'}
        row_attrs = {'class': 'clickable-row'}