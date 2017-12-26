from django.shortcuts import render
from orders.util.queries.count_queries import *
from orders.util.queries.select_queries import *
from orders.util.queries.detail_queries import *
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import OrderSearchForm
from django import forms
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from .tables import CustomerOrdersTable, TransfersTable
from django_tables2 import RequestConfig
from authentication.models import Account


def group_required(*group_names):
    """Requires user membership in at least one of the groups passed in."""
    def in_groups(u):
        if u.is_authenticated():
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser | u.is_admin:
                return True
        return False
    return user_passes_test(in_groups, login_url='/orders/denied/')

# Create your views here.

@login_required
@user_passes_test(lambda u: u.is_staff)
def index(request):
    open_orders = select_open_orders()
    orders_by_status = order_count_status(date.today().strftime("%m/%d/%Y"), 'ST')

    context = {
        'open_orders': open_orders,
        'orders_by_status': orders_by_status,
    }
    return render(request, 'orders/overview/index.html', context)

def denied(request):
    return render(request, 'orders/errors/access_restricted.html')

@login_required
@user_passes_test(lambda u: u.is_staff)
@group_required('Customer Service')
def detail(request, order_id):
    try:
        sales_order = select_single_order(int(order_id))
        sales_order_detail = select_order_detail(int(order_id))
    except TypeError:
        return render(request, 'orders/errors/order_404.html')
    return render(request, 'orders/detail.html', {'sales_order': sales_order, 'sales_order_detail': sales_order_detail})

@login_required
@user_passes_test(lambda u: u.is_staff)
def orders_charts(request, d):
    d_split = []
    d_split = d.split('.')
    orders_date = date(month=int(d_split[0]), day=int(d_split[1]), year=int(d_split[2]))
    orders_by_status = order_count_status(orders_date.strftime("%m/%d/%Y"), 'ST')

    context = {
        'orders_by_status': orders_by_status,
    }
    return render(request, 'orders/overview/charts.html', context)

@login_required
@user_passes_test(lambda u: u.is_staff)
def status_chart(request):
    orders = order_count_status(datetime.today().strftime("%m/%d/%Y"), 'ST')

    return render(request, 'orders/overview/status_chart.html', {'orders': orders})

@login_required
@user_passes_test(lambda u: u.is_staff)
def hour_chart(request):
    kwargs = request.GET.dict()
    begin_date = kwargs.pop('begin_date').replace('.', '/')
    end_date = kwargs.pop('end_date').replace('.', '/')
    interval = kwargs.pop('interval')

    orders = order_count_hour(begin_date, end_date, interval, **kwargs)

    return render(request, 'orders/overview/hour_chart.html', {'orders': orders})

@login_required
@user_passes_test(lambda u: u.is_staff)
def orders_for_hour(request):
    hour = request.GET.get('hour')
    date = request.GET.get('date').replace('.', '/')

    orders_for_hour = orders_by_hour(hour, date)
    context = {
        'orders_for_hour': orders_for_hour,
    }
    return render(request, 'orders/overview/hour_table.html', context)

@login_required
@user_passes_test(lambda u: u.is_staff)
def orders_for_status(request):
    status = request.GET.get('status')
    date = request.GET.get('date').replace('.', '/')

    orders_for_status = orders_by_status(status, date)
    context = {
        'orders_for_status': orders_for_status,
        'status': status,
    }
    return render(request, 'orders/overview/status_table.html', context)

@login_required
@user_passes_test(lambda u: u.is_staff)
def open_orders(request):
    open_orders = select_open_orders()
    return render(request, 'orders/open_orders.html', {'open_orders': open_orders})

@login_required
@user_passes_test(lambda u: u.is_staff)
def warehouse_orders(request):
    warehouse_orders = select_transfer_orders()
    return render(request, 'orders/warehouse_orders/warehouse_orders.html', {'warehouse_orders': warehouse_orders})

@login_required
@user_passes_test(lambda u: u.is_staff)
def warehouse_chart(request):
    orders_by_status = warehouse_order_status()
    return render(request, 'orders/warehouse_orders/warehouse_chart.html', {'orders_by_status': orders_by_status})

@login_required
@user_passes_test(lambda u: u.is_staff)
def backorder_orders(request):
    backorder_orders = select_backorder_orders()
    return render(request, 'orders/backorder_orders.html', {'backorder_orders': backorder_orders})

