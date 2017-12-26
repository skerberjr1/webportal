from django.db import connections
from orders.util.queries.util import *

#-----------------------------------------------------------------------------------------------------------#
#                                                                                                           #
#       Count Queries                                                                                       #
#                                                                                                           #
#-----------------------------------------------------------------------------------------------------------#

def order_count_status(date, order_type):
    query = ("""
        SELECT
            (
                CASE
                    WHEN OrderStatus IN ('*', '\\') THEN 'Cancelled'
                    WHEN OrderStatus = 'F' THEN 'Fulfilled'
                    WHEN OrderStatus = 'S' THEN 'Suspended'
                    ELSE OrderStatus
                END
            ) AS Status,
            COUNT(SalesOrder) AS Cnt
        FROM SorMaster
        WHERE (
            NOT (OrderStatus IN ('9', '\\', '*', 'F'))
            OR (OrderStatus IN ('\\', '*', 'F') AND CONVERT(date, OrderDate) = '%s')
            OR (OrderStatus = '9' AND CONVERT(date, DateLastDocPrt) = '%s')
        )
        AND NOT (SorMaster.Salesperson IN ('AF', 'MM'))
    """ % (date, date))

    if order_type == 'ST':
        query += "AND OrderType IN ('ST', 'UF') "
    elif order_type == 'TR':
        query += "AND OrderType = 'TR' "

    query += ("""
        AND NOT (SorMaster.DocumentType IN ('B', 'C'))
        GROUP BY
            (
                CASE
                    WHEN OrderStatus IN ('*', '\\') THEN 'Cancelled'
                    WHEN OrderStatus = 'F' THEN 'Fulfilled'
                    WHEN OrderStatus = 'S' THEN 'Suspended'
                    ELSE OrderStatus
                END
            )
    """)

    cursor = connections['syspro'].cursor()

    cursor.execute(query)

    rows = namedtuplefetchall(cursor)
    cursor.close()

    return rows

