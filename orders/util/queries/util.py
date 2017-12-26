from django.db import connections
from collections import namedtuple

#-----------------------------------------------------------------------------------------------------------#
#                                                                                                           #
#       Query fetch utils                                                                                   #
#                                                                                                           #
#-----------------------------------------------------------------------------------------------------------#

def namedtuplefetchall(cursor):
    #Return all rows from a cursor as a namedtuple
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*[field_trim(r) for r in row]) for row in cursor.fetchall()]

def dictfetchall(cursor):
    #Return all rows from a cursor as a dict
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def dictfetchone(cursor):
    #Return one row from a cursor as a dict
    columns = [col[0] for col in cursor.description]
    order = dict(zip(columns, cursor.fetchone()))
    order_stripped = dict()
    for k, v in order.items():
        if type(v) == str:
            order_stripped.update({k: field_trim(v.strip())})
        else:
            order_stripped.update({k: v})
    return order_stripped

def field_trim(field):
    try:
        if len(field) > 12 and field.isdigit():
            return field[-8:]
        else:
            return field
    except:
        return field

def get_packers(begin_date, end_date, order_type):
    query = ("""
        SELECT REPLACE(REPLACE(REPLACE(User1, ', ', '-'), ' ', '_'), '.', '')
        FROM NorthShoreShipmentMaster
        WHERE CONVERT(date, DateTimeCompleted) BETWEEN '%s' AND '%s'
    """ % (begin_date, end_date))

    if order_type == 'ST':
        query += " AND OrderType IN ('ST', 'UF') "
    elif order_type == 'TR':
        query += " AND OrderType = 'TR' "

    query += "GROUP BY User1"


    cursor = connections['syspro'].cursor()
    cursor.execute(query)
    packers = cursor.fetchall()
    cursor.close()
    return packers
