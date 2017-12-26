import django_tables2 as tables

class CustomerOrdersTable(tables.Table):
    SalesOrder = tables.Column()
    OrderStatus = tables.Column()
    OrderDate = tables.Column()
    Salesperson = tables.Column()

    class Meta:
        template = 'django_tables2/bootstrap.html'
        attrs = {'class': 'table table-striped sortable pagination'}

class TransfersTable(tables.Table):
    SalesOrder = tables.Column()
    Sku = tables.Column()
    Qty = tables.Column()
    Weight = tables.Column()

    class Meta:
        template = 'django_tables2/bootstrap.html'
        attrs = {'class': 'table table-striped sortable'}