def order_count_hour(begin_date, end_date, interval, **kwargs):
    query = ""

    if interval == 'hour':
        query += """
            SELECT
                (
                    CASE
                        WHEN CaptureHh = 0
                        THEN '12:00 AM'
                        WHEN CaptureHh = 12
                        THEN '12:00 PM'
                        WHEN CaptureHh < 12
                        THEN CONVERT(varchar(2), CaptureHh)  + ':00 AM'
                        ELSE CONVERT(varchar(2), CaptureHh-12) + ':00 PM'
                    END
                )  
        """
        if begin_date != end_date:
            query += " + ' ' + CONVERT(varchar, CONVERT(date, OrderDate), 101) "
        query += "AS CaptureTime, CONVERT(varchar, CONVERT(date, OrderDate), 101) AS OrderDate, "

    elif interval == 'day':
        query += "SELECT CONVERT(varchar, CONVERT(date, OrderDate), 101) AS CaptureTime, "
    elif interval == 'week':
        query += "SELECT CONVERT(varchar, CONVERT(date, MIN(OrderDate)), 101) AS CaptureTime, "
    elif interval == 'month':
        query += "SELECT CONVERT(varchar, DATEPART(mm, OrderDate)) + '/' + CONVERT(varchar, DATEPART(yyyy, OrderDate)) AS CaptureTime, "
    elif interval == 'year':
        query += "SELECT DATEPART(year, OrderDate) AS CaptureTime, "

    if 'unit_display' in kwargs:
        if kwargs['unit_display'] == 'qty_sold':
            query += """
                SUM(D.MOrderQty * ISNULL(B.QtyPer, 1)) AS Cnt,
                SUM(CASE WHEN Salesperson = 'AZ' THEN D.MOrderQty * ISNULL(B.QtyPer, 1) END) AS AZ,
                SUM(CASE WHEN (Salesperson = 'MGN' AND CustomerPoNumber LIKE 'M%%') OR Salesperson = '3DN' THEN D.MOrderQty * ISNULL(B.QtyPer, 1) END) AS MGN,
                SUM(CASE WHEN Salesperson = 'OS' THEN D.MOrderQty * ISNULL(B.QtyPer, 1) END) AS OS,
                SUM(CASE WHEN Salesperson = 'PH' AND OrderType <> 'UF' THEN D.MOrderQty * ISNULL(B.QtyPer, 1) END) AS PH,
                SUM(CASE WHEN (Salesperson = 'PH' AND OrderType = 'UF') OR (Salesperson = 'MGN' AND CustomerPoNumber LIKE 'A%%') THEN D.MOrderQty * ISNULL(B.QtyPer, 1) END) AS UF,
                SUM(CASE WHEN Salesperson = 'WH' THEN D.MOrderQty * ISNULL(B.QtyPer, 1) END) AS WH 
            """
            if 'item_sales' in kwargs:
                query += ", SUM(CASE WHEN Salesperson = 'AF' THEN D.MOrderQty * ISNULL(B.QtyPer, 1) END) AS AF "

        elif kwargs['unit_display'] == 'num_orders':
            query += """
                COUNT(DISTINCT M.SalesOrder) AS Cnt,
                COUNT(DISTINCT CASE WHEN Salesperson = 'AZ' THEN M.SalesOrder END) AS AZ,
                COUNT(DISTINCT CASE WHEN (Salesperson = 'MGN' AND CustomerPoNumber LIKE 'M%%') OR Salesperson = '3DN' THEN M.SalesOrder END) AS MGN,
                COUNT(DISTINCT CASE WHEN Salesperson = 'OS' THEN M.SalesOrder END) AS OS,
                COUNT(DISTINCT CASE WHEN Salesperson = 'PH' AND OrderType <> 'UF' THEN M.SalesOrder END) AS PH,
                COUNT(DISTINCT CASE WHEN (Salesperson = 'PH' AND OrderType = 'UF') OR (Salesperson = 'MGN' AND CustomerPoNumber LIKE 'A%%') THEN M.SalesOrder END) AS UF,
                COUNT(DISTINCT CASE WHEN Salesperson = 'WH' THEN M.SalesOrder END) AS WH 
            """
            if 'item_sales' in kwargs:
                query += ", COUNT(DISTINCT CASE WHEN Salesperson = 'AF' THEN M.SalesOrder END) AS AF "

        elif kwargs['unit_display'] == 'sales_value':
            query += """
                SUM(D.MOrderQty * D.MPrice) AS Cnt,
                SUM(CASE WHEN Salesperson = 'AZ' THEN D.MOrderQty * D.MPrice END) AS AZ,
                SUM(CASE WHEN (Salesperson = 'MGN' AND CustomerPoNumber LIKE 'M%%') OR Salesperson = '3DN' THEN D.MOrderQty * D.MPrice END) AS MGN,
                SUM(CASE WHEN Salesperson = 'OS' THEN D.MOrderQty * D.MPrice END) AS OS,
                SUM(CASE WHEN Salesperson = 'PH' AND OrderType <> 'UF' THEN D.MOrderQty * D.MPrice END) AS PH,
                SUM(CASE WHEN (Salesperson = 'PH' AND OrderType = 'UF') OR (Salesperson = 'MGN' AND CustomerPoNumber LIKE 'A%%') THEN D.MOrderQty * D.MPrice END) AS UF,
                SUM(CASE WHEN Salesperson = 'WH' THEN D.MOrderQty * D.MPrice END) AS WH 
            """
            if 'item_sales' in kwargs:
                query += ", SUM(CASE WHEN Salesperson = 'AF' THEN D.MOrderQty * D.MPrice END) AS AF "
    else:
        query += """
                COUNT(DISTINCT M.SalesOrder) AS Cnt,
                COUNT(DISTINCT CASE WHEN Salesperson = 'AZ' THEN M.SalesOrder END) AS AZ,
                COUNT(DISTINCT CASE WHEN (Salesperson = 'MGN' AND CustomerPoNumber LIKE 'M%%') OR Salesperson = '3DN' THEN M.SalesOrder END) AS MGN,
                COUNT(DISTINCT CASE WHEN Salesperson = 'OS' THEN M.SalesOrder END) AS OS,
                COUNT(DISTINCT CASE WHEN Salesperson = 'PH' AND OrderType <> 'UF' THEN M.SalesOrder END) AS PH,
                COUNT(DISTINCT CASE WHEN (Salesperson = 'PH' AND OrderType = 'UF') OR (Salesperson = 'MGN' AND CustomerPoNumber LIKE 'A%%') THEN M.SalesOrder END) AS UF,
                COUNT(DISTINCT CASE WHEN Salesperson = 'WH' THEN M.SalesOrder END) AS WH 
        """

    if interval == 'hour':
        query += ("""
        FROM SorMaster AS M
        JOIN SorDetail AS D ON M.SalesOrder = D.SalesOrder
        JOIN InvMaster AS I ON D.MStockCode = I.StockCode
        JOIN [InvMaster+] AS IP ON I.StockCode = IP.StockCode
        LEFT JOIN BomStructure AS B ON D.MStockCode = B.ParentPart
        WHERE
        (
            (
                OrderDate = '%s'
                AND CONVERT(time, DATEADD(hour, CaptureHh, DATEADD(minute, CaptureMm, 0)), 108) < '17:13'
            )
            OR
            (
                OrderDate = CONVERT(date, dateadd(d, -1, '%s'),10)
                AND CONVERT(time, DATEADD(hour, CaptureHh, DATEADD(minute, CaptureMm, 0)), 108) >= '17:13'
            ) 
        """ % (end_date, begin_date))
        if begin_date != end_date:
            query += ("""
            OR
            (
                OrderDate >= '%s' AND OrderDate < '%s'
            )
        ) 
            """ % (begin_date, end_date))
        else:
            query += ") "

    else:
        query += ("""
        FROM SorMasterRep AS M
        JOIN SorDetailRep AS D ON M.SalesOrder = D.SalesOrder AND M.InvoiceNumber = D.Invoice
        JOIN InvMaster AS I ON D.StockCode = I.StockCode
        JOIN [InvMaster+] AS IP ON I.StockCode = IP.StockCode
        LEFT JOIN BomStructure AS B ON D.StockCode = B.ParentPart
        WHERE CONVERT(date, OrderDate) BETWEEN '%s' AND '%s' 
        """ % (begin_date, end_date))

    query += """
        AND NOT (Salesperson IN ('AF', 'MM'))
        AND OrderType <> 'TR'
        AND NOT (DocumentType IN ('B', 'C')) 
    """

    if 'group' in kwargs and 'item' in kwargs and kwargs['item'] != 'all':
        item = kwargs['item']

        if kwargs['group'] == 'sku':
            group = 'D.MStockCode'
        elif kwargs['group'] == 'mpn':
            group = 'I.AlternateKey1'
            if item.split('-')[0] == '1225':
                brand = item.split('-')[1]
                item = item.split('-')[0]
                query += "AND IP.Brand = '" + brand + "' "
        elif kwargs['group'] == 'product_class':
            group = 'I.ProductClass'
        elif kwargs['group'] == 'brand':
            group = 'IP.Brand'
        elif kwargs['group'] == 'manufacturer':
            group = 'IP.Manufacturer'
        elif kwargs['group'] == 'supplier':
            group = 'I.Supplier'
            item = item[-15:]

        query += ("""
            AND LOWER(REPLACE(%s, ' ', '-')) = LOWER('%s')
        """ % (group, item))

    if interval == 'hour':
        query += "GROUP BY CaptureHh, OrderDate ORDER BY OrderDate, CaptureHh"
    elif interval == 'day':
        query += "GROUP BY OrderDate ORDER BY OrderDate"
    elif interval == 'week':
        query += "GROUP BY DATEPART(ww, OrderDate) ORDER BY CONVERT(date, MIN(OrderDate), 10)"
    elif interval == 'month':
        query += "GROUP BY DATEPART(mm, OrderDate), DATEPART(yyyy, OrderDate) ORDER BY DATEPART(yyyy, OrderDate), DATEPART(mm, OrderDate)"
    elif interval == 'year':
        query += "GROUP BY DATEPART(year, OrderDate) ORDER BY DATEPART(year, OrderDate)"

    if interval != 'hour':
        query = query.replace('D.MOrderQty', 'D.OrderQty')
        query = query.replace('D.MPrice', 'D.Price')
        query = query.replace('D.MStockCode', 'D.StockCode')

    if 'item_sales' in kwargs:
        query = query.replace("AND NOT (Salesperson IN ('AF', 'MM'))", "AND NOT (Salesperson IN ('MM'))")
        query = query.replace("OrderDate", "EntInvoiceDate")
        query = query.replace("AS EntInvoiceDate", "AS OrderDate")

    cursor = connections['syspro'].cursor()
    cursor.execute(query)
    rows = namedtuplefetchall(cursor)
    cursor.close()

    return rows

