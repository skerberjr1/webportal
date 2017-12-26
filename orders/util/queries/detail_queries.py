from django.db import connections
from orders.util.queries.util import *

#-----------------------------------------------------------------------------------------------------------#
#                                                                                                           #
#       Overview Detail Queries                                                                             #
#                                                                                                           #
#-----------------------------------------------------------------------------------------------------------#

def orders_by_hour(hour, date):
    query = """
        SELECT
            SalesOrder,
            CustomerPoNumber,
            OrderStatus,
            CONVERT(datetime, DATEADD(hour, CaptureHh, DATEADD(minute, CaptureMm, OrderDate)), 0) as OrderDateTime,
            Salesperson,
            Customer
        FROM SorMaster
        WHERE OrderDate = '%s'
        AND NOT (SorMaster.Salesperson IN ('AF', 'MM'))
        AND SorMaster.OrderType <> 'TR'
        AND NOT (SorMaster.DocumentType IN ('B', 'C')) 
    """ % date

    if hour != 'all':
        query += "AND CaptureHh = %s" % hour

    cursor = connections['syspro'].cursor()
    cursor.execute(query)
    rows = namedtuplefetchall(cursor)
    cursor.close()

    return rows

def orders_by_status(status, date):
    cursor = connections['syspro'].cursor()

    cursor.execute("""
        SELECT
            t.SalesOrder,
            t.Status,
            CONVERT(datetime, DATEADD(hour, t.CaptureHh, DATEADD(minute, t.CaptureMm, t.OrderDate)), 0) as OrderDateTime,
            t.Salesperson,
            t.Customer
        FROM (
            SELECT *,
                (
                    CASE
                        WHEN OrderStatus IN ('*', '\\') THEN 'Cancelled'
                        WHEN OrderStatus = 'F' THEN 'Fulfilled'
                        WHEN OrderStatus = 'S' THEN 'Suspended'
                        ELSE OrderStatus
                    END
                ) AS Status
            FROM SorMaster
            WHERE (
                NOT (OrderStatus IN ('9', '\\', '*', 'F'))
                OR (OrderStatus IN ('\\', '*', 'F') AND CONVERT(date, OrderDate) = %s)
                OR (OrderStatus = '9' AND CONVERT(date, DateLastDocPrt) = %s)
            )
            AND NOT (SorMaster.Salesperson IN ('AF', 'MM'))
            AND SorMaster.OrderType <> 'TR'
            AND NOT (SorMaster.DocumentType IN ('B', 'C'))
        ) AS t
        WHERE t.Status = %s
        """, [date, date, status])

    rows = namedtuplefetchall(cursor)
    cursor.close()

    return rows

def transfer_orders(begin_date, end_date):
    cursor = connections['syspro'].cursor()

    cursor.execute("""
        SELECT SorMaster.SalesOrder, MStockCode AS Sku, MOrderQty AS Qty, (ItemWeight * MOrderQty) AS Weight
        FROM SorMaster
        JOIN SorDetail ON SorMaster.SalesOrder = SorDetail.SalesOrder
        JOIN [InvMaster+] ON SorDetail.MStockCode = [InvMaster+].StockCode
        WHERE OrderType = 'TR'
        AND DocumentType = 'O'
        AND OrderDate BETWEEN %s AND %s
        """, [begin_date, end_date])

    rows = namedtuplefetchall(cursor)
    cursor.close()

    return rows

def salesperson_interval_orders(begin_date, end_date, salesperson, group, item):
    if group == 'sku':
        sql_group = 'D.StockCode'
    elif group == 'mpn':
        sql_group = 'I.AlternateKey1'
    elif group == 'product_class':
        sql_group = 'I.ProductClass'
    elif group == 'brand':
        sql_group = 'IP.Brand'
    elif group == 'manufacturer':
        sql_group = 'IP.Manufacturer'
    elif group == 'supplier':
        sql_group = 'I.Supplier'
        
    if salesperson == 'AmazonFBA':
        sql_salesperson = 'AF'
    elif salesperson == 'AmazonFBM':
        sql_salesperson = 'AZ'
    elif salesperson == 'Magento':
        sql_salesperson = 'MGN'
    elif salesperson == 'Overstock':
        sql_salesperson = 'OS'
    elif salesperson == 'Phone':
        sql_salesperson = 'PH'
    elif salesperson == 'Wholesale':
        sql_salesperson = 'WH'
    elif salesperson == 'Recurring':
        sql_salesperson = ''

    query = """
        SELECT DISTINCT M.SalesOrder, M.EntInvoiceDate, M.Salesperson, M.Customer, M.CustomerPoNumber
        FROM SorMasterRep AS M
        JOIN SorDetailRep AS D ON M.SalesOrder = D.SalesOrder
        JOIN InvMaster AS I ON D.StockCode = I.StockCode
        JOIN [InvMaster+] AS IP ON I.StockCode = IP.StockCode
        WHERE EntInvoiceDate >= '%s' AND EntInvoiceDate < '%s'
        AND DocumentType <> 'C'
        AND LOWER(REPLACE(%s, ' ', '-')) = LOWER('%s')
        AND M.Salesperson = '%s'
    """ % (begin_date, end_date, sql_group, item, sql_salesperson)

    if salesperson == 'Recurring':
        query = query.replace("M.Salesperson = ''", "((M.Salesperson = 'PH' AND M.OrderType = 'UF') OR (M.Salesperson = 'MGN' AND M.CustomerPoNumber LIKE 'A%'))")
    elif salesperson == 'Magento':
        query += "AND NOT M.CustomerPoNumber LIKE 'A%'"
    elif salesperson == 'Phone':
        query += "AND M.OrderType <> 'UF'"

    if item == 'all':
        query = query.replace("'all'", sql_group)

    cursor = connections['syspro'].cursor()
    cursor.execute(query)
    rows = namedtuplefetchall(cursor)
    cursor.close()

    return rows
