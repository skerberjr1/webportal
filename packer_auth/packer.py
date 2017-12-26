from django.db import connections
from django.contrib.auth import get_user_model
from orders.util.queries.util import *


def _get_or_create_user(user_data):

    User = get_user_model()

    user_fields = {
        'username': user_data['LastName'] + user_data['FirstName'],
        'password': user_data['UserHashCode'],
        'is_staff': 0,
        'first_name': user_data['FirstName'],
        'last_name': user_data['LastName']
    }

    user_lookup = {
        'username': user_data['LastName'] + user_data['FirstName']
    }

    user, created = User.objects.update_or_create(
        defaults=user_fields,
        **user_lookup
    )

    return user

def get_user(id):
    cursor = connections['syspro'].cursor()

    cursor.execute("""
        SELECT *
        FROM TimeClockEmployee
        WHERE PayType = 'Hourly'
        AND Deleted = 0
        AND UserHashCode = %s
        """, [id])

    try:
        user = dictfetchone(cursor)
        return _get_or_create_user(user)
    except TypeError:
        return None

def authenticate(**kwargs):
    password = kwargs.pop("password")

    if not password:
        return None

    return get_user(password)