def warehouse_order_status():
    cursor = connections['syspro'].cursor()

    cursor.execute("""
        SELECT
            (
                CASE
                    WHEN OrderStatus IN ('*', '\\') THEN 'Cancelled'
                    WHEN OrderStatus = 'F' THEN 'Fulfilled'
                    WHEN OrderStatus = 'S' THEN 'Suspended'
                    ELSE OrderStatus
                END
            ) AS Status,
            COUNT(SalesOrder) AS Cnt
        FROM SorMaster
        WHERE (
            NOT (OrderStatus IN ('9', '\\', '*'))
            OR (OrderStatus = '9' AND CONVERT(date, OrderDate) = CONVERT(date, GETDATE()))
        )
        AND SorMaster.OrderType = 'TR'
        AND NOT (SorMaster.DocumentType IN ('B', 'C'))
        GROUP BY
            (
                CASE
                    WHEN OrderStatus IN ('*', '\\') THEN 'Cancelled'
                    WHEN OrderStatus = 'F' THEN 'Fulfilled'
                    WHEN OrderStatus = 'S' THEN 'Suspended'
                    ELSE OrderStatus
                END
            )
        """)

    rows = namedtuplefetchall(cursor)
    cursor.close()

    return rows

def order_count_transfer(begin_date, end_date, interval):
    query = ''

    if interval == 'Day':
        query += "SELECT CONVERT(varchar, CONVERT(date, OrderDate), 101) AS Date, "
    elif interval == 'Week':
        query += "SELECT CONVERT(varchar, CONVERT(date, MIN(OrderDate)), 101) AS Date, "
    elif interval == 'Month':
        query += "SELECT CONVERT(varchar, DATEPART(mm, OrderDate)) + '/' + CONVERT(varchar, DATEPART(yyyy, OrderDate)) AS Date, "

    query += ("""
        COUNT(DISTINCT SorMaster.SalesOrder) AS Cnt, SUM(ItemWeight * MOrderQty) AS TotalWeight
        FROM SorMaster
        JOIN SorDetail ON SorMaster.SalesOrder = SorDetail.SalesOrder
        JOIN [InvMaster+] ON SorDetail.MStockCode = [InvMaster+].StockCode
        WHERE OrderType = 'TR'
        AND DocumentType = 'O'
        AND OrderDate BETWEEN '%s' AND '%s'
    """ % (begin_date, end_date))

    if interval == 'Day':
        query += "GROUP BY OrderDate ORDER BY OrderDate"
    elif interval == 'Week':
        query += "GROUP BY DATEPART(ww, OrderDate) ORDER BY CONVERT(date, MIN(OrderDate), 10)"
    elif interval == 'Month':
        query += "GROUP BY DATEPART(mm, OrderDate), DATEPART(yyyy, OrderDate) ORDER BY DATEPART(yyyy, OrderDate), DATEPART(mm, OrderDate)"

    cursor = connections['syspro'].cursor()

    cursor.execute(query)

    rows = namedtuplefetchall(cursor)
    cursor.close()

    return rows