@login_required
@user_passes_test(lambda u: u.is_staff)
def search_orders(request):
    form = OrderSearchForm()

    return render(request, 'orders/order_search.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_staff)
def search_results(request):

    form = OrderSearchForm(request.GET)
    kwargs = {}
    try:
        form.is_valid()
        form_cleaned = form.clean()
        for field, value in form_cleaned.items():
            if value != '' and value is not None and value != []:
                kwargs[field] = value

    except forms.ValidationError as err:
        messages.error(request, err.args)
        return render(request, 'orders/order_search.html', {'form': form})

    search_results = select_search_orders(**kwargs)

    if search_results == []:
        return render(request, 'orders/errors/no_results.html')
    else:
        return render(request, 'orders/search_results.html', {'search_results': search_results})


@login_required
@user_passes_test(lambda u: u.is_staff)
def customer_detail(request, customer):
    orders = select_customer_orders(customer)
    table = CustomerOrdersTable(orders)
    RequestConfig(request, paginate={'per_page': 5}).configure(table)

    context = {
        'customer': customer,
        'customer_orders_table': table,
    }

    return render(request, 'orders/customer_detail.html', context)


@login_required
@user_passes_test(lambda u: u.is_staff)
def transfer_orders_chart(request, begin_date, end_date, interval):
    begin_date_split = begin_date.split('.')
    end_date_split = end_date.split('.')
    orders_begin_date = date(month=int(begin_date_split[0]), day=int(begin_date_split[1]), year=int(begin_date_split[2]))
    orders_end_date = date(month=int(end_date_split[0]), day=int(end_date_split[1]), year=int(end_date_split[2]))

    transfer_orders = order_count_transfer(orders_begin_date.strftime("%m/%d/%Y"), orders_end_date.strftime("%m/%d/%Y"), interval)

    return render(request, 'orders/warehouse_orders/transfer_orders_chart.html', {'transfer_orders': transfer_orders})

@login_required
@user_passes_test(lambda u: u.is_staff)
def transfer_orders_table(request):
    begin_date = datetime.strptime(request.GET.get('select_date'), "%m/%d/%Y")
    interval = request.GET.get('interval')
    
    if interval == 'Day':
        end_date = begin_date
    elif interval == 'Week':
        end_date = begin_date + relativedelta(days=7)
    elif interval == 'Month':
        end_date = begin_date + relativedelta(months=1)

    orders = transfer_orders(begin_date.strftime("%m/%d/%Y"), end_date.strftime("%m/%d/%Y"))

    return render(request, 'orders/warehouse_orders/transfer_orders_table.html', {'transfer_orders': orders})

@login_required
@user_passes_test(lambda u: u.is_staff)
def boxes_chart(request):
    d = request.GET.get('completed_date')
    date_split = d.split('.')
    boxes_date = date(month=int(date_split[0]), day=int(date_split[1]), year=int(date_split[2]))

    boxes = box_count_hour(boxes_date.strftime("%m/%d/%Y"))

    return render(request, 'orders/completed_boxes/boxes_chart.html', {'boxes': boxes})

@login_required
def packer_chart(request):
    begin_date = request.GET.get('begin_date').replace('.', '/')
    end_date = request.GET.get('end_date').replace('.', '/')
    interval = request.GET.get('interval')
    order_type = request.GET.get('order_type')
    packer = request.GET.get('packer')
    shipment_pack = request.GET.get('shipment_pack')

    shipments = shipment_count_packer(begin_date, end_date, interval, order_type, packer, shipment_pack)
    if packer == 'all':
        packers = get_packers(begin_date, end_date, order_type)
    else:
        packers = ((packer,),)

    context = {
        'shipments': shipments,
        'packers': packers
    }

    return render(request, 'orders/packer_overview/packer_chart.html', context)

@login_required
@user_passes_test(lambda u: u.is_staff)
def item_sales(request):
    product_classes = select_product_classes()
    skus = select_skus(sample=False)
    mpns = select_mpns()
    brands = select_brands()
    manufacturers = select_manufacturers()
    suppliers = select_suppliers()
    context = {'product_classes': product_classes, 'skus': skus, 'mpns': mpns, 'brands': brands, 'manufacturers': manufacturers, 'suppliers': suppliers}

    return render(request, 'orders/item_sales/item_sales.html', context)

@login_required
@user_passes_test(lambda u: u.is_staff)
def item_sales_table(request):
    begin_date = request.GET.get('begin_date').replace('.', '/')
    end_date = request.GET.get('end_date').replace('.', '/')
    group = request.GET.get('group')
    channel = request.GET.get('channel')

    list_qty_sold = top_skus(begin_date, end_date, group, 'qty_sold', channel)
    list_num_orders = top_skus(begin_date, end_date, group, 'num_orders', channel)
    list_sales_value = top_skus(begin_date, end_date, group, 'sales_value', channel)
    if group == 'sku':
        group_name = 'SKU'
    elif group == 'mpn':
        group_name = 'MPN'
    elif group == 'product_class':
        group_name = 'Product Class'
    elif group == 'brand':
        group_name = 'Brand'
    elif group == 'manufacturer':
        group_name = 'Manufacturer'
    elif group == 'supplier':
        group_name = 'Supplier'

    context = {
        'list_qty_sold': list_qty_sold,
        'list_num_orders': list_num_orders,
        'list_sales_value': list_sales_value,
        'group_name': group_name,
    }

    return render(request, 'orders/item_sales/item_sales_table.html', context)

@login_required
@user_passes_test(lambda u: u.is_staff)
def item_sales_selection_table(request):
    begin_date = datetime.strptime(request.GET.get('begin_date'), '%m/%d/%Y')
    end_date = datetime.strptime(request.GET.get('end_date'), '%m/%d/%Y')
    select_date = request.GET.get('select_date')
    interval = request.GET.get('interval')
    salesperson = request.GET.get('salesperson')
    group = request.GET.get('group')
    item = request.GET.get('item')

    if group == 'supplier':
        item = item[-15:]

    if interval == 'day':
        select_date = datetime.strptime(select_date, '%m/%d/%Y')
        selection_begin_date = select_date
        selection_end_date = select_date + relativedelta(days=1)
    elif interval == 'week':
        select_date = datetime.strptime(select_date, '%m/%d/%Y')
        selection_begin_date = max(select_date, begin_date)
        selection_end_date = min(select_date + relativedelta(days=(7 - select_date.weekday())), end_date + relativedelta(days=1))
    elif interval == 'month':
        select_date = date(select_date.split('/')[1], select_date.split('/')[0], 1)
        selection_begin_date = max(select_date, begin_date)
        selection_end_date = min(select_date + relativedelta(months=1), end_date + relativedelta(days=1))
    elif interval == 'year':
        select_date = date(select_date, 1, 1)
        selection_begin_date = max(select_date, begin_date)
        selection_end_date = min(select_date + relativedelta(years=1), end_date + relativedelta(days=1))

    orders = salesperson_interval_orders(selection_begin_date, selection_end_date, salesperson, group, item)

    context = {
        'orders': orders,
    }

    return render(request, 'orders/item_sales/item_sales_selection_table.html', context)
