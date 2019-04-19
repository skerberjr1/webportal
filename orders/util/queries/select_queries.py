from django.db import connections
from orders.util.queries.util import *

#-----------------------------------------------------------------------------------------------------------#
#                                                                                                           #
#       Select Queries                                                                                      #
#                                                                                                           #
#-----------------------------------------------------------------------------------------------------------#

def select_open_orders():
    cursor = connections['syspro'].cursor()

    cursor.execute("""
        SELECT CONVERT(date, OrderDate, 1) as OrderDateShort,
            CONVERT(time, DATEADD(hour, CaptureHh, DATEADD(minute, CaptureMm, 0)), 108) as OrderTime,
            CONVERT(datetime, DATEADD(hour, CaptureHh, DATEADD(minute, CaptureMm, OrderDate)), 0) as OrderDateTime,
            CONVERT(datetime, DATEADD(hour, TimeDelPrtedHh, DATEADD(minute, TimeDelPrtedMm, LastDelNote)), 0) as DelNoteDateTime,
            SorMaster.*,
            ArCustomer.Name
        FROM SorMaster
        LEFT JOIN ArCustomer ON SorMaster.Customer = ArCustomer.Customer
        WHERE OrderStatus IN ('1', '4', '8')
        AND SorMaster.OrderType <> 'TR'
        AND NOT (SorMaster.DocumentType IN ('B', 'C'))
        """)

    rows = namedtuplefetchall(cursor)
    cursor.close()

    return rows

def select_single_order(self):
    cursor = connections['syspro'].cursor()

    cursor.execute("""
        SELECT SorMaster.*,
            ArCustomer.SoldToAddr1, ArCustomer.SoldToAddr2, ArCustomer.SoldToAddr3, ArCustomer.SoldToAddr4, ArCustomer.SoldToAddr5, ArCustomer.SoldPostalCode, ArCustomer.Telephone,
            vwCustomerCFMasterAlternate.*,
            CONVERT(date, OrderDate, 1) as OrderDateShort,
            CONVERT(time, DATEADD(hour, CaptureHh, DATEADD(minute, CaptureMm, 0)), 108) as OrderTime,
            CONVERT(datetime, DATEADD(hour, CaptureHh, DATEADD(minute, CaptureMm, OrderDate)), 0) as OrderDateTime
        FROM SorMaster
        LEFT JOIN ArCustomer
        ON SorMaster.Customer = ArCustomer.Customer
        LEFT JOIN vwCustomerCFMasterAlternate
        ON ArCustomer.Customer = vwCustomerCFMasterAlternate.KeyField
        WHERE SalesOrder = %s
        """, [self])
    try:
        row = dictfetchone(cursor)
    except TypeError:
        raise

    cursor.close()

    return row

def select_order_detail(self):
    cursor = connections['syspro'].cursor()

    cursor.execute("""
        SELECT SorDetail.*,
            vwInventoryComplete.Description AS FullDescription
        FROM SorDetail
        INNER JOIN vwInventoryComplete
        ON SorDetail.MStockCode = vwInventoryComplete.StockCode
        WHERE SorDetail.SalesOrder = %s
        """, [self])

    rows = namedtuplefetchall(cursor)
    return rows

def select_transfer_orders():
    cursor = connections['syspro'].cursor()

    cursor.execute("""
        SELECT CONVERT(date, SorMaster.OrderDate, 1) as OrderDateShort,
            CONVERT(time, DATEADD(hour, CaptureHh, DATEADD(minute, CaptureMm, 0)), 108) as OrderTime,
            CONVERT(datetime, DATEADD(hour, CaptureHh, DATEADD(minute, CaptureMm, OrderDate)), 0) as OrderDateTime,
            SorMaster.*,
            SorDetail.MStockCode,
            SorDetail.MOrderQty,
            IsNull(
                (
                    SELECT  Round(Sum(QtyOnHand/BomStructure.QtyPer),2)
                    FROM InvWarehouse
                    INNER JOIN BomStructure
                        ON InvWarehouse.StockCode = BomStructure.Component
                        AND InvWarehouse.Warehouse = '01'
                    WHERE BomStructure.ParentPart = SorDetail.MStockCode
                ),
                Round(I.QtyOnHand, 2)
            ) As QtyOnHandConv
        FROM SorMaster
        INNER JOIN SorDetail
            ON SorMaster.SalesOrder = SorDetail.SalesOrder
            AND SorDetail.LineType = '1'
        INNER JOIN InvWarehouse AS I
            ON SorDetail.MStockCode = I.StockCode
            AND I.Warehouse = '01'
        WHERE OrderType = 'TR'
        AND OrderStatus = '4'
    """)

    rows = namedtuplefetchall(cursor)
    cursor.close()

    return rows

