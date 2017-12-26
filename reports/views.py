from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Report
from django.http import Http404, HttpResponse
from collections import defaultdict

# Create your views here.

@login_required
def index(request):
    fulfillment_rate_reports = Report.objects.filter(report_type='fulfillment_rate').order_by('report_date')
    fulfillment_rate_reports_monthly = defaultdict(list)

    for r in fulfillment_rate_reports:
        month = r.name.split('_')[-3] + '/' + r.name.split('_')[-1]
        fulfillment_rate_reports_monthly[month].append(r)

    context = {
        'fulfillment_rate_reports': fulfillment_rate_reports_monthly
    }

    return render(request, 'index.html', context)

@login_required
def report_detail(request, report_id):
    try:
        report = Report.objects.get(pk=report_id)
    except Report.DoesNotExist:
        raise Http404("Question does not exist")


    with open(report.file_path, 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        return response
    pdf.closed
    # return render(request, 'report_detail.html')