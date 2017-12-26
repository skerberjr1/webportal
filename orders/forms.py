from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from crispy_forms.bootstrap import *
from orders.util.queries.select_queries import *
from datetime import date

class OrderSearchForm(forms.Form):
    skus_tuple = select_skus(sample=True)
    skus = []
    for s in skus_tuple:
        skus.append((s.StockCode.strip(), s.StockCode.strip()))
    mpns_tuple = select_mpns()
    mpns = []
    for m in mpns_tuple:
        mpns.append((m.AlternateKey1.strip(), m.AlternateKey1.strip()))

    sales_order = forms.CharField(label='Sales Order', max_length=6, required=False)
    customer = forms.CharField(label='Customer #', max_length=7, required=False)
    order_status = forms.MultipleChoiceField(
        label='Order Status',
        required=True,
        choices=(('1', '1'), ('4', '4'), ('8', '8'), ('9', '9'), ('C', 'Cancelled'), ('F', 'Fulfilled'), ('S', 'Suspended')),
        widget=forms.CheckboxSelectMultiple,
        initial=('1', '4', '8', '9', 'C', 'F', 'S'),
    )
    order_type = forms.ChoiceField(
        label='Order Type',
        choices=(('ST', 'Standard'), ('TR', 'Transfer')),
        widget=forms.RadioSelect,
        initial='ST',
        required=True,
    )
    order_date_start = forms.DateField(label='Order Date Start', initial=date.today().strftime("%m/%d/%y"), required=False)
    order_date_end = forms.DateField(label='Order Date End', initial=date.today().strftime("%m/%d/%y"), required=False)
    skus = forms.TypedMultipleChoiceField(
        label='SKUs',
        required=False,
        choices=skus,
        coerce=str,
        # widget=forms.CheckboxSelectMultiple
    )
    skus_selection = forms.ChoiceField(
        label='',
        choices=(('OR', 'Select orders with any chosen SKU'), ('AND', 'Select orders with all chosen SKUs')),
        widget=forms.RadioSelect,
        initial='OR',
    )
    mpns = forms.TypedMultipleChoiceField(
        label='MPNs',
        required=False,
        choices=mpns,
        coerce=str,
    )
    mpns_selection = forms.ChoiceField(
        label='',
        choices=(('OR', 'Select orders with any chosen MPN'), ('AND', 'Select orders with all chosen MPNs')),
        widget=forms.RadioSelect,
        initial='OR',
    )
    ship_via = forms.MultipleChoiceField(
        label='Ship Via',
        required=False,
        choices=(('fedex_standard', 'FedEx Standard'), ('fedex_express', 'FedEx Express'), ('usps', 'USPS'), ('pickup', 'Pickup')),
        initial=('fedex_standard', 'fedex_express', 'usps', 'pickup'),
        widget=forms.CheckboxSelectMultiple,
    )

    def __init__(self, *args, **kwargs):
        super(OrderSearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-orderSearchForm'
        self.helper.form_class = 'form-vertical'
        self.helper.form_method = 'get'
        self.helper.form_action = 'search_results'
        self.helper.layout = Layout(
            'sales_order',
            'customer',
            Div(
                Div('order_status', css_class='col-md-6'),
                Div('order_type', css_class='col-md-6'),
                css_class='row',
            ),
            Div(
                Div('order_date_start', css_class='col-md-6'),
                Div('order_date_end', css_class='col-md-6'),
                title='Order Date Range',
                css_class='row',
            ),
            'skus',
            'skus_selection',
            'mpns',
            'mpns_selection',
            'ship_via',
            FormActions(
                Submit('search', 'Search'),
            )
        )

    def clean(self):
        cleaned_data = super(OrderSearchForm, self).clean()
        form_empty = True
        for field, value in cleaned_data.items():
            # Check for None or '', so IntegerFields with 0 or similar things don't seem empty.
            if value is not None and value != '':
                form_empty = False
                break
        if form_empty:
            raise forms.ValidationError("You must fill at least one field!")
        if (cleaned_data['order_date_start'] is not None or cleaned_data['order_date_end'] is not None) and (cleaned_data['order_date_start'] is None or cleaned_data['order_date_end'] is None):
            raise forms.ValidationError("Please enter both start and end dates.")

        return cleaned_data   # Important that clean should return cleaned_data!