def select_backorder_orders():
    cursor = connections['syspro'].cursor()

    cursor.execute("""
        SELECT CONVERT(date, OrderDate, 1) as OrderDateShort,
            CONVERT(time, DATEADD(hour, CaptureHh, DATEADD(minute, CaptureMm, 0)), 108) as OrderTime,
            CONVERT(datetime, DATEADD(hour, CaptureHh, DATEADD(minute, CaptureMm, OrderDate)), 0) as OrderDateTime,
            SorMaster.*,
            ArCustomer.Name
        FROM SorMaster
        LEFT JOIN ArCustomer ON SorMaster.Customer = ArCustomer.Customer
        WHERE OrderStatus IN ('2')
        AND SorMaster.OrderType <> 'TR'
        AND NOT (SorMaster.DocumentType IN ('B', 'C'))
        """)

    rows = namedtuplefetchall(cursor)
    cursor.close()

    return rows

def select_skus(sample):
    query = """
        SELECT StockCode
        FROM vwInventoryComplete
        WHERE Discontinued <> 'Y' 
    """

    if not sample:
        query += "AND NOT(StockCode LIKE 'SAM%%') "

    query += "ORDER BY StockCode"

    cursor = connections['syspro'].cursor()

    cursor.execute(query)

    rows = namedtuplefetchall(cursor)
    cursor.close()

    return rows

def select_mpns():
    query = """
        SELECT DISTINCT (CASE WHEN AlternateKey1 = '1225' THEN AlternateKey1 + '-' + Brand ELSE AlternateKey1 END) AS AlternateKey1
        FROM vwInventoryComplete
        WHERE Discontinued <> 'Y'
        AND AlternateKey1 <> ''
        ORDER BY AlternateKey1
    """

    cursor = connections['syspro'].cursor()

    cursor.execute(query)

    rows = namedtuplefetchall(cursor)
    cursor.close()

    return rows

def select_product_classes():
    cursor = connections['syspro'].cursor()

    cursor.execute("""
        SELECT DISTINCT ProductClass
        FROM InvMaster
        WHERE ProductClass < '4000'
        AND ProductClass <> ''
        ORDER BY ProductClass
    """)

    rows = namedtuplefetchall(cursor)
    cursor.close()

    return rows

def select_brands():
    cursor = connections['syspro'].cursor()

    cursor.execute("""
        SELECT DISTINCT Brand
        FROM [InvMaster+]
        WHERE ISNULL(Brand, '') <> ''
        AND DiscontinuedItem <> 'Y'
        ORDER BY Brand
    """)

    rows = namedtuplefetchall(cursor)
    cursor.close()

    return rows

def select_manufacturers():
    cursor = connections['syspro'].cursor()

    cursor.execute("""
        SELECT DISTINCT Manufacturer
        FROM [InvMaster+]
        WHERE ISNULL(Manufacturer, '') <> ''
        AND DiscontinuedItem <> 'Y'
        ORDER BY Manufacturer
    """)

    rows = namedtuplefetchall(cursor)
    cursor.close()

    return rows

def select_suppliers():
    cursor = connections['syspro'].cursor()

    cursor.execute("""
        SELECT SupplierName + ' - ' + Supplier AS ConcatSupplier
        FROM ApSupplier 
        WHERE Supplier in (SELECT DISTINCT Supplier
                           FROM InvMaster
                           WHERE Supplier <> '')
        ORDER BY SupplierName
    """)

    rows = namedtuplefetchall(cursor)
    cursor.close()

    return rows