def box_count_hour(date):
    cursor = connections['syspro'].cursor()

    cursor.execute("""
        SELECT
            (
                CASE
                    WHEN DATEPART(HOUR, RdsTimeConfirmed) = 0
                    THEN '12:00 AM'
                    WHEN DATEPART(HOUR, RdsTimeConfirmed) = 12
                    THEN '12:00 PM'
                    WHEN DATEPART(HOUR, RdsTimeConfirmed) < 12
                    THEN CONVERT(varchar(2), DATEPART(HOUR, RdsTimeConfirmed))  + ':00 AM'
                    ELSE CONVERT(varchar(2), DATEPART(HOUR, RdsTimeConfirmed)-12) + ':00 PM'
                END
            ) AS ConfirmedHour,
            COUNT(LicensePlateNumber) AS Cnt,
            COUNT(CASE WHEN OrderType = 'TR' THEN LicensePlateNumber END) AS Transfer,
            COUNT(CASE WHEN OrderType IN ('UF', 'ST') THEN LicensePlateNumber END) AS Standard
        FROM NorthShoreShipmentPack
        WHERE CONVERT(DATE, RdsTimeConfirmed) = %s
        GROUP BY DATEPART(HOUR, RdsTimeConfirmed)
    """, [date])

    rows = namedtuplefetchall(cursor)
    cursor.close()

    return rows

