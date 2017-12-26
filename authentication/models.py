from django.db import models, connections
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from phonenumber_field.modelfields import PhoneNumberField
from orders.util.queries.util import *

# Create your models here.
class AccountManager(BaseUserManager):
    def create_user(self, username, email, password=None, **kwargs):
        if not username:
            raise ValueError('Users must have a valid username.')

        if not email:
            raise ValueError('Users must have a valid email.')

        account = self.model(
            email=self.normalize_email(email), username=username
        )

        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, username, email, password, **kwargs):
        account = self.create_user(username, email, password, **kwargs)

        account.is_admin = True
        account.save()

        return account

class Account(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=False)
    username = models.CharField(max_length=40, unique=True)

    department = models.CharField(max_length=40, blank=True)

    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    department = models.CharField(max_length=40, blank=True)
    phone_number = PhoneNumberField(blank=True)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    objects = AccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __unicode__(self):
        return self.username

    def __init__(self, *args, **kwargs):
        super(Account, self).__init__(*args, **kwargs)
        details = self.get_employee_details()
        if 'department' in details:
            self.department = details['department']

        # if self.department == 'Customer Service':
        #     self.is_staff = False

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name

    def has_group_permissions(self, groups):
        if (self.is_admin or self.group in groups):
            return True
        else:
            return False

    def get_employee_details(self):
        details = {}
        cursor = connections['syspro'].cursor()

        cursor.execute("""
            SELECT *
            FROM TimeClockEmployee
            WHERE Email = %s
        """, [self.email])

        try:
            row = dictfetchone(cursor)
            cursor.close()

            details['department'] = row['Department']

        except TypeError:
            pass

        cursor.close()
        return details
