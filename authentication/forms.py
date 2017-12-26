from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from crispy_forms.bootstrap import *
from datetime import date
from authentication.models import Account
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget

class AccountDetailForm(forms.ModelForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    department = forms.CharField()
    phone_number = PhoneNumberField(widget=PhoneNumberInternationalFallbackWidget)

    class Meta:
        model = Account
        fields = ('username', 'email', 'department', 'phone_number')

    def __init__(self, *args, **kwargs):
        super(AccountDetailForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_id = 'account_form'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-9'
        self.helper.layout = Layout(
            Field('username', readonly='readonly'),
            Field('email', readonly='readonly'),
            'department',
            'phone_number',
            ButtonHolder(
                Submit('submit', 'Submit', css_class='button white pull-right')
            )
        )
