from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from syspro_web.models import *
from datetime import *
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.template.loader import render_to_string
from codecs import *
from django_tables2 import RequestConfig
import json
from django.db.models import Q, Count
import pywapi
from syspro_web.forms import *
from syspro_web.tables import *
from gviz_api import DataTable
from itertools import groupby


@login_required
def customer_search(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        customers = ArCustomer.objects.filter(name__icontains=q)[:20]
        results = []
        for customer in customers:
            customer_json = {}
            customer_json['id'] = customer.customer
            customer_json['label'] = customer.name
            customer_json['value'] = customer.name
            results.append(customer_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

@login_required
def customer_search_results(request):
    search = request.GET.get('search')
    customers = ArCustomer.objects.filter(Q(name__icontains=search) | Q(email__icontains=search))
    if len(customers) == 1:
        return redirect('customer_detail', pk=customers[0].customer)
    table = CustomerSearchTable(customers)
    RequestConfig(request).configure(table)

    return render(request, 'syspro_web/customer_search_results.html', {'customers_table': table})

@login_required
def order_search(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        orders = SorMaster.objects.filter(Q(customerponumber__icontains=q) | Q(salesorder__icontains=q))[:20]
        results = []
        for order in orders:
            match = order.customerponumber if q in order.customerponumber else order.salesorder.lstrip('0')
            order_json = {}
            order_json['id'] = order.salesorder
            order_json['label'] = match
            order_json['value'] = match
            results.append(order_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

@login_required
def order_search_results(request):
    search = request.GET.get('search')
    orders = SorMaster.objects.filter(Q(customerponumber__icontains=search) | Q(salesorder__icontains=search))
    if len(orders) == 1:
        return redirect('order_detail', pk=orders[0].salesorder)
    table = OrderSearchTable(orders)
    RequestConfig(request).configure(table)

    return render(request, 'syspro_web/order_search_results.html', {'orders_table': table})


@method_decorator(login_required, name='dispatch')
class Index(TemplateView):
    template_name = 'syspro_web/index/index.html'

    def get_context_data(self):
        context = super(Index, self).get_context_data()
        context['data_table'] = self.create_google_table()
        return context

    def get_recent_orders(self):
        salesperson = self.GET.get('salesperson')
        orders = SorMaster.objects.filter(salesperson=salesperson, documenttype='O').order_by('-salesorder')[:25]
        table = IndexOrderTable(orders, show_footer=False)
        RequestConfig(self, paginate=False).configure(table)
        return render(self, 'syspro_web/index/orders_table.html', {'orders_table': table})

    def get_recent_customers(self):
        orders = ArCustomer.objects.order_by('-customer')[:25]
        table = IndexCustomerTable(orders, show_footer=False)
        RequestConfig(self, paginate=False).configure(table)
        return render(self, 'syspro_web/index/customers_table.html', {'customers_table': table})

    def create_google_table(self):
        orders = SorMaster.objects.filter(orderdate__gt=(datetime.date.today() - datetime.timedelta(1)), ordertype='ST', documenttype='O')
        orders = orders.exclude(customerponumber__startswith='A')
        groups = orders.values('capturehh', 'orderdate', 'salesperson').annotate(Count('salesorder'))
        data = []
        for key, group in groupby(groups, lambda x: x['capturehh']):
            n = {'order_datetime': datetime.datetime(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day, key)}
            for count in group:
                n[count['salesperson']] = count['salesorder__count']
            data.append(n)

        for d in data:
            d['amazon'] = d.pop('AZ') if 'AZ' in d else 0
            d['magento'] = d.pop('MGN') if 'MGN' in d else 0
            d['phone'] = d.pop('PH') if 'PH' in d else 0

        description = {
            'order_datetime': ('datetime', ''),
            'amazon': ('number', 'Amazon'),
            'magento': ('number', 'Magento'),
            'phone': ('number', 'Phone'),
        }

        data_table = DataTable(description)
        data_table.LoadData(data)

        return data_table.ToJSon(columns_order=('order_datetime', 'amazon', 'magento', 'phone'))


@method_decorator(login_required, name='dispatch')
class CustomerDetailView(DetailView):
    model = ArCustomer
    template_name = 'syspro_web/customer_detail.html'

    def get_object(self, *args, **kwargs):
        return ArCustomer.objects.get(pk=self.kwargs['pk'].zfill(15))

    def get_context_data(self, **kwargs):
        context = super(CustomerDetailView, self).get_context_data(**kwargs)
        context['customer_plus'] = ArCustomerPlus.objects.get(pk=self.get_object().customer)

        recent_orders = SorMaster.objects.filter(customer=self.get_object().customer).order_by('-orderdate')
        reprint_orders = SorMasterRep.objects.filter(customer=self.get_object())
        reprint_orders = reprint_orders.exclude(pk__in=recent_orders).order_by('-orderdate')
        context['recent_orders'] = recent_orders
        context['reprint_orders'] = reprint_orders
        orders_table = CustomerOrderTable(recent_orders)
        RequestConfig(self.request, paginate={'per_page': 5}).configure(orders_table)
        reprint_table = CustomerReprintTable(reprint_orders, prefix='2-')
        RequestConfig(self.request, paginate={'per_page': 5}).configure(reprint_table)
        context['orders_table'] = orders_table
        context['reprint_table'] = reprint_table

        context['ship_weather'] = pywapi.get_weather_from_weather_com(self.get_object().shippostalcode, units='imperial')
        context['bill_weather'] = pywapi.get_weather_from_weather_com(self.get_object().soldpostalcode, units='imperial')

        return context


@method_decorator(login_required, name='dispatch')
class CustomerSearchView(FormView):
    template_name = 'syspro_web/customer_advanced_search.html'
    form_class = CustomerSearchForm
    success_url = 'customer_advanced_search_results'


@method_decorator(login_required, name='dispatch')
class CustomerSearchResults(ListView):
    model = ArCustomer
    template_name = 'syspro_web/advanced_search_results.html'

    def get_queryset(self):
        form = CustomerSearchForm(self.request.GET)
        form.is_valid()
        form_cleaned = form.clean()
        customers = ArCustomer.objects.none()

        kwargs = {k + '__tele' if k == 'telephone' else k + '__icontains': v for k, v in form_cleaned.items() if v}
        customers = ArCustomer.objects.filter(**kwargs)

        return customers

    def get_context_data(self, **kwargs):
        context = super(CustomerSearchResults, self).get_context_data(**kwargs)
        table = CustomerSearchTable(self.get_queryset())
        RequestConfig(self.request).configure(table)
        context['table'] = table

        return context


@method_decorator(login_required, name='dispatch')
class OrderDetailView(DetailView):
    model = SorMaster
    template_name = 'syspro_web/order_detail.html'

    def get_object(self, *args, **kwargs):
        return SorMaster.objects.get(pk=self.kwargs['pk'].zfill(15))

    def get_context_data(self, **kwargs):
        context = super(OrderDetailView, self).get_context_data(**kwargs)
        context['order_plus'] = CusSorMaster.objects.filter(pk=self.get_object(), invoicenumber=self.get_object().lastinvoice)
        context['customer'] = self.get_object().customer
        context['detail_lines'] = SorDetail.objects.filter(salesorder=self.get_object().salesorder, linetype='1').order_by('salesorderline')
        context['shipment_packs'] = NorthShoreShipmentPack.objects.filter(salesorder=self.get_object())
        return context

@method_decorator(login_required, name='dispatch')
class OrderSearchView(FormView):
    template_name = 'syspro_web/order_advanced_search.html'
    form_class = OrderSearchForm
    success_url = 'customer_advanced_search_results'

@method_decorator(login_required, name='dispatch')
class OrderSearchResults(ListView):
    model = SorMaster
    template_name = 'syspro_web/advanced_search_results.html'

    def get_queryset(self):
        form = OrderSearchForm(self.request.GET)
        form.is_valid()
        form_cleaned = form.clean()
        orders = SorMaster.objects.none()

        kwargs = {k + '__in' if isinstance(v, list) else k: v for k, v in form_cleaned.items() if v}
        orders = SorMaster.objects.filter(**kwargs)
        orders = orders.exclude(ordertype='TR')

        orders = orders.order_by('-orderdate')

        return orders

    def get_context_data(self, **kwargs):
        context = super(OrderSearchResults, self).get_context_data(**kwargs)
        table = OrderSearchTable(self.get_queryset())
        RequestConfig(self.request).configure(table)
        context['table'] = table
        return context
