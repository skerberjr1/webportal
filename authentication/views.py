from rest_framework import permissions, viewsets
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from authentication.models import Account
from authentication.permissions import IsAccountOwner
from authentication.serializers import AccountSerializer
from authentication.forms import AccountDetailForm


class AccountViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsAccountOwner(),)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            Account.objects.create_user(**serializer.validated_data)

            return HttpResponse(serializer.validated_data, status=201)

        return HttpResponse({
            'status': 'Bad Request',
            'message': 'Account could not be created with received data.'
        }, status=400)

@method_decorator(login_required, name='dispatch')
class AccountProfileView(UpdateView):
    model = Account
    template_name = 'authentication/account_profile.html'
    form_class = AccountDetailForm
    success_url = '#'

    def get(self, request, *args, **kwargs):
        account = self.get_object()
        account.get_employee_details()

        if request.user == account:
            return super().get(request, *args, **kwargs)
        else:
            return render(request, 'orders/errors/access_restricted.html')

@method_decorator(login_required, name='dispatch')
class AccountDetailView(DetailView):
    model = Account
    template_name = 'authentication/account_list_detail.html'

@method_decorator(login_required, name='dispatch')
class AccountListView(ListView):
    queryset = Account.objects.filter(is_staff=True)
