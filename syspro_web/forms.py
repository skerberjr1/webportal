from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from crispy_forms.bootstrap import *
from orders.util.queries.select_queries import *
from datetime import date
from syspro_web.models import SorMaster, InvMaster


class SelectMultipleButtonsWidget(forms.SelectMultiple):
    template_name = 'widgets/multiple_select_buttons.html'
    option_template_name = 'widgets/multiple_select_buttons_option.html'


class CustomerSearchForm(forms.Form):
    states = [('', ''), ('AL', 'AL'), ('AK', 'AK'), ('AS', 'AS'), ('AZ', 'AZ'), ('AR', 'AR'), ('CA', 'CA'), ('CO', 'CO'), ('CT', 'CT'), ('DE', 'DE'), ('DC', 'DC'), ('FL', 'FL'),
        ('GA', 'GA'), ('GU', 'GU'), ('HI', 'HI'), ('ID', 'ID'), ('IL', 'IL'), ('IN', 'IN'), ('IA', 'IA'), ('KS', 'KS'), ('KY', 'KY'), ('LA', 'LA'), ('ME', 'ME'), ('MD', 'MD'),
        ('MH', 'MH'), ('MA', 'MA'), ('MI', 'MI'), ('FM', 'FM'), ('MN', 'MN'), ('MS', 'MS'), ('MO', 'MO'), ('MT', 'MT'), ('NE', 'NE'), ('NV', 'NV'), ('NH', 'NH'), ('NJ', 'NJ'),
        ('NM', 'NM'), ('NY', 'NY'), ('NC', 'NC'), ('ND', 'ND'), ('MP', 'MP'), ('OH', 'OH'), ('OK', 'OK'), ('OR', 'OR'), ('PW', 'PW'), ('PA', 'PA'), ('PR', 'PR'), ('RI', 'RI'),
        ('SC', 'SC'), ('SD', 'SD'), ('TN', 'TN'), ('TX', 'TX'), ('UT', 'UT'), ('VT', 'VT'), ('VA', 'VA'), ('VI', 'VI'), ('WA', 'WA'), ('WV', 'WV'), ('WI', 'WI'), ('WY', 'WY')
    ]

    name = forms.CharField(label='Customer Name', required=False)
    email = forms.EmailField(label='Email', required=False)
    telephone = forms.CharField(label='Telephone', max_length=10, required=False)
    soldtoaddr3 = forms.CharField(label='Street Address', max_length=80, required=False)
    city = forms.CharField(label='City', max_length=50, required=False)
    state = forms.ChoiceField(
        label='State',
        choices=states,
        # choices=(('', ''), ('IL', 'IL'),),
        required=False
    )

    def __init__(self, *args, **kwargs):
        super(CustomerSearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'customer_search_form'
        self.helper.form_class = 'form-vertical'
        self.helper.form_method = 'get'
        self.helper.form_action = 'javascript:loadResults()'

        self.helper.layout = Layout(
            'name',
            'email',
            Field('telephone', placeholder='e.g. "8475598580"'),
            'soldtoaddr3',
            Div(
                Div('city', css_class='col-md-8'),
                Div('state', css_class='col-md-4'),
                css_class='row'
            ),
            FormActions(
                Submit('search', 'Search'),
            )
        )

    def clean(self):
        cleaned_data = super(CustomerSearchForm, self).clean()
        telephone = cleaned_data['telephone'].replace(' ', '').replace('(', '').replace(')', '').replace('.', '').replace('//', '').replace('-', '')
        cleaned_data['telephone'] = telephone

        if 'city' and 'state' in cleaned_data:
            city = cleaned_data.pop('city')
            state = cleaned_data.pop('state')
            cleaned_data['soldtoaddr5'] = city + ', ' + state

        return cleaned_data


class OrderSearchForm(forms.Form):
    orderdate = forms.DateField(
        label='Order Date',
        required=False,
        widget=forms.TextInput(     
            attrs={'type': 'date'} 
        ),
    )
    enddate = forms.DateField(
        label='End Date',
        required=False,
        widget=forms.TextInput(     
            attrs={'type': 'date'} 
        ),
    )
    orderstatus = forms.MultipleChoiceField(
        label='Order Status',
        choices=(
            (i, i) for i, j in SorMaster._meta.get_field('orderstatus').choices
        ),
        initial=['0', '1', '2', '3', '4', '8', '9'],
        widget=SelectMultipleButtonsWidget(),
        required=False,
    )
    salesperson = forms.MultipleChoiceField(
        label='Salesperson',
        choices=(('3DU', '3DU'), ('AF', 'AF'), ('AZ', 'AZ'), ('PH', 'PH'), ('MGN', 'MGN'), ('AP', 'AP')),
        initial=['3DU', 'AZ', 'PH', 'MGN'],
        widget=SelectMultipleButtonsWidget(),
        required=False,
    )
    skus = forms.TypedMultipleChoiceField(
        label='SKUs Included',
        choices=(
            (i.stockcode, i.stockcode) for i in InvMaster.objects.exclude(invmasterplus__discontinueditem='Y').filter(warehousetouse='01')
        ),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super(OrderSearchForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'order_search_form'
        self.helper.form_class = 'form-vertical'
        self.helper.form_method = 'get'
        self.helper.form_action = 'javascript:loadResults()'

        self.helper.layout = Layout(
            Div(
                Div('orderdate', css_class='col-md-6'),
                Div('enddate', css_class='col-md-6'),
                css_class='row'
            ),
            'orderstatus',
            'salesperson',
            'skus',
            FormActions(
                Submit('search', 'Search'),
            )
        )

    def clean(self):
        cleaned_data = super(OrderSearchForm, self).clean()

        if 'enddate' in cleaned_data and cleaned_data['enddate'] is not None:
            cleaned_data['orderdate'] = [cleaned_data['orderdate'], cleaned_data.pop('enddate')]

        if 'skus' in cleaned_data:
            cleaned_data['sordetail__mstockcode'] = cleaned_data.pop('skus')

        return cleaned_data