def select_search_orders(*args, **kwargs):
    cursor = connections['syspro'].cursor()

    query = ("""
        SELECT DISTINCT TOP 1000 CONVERT(date, OrderDate, 1) as OrderDateShort,
            CONVERT(time, DATEADD(hour, CaptureHh, DATEADD(minute, CaptureMm, 0)), 108) as OrderTime,
            CONVERT(datetime, DATEADD(hour, CaptureHh, DATEADD(minute, CaptureMm, OrderDate)), 0) as OrderDateTime,
            CONVERT(datetime, DATEADD(hour, TimeDelPrtedHh, DATEADD(minute, TimeDelPrtedMm, LastDelNote)), 0) as DelNoteDateTime,
            SorMaster.*,
            SorMaster.ShippingInstrs AS ShipVia
        FROM SorMaster
    """)

    if 'skus' in kwargs or 'mpns' in kwargs:
        query += ("""
            INNER JOIN SorDetail ON SorMaster.SalesOrder = SorDetail.SalesOrder
            INNER JOIN vwInventoryComplete ON SorDetail.MStockCode = vwInventoryComplete.StockCode
            """)

    query += ("WHERE OrderStatus IN ('%s'" % kwargs['order_status'][0])
    for s in kwargs['order_status'][1:]:
        query += (", '%s'" % s)
    query += ")\n"

    if kwargs['order_type'] == 'ST':
        query += "AND SorMaster.OrderType IN ('ST', 'UF')\n"
    elif kwargs['order_type'] == 'AP':
        query += "AND SorMaster.OrderType = 'AP'\n"
    else:
        query += "AND SorMaster.OrderType = 'TR'\n"

    if 'sales_order' in kwargs:
        query += ("AND SorMaster.SalesOrder = %s " % kwargs['sales_order'])

    if 'customer' in kwargs:
        query += ("AND SorMaster.Customer = %s " % kwargs['customer'])

    if 'order_date_start' in kwargs:
        query += ("AND OrderDate BETWEEN CONVERT(date, '%s') " % kwargs['order_date_start'])
        query += ("AND CONVERT(date, '%s') " % kwargs['order_date_end'])

    if 'skus' in kwargs:
        if kwargs['skus_selection'] == 'OR':
            query += ("AND (1 = 2 ")
            for s in kwargs['skus']:
                query += ("OR MStockCode = '%s' " % s)
            query += (") ")
        else:
            for s in kwargs['skus']:
                query += ("AND SorMaster.SalesOrder IN (SELECT SalesOrder FROM SorDetail WHERE MStockCode = '%s') " % s)

    if 'mpns' in kwargs:
        if kwargs['mpns_selection'] == 'OR':
            query += ("AND (1 = 2 ")
            for m in kwargs['mpns']:
                query += ("OR AlternateKey1 = '%s' " % m)
            query += (") ")
        else:
            for m in kwargs['mpns']:
                query += ("""
                    AND SorMaster.SalesOrder IN (
                        SELECT SalesOrder
                        FROM SorDetail
                        JOIN vwInventoryComplete ON SorDetail.MStockCode = vwInventoryComplete.StockCode
                        WHERE AlternateKey1 = '%s'
                    ) 
                """ % m)

    if 'ship_via' in kwargs:
        query += ("AND (1 = 2 ")
        if 'fedex_standard' in kwargs['ship_via']:
            query += "OR ShippingInstrsCod IN ('FG', 'SP') "
        if 'fedex_express' in kwargs['ship_via']:
            query += "OR ShippingInstrsCod LIKE 'F[^G]' "
        if 'usps' in kwargs['ship_via']:
            query += "OR ShippingInstrsCod LIKE 'U_' "
        if 'pickup' in kwargs['ship_via']:
            query += "OR ShippingInstrsCod IN ('PU', 'NP') "
        query += (") ")

    cursor.execute(query)

    rows = namedtuplefetchall(cursor)
    cursor.close()

    return rows

def select_customer_orders(customer):
    cursor = connections['syspro'].cursor()

    cursor.execute("""
        SELECT *
        FROM SorMaster
        WHERE Customer = %s
        """, [customer])

    rows = namedtuplefetchall(cursor)
    cursor.close()
    
    return rows