def shipment_count_packer(begin_date, end_date, interval, order_type, packer, shipment_pack):
    if packer == 'all':
        packers = get_packers(begin_date, end_date, order_type)
    else:
        packers = (packer.split(', '),)


    query = ''

    if interval == 'hour':
        query += """
            SELECT
            (
                CASE
                    WHEN DATEPART(HOUR, DateTimeCompleted) = 0
                    THEN CONVERT(varchar, CONVERT(date, DateTimeCompleted), 101) + ' 12:00 AM'
                    WHEN DATEPART(HOUR, DateTimeCompleted) = 12
                    THEN CONVERT(varchar, CONVERT(date, DateTimeCompleted), 101) + ' 12:00 PM'
                    WHEN DATEPART(HOUR, DateTimeCompleted) < 12
                    THEN CONVERT(varchar, CONVERT(date, DateTimeCompleted), 101) + ' ' + CONVERT(varchar(2), DATEPART(HOUR, DateTimeCompleted))  + ':00 AM'
                    ELSE CONVERT(varchar, CONVERT(date, DateTimeCompleted), 101) + ' ' + CONVERT(varchar(2), DATEPART(HOUR, DateTimeCompleted)-12) + ':00 PM'
                END
            ) AS CompletedHour, 
        """
    elif interval == 'day':
        query += "SELECT CONVERT(varchar, CONVERT(date, DateTimeCompleted), 101) AS Date, "
    elif interval == 'week':
        query += "SELECT CONVERT(varchar, CONVERT(date, MIN(DateTimeCompleted)), 101) AS Date, "

    for p in packers:
        if shipment_pack == 'shipment':
            query += "COUNT(DISTINCT CASE WHEN NorthShoreShipmentMaster.User1 LIKE '%s' THEN NorthShoreShipmentMaster.ShipmentNumber END) AS [%s], " % (p[0].replace('-', '%').replace('_', ' '), p[0].replace('-', ''))
        elif shipment_pack == 'pack':
            query += "COUNT(DISTINCT CASE WHEN NorthShoreShipmentMaster.User1 LIKE '%s' THEN LicensePlateNumber END) AS [%s], " % (p[0].replace('-', '%').replace('_', ' '), p[0].replace('-', ''))

    if shipment_pack == 'shipment':
        query += "COUNT(DISTINCT NorthShoreShipmentMaster.ShipmentNumber) AS Total "
    elif shipment_pack == 'pack':
        query += "COUNT(DISTINCT NorthShoreShipmentPack.LicensePlateNumber) AS Total "

    query += ("""
        FROM NorthShoreShipmentMaster
        JOIN NorthShoreShipmentPack ON NorthShoreShipmentMaster.ShipmentNumber = NorthShoreShipmentPack.ShipmentNumber
        WHERE CONVERT(date, DateTimeCompleted) BETWEEN '%s' AND '%s'
    """ % (begin_date, end_date))

    if order_type == 'ST':
        query += "AND NorthShoreShipmentMaster.OrderType IN ('UF', 'ST')"
    elif order_type == 'TR':
        query += "AND NorthShoreShipmentMaster.OrderType = 'TR'"

    if interval == 'hour':
        query += "GROUP BY DATEPART(HOUR, DateTimeCompleted), CONVERT(date, DateTimeCompleted) ORDER BY CONVERT(date, DateTimeCompleted), DATEPART(HOUR, DateTimeCompleted) "
    elif interval == 'day':
        query += "GROUP BY CONVERT(date, DateTimeCompleted) ORDER BY CONVERT(date, DateTimeCompleted) "
    elif interval == 'week':
        query += "GROUP BY DATEPART(ww, DateTimeCompleted) ORDER BY CONVERT(date, MIN(DateTimeCompleted), 10)"

    cursor = connections['syspro'].cursor()

    cursor.execute(query)

    rows = namedtuplefetchall(cursor)
    cursor.close()

    return rows

def top_skus(begin_date, end_date, group, unit_sum, channel):
    query = "SELECT TOP 20 "

    if group == 'sku':
        query += "D.StockCode AS Item, MAX(I.PickDescription) AS Description, "
    elif group == 'mpn':
        query += "I.AlternateKey1 AS Item, MAX(I.PickDescription) AS Description, "
    elif group == 'product_class':
        query += "I.ProductClass AS Item, MAX(PD.Description) AS Description, "
    elif group == 'brand':
        query += "I.Brand AS Item, '' AS Description, "
    elif group == 'manufacturer':
        query += "I.Manufacturer AS Item, '' AS Description, "
    elif group == 'supplier':
        query += "LEFT(S.SupplierName + ' - ' + S.Supplier,CHARINDEX(' - ', S.SupplierName + ' - ' + S.Supplier) - 1)  AS Item, '' AS Description, "

    if unit_sum == 'qty_sold':
        query += "SUM(D.OrderQty * ISNULL(B.QtyPer, 1)) AS Qty "
    elif unit_sum == 'num_orders':
        query += "COUNT(DISTINCT D.SalesOrder) AS Qty "
    elif unit_sum == 'sales_value':
        query += "SUM(D.Price * D.OrderQty) AS Qty "

    query += ("""
    FROM SorDetailRep AS D
    LEFT JOIN SorMasterRep AS M ON D.SalesOrder = M.SalesOrder AND D.Invoice = M.InvoiceNumber
    JOIN vwInventoryComplete AS I ON D.StockCode = I.StockCode
    LEFT JOIN BomStructure AS B ON D.StockCode = B.ParentPart
    LEFT JOIN ApSupplier AS S ON I.Supplier = S.Supplier
    WHERE M.OrderDate BETWEEN '%s' AND '%s' 
    AND M.OrderType <> 'TR'
    AND NOT (M.DocumentType IN ('B', 'C')) 
    AND NOT (D.StockCode LIKE 'SAM%%') 
    AND isnull(S.Supplier,'') <> ''
    """ % (begin_date, end_date))

    if channel == 'northshore':
        query += "AND NOT Salesperson IN ('AZ', 'AF', 'OS') "
    elif channel == 'amazon':
        query += "AND Salesperson IN ('AZ', 'AF') "
    elif channel == 'overstock':
        query += "AND Salesperson = 'OS'"

    if group == 'sku':
        query += "GROUP BY D.StockCode "
    elif group == 'mpn':
        query += "GROUP BY I.AlternateKey1 "
    elif group == 'product_class':
        query += "GROUP BY I.ProductClass "
        query = query.replace('JOIN vwInventoryComplete AS I ON D.StockCode = I.StockCode', 'JOIN vwInventoryComplete AS I ON D.StockCode = I.StockCode JOIN SalProductClassDes AS PD ON I.ProductClass = PD.ProductClass')
    elif group == 'brand':
        query += "GROUP BY I.Brand "
    elif group == 'manufacturer':
        query += "GROUP BY I.Manufacturer "
    elif group == 'supplier':
        query += "GROUP BY S.SupplierName + ' - ' + S.Supplier "

    if unit_sum == 'qty_sold':
        query += "ORDER BY SUM(D.OrderQty * ISNULL(B.QtyPer, 1)) DESC"
    elif unit_sum == 'num_orders':
        query += "ORDER BY COUNT(DISTINCT D.SalesOrder) DESC"
    elif unit_sum == 'sales_value':
        query += "ORDER BY SUM(D.Price * D.OrderQty) DESC"

    cursor = connections['syspro'].cursor()

    cursor.execute(query)

    rows = namedtuplefetchall(cursor)
    cursor.close()

    return rows
