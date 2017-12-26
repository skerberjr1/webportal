# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import *
import decimal
from django.db.models import Lookup


class MakeshiftBoolField(models.CharField):
    default_bool = 'N'

    def __init__(self, default_bool, *args, **kwargs):
        super(MakeshiftBoolField, self).__init__(self, *args, **kwargs)
        self.default_bool = default_bool

    def from_db_value(self, value, expression, connection, context):
        if value:
            if value.strip() == '':
                return self.default_bool
            else:
                return value

        return self.default_bool

    def to_python(self, value):
        if value:
            if value.strip() == '':
                return self.default_bool

        return value

class ZipCodeField(models.CharField):

    def from_db_value(self, value, expression, connection, context):
        if value:
            if value[0].isalpha():
                return value
            elif len(value) > 5:
                return value[:5]
            else:
                return value
        return value

class TelephoneField(models.CharField):

    def from_db_value(self, value, expression, connection, context):
        if value:
            return value.replace(' ', '').replace('(', '').replace(')', '').replace('.', '').replace('//', '').replace('-', '')


@TelephoneField.register_lookup
class TelephoneLookup(Lookup):
    lookup_name = 'tele'

    def as_sql(self, compiler, connection):
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)

        if len(rhs_params[0]) >= 10:
            rhs_params[0] = rhs_params[0][:3] + '%' + rhs_params[0][3:6] + '%' + rhs_params[0][6:10]
        params = lhs_params + rhs_params

        return '%s LIKE %s' % (lhs, rhs), params


class InvMaster(models.Model):
    stockcode = models.TextField(db_column='StockCode', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50)  # Field name made lowercase.
    longdesc = models.CharField(db_column='LongDesc', max_length=100)  # Field name made lowercase.
    alternatekey1 = models.CharField(db_column='AlternateKey1', max_length=20)  # Field name made lowercase.
    alternatekey2 = models.CharField(db_column='AlternateKey2', max_length=20)  # Field name made lowercase.
    eccuser = models.TextField(db_column='EccUser')  # Field name made lowercase.
    stockuom = models.CharField(db_column='StockUom', max_length=10)  # Field name made lowercase.
    alternateuom = models.CharField(db_column='AlternateUom', max_length=10)  # Field name made lowercase.
    otheruom = models.CharField(db_column='OtherUom', max_length=10)  # Field name made lowercase.
    convfactaltuom = models.DecimalField(db_column='ConvFactAltUom', max_digits=12, decimal_places=6)  # Field name made lowercase.
    convmuldiv = models.CharField(db_column='ConvMulDiv', max_length=1)  # Field name made lowercase.
    convfactothuom = models.DecimalField(db_column='ConvFactOthUom', max_digits=12, decimal_places=6)  # Field name made lowercase.
    muldiv = models.CharField(db_column='MulDiv', max_length=1)  # Field name made lowercase.
    mass = models.DecimalField(db_column='Mass', max_digits=18, decimal_places=6)  # Field name made lowercase.
    volume = models.DecimalField(db_column='Volume', max_digits=18, decimal_places=6)  # Field name made lowercase.
    decimals = models.DecimalField(db_column='Decimals', max_digits=1, decimal_places=0)  # Field name made lowercase.
    pricecategory = models.CharField(db_column='PriceCategory', max_length=1)  # Field name made lowercase.
    pricemethod = models.CharField(db_column='PriceMethod', max_length=1)  # Field name made lowercase.
    supplier = models.TextField(db_column='Supplier')  # Field name made lowercase.
    cyclecount = models.DecimalField(db_column='CycleCount', max_digits=2, decimal_places=0)  # Field name made lowercase.
    productclass = models.TextField(db_column='ProductClass')  # Field name made lowercase.
    taxcode = models.TextField(db_column='TaxCode')  # Field name made lowercase.
    othertaxcode = models.CharField(db_column='OtherTaxCode', max_length=3)  # Field name made lowercase.
    listpricecode = models.TextField(db_column='ListPriceCode')  # Field name made lowercase.
    serialmethod = models.CharField(db_column='SerialMethod', max_length=1)  # Field name made lowercase.
    interfaceflag = models.CharField(db_column='InterfaceFlag', max_length=1)  # Field name made lowercase.
    kittype = models.CharField(db_column='KitType', max_length=1)  # Field name made lowercase.
    lowlevelcode = models.DecimalField(db_column='LowLevelCode', max_digits=2, decimal_places=0)  # Field name made lowercase.
    buyer = models.TextField(db_column='Buyer')  # Field name made lowercase.
    planner = models.TextField(db_column='Planner')  # Field name made lowercase.
    traceabletype = models.CharField(db_column='TraceableType', max_length=1)  # Field name made lowercase.
    mpsflag = models.CharField(db_column='MpsFlag', max_length=1)  # Field name made lowercase.
    bulkissueflag = models.CharField(db_column='BulkIssueFlag', max_length=1)  # Field name made lowercase.
    abcclass = models.CharField(db_column='AbcClass', max_length=1)  # Field name made lowercase.
    leadtime = models.DecimalField(db_column='LeadTime', max_digits=10, decimal_places=0)  # Field name made lowercase.
    stockmovementreq = models.CharField(db_column='StockMovementReq', max_length=1)  # Field name made lowercase.
    clearingflag = models.CharField(db_column='ClearingFlag', max_length=1)  # Field name made lowercase.
    supercessiondate = models.DateTimeField(db_column='SupercessionDate', blank=True, null=True)  # Field name made lowercase.
    abcanalysisreq = models.CharField(db_column='AbcAnalysisReq', max_length=1)  # Field name made lowercase.
    abccostingreq = models.CharField(db_column='AbcCostingReq', max_length=1)  # Field name made lowercase.
    costuom = models.CharField(db_column='CostUom', max_length=10)  # Field name made lowercase.
    minpricepct = models.DecimalField(db_column='MinPricePct', max_digits=5, decimal_places=2)  # Field name made lowercase.
    labourcost = models.DecimalField(db_column='LabourCost', max_digits=15, decimal_places=5)  # Field name made lowercase.
    materialcost = models.DecimalField(db_column='MaterialCost', max_digits=15, decimal_places=5)  # Field name made lowercase.
    fixoverhead = models.DecimalField(db_column='FixOverhead', max_digits=15, decimal_places=5)  # Field name made lowercase.
    variableoverhead = models.DecimalField(db_column='VariableOverhead', max_digits=15, decimal_places=5)  # Field name made lowercase.
    partcategory = models.CharField(db_column='PartCategory', max_length=1)  # Field name made lowercase.
    drawofficenum = models.TextField(db_column='DrawOfficeNum')  # Field name made lowercase.
    warehousetouse = models.CharField(db_column='WarehouseToUse', max_length=10)  # Field name made lowercase.
    buyingrule = models.CharField(db_column='BuyingRule', max_length=1)  # Field name made lowercase.
    specificgravity = models.DecimalField(db_column='SpecificGravity', max_digits=6, decimal_places=4)  # Field name made lowercase.
    implosionnum = models.DecimalField(db_column='ImplosionNum', max_digits=5, decimal_places=0)  # Field name made lowercase.
    ebq = models.DecimalField(db_column='Ebq', max_digits=18, decimal_places=6)  # Field name made lowercase.
    componentcount = models.DecimalField(db_column='ComponentCount', max_digits=5, decimal_places=0)  # Field name made lowercase.
    fixtimeperiod = models.DecimalField(db_column='FixTimePeriod', max_digits=2, decimal_places=0)  # Field name made lowercase.
    pansize = models.DecimalField(db_column='PanSize', max_digits=18, decimal_places=6)  # Field name made lowercase.
    docktostock = models.DecimalField(db_column='DockToStock', max_digits=10, decimal_places=0)  # Field name made lowercase.
    outputmassflag = models.CharField(db_column='OutputMassFlag', max_length=1)  # Field name made lowercase.
    shelflife = models.DecimalField(db_column='ShelfLife', max_digits=4, decimal_places=0)  # Field name made lowercase.
    version = models.TextField(db_column='Version')  # Field name made lowercase.
    release = models.TextField(db_column='Release')  # Field name made lowercase.
    demandtimefence = models.DecimalField(db_column='DemandTimeFence', max_digits=10, decimal_places=0)  # Field name made lowercase.
    maketoorderflag = models.CharField(db_column='MakeToOrderFlag', max_length=1)  # Field name made lowercase.
    manufleadtime = models.DecimalField(db_column='ManufLeadTime', max_digits=10, decimal_places=0)  # Field name made lowercase.
    grossreqrule = models.CharField(db_column='GrossReqRule', max_length=1)  # Field name made lowercase.
    percentageyield = models.DecimalField(db_column='PercentageYield', max_digits=3, decimal_places=0)  # Field name made lowercase.
    abcpreprod = models.DecimalField(db_column='AbcPreProd', max_digits=15, decimal_places=5)  # Field name made lowercase.
    abcmanufacturing = models.DecimalField(db_column='AbcManufacturing', max_digits=15, decimal_places=5)  # Field name made lowercase.
    abcsales = models.DecimalField(db_column='AbcSales', max_digits=15, decimal_places=5)  # Field name made lowercase.
    abccumpreprod = models.DecimalField(db_column='AbcCumPreProd', max_digits=15, decimal_places=5)  # Field name made lowercase.
    abccummanuf = models.DecimalField(db_column='AbcCumManuf', max_digits=15, decimal_places=5)  # Field name made lowercase.
    wipctlglcode = models.CharField(db_column='WipCtlGlCode', max_length=35)  # Field name made lowercase.
    resourcecode = models.CharField(db_column='ResourceCode', max_length=30)  # Field name made lowercase.
    gsttaxcode = models.CharField(db_column='GstTaxCode', max_length=3)  # Field name made lowercase.
    prcinclgst = models.CharField(db_column='PrcInclGst', max_length=1)  # Field name made lowercase.
    serentryatsale = models.CharField(db_column='SerEntryAtSale', max_length=1)  # Field name made lowercase.
    stpselection = models.CharField(db_column='StpSelection', max_length=1)  # Field name made lowercase.
    userfield1 = models.CharField(db_column='UserField1', max_length=30)  # Field name made lowercase.
    userfield2 = models.DecimalField(db_column='UserField2', max_digits=17, decimal_places=5)  # Field name made lowercase.
    userfield3 = models.CharField(db_column='UserField3', max_length=1)  # Field name made lowercase.
    userfield4 = models.CharField(db_column='UserField4', max_length=1)  # Field name made lowercase.
    userfield5 = models.CharField(db_column='UserField5', max_length=1)  # Field name made lowercase.
    tariffcode = models.CharField(db_column='TariffCode', max_length=15)  # Field name made lowercase.
    supplementaryunit = models.CharField(db_column='SupplementaryUnit', max_length=1)  # Field name made lowercase.
    ebqpan = models.CharField(db_column='EbqPan', max_length=1)  # Field name made lowercase.
    stdlandedcost = models.DecimalField(db_column='StdLandedCost', max_digits=15, decimal_places=5)  # Field name made lowercase.
    lctrequired = models.CharField(db_column='LctRequired', max_length=1)  # Field name made lowercase.
    stdlctroute = models.CharField(db_column='StdLctRoute', max_length=8)  # Field name made lowercase.
    issmultlotsflag = models.CharField(db_column='IssMultLotsFlag', max_length=1)  # Field name made lowercase.
    inclinstrvalid = models.CharField(db_column='InclInStrValid', max_length=1)  # Field name made lowercase.
    stdlabcostsbill = models.DecimalField(db_column='StdLabCostsBill', max_digits=15, decimal_places=5)  # Field name made lowercase.
    phantomifcomp = models.CharField(db_column='PhantomIfComp', max_length=1)  # Field name made lowercase.
    countryoforigin = models.CharField(db_column='CountryOfOrigin', max_length=3)  # Field name made lowercase.
    stockonhold = models.CharField(db_column='StockOnHold', max_length=1)  # Field name made lowercase.
    stockonholdreason = models.CharField(db_column='StockOnHoldReason', max_length=6)  # Field name made lowercase.
    eccflag = models.CharField(db_column='EccFlag', max_length=1)  # Field name made lowercase.
    stockandaltum = models.CharField(db_column='StockAndAltUm', max_length=1)  # Field name made lowercase.
    altunitchar = models.DecimalField(db_column='AltUnitChar', max_digits=1, decimal_places=0)  # Field name made lowercase.
    jobsonhold = models.CharField(db_column='JobsOnHold', max_length=1)  # Field name made lowercase.
    jobholdallocs = models.CharField(db_column='JobHoldAllocs', max_length=1)  # Field name made lowercase.
    purchonhold = models.CharField(db_column='PurchOnHold', max_length=1)  # Field name made lowercase.
    salesonhold = models.CharField(db_column='SalesOnHold', max_length=1)  # Field name made lowercase.
    maintonhold = models.CharField(db_column='MaintOnHold', max_length=1)  # Field name made lowercase.
    batchbill = models.CharField(db_column='BatchBill', max_length=1)  # Field name made lowercase.
    blanketpoexists = models.CharField(db_column='BlanketPoExists', max_length=1)  # Field name made lowercase.
    calloffbpoexists = models.CharField(db_column='CallOffBpoExists', max_length=1)  # Field name made lowercase.
    distwarehousetouse = models.CharField(db_column='DistWarehouseToUse', max_length=10)  # Field name made lowercase.
    jobclassification = models.TextField(db_column='JobClassification')  # Field name made lowercase.
    subcontractcost = models.DecimalField(db_column='SubContractCost', max_digits=15, decimal_places=5)  # Field name made lowercase.
    datestkadded = models.DateTimeField(db_column='DateStkAdded', blank=True, null=True)  # Field name made lowercase.
    inspectionflag = models.CharField(db_column='InspectionFlag', max_length=1)  # Field name made lowercase.
    serialprefix = models.CharField(db_column='SerialPrefix', max_length=35)  # Field name made lowercase.
    serialsuffix = models.CharField(db_column='SerialSuffix', max_length=15)  # Field name made lowercase.
    returnableitem = models.CharField(db_column='ReturnableItem', max_length=1)  # Field name made lowercase.
    productgroup = models.TextField(db_column='ProductGroup')  # Field name made lowercase.
    pricetype = models.CharField(db_column='PriceType', max_length=1)  # Field name made lowercase.
    basis = models.CharField(db_column='Basis', max_length=1)  # Field name made lowercase.
    manualcostflag = models.CharField(db_column='ManualCostFlag', max_length=1)  # Field name made lowercase.
    manufactureuom = models.CharField(db_column='ManufactureUom', max_length=10)  # Field name made lowercase.
    convfactmum = models.DecimalField(db_column='ConvFactMuM', max_digits=12, decimal_places=6)  # Field name made lowercase.
    manmuldiv = models.CharField(db_column='ManMulDiv', max_length=1)  # Field name made lowercase.
    lookaheadwin = models.DecimalField(db_column='LookAheadWin', max_digits=10, decimal_places=0)  # Field name made lowercase.
    loadingfactor = models.DecimalField(db_column='LoadingFactor', max_digits=9, decimal_places=3)  # Field name made lowercase.
    supplunitcode = models.TextField(db_column='SupplUnitCode')  # Field name made lowercase.
    storagesecurity = models.TextField(db_column='StorageSecurity')  # Field name made lowercase.
    storagehazard = models.TextField(db_column='StorageHazard')  # Field name made lowercase.
    storagecondition = models.TextField(db_column='StorageCondition')  # Field name made lowercase.
    productshelflife = models.DecimalField(db_column='ProductShelfLife', max_digits=4, decimal_places=0)  # Field name made lowercase.
    internalshelflife = models.DecimalField(db_column='InternalShelfLife', max_digits=4, decimal_places=0)  # Field name made lowercase.
    altmethodflag = models.CharField(db_column='AltMethodFlag', max_length=1)  # Field name made lowercase.
    altsisoflag = models.CharField(db_column='AltSisoFlag', max_length=1)  # Field name made lowercase.
    altreductionflag = models.CharField(db_column='AltReductionFlag', max_length=1)  # Field name made lowercase.
    withtaxexpensetype = models.CharField(db_column='WithTaxExpenseType', max_length=1)  # Field name made lowercase.
    timestamp = models.TextField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    barcode = models.TextField(db_column='Barcode', blank=True, null=True)  # Field name made lowercase.

    @property
    def full_description(self):
        return getattr(self, 'description') + getattr(self, 'longdesc') + getattr(InvMasterPlus.objects.get(pk=self.stockcode), 'finaldescription')

    class Meta:
        managed = False
        db_table = 'InvMaster'
        unique_together = (('description', 'stockcode'), ('stockcode', 'stockcode', 'stockcode', 'stockcode', 'stockcode'), ('productclass', 'stockcode'), ('eccuser', 'stockcode'), ('alternatekey1', 'stockcode'), ('alternatekey2', 'stockcode'), ('supplier', 'stockcode'), ('longdesc', 'stockcode'),)


class ArCustomer(models.Model):
    price_codes = [('A', 'A - Binder Pricing'), ('B', 'B - 5% Off'), ('BB', 'BB'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F - 10% Off'), ('G', 'G')]

    customer = models.CharField(db_column='Customer', primary_key=True, max_length=20, verbose_name="Customer Number")  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, verbose_name='Customer Name')  # Field name made lowercase.
    shortname = models.CharField(db_column='ShortName', max_length=20)  # Field name made lowercase.
    exemptfinchg = models.CharField(db_column='ExemptFinChg', max_length=1)  # Field name made lowercase.
    mainthistory = models.CharField(db_column='MaintHistory', max_length=1)  # Field name made lowercase.
    customertype = models.CharField(db_column='CustomerType', max_length=1)  # Field name made lowercase.
    masteraccount = models.CharField(db_column='MasterAccount', max_length=15)  # Field name made lowercase.
    storenumber = models.CharField(db_column='StoreNumber', max_length=20)  # Field name made lowercase.
    prtmasteradd = models.CharField(db_column='PrtMasterAdd', max_length=1)  # Field name made lowercase.
    creditstatus = models.CharField(db_column='CreditStatus', max_length=1)  # Field name made lowercase.
    creditlimit = models.DecimalField(db_column='CreditLimit', max_digits=12, decimal_places=0)  # Field name made lowercase.
    invoicecount = models.DecimalField(db_column='InvoiceCount', max_digits=10, decimal_places=0, verbose_name='Invoice Count')  # Field name made lowercase.
    salesperson = models.TextField(db_column='Salesperson', verbose_name='Salesperson')  # Field name made lowercase.
    salesperson1 = models.TextField(db_column='Salesperson1')  # Field name made lowercase.
    salesperson2 = models.TextField(db_column='Salesperson2')  # Field name made lowercase.
    salesperson3 = models.TextField(db_column='Salesperson3')  # Field name made lowercase.
    pricecode = models.TextField(db_column='PriceCode', choices=price_codes)  # Field name made lowercase.
    customerclass = models.CharField(db_column='CustomerClass', max_length=10)  # Field name made lowercase.
    branch = models.TextField(db_column='Branch')  # Field name made lowercase.
    termscode = models.TextField(db_column='TermsCode')  # Field name made lowercase.
    invdisccode = models.CharField(db_column='InvDiscCode', max_length=10)  # Field name made lowercase.
    balancetype = models.CharField(db_column='BalanceType', max_length=1)  # Field name made lowercase.
    area = models.TextField(db_column='Area')  # Field name made lowercase.
    linedisccode = models.CharField(db_column='LineDiscCode', max_length=10)  # Field name made lowercase.
    taxstatus = models.CharField(db_column='TaxStatus', max_length=1)  # Field name made lowercase.
    taxexemptnumber = models.CharField(db_column='TaxExemptNumber', max_length=30)  # Field name made lowercase.
    specialinstrs = models.CharField(db_column='SpecialInstrs', max_length=30)  # Field name made lowercase.
    pricecategorytable = models.CharField(db_column='PriceCategoryTable', max_length=260)  # Field name made lowercase.
    datelastsale = models.DateTimeField(db_column='DateLastSale', blank=True, null=True)  # Field name made lowercase.
    datelastpay = models.DateTimeField(db_column='DateLastPay', blank=True, null=True)  # Field name made lowercase.
    outstordval = models.DecimalField(db_column='OutstOrdVal', max_digits=14, decimal_places=2)  # Field name made lowercase.
    numoutstord = models.DecimalField(db_column='NumOutstOrd', max_digits=10, decimal_places=0)  # Field name made lowercase.
    telephone = TelephoneField(db_column='Telephone', max_length=20)  # Field name made lowercase.
    contact = models.CharField(db_column='Contact', max_length=50)  # Field name made lowercase.
    addtelephone = models.CharField(db_column='AddTelephone', max_length=20)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=20)  # Field name made lowercase.
    telex = models.CharField(db_column='Telex', max_length=10)  # Field name made lowercase.
    telephoneextn = models.CharField(db_column='TelephoneExtn', max_length=5)  # Field name made lowercase.
    currency = models.TextField(db_column='Currency')  # Field name made lowercase.
    userfield1 = models.CharField(db_column='UserField1', max_length=10)  # Field name made lowercase.
    userfield2 = models.DecimalField(db_column='UserField2', max_digits=14, decimal_places=2)  # Field name made lowercase.
    gstexemptflag = models.CharField(db_column='GstExemptFlag', max_length=1)  # Field name made lowercase.
    gstexemptnum = models.CharField(db_column='GstExemptNum', max_length=15)  # Field name made lowercase.
    gstlevel = models.CharField(db_column='GstLevel', max_length=1)  # Field name made lowercase.
    detailmovereqd = models.CharField(db_column='DetailMoveReqd', max_length=1)  # Field name made lowercase.
    interfaceflag = models.CharField(db_column='InterfaceFlag', max_length=1)  # Field name made lowercase.
    contractprcreqd = models.CharField(db_column='ContractPrcReqd', max_length=1)  # Field name made lowercase.
    buyinggroup1 = models.TextField(db_column='BuyingGroup1')  # Field name made lowercase.
    buyinggroup2 = models.TextField(db_column='BuyingGroup2')  # Field name made lowercase.
    buyinggroup3 = models.TextField(db_column='BuyingGroup3')  # Field name made lowercase.
    buyinggroup4 = models.TextField(db_column='BuyingGroup4')  # Field name made lowercase.
    buyinggroup5 = models.TextField(db_column='BuyingGroup5')  # Field name made lowercase.
    statementreqd = models.CharField(db_column='StatementReqd', max_length=1)  # Field name made lowercase.
    backordreqd = models.CharField(db_column='BackOrdReqd', max_length=1)  # Field name made lowercase.
    shippinginstrs = models.CharField(db_column='ShippingInstrs', max_length=50)  # Field name made lowercase.
    shippinginstrscod = models.CharField(db_column='ShippingInstrsCod', max_length=6)  # Field name made lowercase.
    statecode = models.CharField(db_column='StateCode', max_length=3)  # Field name made lowercase.
    datecustadded = models.DateTimeField(db_column='DateCustAdded', blank=True, null=True, verbose_name="Date Customer Added")  # Field name made lowercase.
    stockinterchange = models.CharField(db_column='StockInterchange', max_length=1)  # Field name made lowercase.
    maintlastprcpaid = models.CharField(db_column='MaintLastPrcPaid', max_length=1)  # Field name made lowercase.
    ibtcustomer = models.CharField(db_column='IbtCustomer', max_length=1)  # Field name made lowercase.
    sodefaultdoc = models.CharField(db_column='SoDefaultDoc', max_length=2)  # Field name made lowercase.
    counterslsonly = models.CharField(db_column='CounterSlsOnly', max_length=1)  # Field name made lowercase.
    paymentstatus = models.CharField(db_column='PaymentStatus', max_length=1)  # Field name made lowercase.
    nationality = models.CharField(db_column='Nationality', max_length=3)  # Field name made lowercase.
    highestbalance = models.DecimalField(db_column='HighestBalance', max_digits=14, decimal_places=2)  # Field name made lowercase.
    customeronhold = models.CharField(db_column='CustomerOnHold', max_length=1)  # Field name made lowercase.
    invcommentcode = models.CharField(db_column='InvCommentCode', max_length=10)  # Field name made lowercase.
    edisendercode = models.CharField(db_column='EdiSenderCode', max_length=40)  # Field name made lowercase.
    relordosvalue = models.DecimalField(db_column='RelOrdOsValue', max_digits=14, decimal_places=2)  # Field name made lowercase.
    ediflag = models.CharField(db_column='EdiFlag', max_length=1)  # Field name made lowercase.
    sodefaulttype = models.CharField(db_column='SoDefaultType', max_length=2)  # Field name made lowercase.
    email = models.EmailField(db_column='Email', max_length=255, verbose_name='Email')  # Field name made lowercase.
    applyorddisc = models.CharField(db_column='ApplyOrdDisc', max_length=1)  # Field name made lowercase.
    applylinedisc = models.CharField(db_column='ApplyLineDisc', max_length=1)  # Field name made lowercase.
    faxinvoices = models.CharField(db_column='FaxInvoices', max_length=1)  # Field name made lowercase.
    faxstatements = models.CharField(db_column='FaxStatements', max_length=1)  # Field name made lowercase.
    highinvdays = models.DecimalField(db_column='HighInvDays', max_digits=4, decimal_places=0)  # Field name made lowercase.
    highinv = models.CharField(db_column='HighInv', max_length=20)  # Field name made lowercase.
    docfax = models.CharField(db_column='DocFax', max_length=20)  # Field name made lowercase.
    docfaxcontact = models.CharField(db_column='DocFaxContact', max_length=50)  # Field name made lowercase.
    soldtoaddr1 = models.CharField(db_column='SoldToAddr1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    soldtoaddr2 = models.CharField(db_column='SoldToAddr2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    soldtoaddr3 = models.CharField(db_column='SoldToAddr3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    soldtoaddr3loc = models.CharField(db_column='SoldToAddr3Loc', max_length=40, blank=True, null=True)  # Field name made lowercase.
    soldtoaddr4 = models.CharField(db_column='SoldToAddr4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    soldtoaddr5 = models.CharField(db_column='SoldToAddr5', max_length=40, blank=True, null=True)  # Field name made lowercase.
    soldpostalcode = ZipCodeField(db_column='SoldPostalCode', max_length=10)  # Field name made lowercase.
    soldtogpslat = models.DecimalField(db_column='SoldToGpsLat', max_digits=8, decimal_places=6)  # Field name made lowercase.
    soldtogpslong = models.DecimalField(db_column='SoldToGpsLong', max_digits=9, decimal_places=6)  # Field name made lowercase.
    shiptoaddr1 = models.CharField(db_column='ShipToAddr1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    shiptoaddr2 = models.CharField(db_column='ShipToAddr2', max_length=40)  # Field name made lowercase.
    shiptoaddr3 = models.CharField(db_column='ShipToAddr3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    shiptoaddr3loc = models.CharField(db_column='ShipToAddr3Loc', max_length=40, blank=True, null=True)  # Field name made lowercase.
    shiptoaddr4 = models.CharField(db_column='ShipToAddr4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    shiptoaddr5 = models.CharField(db_column='ShipToAddr5', max_length=40, blank=True, null=True)  # Field name made lowercase.
    shippostalcode = ZipCodeField(db_column='ShipPostalCode', max_length=10)  # Field name made lowercase.
    shiptogpslat = models.DecimalField(db_column='ShipToGpsLat', max_digits=8, decimal_places=6)  # Field name made lowercase.
    shiptogpslong = models.DecimalField(db_column='ShipToGpsLong', max_digits=9, decimal_places=6)  # Field name made lowercase.
    state = models.TextField(db_column='State')  # Field name made lowercase.
    countyzip = models.TextField(db_column='CountyZip')  # Field name made lowercase.
    city = models.TextField(db_column='City')  # Field name made lowercase.
    state1 = models.CharField(db_column='State1', max_length=2)  # Field name made lowercase.
    countyzip1 = models.CharField(db_column='CountyZip1', max_length=5)  # Field name made lowercase.
    city1 = models.CharField(db_column='City1', max_length=3)  # Field name made lowercase.
    defaultordtype = models.CharField(db_column='DefaultOrdType', max_length=2)  # Field name made lowercase.
    ponumbermandatory = models.CharField(db_column='PoNumberMandatory', max_length=1)  # Field name made lowercase.
    creditcheckflag = models.CharField(db_column='CreditCheckFlag', max_length=1)  # Field name made lowercase.
    companytaxnumber = models.CharField(db_column='CompanyTaxNumber', max_length=15)  # Field name made lowercase.
    deliveryterms = models.TextField(db_column='DeliveryTerms')  # Field name made lowercase.
    transactionnature = models.TextField(db_column='TransactionNature')  # Field name made lowercase.
    deliverytermsc = models.CharField(db_column='DeliveryTermsC', max_length=3)  # Field name made lowercase.
    transactionnaturec = models.DecimalField(db_column='TransactionNatureC', max_digits=3, decimal_places=0)  # Field name made lowercase.
    routecode = models.TextField(db_column='RouteCode')  # Field name made lowercase.
    faxquotes = models.CharField(db_column='FaxQuotes', max_length=1)  # Field name made lowercase.
    routedistance = models.DecimalField(db_column='RouteDistance', max_digits=4, decimal_places=0)  # Field name made lowercase.
    tpmcustomerflag = models.CharField(db_column='TpmCustomerFlag', max_length=1)  # Field name made lowercase.
    saleswarehouse = models.TextField(db_column='SalesWarehouse')  # Field name made lowercase.
    tpmpricingflag = models.CharField(db_column='TpmPricingFlag', max_length=1)  # Field name made lowercase.
    arstatementno = models.CharField(db_column='ArStatementNo', max_length=2)  # Field name made lowercase.
    tpmcreditcheck = models.CharField(db_column='TpmCreditCheck', max_length=1)  # Field name made lowercase.
    wholeordershipflag = models.CharField(db_column='WholeOrderShipFlag', max_length=1)  # Field name made lowercase.
    minimumordervalue = models.DecimalField(db_column='MinimumOrderValue', max_digits=10, decimal_places=0)  # Field name made lowercase.
    minimumorderchgcod = models.CharField(db_column='MinimumOrderChgCod', max_length=6)  # Field name made lowercase.
    ukvatflag = models.CharField(db_column='UkVatFlag', max_length=1)  # Field name made lowercase.
    ukcurrency = models.CharField(db_column='UkCurrency', max_length=3)  # Field name made lowercase.
    languagecode = models.CharField(db_column='LanguageCode', max_length=2)  # Field name made lowercase.
    shippinglocation = models.TextField(db_column='ShippingLocation')  # Field name made lowercase.
    altmethodflag = models.CharField(db_column='AltMethodFlag', max_length=1)  # Field name made lowercase.
    salesallowed = models.CharField(db_column='SalesAllowed', max_length=1)  # Field name made lowercase.
    unapppayallowed = models.CharField(db_column='UnappPayAllowed', max_length=1)  # Field name made lowercase.
    paymentsallowed = models.CharField(db_column='PaymentsAllowed', max_length=1)  # Field name made lowercase.
    quotesallowed = models.CharField(db_column='QuotesAllowed', max_length=1)  # Field name made lowercase.
    crnotesallowed = models.CharField(db_column='CrNotesAllowed', max_length=1)  # Field name made lowercase.
    drnotesallowed = models.CharField(db_column='DrNotesAllowed', max_length=1)  # Field name made lowercase.
    queryallowed = models.CharField(db_column='QueryAllowed', max_length=1)  # Field name made lowercase.
    timestamp = models.TextField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    trustpilotreview = models.CharField(db_column='TrustPilotReview', max_length=1, blank=True, null=True)  # Field name made lowercase.
    wb599 = models.CharField(db_column='WB599', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ArCustomer'
        unique_together = (('telephone', 'customer'), ('shortname', 'customer'), ('salesperson', 'customer'), ('name', 'customer'), ('customer', 'customer'), ('edisendercode', 'customer'),)
        verbose_name = 'Customer'


class ArInvoice(models.Model):
    customer = models.ForeignKey(ArCustomer, models.DO_NOTHING, db_column='Customer')  # Field name made lowercase.
    invoice = models.CharField(db_column='Invoice', max_length=20, primary_key=True)  # Field name made lowercase.
    documenttype = models.TextField(db_column='DocumentType')  # Field name made lowercase.
    nextpaymentry = models.DecimalField(db_column='NextPaymEntry', max_digits=10, decimal_places=0)  # Field name made lowercase.
    invoicedate = models.DateTimeField(db_column='InvoiceDate', blank=True, null=True)  # Field name made lowercase.
    salesorder = models.ForeignKey('SorMaster', models.DO_NOTHING, db_column='SalesOrder')  # Field name made lowercase.
    customerponumber = models.CharField(db_column='CustomerPoNumber', max_length=30)  # Field name made lowercase.
    salesperson = models.TextField(db_column='Salesperson')  # Field name made lowercase.
    branch = models.TextField(db_column='Branch')  # Field name made lowercase.
    area = models.TextField(db_column='Area')  # Field name made lowercase.
    termscode = models.TextField(db_column='TermsCode')  # Field name made lowercase.
    origdiscvalue = models.DecimalField(db_column='OrigDiscValue', max_digits=14, decimal_places=2)  # Field name made lowercase.
    invoicebal1 = models.DecimalField(db_column='InvoiceBal1', max_digits=14, decimal_places=2)  # Field name made lowercase.
    invoicebal2 = models.DecimalField(db_column='InvoiceBal2', max_digits=14, decimal_places=2)  # Field name made lowercase.
    invoicebal3 = models.DecimalField(db_column='InvoiceBal3', max_digits=14, decimal_places=2)  # Field name made lowercase.
    invoiceyear = models.DecimalField(db_column='InvoiceYear', max_digits=4, decimal_places=0)  # Field name made lowercase.
    invoicemonth = models.DecimalField(db_column='InvoiceMonth', max_digits=2, decimal_places=0)  # Field name made lowercase.
    yearinvbalzero = models.DecimalField(db_column='YearInvBalZero', max_digits=4, decimal_places=0)  # Field name made lowercase.
    monthinvbalzero = models.DecimalField(db_column='MonthInvBalZero', max_digits=2, decimal_places=0)  # Field name made lowercase.
    lastdelnote = models.CharField(db_column='LastDelNote', max_length=20)  # Field name made lowercase.
    storenumber = models.CharField(db_column='StoreNumber', max_length=20)  # Field name made lowercase.
    proofofdelivery = models.CharField(db_column='ProofOfDelivery', max_length=1)  # Field name made lowercase.
    podentrydate = models.DateTimeField(db_column='PodEntryDate', blank=True, null=True)  # Field name made lowercase.
    podreference = models.CharField(db_column='PodReference', max_length=30)  # Field name made lowercase.
    currencyvalue = models.DecimalField(db_column='CurrencyValue', max_digits=14, decimal_places=2)  # Field name made lowercase.
    postcurrency = models.CharField(db_column='PostCurrency', max_length=3)  # Field name made lowercase.
    convrate = models.DecimalField(db_column='ConvRate', max_digits=12, decimal_places=6)  # Field name made lowercase.
    muldiv = models.CharField(db_column='MulDiv', max_length=1)  # Field name made lowercase.
    accountcur = models.CharField(db_column='AccountCur', max_length=3)  # Field name made lowercase.
    accconvrate = models.DecimalField(db_column='AccConvRate', max_digits=12, decimal_places=6)  # Field name made lowercase.
    accmuldiv = models.CharField(db_column='AccMulDiv', max_length=1)  # Field name made lowercase.
    triangcurrency = models.CharField(db_column='TriangCurrency', max_length=3)  # Field name made lowercase.
    triangrate = models.DecimalField(db_column='TriangRate', max_digits=12, decimal_places=6)  # Field name made lowercase.
    triangmuldiv = models.CharField(db_column='TriangMulDiv', max_length=1)  # Field name made lowercase.
    retentioninv = models.CharField(db_column='RetentionInv', max_length=1)  # Field name made lowercase.
    taxstatus = models.CharField(db_column='TaxStatus', max_length=1)  # Field name made lowercase.
    taxportion = models.DecimalField(db_column='TaxPortion', max_digits=14, decimal_places=2)  # Field name made lowercase.
    fixexchangerate = models.CharField(db_column='FixExchangeRate', max_length=1)  # Field name made lowercase.
    nextrevalno = models.DecimalField(db_column='NextRevalNo', max_digits=10, decimal_places=0)  # Field name made lowercase.
    taxcode = models.TextField(db_column='TaxCode')  # Field name made lowercase.
    discbal = models.DecimalField(db_column='DiscBal', max_digits=14, decimal_places=2)  # Field name made lowercase.
    paymentrunflag = models.CharField(db_column='PaymentRunFlag', max_length=1)  # Field name made lowercase.
    collectionrunflag = models.CharField(db_column='CollectionRunFlag', max_length=1)  # Field name made lowercase.
    invoicepdcflag = models.CharField(db_column='InvoicePdcFlag', max_length=1)  # Field name made lowercase.
    originvrate = models.DecimalField(db_column='OrigInvRate', max_digits=12, decimal_places=6)  # Field name made lowercase.
    timestamp = models.TextField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'ArInvoice'
        unique_together = (('invoice', 'customer', 'documenttype'), ('customer', 'customer', 'customer', 'customer', 'customer', 'invoice', 'invoice', 'invoice', 'invoice', 'invoice', 'invoice', 'documenttype', 'documenttype', 'documenttype'),)


class SorMaster(models.Model):
    order_statuses = [
        ('0', '0 - In Process'), 
        ('1', '1 - Open Order'), 
        ('2', '2 - Open Backorder'), 
        ('3', '3 - Released Backorder'),
        ('4', '4 - Released Order'),
        ('8', '8 - Ready to Invoice'),
        ('9', '9 - Completed'),
        ('*', '* - Cancelled'),
        ('\\', '\\ - Cancelled'),
        ('S', 'S - Suspended'),
        ('F', 'F - Fulfillment Order')
    ]

    salesorder = models.CharField(db_column='SalesOrder', primary_key=True, max_length=20, verbose_name='Sales Order')  # Field name made lowercase.
    nextdetailline = models.DecimalField(db_column='NextDetailLine', max_digits=4, decimal_places=0)  # Field name made lowercase.
    orderstatus = models.CharField(db_column='OrderStatus', max_length=1, verbose_name='Order Status', choices=order_statuses)  # Field name made lowercase.
    activeflag = models.CharField(db_column='ActiveFlag', max_length=1)  # Field name made lowercase.
    cancelledflag = models.CharField(db_column='CancelledFlag', max_length=1)  # Field name made lowercase.
    documenttype = models.CharField(db_column='DocumentType', max_length=1, verbose_name='Document Type')  # Field name made lowercase.
    customer = models.ForeignKey('ArCustomer', models.DO_NOTHING, db_column='Customer')  # Field name made lowercase.
    salesperson = models.TextField(db_column='Salesperson', verbose_name='Salesperson')  # Field name made lowercase.
    customerponumber = models.CharField(db_column='CustomerPoNumber', max_length=30, verbose_name='Customer PO')  # Field name made lowercase.
    orderdate = models.DateField(db_column='OrderDate', blank=True, null=True, verbose_name='Order Date')  # Field name made lowercase.
    entrysystemdate = models.DateTimeField(db_column='EntrySystemDate', blank=True, null=True)  # Field name made lowercase.
    reqshipdate = models.DateTimeField(db_column='ReqShipDate', blank=True, null=True)  # Field name made lowercase.
    datelastdocprt = models.DateTimeField(db_column='DateLastDocPrt', blank=True, null=True)  # Field name made lowercase.
    shippinginstrs = models.CharField(db_column='ShippingInstrs', max_length=50)  # Field name made lowercase.
    shippinginstrscod = models.CharField(db_column='ShippingInstrsCod', max_length=6)  # Field name made lowercase.
    altshipaddrflag = models.CharField(db_column='AltShipAddrFlag', max_length=1)  # Field name made lowercase.
    invoicecount = models.DecimalField(db_column='InvoiceCount', max_digits=2, decimal_places=0)  # Field name made lowercase.
    invtermsoverride = models.CharField(db_column='InvTermsOverride', max_length=2)  # Field name made lowercase.
    creditauthority = models.CharField(db_column='CreditAuthority', max_length=3)  # Field name made lowercase.
    branch = models.TextField(db_column='Branch')  # Field name made lowercase.
    specialinstrs = models.CharField(db_column='SpecialInstrs', max_length=30)  # Field name made lowercase.
    entinvoice = models.CharField(db_column='EntInvoice', max_length=20)  # Field name made lowercase.
    entinvoicedate = models.DateTimeField(db_column='EntInvoiceDate', blank=True, null=True)  # Field name made lowercase.
    discpct1 = models.DecimalField(db_column='DiscPct1', max_digits=5, decimal_places=2)  # Field name made lowercase.
    discpct2 = models.DecimalField(db_column='DiscPct2', max_digits=5, decimal_places=2)  # Field name made lowercase.
    discpct3 = models.DecimalField(db_column='DiscPct3', max_digits=5, decimal_places=2)  # Field name made lowercase.
    ordertype = models.TextField(db_column='OrderType')  # Field name made lowercase.
    taxexemptflag = models.CharField(db_column='TaxExemptFlag', max_length=1)  # Field name made lowercase.
    area = models.TextField(db_column='Area')  # Field name made lowercase.
    taxexemptnumber = models.CharField(db_column='TaxExemptNumber', max_length=30)  # Field name made lowercase.
    taxexemptoverride = models.CharField(db_column='TaxExemptOverride', max_length=1)  # Field name made lowercase.
    cashcredit = models.CharField(db_column='CashCredit', max_length=2)  # Field name made lowercase.
    warehouse = models.TextField(db_column='Warehouse')  # Field name made lowercase.
    lastinvoice = models.CharField(db_column='LastInvoice', max_length=20)  # Field name made lowercase.
    scheduledordflag = models.CharField(db_column='ScheduledOrdFlag', max_length=1)  # Field name made lowercase.
    gstexemptflag = models.CharField(db_column='GstExemptFlag', max_length=1)  # Field name made lowercase.
    gstexemptnum = models.CharField(db_column='GstExemptNum', max_length=15)  # Field name made lowercase.
    gstexemptoride = models.CharField(db_column='GstExemptORide', max_length=1)  # Field name made lowercase.
    ibtflag = models.CharField(db_column='IbtFlag', max_length=1)  # Field name made lowercase.
    ordacknwprinted = models.CharField(db_column='OrdAcknwPrinted', max_length=1)  # Field name made lowercase.
    detcustmvmtreqd = models.CharField(db_column='DetCustMvmtReqd', max_length=1)  # Field name made lowercase.
    documentformat = models.CharField(db_column='DocumentFormat', max_length=2)  # Field name made lowercase.
    fixexchangerate = models.CharField(db_column='FixExchangeRate', max_length=1)  # Field name made lowercase.
    exchangerate = models.DecimalField(db_column='ExchangeRate', max_digits=12, decimal_places=6)  # Field name made lowercase.
    muldiv = models.CharField(db_column='MulDiv', max_length=1)  # Field name made lowercase.
    currency = models.TextField(db_column='Currency')  # Field name made lowercase.
    gstdeduction = models.CharField(db_column='GstDeduction', max_length=1)  # Field name made lowercase.
    orderstatusfail = models.CharField(db_column='OrderStatusFail', max_length=1)  # Field name made lowercase.
    consolidatedorder = models.CharField(db_column='ConsolidatedOrder', max_length=1)  # Field name made lowercase.
    creditedinvdate = models.DateTimeField(db_column='CreditedInvDate', blank=True, null=True)  # Field name made lowercase.
    job = models.TextField(db_column='Job')  # Field name made lowercase.
    serialisedflag = models.CharField(db_column='SerialisedFlag', max_length=1)  # Field name made lowercase.
    countersalesflag = models.CharField(db_column='CounterSalesFlag', max_length=1)  # Field name made lowercase.
    nationality = models.CharField(db_column='Nationality', max_length=3)  # Field name made lowercase.
    deliveryterms = models.TextField(db_column='DeliveryTerms')  # Field name made lowercase.
    transactionnature = models.TextField(db_column='TransactionNature')  # Field name made lowercase.
    transportmode = models.DecimalField(db_column='TransportMode', max_digits=2, decimal_places=0)  # Field name made lowercase.
    processflag = models.DecimalField(db_column='ProcessFlag', max_digits=1, decimal_places=0)  # Field name made lowercase.
    jobsexistflag = models.CharField(db_column='JobsExistFlag', max_length=1)  # Field name made lowercase.
    alternatekey = models.CharField(db_column='AlternateKey', max_length=10)  # Field name made lowercase.
    lastoperator = models.CharField(db_column='LastOperator', max_length=20)  # Field name made lowercase.
    hierarchyflag = models.CharField(db_column='HierarchyFlag', max_length=1)  # Field name made lowercase.
    depositflag = models.CharField(db_column='DepositFlag', max_length=1)  # Field name made lowercase.
    edisource = models.CharField(db_column='EdiSource', max_length=1)  # Field name made lowercase.
    deliverynote = models.CharField(db_column='DeliveryNote', max_length=20)  # Field name made lowercase.
    operator = models.TextField(db_column='Operator')  # Field name made lowercase.
    linecomp = models.CharField(db_column='LineComp', max_length=1)  # Field name made lowercase.
    capturehh = models.IntegerField(db_column='CaptureHh')  # Field name made lowercase.
    capturemm = models.IntegerField(db_column='CaptureMm')  # Field name made lowercase.
    lastdelnote = models.DateTimeField(db_column='LastDelNote', blank=True, null=True)  # Field name made lowercase.
    timedelprtedhh = models.DecimalField(db_column='TimeDelPrtedHh', max_digits=2, decimal_places=0)  # Field name made lowercase.
    timedelprtedmm = models.DecimalField(db_column='TimeDelPrtedMm', max_digits=2, decimal_places=0)  # Field name made lowercase.
    timeinvprtedhh = models.DecimalField(db_column='TimeInvPrtedHh', max_digits=2, decimal_places=0)  # Field name made lowercase.
    timeinvprtedmm = models.DecimalField(db_column='TimeInvPrtedMm', max_digits=2, decimal_places=0)  # Field name made lowercase.
    datelastinvprt = models.DateTimeField(db_column='DateLastInvPrt', blank=True, null=True)  # Field name made lowercase.
    salesperson2 = models.CharField(db_column='Salesperson2', max_length=20)  # Field name made lowercase.
    salesperson3 = models.CharField(db_column='Salesperson3', max_length=20)  # Field name made lowercase.
    salesperson4 = models.CharField(db_column='Salesperson4', max_length=20)  # Field name made lowercase.
    commissionsales1 = models.DecimalField(db_column='CommissionSales1', max_digits=4, decimal_places=2)  # Field name made lowercase.
    commissionsales2 = models.DecimalField(db_column='CommissionSales2', max_digits=4, decimal_places=2)  # Field name made lowercase.
    commissionsales3 = models.DecimalField(db_column='CommissionSales3', max_digits=4, decimal_places=2)  # Field name made lowercase.
    commissionsales4 = models.DecimalField(db_column='CommissionSales4', max_digits=4, decimal_places=2)  # Field name made lowercase.
    timetakentoadd = models.DecimalField(db_column='TimeTakenToAdd', max_digits=3, decimal_places=0)  # Field name made lowercase.
    timetakentochg = models.DecimalField(db_column='TimeTakenToChg', max_digits=3, decimal_places=0)  # Field name made lowercase.
    faxinvinbatch = models.CharField(db_column='FaxInvInBatch', max_length=1)  # Field name made lowercase.
    interwhsale = models.CharField(db_column='InterWhSale', max_length=1)  # Field name made lowercase.
    sourcewarehouse = models.TextField(db_column='SourceWarehouse')  # Field name made lowercase.
    targetwarehouse = models.TextField(db_column='TargetWarehouse')  # Field name made lowercase.
    dispatchesmade = models.CharField(db_column='DispatchesMade', max_length=1)  # Field name made lowercase.
    livedispexist = models.CharField(db_column='LiveDispExist', max_length=1)  # Field name made lowercase.
    numdispatches = models.DecimalField(db_column='NumDispatches', max_digits=4, decimal_places=0)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=50)  # Field name made lowercase.
    shipaddress1 = models.CharField(db_column='ShipAddress1', max_length=40, verbose_name='Customer Name')  # Field name made lowercase.
    shipaddress2 = models.CharField(db_column='ShipAddress2', max_length=40)  # Field name made lowercase.
    shipaddress3 = models.CharField(db_column='ShipAddress3', max_length=40)  # Field name made lowercase.
    shipaddress3loc = models.CharField(db_column='ShipAddress3Loc', max_length=40)  # Field name made lowercase.
    shipaddress4 = models.CharField(db_column='ShipAddress4', max_length=40)  # Field name made lowercase.
    shipaddress5 = models.CharField(db_column='ShipAddress5', max_length=40)  # Field name made lowercase.
    shippostalcode = ZipCodeField(db_column='ShipPostalCode', max_length=10)  # Field name made lowercase.
    shiptogpslat = models.DecimalField(db_column='ShipToGpsLat', max_digits=8, decimal_places=6)  # Field name made lowercase.
    shiptogpslong = models.DecimalField(db_column='ShipToGpsLong', max_digits=9, decimal_places=6)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=2)  # Field name made lowercase.
    countyzip = models.CharField(db_column='CountyZip', max_length=5)  # Field name made lowercase.
    extendedtaxcode = models.CharField(db_column='ExtendedTaxCode', max_length=3)  # Field name made lowercase.
    multishipcode = models.CharField(db_column='MultiShipCode', max_length=5)  # Field name made lowercase.
    webcreated = models.CharField(db_column='WebCreated', max_length=1)  # Field name made lowercase.
    quote = models.TextField(db_column='Quote')  # Field name made lowercase.
    quoteversion = models.TextField(db_column='QuoteVersion')  # Field name made lowercase.
    gtrreference = models.TextField(db_column='GtrReference')  # Field name made lowercase.
    nonmerchflag = models.CharField(db_column='NonMerchFlag', max_length=1)  # Field name made lowercase.
    email = models.EmailField(db_column='Email', max_length=255, verbose_name='Email')  # Field name made lowercase.
    user1 = models.CharField(db_column='User1', max_length=1)  # Field name made lowercase.
    companytaxno = models.CharField(db_column='CompanyTaxNo', max_length=15)  # Field name made lowercase.
    tpmpickupflag = models.CharField(db_column='TpmPickupFlag', max_length=1)  # Field name made lowercase.
    tpmevaluatedflag = models.CharField(db_column='TpmEvaluatedFlag', max_length=1)  # Field name made lowercase.
    standardcomment = models.CharField(db_column='StandardComment', max_length=10)  # Field name made lowercase.
    detailstatus = models.CharField(db_column='DetailStatus', max_length=1)  # Field name made lowercase.
    salesordersource = models.CharField(db_column='SalesOrderSource', max_length=6)  # Field name made lowercase.
    salesordersrcdesc = models.CharField(db_column='SalesOrderSrcDesc', max_length=50)  # Field name made lowercase.
    languagecode = models.CharField(db_column='LanguageCode', max_length=2)  # Field name made lowercase.
    shippinglocation = models.TextField(db_column='ShippingLocation')  # Field name made lowercase.
    includeinmrp = models.CharField(db_column='IncludeInMrp', max_length=1)  # Field name made lowercase.
    timestamp = models.TextField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    @property
    def order_time(self):
        return time(hour=getattr(self, 'capturehh'), minute=getattr(self, 'capturemm'))

    @property
    def order_datetime(self):
        return datetime(self.orderdate.year, self.orderdate.month, self.orderdate.day, self.order_time.hour, self.order_time.minute)

    @property
    def subtotal(self):
        lines = SorDetail.objects.filter(pk=self)
        return sum(line.extended_price for line in lines)

    @property 
    def freight_total(self):
        lines = SorDetail.objects.filter(pk=self)
        return sum(line.freight_price for line in lines)

    @property
    def sales_tax(self):
        return round(((self.subtotal + self.freight_total) * decimal.Decimal(.8)), 2) if self.taxexemptflag != 'E' else 0

    @property
    def total(self):
        return self.subtotal + self.freight_total + self.sales_tax

    class Meta:
        managed = False
        db_table = 'SorMaster'
        unique_together = (('cancelledflag', 'customerponumber', 'salesorder'), ('cancelledflag', 'interwhsale', 'salesorder'), ('cancelledflag', 'detailstatus', 'salesorder'), ('activeflag', 'salesorder'), ('cancelledflag', 'customer', 'salesorder'), ('salesorder', 'salesorder'),)
        verbose_name = 'Sales Order'

class SorMasterRep(models.Model):
    invoicenumber = models.CharField(db_column='InvoiceNumber', max_length=20)  # Field name made lowercase.
    salesorder = models.CharField(db_column='SalesOrder', max_length=20, primary_key=True, verbose_name='Sales Order')  # Field name made lowercase.
    trnyear = models.DecimalField(db_column='TrnYear', max_digits=4, decimal_places=0)  # Field name made lowercase.
    trnmonth = models.DecimalField(db_column='TrnMonth', max_digits=2, decimal_places=0)  # Field name made lowercase.
    register = models.DecimalField(db_column='Register', max_digits=10, decimal_places=0)  # Field name made lowercase.
    summaryline = models.DecimalField(db_column='SummaryLine', max_digits=10, decimal_places=0)  # Field name made lowercase.
    nextdetailline = models.DecimalField(db_column='NextDetailLine', max_digits=4, decimal_places=0)  # Field name made lowercase.
    orderstatus = models.CharField(db_column='OrderStatus', max_length=1)  # Field name made lowercase.
    activeflag = models.CharField(db_column='ActiveFlag', max_length=1)  # Field name made lowercase.
    cancelledflag = models.CharField(db_column='CancelledFlag', max_length=1)  # Field name made lowercase.
    documenttype = models.TextField(db_column='DocumentType', verbose_name='Document Type')  # Field name made lowercase.
    customer = models.ForeignKey(ArCustomer, models.DO_NOTHING, db_column='Customer')  # Field name made lowercase.
    salesperson = models.TextField(db_column='Salesperson', verbose_name='Salesperson')  # Field name made lowercase.
    customerponumber = models.CharField(db_column='CustomerPoNumber', max_length=30, verbose_name='Customer PO')  # Field name made lowercase.
    orderdate = models.DateTimeField(db_column='OrderDate', blank=True, null=True, verbose_name='Order Date')  # Field name made lowercase.
    entrysystemdate = models.DateTimeField(db_column='EntrySystemDate', blank=True, null=True)  # Field name made lowercase.
    reqshipdate = models.DateTimeField(db_column='ReqShipDate', blank=True, null=True)  # Field name made lowercase.
    datelastdocprt = models.DateTimeField(db_column='DateLastDocPrt', blank=True, null=True)  # Field name made lowercase.
    shippinginstrs = models.CharField(db_column='ShippingInstrs', max_length=50)  # Field name made lowercase.
    shippinginstrscod = models.CharField(db_column='ShippingInstrsCod', max_length=6)  # Field name made lowercase.
    altshipaddrflag = models.CharField(db_column='AltShipAddrFlag', max_length=1)  # Field name made lowercase.
    invoicecount = models.DecimalField(db_column='InvoiceCount', max_digits=2, decimal_places=0)  # Field name made lowercase.
    invtermsoverride = models.CharField(db_column='InvTermsOverride', max_length=2)  # Field name made lowercase.
    creditauthority = models.CharField(db_column='CreditAuthority', max_length=3)  # Field name made lowercase.
    branch = models.TextField(db_column='Branch')  # Field name made lowercase.
    specialinstrs = models.CharField(db_column='SpecialInstrs', max_length=30)  # Field name made lowercase.
    entinvoice = models.CharField(db_column='EntInvoice', max_length=20)  # Field name made lowercase.
    entinvoicedate = models.DateTimeField(db_column='EntInvoiceDate', blank=True, null=True)  # Field name made lowercase.
    discpct1 = models.DecimalField(db_column='DiscPct1', max_digits=5, decimal_places=2)  # Field name made lowercase.
    discpct2 = models.DecimalField(db_column='DiscPct2', max_digits=5, decimal_places=2)  # Field name made lowercase.
    discpct3 = models.DecimalField(db_column='DiscPct3', max_digits=5, decimal_places=2)  # Field name made lowercase.
    ordertype = models.TextField(db_column='OrderType')  # Field name made lowercase.
    taxexemptflag = models.CharField(db_column='TaxExemptFlag', max_length=1)  # Field name made lowercase.
    area = models.TextField(db_column='Area')  # Field name made lowercase.
    taxexemptnumber = models.CharField(db_column='TaxExemptNumber', max_length=30)  # Field name made lowercase.
    taxexemptoverride = models.CharField(db_column='TaxExemptOverride', max_length=1)  # Field name made lowercase.
    cashcredit = models.CharField(db_column='CashCredit', max_length=2)  # Field name made lowercase.
    warehouse = models.TextField(db_column='Warehouse')  # Field name made lowercase.
    lastinvoice = models.CharField(db_column='LastInvoice', max_length=20)  # Field name made lowercase.
    scheduledordflag = models.CharField(db_column='ScheduledOrdFlag', max_length=1)  # Field name made lowercase.
    gstexemptflag = models.CharField(db_column='GstExemptFlag', max_length=1)  # Field name made lowercase.
    gstexemptnum = models.CharField(db_column='GstExemptNum', max_length=15)  # Field name made lowercase.
    gstexemptoride = models.CharField(db_column='GstExemptORide', max_length=1)  # Field name made lowercase.
    ibtflag = models.CharField(db_column='IbtFlag', max_length=1)  # Field name made lowercase.
    ordacknwprinted = models.CharField(db_column='OrdAcknwPrinted', max_length=1)  # Field name made lowercase.
    detcustmvmtreqd = models.CharField(db_column='DetCustMvmtReqd', max_length=1)  # Field name made lowercase.
    documentformat = models.CharField(db_column='DocumentFormat', max_length=2)  # Field name made lowercase.
    fixexchangerate = models.CharField(db_column='FixExchangeRate', max_length=1)  # Field name made lowercase.
    exchangerate = models.DecimalField(db_column='ExchangeRate', max_digits=12, decimal_places=6)  # Field name made lowercase.
    muldiv = models.CharField(db_column='MulDiv', max_length=1)  # Field name made lowercase.
    currency = models.TextField(db_column='Currency')  # Field name made lowercase.
    gstdeduction = models.CharField(db_column='GstDeduction', max_length=1)  # Field name made lowercase.
    orderstatusfail = models.CharField(db_column='OrderStatusFail', max_length=1)  # Field name made lowercase.
    consolidatedorder = models.CharField(db_column='ConsolidatedOrder', max_length=1)  # Field name made lowercase.
    creditedinvdate = models.DateTimeField(db_column='CreditedInvDate', blank=True, null=True)  # Field name made lowercase.
    job = models.TextField(db_column='Job')  # Field name made lowercase.
    serialisedflag = models.CharField(db_column='SerialisedFlag', max_length=1)  # Field name made lowercase.
    countersalesflag = models.CharField(db_column='CounterSalesFlag', max_length=1)  # Field name made lowercase.
    nationality = models.CharField(db_column='Nationality', max_length=3)  # Field name made lowercase.
    deliveryterms = models.TextField(db_column='DeliveryTerms')  # Field name made lowercase.
    transactionnature = models.TextField(db_column='TransactionNature')  # Field name made lowercase.
    transportmode = models.DecimalField(db_column='TransportMode', max_digits=2, decimal_places=0)  # Field name made lowercase.
    processflag = models.DecimalField(db_column='ProcessFlag', max_digits=1, decimal_places=0)  # Field name made lowercase.
    jobsexistflag = models.CharField(db_column='JobsExistFlag', max_length=1)  # Field name made lowercase.
    alternatekey = models.CharField(db_column='AlternateKey', max_length=10)  # Field name made lowercase.
    lastoperator = models.CharField(db_column='LastOperator', max_length=20)  # Field name made lowercase.
    hierarchyflag = models.CharField(db_column='HierarchyFlag', max_length=1)  # Field name made lowercase.
    depositflag = models.CharField(db_column='DepositFlag', max_length=1)  # Field name made lowercase.
    edisource = models.CharField(db_column='EdiSource', max_length=1)  # Field name made lowercase.
    deliverynote = models.CharField(db_column='DeliveryNote', max_length=20)  # Field name made lowercase.
    operator = models.TextField(db_column='Operator')  # Field name made lowercase.
    linecomp = models.CharField(db_column='LineComp', max_length=1)  # Field name made lowercase.
    capturehh = models.DecimalField(db_column='CaptureHh', max_digits=2, decimal_places=0)  # Field name made lowercase.
    capturemm = models.DecimalField(db_column='CaptureMm', max_digits=2, decimal_places=0)  # Field name made lowercase.
    lastdelnote = models.DateTimeField(db_column='LastDelNote', blank=True, null=True)  # Field name made lowercase.
    timedelprtedhh = models.DecimalField(db_column='TimeDelPrtedHh', max_digits=2, decimal_places=0)  # Field name made lowercase.
    timedelprtedmm = models.DecimalField(db_column='TimeDelPrtedMm', max_digits=2, decimal_places=0)  # Field name made lowercase.
    timeinvprtedhh = models.DecimalField(db_column='TimeInvPrtedHh', max_digits=2, decimal_places=0)  # Field name made lowercase.
    timeinvprtedmm = models.DecimalField(db_column='TimeInvPrtedMm', max_digits=2, decimal_places=0)  # Field name made lowercase.
    datelastinvprt = models.DateTimeField(db_column='DateLastInvPrt', blank=True, null=True)  # Field name made lowercase.
    salesperson2 = models.CharField(db_column='Salesperson2', max_length=20)  # Field name made lowercase.
    salesperson3 = models.CharField(db_column='Salesperson3', max_length=20)  # Field name made lowercase.
    salesperson4 = models.CharField(db_column='Salesperson4', max_length=20)  # Field name made lowercase.
    commissionsales1 = models.DecimalField(db_column='CommissionSales1', max_digits=4, decimal_places=2)  # Field name made lowercase.
    commissionsales2 = models.DecimalField(db_column='CommissionSales2', max_digits=4, decimal_places=2)  # Field name made lowercase.
    commissionsales3 = models.DecimalField(db_column='CommissionSales3', max_digits=4, decimal_places=2)  # Field name made lowercase.
    commissionsales4 = models.DecimalField(db_column='CommissionSales4', max_digits=4, decimal_places=2)  # Field name made lowercase.
    timetakentoadd = models.DecimalField(db_column='TimeTakenToAdd', max_digits=3, decimal_places=0)  # Field name made lowercase.
    timetakentochg = models.DecimalField(db_column='TimeTakenToChg', max_digits=3, decimal_places=0)  # Field name made lowercase.
    faxinvinbatch = models.CharField(db_column='FaxInvInBatch', max_length=1)  # Field name made lowercase.
    interwhsale = models.CharField(db_column='InterWhSale', max_length=1)  # Field name made lowercase.
    sourcewarehouse = models.TextField(db_column='SourceWarehouse')  # Field name made lowercase.
    targetwarehouse = models.TextField(db_column='TargetWarehouse')  # Field name made lowercase.
    dispatchesmade = models.CharField(db_column='DispatchesMade', max_length=1)  # Field name made lowercase.
    livedispexist = models.CharField(db_column='LiveDispExist', max_length=1)  # Field name made lowercase.
    numdispatches = models.DecimalField(db_column='NumDispatches', max_digits=4, decimal_places=0)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=50)  # Field name made lowercase.
    shipaddr1 = models.CharField(db_column='ShipAddr1', max_length=40)  # Field name made lowercase.
    shipaddr2 = models.CharField(db_column='ShipAddr2', max_length=40)  # Field name made lowercase.
    shipaddr3 = models.CharField(db_column='ShipAddr3', max_length=40)  # Field name made lowercase.
    shipaddr3loc = models.CharField(db_column='ShipAddr3Loc', max_length=40)  # Field name made lowercase.
    shipaddr4 = models.CharField(db_column='ShipAddr4', max_length=40)  # Field name made lowercase.
    shipaddr5 = models.CharField(db_column='ShipAddr5', max_length=40)  # Field name made lowercase.
    postalcode = models.CharField(db_column='PostalCode', max_length=10)  # Field name made lowercase.
    shiptogpslat = models.DecimalField(db_column='ShipToGpsLat', max_digits=8, decimal_places=6)  # Field name made lowercase.
    shiptogpslong = models.DecimalField(db_column='ShipToGpsLong', max_digits=9, decimal_places=6)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=2)  # Field name made lowercase.
    countyzip = models.CharField(db_column='CountyZip', max_length=5)  # Field name made lowercase.
    extendedtaxcode = models.CharField(db_column='ExtendedTaxCode', max_length=3)  # Field name made lowercase.
    multishipcode = models.CharField(db_column='MultiShipCode', max_length=5)  # Field name made lowercase.
    webcreated = models.CharField(db_column='WebCreated', max_length=1)  # Field name made lowercase.
    quote = models.TextField(db_column='Quote')  # Field name made lowercase.
    quoteversion = models.TextField(db_column='QuoteVersion')  # Field name made lowercase.
    gtrreference = models.TextField(db_column='GtrReference')  # Field name made lowercase.
    nonmerchflag = models.CharField(db_column='NonMerchFlag', max_length=1)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255)  # Field name made lowercase.
    companytaxno = models.CharField(db_column='CompanyTaxNo', max_length=15)  # Field name made lowercase.
    tpmpickupflag = models.CharField(db_column='TpmPickupFlag', max_length=1)  # Field name made lowercase.
    tpmevaluatedflag = models.CharField(db_column='TpmEvaluatedFlag', max_length=1)  # Field name made lowercase.
    standardcomment = models.CharField(db_column='StandardComment', max_length=10)  # Field name made lowercase.
    detailstatus = models.CharField(db_column='DetailStatus', max_length=1)  # Field name made lowercase.
    salesordersource = models.CharField(db_column='SalesOrderSource', max_length=6)  # Field name made lowercase.
    salesordersrcdesc = models.CharField(db_column='SalesOrderSrcDesc', max_length=50)  # Field name made lowercase.
    languagecode = models.CharField(db_column='LanguageCode', max_length=2)  # Field name made lowercase.
    shippinglocation = models.TextField(db_column='ShippingLocation')  # Field name made lowercase.
    timestamp = models.TextField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'SorMasterRep'
        unique_together = (('invoicenumber', 'invoicenumber', 'invoicenumber', 'invoicenumber', 'invoicenumber', 'invoicenumber', 'salesorder', 'salesorder', 'salesorder', 'salesorder'), ('interwhsale', 'gtrreference', 'invoicenumber', 'salesorder'),)
        verbose_name ='Sales Order'


class SorDetail(models.Model):
    salesorder = models.ForeignKey(SorMaster, models.DO_NOTHING, db_column='SalesOrder', primary_key=True)  # Field name made lowercase.
    salesorderline = models.DecimalField(db_column='SalesOrderLine', max_digits=4, decimal_places=0)  # Field name made lowercase.
    linetype = models.CharField(db_column='LineType', max_length=1)  # Field name made lowercase.
    mstockcode = models.ForeignKey(InvMaster, models.DO_NOTHING, db_column='MStockCode')  # Field name made lowercase.
    mstockdes = models.CharField(db_column='MStockDes', max_length=50)  # Field name made lowercase.
    mwarehouse = models.TextField(db_column='MWarehouse')  # Field name made lowercase.
    mbin = models.TextField(db_column='MBin')  # Field name made lowercase.
    morderqty = models.DecimalField(db_column='MOrderQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    mshipqty = models.DecimalField(db_column='MShipQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    mbackorderqty = models.DecimalField(db_column='MBackOrderQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    munitcost = models.DecimalField(db_column='MUnitCost', max_digits=15, decimal_places=5)  # Field name made lowercase.
    mbomflag = models.CharField(db_column='MBomFlag', max_length=1)  # Field name made lowercase.
    mparentkittype = models.CharField(db_column='MParentKitType', max_length=1)  # Field name made lowercase.
    mqtyper = models.DecimalField(db_column='MQtyPer', max_digits=18, decimal_places=6)  # Field name made lowercase.
    mscrappercentage = models.DecimalField(db_column='MScrapPercentage', max_digits=4, decimal_places=2)  # Field name made lowercase.
    mprintcomponent = models.CharField(db_column='MPrintComponent', max_length=1)  # Field name made lowercase.
    mcomponentseq = models.CharField(db_column='MComponentSeq', max_length=6)  # Field name made lowercase.
    mqtychangesflag = models.CharField(db_column='MQtyChangesFlag', max_length=1)  # Field name made lowercase.
    moptionalflag = models.CharField(db_column='MOptionalFlag', max_length=1)  # Field name made lowercase.
    mdecimals = models.DecimalField(db_column='MDecimals', max_digits=1, decimal_places=0)  # Field name made lowercase.
    morderuom = models.TextField(db_column='MOrderUom')  # Field name made lowercase.
    mstockqtytoshp = models.DecimalField(db_column='MStockQtyToShp', max_digits=18, decimal_places=6)  # Field name made lowercase.
    mstockinguom = models.CharField(db_column='MStockingUom', max_length=10)  # Field name made lowercase.
    mconvfactordum = models.DecimalField(db_column='MConvFactOrdUm', max_digits=12, decimal_places=6)  # Field name made lowercase.
    mmuldivprcfct = models.CharField(db_column='MMulDivPrcFct', max_length=1)  # Field name made lowercase.
    mprice = models.DecimalField(db_column='MPrice', max_digits=15, decimal_places=5)  # Field name made lowercase.
    mpriceuom = models.TextField(db_column='MPriceUom')  # Field name made lowercase.
    mcommissioncode = models.TextField(db_column='MCommissionCode')  # Field name made lowercase.
    mdiscpct1 = models.DecimalField(db_column='MDiscPct1', max_digits=5, decimal_places=2)  # Field name made lowercase.
    mdiscpct2 = models.DecimalField(db_column='MDiscPct2', max_digits=5, decimal_places=2)  # Field name made lowercase.
    mdiscpct3 = models.DecimalField(db_column='MDiscPct3', max_digits=5, decimal_places=2)  # Field name made lowercase.
    mdiscvalflag = models.CharField(db_column='MDiscValFlag', max_length=1)  # Field name made lowercase.
    mdiscvalue = models.DecimalField(db_column='MDiscValue', max_digits=14, decimal_places=2)  # Field name made lowercase.
    mproductclass = models.TextField(db_column='MProductClass')  # Field name made lowercase.
    mtaxcode = models.TextField(db_column='MTaxCode')  # Field name made lowercase.
    mlineshipdate = models.DateTimeField(db_column='MLineShipDate', blank=True, null=True)  # Field name made lowercase.
    mallocstatsched = models.CharField(db_column='MAllocStatSched', max_length=1)  # Field name made lowercase.
    mfsttaxcode = models.CharField(db_column='MFstTaxCode', max_length=3)  # Field name made lowercase.
    mstockunitmass = models.DecimalField(db_column='MStockUnitMass', max_digits=18, decimal_places=6)  # Field name made lowercase.
    mstockunitvol = models.DecimalField(db_column='MStockUnitVol', max_digits=18, decimal_places=6)  # Field name made lowercase.
    mpricecode = models.TextField(db_column='MPriceCode')  # Field name made lowercase.
    mconvfactalloc = models.DecimalField(db_column='MConvFactAlloc', max_digits=12, decimal_places=6)  # Field name made lowercase.
    mmuldivqtyfct = models.CharField(db_column='MMulDivQtyFct', max_length=1)  # Field name made lowercase.
    mtraceabletype = models.CharField(db_column='MTraceableType', max_length=1)  # Field name made lowercase.
    mmpsflag = models.CharField(db_column='MMpsFlag', max_length=1)  # Field name made lowercase.
    mpickingslip = models.CharField(db_column='MPickingSlip', max_length=1)  # Field name made lowercase.
    mmovementreqd = models.CharField(db_column='MMovementReqd', max_length=1)  # Field name made lowercase.
    mserialmethod = models.CharField(db_column='MSerialMethod', max_length=1)  # Field name made lowercase.
    mzeroqtycrnote = models.CharField(db_column='MZeroQtyCrNote', max_length=1)  # Field name made lowercase.
    mabcapplied = models.CharField(db_column='MAbcApplied', max_length=1)  # Field name made lowercase.
    mmpsgrossreqd = models.CharField(db_column='MMpsGrossReqd', max_length=1)  # Field name made lowercase.
    mcontract = models.TextField(db_column='MContract')  # Field name made lowercase.
    mbuyinggroup = models.TextField(db_column='MBuyingGroup')  # Field name made lowercase.
    mcussupstkcode = models.CharField(db_column='MCusSupStkCode', max_length=30)  # Field name made lowercase.
    mcusretailprice = models.DecimalField(db_column='MCusRetailPrice', max_digits=15, decimal_places=5)  # Field name made lowercase.
    mtariffcode = models.CharField(db_column='MTariffCode', max_length=15)  # Field name made lowercase.
    mlinereceiptdat = models.DateTimeField(db_column='MLineReceiptDat', blank=True, null=True)  # Field name made lowercase.
    mleadtime = models.DecimalField(db_column='MLeadTime', max_digits=10, decimal_places=0)  # Field name made lowercase.
    mtrfcostmult = models.DecimalField(db_column='MTrfCostMult', max_digits=9, decimal_places=6)  # Field name made lowercase.
    msupplementaryun = models.CharField(db_column='MSupplementaryUn', max_length=1)  # Field name made lowercase.
    mreviewflag = models.CharField(db_column='MReviewFlag', max_length=1)  # Field name made lowercase.
    mreviewstatus = models.CharField(db_column='MReviewStatus', max_length=1)  # Field name made lowercase.
    minvoiceprinted = models.CharField(db_column='MInvoicePrinted', max_length=1)  # Field name made lowercase.
    mdelnoteprinted = models.CharField(db_column='MDelNotePrinted', max_length=1)  # Field name made lowercase.
    mordackprinted = models.CharField(db_column='MOrdAckPrinted', max_length=1)  # Field name made lowercase.
    mhierarchyjob = models.CharField(db_column='MHierarchyJob', max_length=20)  # Field name made lowercase.
    mcustrequestdat = models.DateTimeField(db_column='MCustRequestDat', blank=True, null=True)  # Field name made lowercase.
    mlastdelnote = models.CharField(db_column='MLastDelNote', max_length=20)  # Field name made lowercase.
    muserdef = models.CharField(db_column='MUserDef', max_length=4)  # Field name made lowercase.
    mqtydispatched = models.DecimalField(db_column='MQtyDispatched', max_digits=18, decimal_places=6)  # Field name made lowercase.
    mdiscchanged = models.CharField(db_column='MDiscChanged', max_length=1)  # Field name made lowercase.
    mcreditorderno = models.CharField(db_column='MCreditOrderNo', max_length=20)  # Field name made lowercase.
    mcreditorderline = models.DecimalField(db_column='MCreditOrderLine', max_digits=4, decimal_places=0)  # Field name made lowercase.
    munitquantity = models.CharField(db_column='MUnitQuantity', max_length=1)  # Field name made lowercase.
    mconvfactunitq = models.DecimalField(db_column='MConvFactUnitQ', max_digits=6, decimal_places=0)  # Field name made lowercase.
    maltuomunitq = models.CharField(db_column='MAltUomUnitQ', max_length=10)  # Field name made lowercase.
    mdecimalsunitq = models.DecimalField(db_column='MDecimalsUnitQ', max_digits=1, decimal_places=0)  # Field name made lowercase.
    meccflag = models.CharField(db_column='MEccFlag', max_length=1)  # Field name made lowercase.
    mversion = models.TextField(db_column='MVersion')  # Field name made lowercase.
    mrelease = models.TextField(db_column='MRelease')  # Field name made lowercase.
    mcommitdate = models.DateTimeField(db_column='MCommitDate', blank=True, null=True)  # Field name made lowercase.
    qtyreserved = models.DecimalField(db_column='QtyReserved', max_digits=18, decimal_places=6)  # Field name made lowercase.
    ncomment = models.CharField(db_column='NComment', max_length=100)  # Field name made lowercase.
    ncommentfromlin = models.DecimalField(db_column='NCommentFromLin', max_digits=4, decimal_places=0)  # Field name made lowercase.
    nmscchargevalue = models.DecimalField(db_column='NMscChargeValue', max_digits=14, decimal_places=2)  # Field name made lowercase.
    nmscproductcls = models.CharField(db_column='NMscProductCls', max_length=20)  # Field name made lowercase.
    nmscchargecost = models.DecimalField(db_column='NMscChargeCost', max_digits=14, decimal_places=2)  # Field name made lowercase.
    nmscinvcharge = models.CharField(db_column='NMscInvCharge', max_length=1)  # Field name made lowercase.
    ncommenttype = models.CharField(db_column='NCommentType', max_length=2)  # Field name made lowercase.
    nmsctaxcode = models.CharField(db_column='NMscTaxCode', max_length=3)  # Field name made lowercase.
    nmscfstcode = models.CharField(db_column='NMscFstCode', max_length=3)  # Field name made lowercase.
    ncommenttexttyp = models.CharField(db_column='NCommentTextTyp', max_length=1)  # Field name made lowercase.
    nmscchargeqty = models.DecimalField(db_column='NMscChargeQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    nsrvinctotal = models.CharField(db_column='NSrvIncTotal', max_length=1)  # Field name made lowercase.
    nsrvsummary = models.CharField(db_column='NSrvSummary', max_length=1)  # Field name made lowercase.
    nsrvchargetype = models.CharField(db_column='NSrvChargeType', max_length=1)  # Field name made lowercase.
    nsrvparentline = models.DecimalField(db_column='NSrvParentLine', max_digits=4, decimal_places=0)  # Field name made lowercase.
    nsrvunitprice = models.DecimalField(db_column='NSrvUnitPrice', max_digits=15, decimal_places=5)  # Field name made lowercase.
    nsrvunitcost = models.DecimalField(db_column='NSrvUnitCost', max_digits=15, decimal_places=5)  # Field name made lowercase.
    nsrvqtyfactor = models.DecimalField(db_column='NSrvQtyFactor', max_digits=12, decimal_places=6)  # Field name made lowercase.
    nsrvapplyfactor = models.CharField(db_column='NSrvApplyFactor', max_length=1)  # Field name made lowercase.
    nsrvdecimalrnd = models.DecimalField(db_column='NSrvDecimalRnd', max_digits=1, decimal_places=0)  # Field name made lowercase.
    nsrvdecrndflag = models.CharField(db_column='NSrvDecRndFlag', max_length=1)  # Field name made lowercase.
    nsrvminvalue = models.DecimalField(db_column='NSrvMinValue', max_digits=14, decimal_places=2)  # Field name made lowercase.
    nsrvmaxvalue = models.DecimalField(db_column='NSrvMaxValue', max_digits=14, decimal_places=2)  # Field name made lowercase.
    nsrvmuldiv = models.CharField(db_column='NSrvMulDiv', max_length=1)  # Field name made lowercase.
    nprtoninv = models.CharField(db_column='NPrtOnInv', max_length=1)  # Field name made lowercase.
    nprtondel = models.CharField(db_column='NPrtOnDel', max_length=1)  # Field name made lowercase.
    nprtonack = models.CharField(db_column='NPrtOnAck', max_length=1)  # Field name made lowercase.
    ntaxamountflag = models.CharField(db_column='NTaxAmountFlag', max_length=1)  # Field name made lowercase.
    ndepretflagproj = models.CharField(db_column='NDepRetFlagProj', max_length=1)  # Field name made lowercase.
    nretentionjob = models.CharField(db_column='NRetentionJob', max_length=20)  # Field name made lowercase.
    nsrvminquantity = models.DecimalField(db_column='NSrvMinQuantity', max_digits=18, decimal_places=6)  # Field name made lowercase.
    nchargecode = models.CharField(db_column='NChargeCode', max_length=6)  # Field name made lowercase.
    includeinmrp = models.CharField(db_column='IncludeInMrp', max_length=1)  # Field name made lowercase.
    productcode = models.TextField(db_column='ProductCode')  # Field name made lowercase.
    librarycode = models.CharField(db_column='LibraryCode', max_length=5)  # Field name made lowercase.
    materialallocline = models.CharField(db_column='MaterialAllocLine', max_length=2)  # Field name made lowercase.
    scrapquantity = models.DecimalField(db_column='ScrapQuantity', max_digits=18, decimal_places=6)  # Field name made lowercase.
    fixedqtyperflag = models.CharField(db_column='FixedQtyPerFlag', max_length=1)  # Field name made lowercase.
    fixedqtyper = models.DecimalField(db_column='FixedQtyPer', max_digits=18, decimal_places=6)  # Field name made lowercase.
    multishipcode = models.CharField(db_column='MultiShipCode', max_length=5)  # Field name made lowercase.
    user1 = models.CharField(db_column='User1', max_length=1)  # Field name made lowercase.
    creditreason = models.TextField(db_column='CreditReason')  # Field name made lowercase.
    origshipdateaps = models.DateTimeField(db_column='OrigShipDateAps', blank=True, null=True)  # Field name made lowercase.
    tpmusageflag = models.CharField(db_column='TpmUsageFlag', max_length=1)  # Field name made lowercase.
    promotioncode = models.TextField(db_column='PromotionCode')  # Field name made lowercase.
    tpmsequence = models.TextField(db_column='TpmSequence')  # Field name made lowercase.
    salesorderinitline = models.TextField(db_column='SalesOrderInitLine')  # Field name made lowercase.
    preactorpriority = models.DecimalField(db_column='PreactorPriority', max_digits=2, decimal_places=0)  # Field name made lowercase.
    salesorderdetstat = models.CharField(db_column='SalesOrderDetStat', max_length=1)  # Field name made lowercase.
    salesorderresstat = models.CharField(db_column='SalesOrderResStat', max_length=1)  # Field name made lowercase.
    qtyreservedship = models.DecimalField(db_column='QtyReservedShip', max_digits=18, decimal_places=6)  # Field name made lowercase.
    timestamp = models.TextField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    @property
    def extended_price(self):
        disc_pct = self.mprice * self.mdiscpct1 * decimal.Decimal(0.01)
        disc_unit = self.mdiscvalue if self.mdiscvalflag == 'U' else 0
        unit_price = self.mprice - disc_pct - disc_unit

        if self.mdiscvalflag == 'V':
            return unit_price * (self.morderqty if self.mshipqty == 0 else self.mshipqty) - self.mdiscvalue
        else:
            return unit_price * (self.morderqty if self.mshipqty == 0 else self.mshipqty)

    @property
    def freight_price(self):
        return self.nmscchargevalue if self.nmscproductcls == '_FRT' else 0

    class Meta:
        managed = False
        db_table = 'SorDetail'
        unique_together = (('salesorder', 'salesorderinitline', 'salesorderline'), ('salesorderdetstat', 'salesorder', 'salesorderline'), ('mstockcode', 'salesorder', 'salesorderline'), ('salesorder', 'salesorder', 'salesorder', 'salesorder', 'salesorderline'),)


class SorDetailRep(models.Model):
    invoice = models.ForeignKey(ArInvoice, models.DO_NOTHING, db_column='Invoice', primary_key=True)  # Field name made lowercase.
    salesorder = models.ForeignKey(SorMaster, models.DO_NOTHING, db_column='SalesOrder')  # Field name made lowercase.
    salesorderline = models.ForeignKey(SorDetail, models.DO_NOTHING, db_column='SalesOrderLine')  # Field name made lowercase.
    linetype = models.CharField(db_column='LineType', max_length=1)  # Field name made lowercase.
    stockcode = models.ForeignKey(InvMaster, models.DO_NOTHING, db_column='StockCode')  # Field name made lowercase.
    stockdescription = models.CharField(db_column='StockDescription', max_length=50)  # Field name made lowercase.
    warehouse = models.TextField(db_column='Warehouse')  # Field name made lowercase.
    bin = models.TextField(db_column='Bin')  # Field name made lowercase.
    orderqty = models.DecimalField(db_column='OrderQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    shipqty = models.DecimalField(db_column='ShipQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    backorderqty = models.DecimalField(db_column='BackOrderQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    unitcost = models.DecimalField(db_column='UnitCost', max_digits=15, decimal_places=5)  # Field name made lowercase.
    bomflag = models.CharField(db_column='BomFlag', max_length=1)  # Field name made lowercase.
    parentkittype = models.CharField(db_column='ParentKitType', max_length=1)  # Field name made lowercase.
    qtyper = models.DecimalField(db_column='QtyPer', max_digits=18, decimal_places=6)  # Field name made lowercase.
    scrappercentage = models.DecimalField(db_column='ScrapPercentage', max_digits=4, decimal_places=2)  # Field name made lowercase.
    printcomponent = models.CharField(db_column='PrintComponent', max_length=1)  # Field name made lowercase.
    componentseqnum = models.CharField(db_column='ComponentSeqNum', max_length=6)  # Field name made lowercase.
    qtychangesflag = models.CharField(db_column='QtyChangesFlag', max_length=1)  # Field name made lowercase.
    optionalflag = models.CharField(db_column='OptionalFlag', max_length=1)  # Field name made lowercase.
    decimals = models.DecimalField(db_column='Decimals', max_digits=1, decimal_places=0)  # Field name made lowercase.
    orderuom = models.TextField(db_column='OrderUom')  # Field name made lowercase.
    stockqtytoship = models.DecimalField(db_column='StockQtyToShip', max_digits=18, decimal_places=6)  # Field name made lowercase.
    stockinguom = models.CharField(db_column='StockingUom', max_length=10)  # Field name made lowercase.
    convfactorduom = models.DecimalField(db_column='ConvFactOrdUom', max_digits=12, decimal_places=6)  # Field name made lowercase.
    muldivc = models.CharField(db_column='MulDivC', max_length=1)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=15, decimal_places=5)  # Field name made lowercase.
    priceuom = models.TextField(db_column='PriceUom')  # Field name made lowercase.
    commissioncode = models.TextField(db_column='CommissionCode')  # Field name made lowercase.
    discpct1 = models.DecimalField(db_column='DiscPct1', max_digits=5, decimal_places=2)  # Field name made lowercase.
    discpct2 = models.DecimalField(db_column='DiscPct2', max_digits=5, decimal_places=2)  # Field name made lowercase.
    discpct3 = models.DecimalField(db_column='DiscPct3', max_digits=5, decimal_places=2)  # Field name made lowercase.
    discvalflag = models.CharField(db_column='DiscValFlag', max_length=1)  # Field name made lowercase.
    discvalue = models.DecimalField(db_column='DiscValue', max_digits=14, decimal_places=2)  # Field name made lowercase.
    productclass = models.TextField(db_column='ProductClass')  # Field name made lowercase.
    taxcode = models.TextField(db_column='TaxCode')  # Field name made lowercase.
    lineshipdate = models.DateTimeField(db_column='LineShipDate', blank=True, null=True)  # Field name made lowercase.
    allocstatussched = models.CharField(db_column='AllocStatusSched', max_length=1)  # Field name made lowercase.
    fsttaxcode = models.CharField(db_column='FstTaxCode', max_length=3)  # Field name made lowercase.
    stockingunitmass = models.DecimalField(db_column='StockingUnitMass', max_digits=18, decimal_places=6)  # Field name made lowercase.
    stockingunitvol = models.DecimalField(db_column='StockingUnitVol', max_digits=18, decimal_places=6)  # Field name made lowercase.
    pricecode = models.TextField(db_column='PriceCode')  # Field name made lowercase.
    convfactoralloc = models.DecimalField(db_column='ConvFactorAlloc', max_digits=12, decimal_places=6)  # Field name made lowercase.
    muldiva = models.CharField(db_column='MulDivA', max_length=1)  # Field name made lowercase.
    traceabletype = models.CharField(db_column='TraceableType', max_length=1)  # Field name made lowercase.
    mpsflag = models.CharField(db_column='MpsFlag', max_length=1)  # Field name made lowercase.
    pickingslipprted = models.CharField(db_column='PickingSlipPrted', max_length=1)  # Field name made lowercase.
    movementreqd = models.CharField(db_column='MovementReqd', max_length=1)  # Field name made lowercase.
    serialmethod = models.CharField(db_column='SerialMethod', max_length=1)  # Field name made lowercase.
    zeroqtycrnote = models.CharField(db_column='ZeroQtyCrNote', max_length=1)  # Field name made lowercase.
    abcapplied = models.CharField(db_column='AbcApplied', max_length=1)  # Field name made lowercase.
    mpsgrossreqd = models.CharField(db_column='MpsGrossReqd', max_length=1)  # Field name made lowercase.
    contract = models.TextField(db_column='Contract')  # Field name made lowercase.
    buyinggroup = models.TextField(db_column='BuyingGroup')  # Field name made lowercase.
    custsupstkcode = models.CharField(db_column='CustSupStkCode', max_length=30)  # Field name made lowercase.
    custretailprice = models.DecimalField(db_column='CustRetailPrice', max_digits=15, decimal_places=5)  # Field name made lowercase.
    tariffcode = models.CharField(db_column='TariffCode', max_length=15)  # Field name made lowercase.
    linereceiptdate = models.DateTimeField(db_column='LineReceiptDate', blank=True, null=True)  # Field name made lowercase.
    leadtime = models.DecimalField(db_column='LeadTime', max_digits=10, decimal_places=0)  # Field name made lowercase.
    trfcostmultiply = models.DecimalField(db_column='TrfCostMultiply', max_digits=9, decimal_places=6)  # Field name made lowercase.
    supplementaryunit = models.CharField(db_column='SupplementaryUnit', max_length=1)  # Field name made lowercase.
    reviewflag = models.CharField(db_column='ReviewFlag', max_length=1)  # Field name made lowercase.
    reviewstatus = models.CharField(db_column='ReviewStatus', max_length=1)  # Field name made lowercase.
    invoiceprinted = models.CharField(db_column='InvoicePrinted', max_length=1)  # Field name made lowercase.
    delnoteprinted = models.CharField(db_column='DelNotePrinted', max_length=1)  # Field name made lowercase.
    ordacknwprinted = models.CharField(db_column='OrdAcknwPrinted', max_length=1)  # Field name made lowercase.
    hierarchyjob = models.CharField(db_column='HierarchyJob', max_length=20)  # Field name made lowercase.
    custrequestdate = models.DateTimeField(db_column='CustRequestDate', blank=True, null=True)  # Field name made lowercase.
    lastdelnote = models.CharField(db_column='LastDelNote', max_length=20)  # Field name made lowercase.
    userdef = models.CharField(db_column='UserDef', max_length=4)  # Field name made lowercase.
    qtydispatched = models.DecimalField(db_column='QtyDispatched', max_digits=18, decimal_places=6)  # Field name made lowercase.
    discchanged = models.CharField(db_column='DiscChanged', max_length=1)  # Field name made lowercase.
    qtyalreadycredited = models.DecimalField(db_column='QtyAlreadyCredited', max_digits=18, decimal_places=6)  # Field name made lowercase.
    creditorderno = models.CharField(db_column='CreditOrderNo', max_length=20)  # Field name made lowercase.
    creditorderline = models.DecimalField(db_column='CreditOrderLine', max_digits=4, decimal_places=0)  # Field name made lowercase.
    munitquantity = models.CharField(db_column='MUnitQuantity', max_length=1)  # Field name made lowercase.
    mconvfactunitq = models.DecimalField(db_column='MConvFactUnitQ', max_digits=6, decimal_places=0)  # Field name made lowercase.
    maltuomunitq = models.CharField(db_column='MAltUomUnitQ', max_length=10)  # Field name made lowercase.
    mdecimalsunitq = models.DecimalField(db_column='MDecimalsUnitQ', max_digits=1, decimal_places=0)  # Field name made lowercase.
    meccflag = models.CharField(db_column='MEccFlag', max_length=1)  # Field name made lowercase.
    mversion = models.TextField(db_column='MVersion')  # Field name made lowercase.
    mrelease = models.TextField(db_column='MRelease')  # Field name made lowercase.
    mcommitdate = models.DateTimeField(db_column='MCommitDate', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=100)  # Field name made lowercase.
    commentfromline = models.DecimalField(db_column='CommentFromLine', max_digits=4, decimal_places=0)  # Field name made lowercase.
    mscchargevalue = models.DecimalField(db_column='MscChargeValue', max_digits=14, decimal_places=2)  # Field name made lowercase.
    mscproductclass = models.CharField(db_column='MscProductClass', max_length=20)  # Field name made lowercase.
    mscchargecost = models.DecimalField(db_column='MscChargeCost', max_digits=14, decimal_places=2)  # Field name made lowercase.
    mscinvcharge = models.CharField(db_column='MscInvCharge', max_length=1)  # Field name made lowercase.
    commenttype = models.CharField(db_column='CommentType', max_length=2)  # Field name made lowercase.
    msctaxcode = models.CharField(db_column='MscTaxCode', max_length=3)  # Field name made lowercase.
    mscfstcode = models.CharField(db_column='MscFstCode', max_length=3)  # Field name made lowercase.
    texttype = models.CharField(db_column='TextType', max_length=1)  # Field name made lowercase.
    mscchargeqty = models.DecimalField(db_column='MscChargeQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    srvinctotal = models.CharField(db_column='SrvIncTotal', max_length=1)  # Field name made lowercase.
    srvsummary = models.CharField(db_column='SrvSummary', max_length=1)  # Field name made lowercase.
    srvchargetype = models.CharField(db_column='SrvChargeType', max_length=1)  # Field name made lowercase.
    srvparentline = models.DecimalField(db_column='SrvParentLine', max_digits=4, decimal_places=0)  # Field name made lowercase.
    srvunitprice = models.DecimalField(db_column='SrvUnitPrice', max_digits=15, decimal_places=5)  # Field name made lowercase.
    srvunitcost = models.DecimalField(db_column='SrvUnitCost', max_digits=15, decimal_places=5)  # Field name made lowercase.
    srvqtyfactor = models.DecimalField(db_column='SrvQtyFactor', max_digits=12, decimal_places=6)  # Field name made lowercase.
    srvapplyfactor = models.CharField(db_column='SrvApplyFactor', max_length=1)  # Field name made lowercase.
    srvdecimalrnd = models.DecimalField(db_column='SrvDecimalRnd', max_digits=1, decimal_places=0)  # Field name made lowercase.
    srvdecrndflag = models.CharField(db_column='SrvDecRndFlag', max_length=1)  # Field name made lowercase.
    srvminvalue = models.DecimalField(db_column='SrvMinValue', max_digits=14, decimal_places=2)  # Field name made lowercase.
    srvmaxvalue = models.DecimalField(db_column='SrvMaxValue', max_digits=14, decimal_places=2)  # Field name made lowercase.
    srvmuldiv = models.CharField(db_column='SrvMulDiv', max_length=1)  # Field name made lowercase.
    prtoninv = models.CharField(db_column='PrtOnInv', max_length=1)  # Field name made lowercase.
    prtondel = models.CharField(db_column='PrtOnDel', max_length=1)  # Field name made lowercase.
    prtonack = models.CharField(db_column='PrtOnAck', max_length=1)  # Field name made lowercase.
    amounttaxflag = models.CharField(db_column='AmountTaxFlag', max_length=1)  # Field name made lowercase.
    ndepretflagproj = models.CharField(db_column='NDepRetFlagProj', max_length=1)  # Field name made lowercase.
    nretentionjob = models.CharField(db_column='NRetentionJob', max_length=20)  # Field name made lowercase.
    nsrvminquantity = models.DecimalField(db_column='NSrvMinQuantity', max_digits=18, decimal_places=6)  # Field name made lowercase.
    nchargecode = models.CharField(db_column='NChargeCode', max_length=6)  # Field name made lowercase.
    productcode = models.TextField(db_column='ProductCode')  # Field name made lowercase.
    librarycode = models.CharField(db_column='LibraryCode', max_length=5)  # Field name made lowercase.
    user1 = models.CharField(db_column='User1', max_length=1)  # Field name made lowercase.
    creditreason = models.CharField(db_column='CreditReason', max_length=6)  # Field name made lowercase.
    origshipdateaps = models.DateTimeField(db_column='OrigShipDateAps', blank=True, null=True)  # Field name made lowercase.
    tpmusageflag = models.CharField(db_column='TpmUsageFlag', max_length=1)  # Field name made lowercase.
    promotioncode = models.TextField(db_column='PromotionCode')  # Field name made lowercase.
    tpmsequence = models.TextField(db_column='TpmSequence')  # Field name made lowercase.
    salesorderinitline = models.TextField(db_column='SalesOrderInitLine')  # Field name made lowercase.
    preactorpriority = models.DecimalField(db_column='PreactorPriority', max_digits=2, decimal_places=0)  # Field name made lowercase.
    salesorderdetstat = models.CharField(db_column='SalesOrderDetStat', max_length=1)  # Field name made lowercase.
    materialallocline = models.CharField(db_column='MaterialAllocLine', max_length=2)  # Field name made lowercase.
    scrapquantity = models.DecimalField(db_column='ScrapQuantity', max_digits=18, decimal_places=6)  # Field name made lowercase.
    fixedqtyperflag = models.CharField(db_column='FixedQtyPerFlag', max_length=1)  # Field name made lowercase.
    fixedqtyper = models.DecimalField(db_column='FixedQtyPer', max_digits=18, decimal_places=6)  # Field name made lowercase.
    timestamp = models.TextField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'SorDetailRep'
        unique_together = (('invoice', 'invoice', 'invoice', 'salesorder', 'salesorder', 'salesorder', 'salesorder', 'salesorder', 'salesorder', 'salesorder', 'salesorderline'),)


class ArInvoicePay(models.Model):
    customer = models.ForeignKey(ArCustomer, models.DO_NOTHING, db_column='Customer', primary_key=True)  # Field name made lowercase.
    invoice = models.ForeignKey(ArInvoice, models.DO_NOTHING, db_column='Invoice')  # Field name made lowercase.
    documenttype = models.TextField(db_column='DocumentType')  # Field name made lowercase.
    entrynumber = models.TextField(db_column='EntryNumber')  # Field name made lowercase.
    trntype = models.CharField(db_column='TrnType', max_length=1)  # Field name made lowercase.
    journaldate = models.DateTimeField(db_column='JournalDate', blank=True, null=True)  # Field name made lowercase.
    journal = models.TextField(db_column='Journal')  # Field name made lowercase.
    reference = models.CharField(db_column='Reference', max_length=30)  # Field name made lowercase.
    trnvalue = models.DecimalField(db_column='TrnValue', max_digits=14, decimal_places=2)  # Field name made lowercase.
    discvalue = models.DecimalField(db_column='DiscValue', max_digits=14, decimal_places=2)  # Field name made lowercase.
    trnyear = models.TextField(db_column='TrnYear')  # Field name made lowercase.
    trnmonth = models.TextField(db_column='TrnMonth')  # Field name made lowercase.
    salesorder = models.ForeignKey('SorMaster', models.DO_NOTHING, db_column='SalesOrder')  # Field name made lowercase.
    postvalue = models.DecimalField(db_column='PostValue', max_digits=14, decimal_places=2)  # Field name made lowercase.
    postcurrency = models.CharField(db_column='PostCurrency', max_length=3)  # Field name made lowercase.
    postconvrate = models.DecimalField(db_column='PostConvRate', max_digits=12, decimal_places=6)  # Field name made lowercase.
    postmuldiv = models.CharField(db_column='PostMulDiv', max_length=1)  # Field name made lowercase.
    accountcur = models.CharField(db_column='AccountCur', max_length=3)  # Field name made lowercase.
    accountconvrate = models.DecimalField(db_column='AccountConvRate', max_digits=12, decimal_places=6)  # Field name made lowercase.
    accountmuldiv = models.CharField(db_column='AccountMulDiv', max_length=1)  # Field name made lowercase.
    triangcurrency = models.CharField(db_column='TriangCurrency', max_length=3)  # Field name made lowercase.
    triangconvrate = models.DecimalField(db_column='TriangConvRate', max_digits=12, decimal_places=6)  # Field name made lowercase.
    triangmuldiv = models.CharField(db_column='TriangMulDiv', max_length=1)  # Field name made lowercase.
    branch = models.TextField(db_column='Branch')  # Field name made lowercase.
    paymentnumber = models.TextField(db_column='PaymentNumber')  # Field name made lowercase.
    collector = models.TextField(db_column='Collector')  # Field name made lowercase.
    salesperson = models.TextField(db_column='Salesperson')  # Field name made lowercase.
    invoicenotation = models.CharField(db_column='InvoiceNotation', max_length=50)  # Field name made lowercase.
    area = models.TextField(db_column='Area')  # Field name made lowercase.
    collectornumberar = models.CharField(db_column='CollectorNumberAr', max_length=15)  # Field name made lowercase.
    timestamp = models.TextField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'ArInvoicePay'
        unique_together = (('customer', 'customer', 'customer', 'customer', 'customer', 'customer', 'customer', 'customer', 'customer', 'invoice', 'invoice', 'invoice', 'invoice', 'invoice', 'invoice', 'invoice', 'invoice', 'invoice', 'documenttype', 'documenttype', 'documenttype', 'documenttype', 'documenttype', 'entrynumber', 'entrynumber'),)


class ArCustomerPlus(models.Model):
    customer = models.ForeignKey(ArCustomer, models.DO_NOTHING, db_column='Customer', primary_key=True, max_length=15)  # Field name made lowercase.
    shippingaccount = models.CharField(db_column='ShippingAccount', max_length=10, blank=True, null=True)  # Field name made lowercase.
    shippingphone = models.CharField(db_column='ShippingPhone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    shippingemailifdif = models.CharField(db_column='ShippingEmailIfDif', max_length=50, blank=True, null=True)  # Field name made lowercase.
    alternatecontact = models.CharField(db_column='AlternateContact', max_length=30, blank=True, null=True)  # Field name made lowercase.
    followupaction = models.CharField(db_column='FollowUpAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    followupactiondate = models.DateTimeField(db_column='FollowUpActionDate', blank=True, null=True)  # Field name made lowercase.
    customeralert = models.CharField(db_column='CustomerAlert', max_length=45, blank=True, null=True)  # Field name made lowercase.
    shippingname = models.CharField(db_column='ShippingName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    countrybill = models.CharField(db_column='CountryBill', max_length=2, blank=True, null=True)  # Field name made lowercase.
    countryship = models.CharField(db_column='CountryShip', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tbcmember = MakeshiftBoolField(db_column='TbcMember', max_length=1, blank=True, null=True, default_bool='N')  # Field name made lowercase.
    tbcdateenteredprog = models.DateTimeField(db_column='TbcDateEnteredProg', blank=True, null=True)  # Field name made lowercase.
    taxcategory = models.CharField(db_column='TaxCategory', max_length=20, blank=True, null=True)  # Field name made lowercase.
    addresstype = models.CharField(db_column='AddressType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fedexsignature = models.CharField(db_column='FedexSignature', max_length=30, blank=True, null=True)  # Field name made lowercase.
    shipfromaddress = models.CharField(db_column='ShipFromAddress', max_length=30, blank=True, null=True)  # Field name made lowercase.
    uspsdeliveryflag = models.CharField(db_column='UspsDeliveryFlag', max_length=20, blank=True, null=True)  # Field name made lowercase.
    includeinphysical = MakeshiftBoolField(db_column='IncludeInPhysical', max_length=1, blank=True, null=True, default_bool='Y')  # Field name made lowercase.
    chargecode = models.CharField(db_column='ChargeCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    includeaddonitems = MakeshiftBoolField(db_column='IncludeAddOnItems', max_length=10, blank=True, null=True, default_bool='Y')  # Field name made lowercase.
    productdecisionmak = models.CharField(db_column='ProductDecisionMak', max_length=100, blank=True, null=True)  # Field name made lowercase.
    userlifestyle = models.CharField(db_column='UserLifestyle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    userlifestage = models.CharField(db_column='UserLifeStage', max_length=100, blank=True, null=True)  # Field name made lowercase.
    usergender = models.CharField(db_column='UserGender', max_length=100, blank=True, null=True)  # Field name made lowercase.
    need = models.CharField(db_column='Need', max_length=100, blank=True, null=True)  # Field name made lowercase.
    incontinencetype = models.CharField(db_column='IncontinenceType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    orderinsertprefere = models.CharField(db_column='OrderInsertPrefere', max_length=30, blank=True, null=True)  # Field name made lowercase.
    customerusagetype = models.CharField(db_column='CustomerUsageType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    timestamp = models.TextField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    massmailingsample = models.CharField(db_column='MassMailingSample', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ArCustomer+'


class BomStructure(models.Model):
    parentpart = models.ForeignKey(InvMaster, models.DO_NOTHING, db_column='ParentPart', primary_key=True)  # Field name made lowercase.
    version = models.TextField(db_column='Version')  # Field name made lowercase.
    release = models.TextField(db_column='Release')  # Field name made lowercase.
    route = models.TextField(db_column='Route')  # Field name made lowercase.
    sequencenum = models.TextField(db_column='SequenceNum')  # Field name made lowercase.
    component = models.TextField(db_column='Component')  # Field name made lowercase.
    comversion = models.CharField(db_column='ComVersion', max_length=5)  # Field name made lowercase.
    comrelease = models.CharField(db_column='ComRelease', max_length=5)  # Field name made lowercase.
    eccconsumption = models.CharField(db_column='EccConsumption', max_length=1)  # Field name made lowercase.
    structureondate = models.DateTimeField(db_column='StructureOnDate', blank=True, null=True)  # Field name made lowercase.
    structureoffdate = models.DateTimeField(db_column='StructureOffDate', blank=True, null=True)  # Field name made lowercase.
    opoffsetflag = models.CharField(db_column='OpOffsetFlag', max_length=1)  # Field name made lowercase.
    operationoffset = models.DecimalField(db_column='OperationOffset', max_digits=5, decimal_places=0)  # Field name made lowercase.
    qtyper = models.DecimalField(db_column='QtyPer', max_digits=18, decimal_places=6)  # Field name made lowercase.
    scrappercentage = models.DecimalField(db_column='ScrapPercentage', max_digits=4, decimal_places=2)  # Field name made lowercase.
    scrapquantity = models.DecimalField(db_column='ScrapQuantity', max_digits=18, decimal_places=6)  # Field name made lowercase.
    sooptionflag = models.CharField(db_column='SoOptionFlag', max_length=1)  # Field name made lowercase.
    soprintflag = models.CharField(db_column='SoPrintFlag', max_length=1)  # Field name made lowercase.
    inclscrapflag = models.CharField(db_column='InclScrapFlag', max_length=1)  # Field name made lowercase.
    reasonforchange = models.CharField(db_column='ReasonForChange', max_length=30)  # Field name made lowercase.
    refdesignator = models.CharField(db_column='RefDesignator', max_length=50)  # Field name made lowercase.
    assemblyplace = models.CharField(db_column='AssemblyPlace', max_length=50)  # Field name made lowercase.
    itemnumber = models.CharField(db_column='ItemNumber', max_length=50)  # Field name made lowercase.
    autonarrcode = models.DecimalField(db_column='AutoNarrCode', max_digits=10, decimal_places=0)  # Field name made lowercase.
    componenttype = models.TextField(db_column='ComponentType')  # Field name made lowercase.
    inclkitissues = models.CharField(db_column='InclKitIssues', max_length=1)  # Field name made lowercase.
    createsubjob = models.CharField(db_column='CreateSubJob', max_length=1)  # Field name made lowercase.
    wetweightpercent = models.DecimalField(db_column='WetWeightPercent', max_digits=8, decimal_places=6)  # Field name made lowercase.
    includebatch = models.CharField(db_column='IncludeBatch', max_length=1)  # Field name made lowercase.
    includefromjob = models.CharField(db_column='IncludeFromJob', max_length=20)  # Field name made lowercase.
    includetojob = models.CharField(db_column='IncludeToJob', max_length=20)  # Field name made lowercase.
    fixedqtyperflag = models.CharField(db_column='FixedQtyPerFlag', max_length=1)  # Field name made lowercase.
    fixedqtyper = models.DecimalField(db_column='FixedQtyPer', max_digits=18, decimal_places=6)  # Field name made lowercase.
    rollupcost = models.CharField(db_column='RollUpCost', max_length=1)  # Field name made lowercase.
    warehouse = models.TextField(db_column='Warehouse')  # Field name made lowercase.
    ignorefloorflag = models.CharField(db_column='IgnoreFloorFlag', max_length=1)  # Field name made lowercase.
    coproductcostval = models.CharField(db_column='CoProductCostVal', max_length=1)  # Field name made lowercase.
    uomflag = models.CharField(db_column='UomFlag', max_length=1)  # Field name made lowercase.
    qtyperent = models.DecimalField(db_column='QtyPerEnt', max_digits=18, decimal_places=6)  # Field name made lowercase.
    scrapquantityent = models.DecimalField(db_column='ScrapQuantityEnt', max_digits=18, decimal_places=6)  # Field name made lowercase.
    fixedqtyperent = models.DecimalField(db_column='FixedQtyPerEnt', max_digits=18, decimal_places=6)  # Field name made lowercase.
    productcode = models.TextField(db_column='ProductCode')  # Field name made lowercase.
    librarycode = models.CharField(db_column='LibraryCode', max_length=5)  # Field name made lowercase.
    firstseq = models.DecimalField(db_column='FirstSeq', max_digits=3, decimal_places=0)  # Field name made lowercase.
    secondseq = models.DecimalField(db_column='SecondSeq', max_digits=3, decimal_places=0)  # Field name made lowercase.
    ovreccspeciss = models.CharField(db_column='OvrEccSpecIss', max_length=1)  # Field name made lowercase.
    timestamp = models.TextField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'BomStructure'
        unique_together = (('parentpart', 'parentpart', 'parentpart', 'version', 'release', 'route', 'route', 'route', 'route', 'sequencenum', 'component'), ('parentpart', 'version', 'release', 'route', 'opoffsetflag', 'operationoffset', 'sequencenum', 'component'), ('component', 'route', 'parentpart', 'version', 'release', 'sequencenum'),)


class ArTrnDetail(models.Model):
    trnyear = models.TextField(db_column='TrnYear', primary_key=True)  # Field name made lowercase.
    trnmonth = models.TextField(db_column='TrnMonth')  # Field name made lowercase.
    register = models.TextField(db_column='Register')  # Field name made lowercase.
    invoice = models.ForeignKey(ArInvoice, models.DO_NOTHING, db_column='Invoice')  # Field name made lowercase.
    summaryline = models.TextField(db_column='SummaryLine')  # Field name made lowercase.
    detailline = models.TextField(db_column='DetailLine')  # Field name made lowercase.
    invoicedate = models.DateTimeField(db_column='InvoiceDate', blank=True, null=True)  # Field name made lowercase.
    branch = models.TextField(db_column='Branch')  # Field name made lowercase.
    salesperson = models.TextField(db_column='Salesperson')  # Field name made lowercase.
    customer = models.ForeignKey(ArCustomer, models.DO_NOTHING, db_column='Customer')  # Field name made lowercase.
    ordertype = models.TextField(db_column='OrderType')  # Field name made lowercase.
    interbranchtrf = models.CharField(db_column='InterBranchTrf', max_length=1)  # Field name made lowercase.
    stockcode = models.ForeignKey(InvMaster, models.DO_NOTHING, db_column='StockCode')  # Field name made lowercase.
    warehouse = models.TextField(db_column='Warehouse')  # Field name made lowercase.
    area = models.TextField(db_column='Area')  # Field name made lowercase.
    productclass = models.TextField(db_column='ProductClass')  # Field name made lowercase.
    taxcode = models.TextField(db_column='TaxCode')  # Field name made lowercase.
    taxstatus = models.CharField(db_column='TaxStatus', max_length=1)  # Field name made lowercase.
    historyreqd = models.CharField(db_column='HistoryReqd', max_length=1)  # Field name made lowercase.
    customerclass = models.CharField(db_column='CustomerClass', max_length=10)  # Field name made lowercase.
    qtyinvoiced = models.DecimalField(db_column='QtyInvoiced', max_digits=18, decimal_places=6)  # Field name made lowercase.
    mass = models.DecimalField(db_column='Mass', max_digits=18, decimal_places=6)  # Field name made lowercase.
    volume = models.DecimalField(db_column='Volume', max_digits=18, decimal_places=6)  # Field name made lowercase.
    netsalesvalue = models.DecimalField(db_column='NetSalesValue', max_digits=14, decimal_places=2)  # Field name made lowercase.
    taxvalue = models.DecimalField(db_column='TaxValue', max_digits=14, decimal_places=2)  # Field name made lowercase.
    costvalue = models.DecimalField(db_column='CostValue', max_digits=14, decimal_places=2)  # Field name made lowercase.
    discvalue = models.DecimalField(db_column='DiscValue', max_digits=14, decimal_places=2)  # Field name made lowercase.
    linetype = models.CharField(db_column='LineType', max_length=1)  # Field name made lowercase.
    pricecode = models.TextField(db_column='PriceCode')  # Field name made lowercase.
    documenttype = models.TextField(db_column='DocumentType')  # Field name made lowercase.
    productclassupd = models.CharField(db_column='ProductClassUpd', max_length=1)  # Field name made lowercase.
    gldistrupd = models.CharField(db_column='GlDistrUpd', max_length=1)  # Field name made lowercase.
    salespersonupd = models.CharField(db_column='SalespersonUpd', max_length=1)  # Field name made lowercase.
    salesglintreqd = models.CharField(db_column='SalesGlIntReqd', max_length=1)  # Field name made lowercase.
    stockupd = models.CharField(db_column='StockUpd', max_length=1)  # Field name made lowercase.
    interfaceflag = models.CharField(db_column='InterfaceFlag', max_length=1)  # Field name made lowercase.
    glyear = models.TextField(db_column='GlYear')  # Field name made lowercase.
    glperiod = models.TextField(db_column='GlPeriod')  # Field name made lowercase.
    salesturnoprted = models.CharField(db_column='SalesTurnOPrted', max_length=1)  # Field name made lowercase.
    taxcodefst = models.CharField(db_column='TaxCodeFst', max_length=3)  # Field name made lowercase.
    taxvaluefst = models.DecimalField(db_column='TaxValueFst', max_digits=14, decimal_places=2)  # Field name made lowercase.
    salesorder = models.ForeignKey('SorMaster', models.DO_NOTHING, db_column='SalesOrder')  # Field name made lowercase.
    contractprcnum = models.CharField(db_column='ContractPrcNum', max_length=20)  # Field name made lowercase.
    bin = models.TextField(db_column='Bin')  # Field name made lowercase.
    lineinvoicedisc = models.DecimalField(db_column='LineInvoiceDisc', max_digits=14, decimal_places=2)  # Field name made lowercase.
    userfield1 = models.CharField(db_column='UserField1', max_length=1)  # Field name made lowercase.
    userfield2 = models.CharField(db_column='UserField2', max_length=1)  # Field name made lowercase.
    taxablevalue = models.DecimalField(db_column='TaxableValue', max_digits=14, decimal_places=2)  # Field name made lowercase.
    customerponumber = models.CharField(db_column='CustomerPoNumber', max_length=30)  # Field name made lowercase.
    abcupd = models.CharField(db_column='AbcUpd', max_length=1)  # Field name made lowercase.
    buyinggroup = models.TextField(db_column='BuyingGroup')  # Field name made lowercase.
    postvalue = models.DecimalField(db_column='PostValue', max_digits=14, decimal_places=2)  # Field name made lowercase.
    postcurrency = models.CharField(db_column='PostCurrency', max_length=3)  # Field name made lowercase.
    postconvrate = models.DecimalField(db_column='PostConvRate', max_digits=12, decimal_places=6)  # Field name made lowercase.
    postmuldiv = models.CharField(db_column='PostMulDiv', max_length=1)  # Field name made lowercase.
    accountcur = models.CharField(db_column='AccountCur', max_length=3)  # Field name made lowercase.
    accountconvrate = models.DecimalField(db_column='AccountConvRate', max_digits=12, decimal_places=6)  # Field name made lowercase.
    accountmuldiv = models.CharField(db_column='AccountMulDiv', max_length=1)  # Field name made lowercase.
    triangcurrency = models.CharField(db_column='TriangCurrency', max_length=3)  # Field name made lowercase.
    triangconvrate = models.DecimalField(db_column='TriangConvRate', max_digits=12, decimal_places=6)  # Field name made lowercase.
    triangmuldiv = models.CharField(db_column='TriangMulDiv', max_length=1)  # Field name made lowercase.
    version = models.TextField(db_column='Version')  # Field name made lowercase.
    release = models.TextField(db_column='Release')  # Field name made lowercase.
    eecinvoiceflag = models.CharField(db_column='EecInvoiceFlag', max_length=1)  # Field name made lowercase.
    nationality = models.CharField(db_column='Nationality', max_length=3)  # Field name made lowercase.
    salesorderline = models.TextField(db_column='SalesOrderLine')  # Field name made lowercase.
    transactionglcode = models.CharField(db_column='TransactionGlCode', max_length=35)  # Field name made lowercase.
    discountglcode = models.CharField(db_column='DiscountGlCode', max_length=35)  # Field name made lowercase.
    costglcode = models.CharField(db_column='CostGlCode', max_length=35)  # Field name made lowercase.
    glintupdated = models.CharField(db_column='GlIntUpdated', max_length=1)  # Field name made lowercase.
    glintprinted = models.CharField(db_column='GlIntPrinted', max_length=1)  # Field name made lowercase.
    glintyear = models.DecimalField(db_column='GlIntYear', max_digits=4, decimal_places=0)  # Field name made lowercase.
    glintperiod = models.DecimalField(db_column='GlIntPeriod', max_digits=2, decimal_places=0)  # Field name made lowercase.
    gljournal = models.TextField(db_column='GlJournal')  # Field name made lowercase.
    controltype = models.CharField(db_column='ControlType', max_length=1)  # Field name made lowercase.
    trananalysisentry = models.DecimalField(db_column='TranAnalysisEntry', max_digits=10, decimal_places=0)  # Field name made lowercase.
    dscanalysisentry = models.DecimalField(db_column='DscAnalysisEntry', max_digits=10, decimal_places=0)  # Field name made lowercase.
    cstanalysisentry = models.DecimalField(db_column='CstAnalysisEntry', max_digits=10, decimal_places=0)  # Field name made lowercase.
    warehouseaccount = models.CharField(db_column='WarehouseAccount', max_length=35)  # Field name made lowercase.
    whanalysisentry = models.DecimalField(db_column='WhAnalysisEntry', max_digits=10, decimal_places=0)  # Field name made lowercase.
    warehouseamount = models.DecimalField(db_column='WarehouseAmount', max_digits=14, decimal_places=2)  # Field name made lowercase.
    taxaccount = models.CharField(db_column='TaxAccount', max_length=35)  # Field name made lowercase.
    timestamp = models.TextField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'ArTrnDetail'
        unique_together = (('trnyear', 'trnyear', 'trnyear', 'trnyear', 'trnyear', 'trnyear', 'trnmonth', 'trnmonth', 'trnmonth', 'trnmonth', 'trnmonth', 'trnmonth', 'register', 'register', 'register', 'register', 'register', 'register', 'invoice', 'invoice', 'invoice', 'invoice', 'invoice', 'invoice', 'invoice', 'invoice', 'invoice', 'invoice', 'invoice', 'invoice', 'invoice', 'invoice', 'summaryline', 'summaryline', 'summaryline', 'summaryline', 'summaryline', 'summaryline', 'detailline'), ('glintyear', 'glintperiod', 'gljournal', 'invoice', 'summaryline', 'detailline', 'trnyear', 'trnmonth', 'register'),)


class ArTrnSummary(models.Model):
    trnyear = models.TextField(db_column='TrnYear', primary_key=True)  # Field name made lowercase.
    trnmonth = models.TextField(db_column='TrnMonth')  # Field name made lowercase.
    register = models.TextField(db_column='Register')  # Field name made lowercase.
    invoice = models.ForeignKey(ArInvoice, models.DO_NOTHING, db_column='Invoice')  # Field name made lowercase.
    summaryline = models.TextField(db_column='SummaryLine')  # Field name made lowercase.
    invoicedate = models.DateTimeField(db_column='InvoiceDate', blank=True, null=True)  # Field name made lowercase.
    branch = models.TextField(db_column='Branch')  # Field name made lowercase.
    salesperson = models.TextField(db_column='Salesperson')  # Field name made lowercase.
    customer = models.ForeignKey(ArCustomer, models.DO_NOTHING, db_column='Customer')  # Field name made lowercase.
    ordertype = models.TextField(db_column='OrderType')  # Field name made lowercase.
    interbranchtrf = models.CharField(db_column='InterBranchTrf', max_length=1)  # Field name made lowercase.
    customerponumber = models.CharField(db_column='CustomerPoNumber', max_length=30)  # Field name made lowercase.
    merchandisevalue = models.DecimalField(db_column='MerchandiseValue', max_digits=14, decimal_places=2)  # Field name made lowercase.
    freightvalue = models.DecimalField(db_column='FreightValue', max_digits=14, decimal_places=2)  # Field name made lowercase.
    othervalue = models.DecimalField(db_column='OtherValue', max_digits=14, decimal_places=2)  # Field name made lowercase.
    taxvalue = models.DecimalField(db_column='TaxValue', max_digits=14, decimal_places=2)  # Field name made lowercase.
    foreignmerchval = models.DecimalField(db_column='ForeignMerchVal', max_digits=14, decimal_places=2)  # Field name made lowercase.
    foreignfreightval = models.DecimalField(db_column='ForeignFreightVal', max_digits=14, decimal_places=2)  # Field name made lowercase.
    foreignotherval = models.DecimalField(db_column='ForeignOtherVal', max_digits=14, decimal_places=2)  # Field name made lowercase.
    foreigntaxval = models.DecimalField(db_column='ForeignTaxVal', max_digits=14, decimal_places=2)  # Field name made lowercase.
    exchangerate = models.DecimalField(db_column='ExchangeRate', max_digits=12, decimal_places=6)  # Field name made lowercase.
    muldiv = models.CharField(db_column='MulDiv', max_length=1)  # Field name made lowercase.
    currency = models.TextField(db_column='Currency')  # Field name made lowercase.
    commissionvalue = models.DecimalField(db_column='CommissionValue', max_digits=14, decimal_places=2)  # Field name made lowercase.
    discvalue = models.DecimalField(db_column='DiscValue', max_digits=14, decimal_places=2)  # Field name made lowercase.
    merchandisecost = models.DecimalField(db_column='MerchandiseCost', max_digits=14, decimal_places=2)  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=1)  # Field name made lowercase.
    documenttype = models.TextField(db_column='DocumentType')  # Field name made lowercase.
    taxexemptnumber = models.CharField(db_column='TaxExemptNumber', max_length=30)  # Field name made lowercase.
    taxexemptoverride = models.CharField(db_column='TaxExemptOverride', max_length=1)  # Field name made lowercase.
    settlementdisc = models.DecimalField(db_column='SettlementDisc', max_digits=5, decimal_places=2)  # Field name made lowercase.
    exemptvalue = models.DecimalField(db_column='ExemptValue', max_digits=14, decimal_places=2)  # Field name made lowercase.
    cashcredit = models.CharField(db_column='CashCredit', max_length=2)  # Field name made lowercase.
    taxupd = models.CharField(db_column='TaxUpd', max_length=1)  # Field name made lowercase.
    invoiceregprted = models.CharField(db_column='InvoiceRegPrted', max_length=1)  # Field name made lowercase.
    commissionsupd = models.CharField(db_column='CommissionsUpd', max_length=1)  # Field name made lowercase.
    salesorder = models.ForeignKey(SorMasterRep, models.DO_NOTHING, db_column='SalesOrder')  # Field name made lowercase.
    ordinvxrefprted = models.CharField(db_column='OrdInvXrefPrted', max_length=1)  # Field name made lowercase.
    salesturnoprted = models.CharField(db_column='SalesTurnOPrted', max_length=1)  # Field name made lowercase.
    invoicecount = models.DecimalField(db_column='InvoiceCount', max_digits=10, decimal_places=0)  # Field name made lowercase.
    area = models.TextField(db_column='Area')  # Field name made lowercase.
    interfaceflag = models.CharField(db_column='InterfaceFlag', max_length=1)  # Field name made lowercase.
    termscode = models.TextField(db_column='TermsCode')  # Field name made lowercase.
    fstupdated = models.CharField(db_column='FstUpdated', max_length=1)  # Field name made lowercase.
    creditedinvoice = models.CharField(db_column='CreditedInvoice', max_length=20)  # Field name made lowercase.
    globaltaxupd = models.CharField(db_column='GlobalTaxUpd', max_length=1)  # Field name made lowercase.
    salesorderjob = models.CharField(db_column='SalesOrderJob', max_length=20)  # Field name made lowercase.
    operator = models.TextField(db_column='Operator')  # Field name made lowercase.
    deposittype = models.CharField(db_column='DepositType', max_length=1)  # Field name made lowercase.
    lastprinteddel = models.CharField(db_column='LastPrintedDel', max_length=20)  # Field name made lowercase.
    inprocessflag = models.CharField(db_column='InProcessFlag', max_length=1)  # Field name made lowercase.
    subaccount = models.CharField(db_column='SubAccount', max_length=15)  # Field name made lowercase.
    userfield1 = models.CharField(db_column='UserField1', max_length=1)  # Field name made lowercase.
    userfield2 = models.CharField(db_column='UserField2', max_length=1)  # Field name made lowercase.
    userfield3 = models.CharField(db_column='UserField3', max_length=1)  # Field name made lowercase.
    eecinvoiceflag = models.CharField(db_column='EecInvoiceFlag', max_length=1)  # Field name made lowercase.
    nationality = models.CharField(db_column='Nationality', max_length=3)  # Field name made lowercase.
    dispatchaccount = models.CharField(db_column='DispatchAccount', max_length=35)  # Field name made lowercase.
    disanalysisentry = models.DecimalField(db_column='DisAnalysisEntry', max_digits=10, decimal_places=0)  # Field name made lowercase.
    dispatchamount = models.DecimalField(db_column='DispatchAmount', max_digits=14, decimal_places=2)  # Field name made lowercase.
    warehouseaccount = models.CharField(db_column='WarehouseAccount', max_length=35)  # Field name made lowercase.
    whanalysisentry = models.DecimalField(db_column='WhAnalysisEntry', max_digits=10, decimal_places=0)  # Field name made lowercase.
    warehouseamount = models.DecimalField(db_column='WarehouseAmount', max_digits=14, decimal_places=2)  # Field name made lowercase.
    branchsalesaccount = models.CharField(db_column='BranchSalesAccount', max_length=35)  # Field name made lowercase.
    brsalesanaentry = models.DecimalField(db_column='BrSalesAnaEntry', max_digits=10, decimal_places=0)  # Field name made lowercase.
    branchsalesamount = models.DecimalField(db_column='BranchSalesAmount', max_digits=14, decimal_places=2)  # Field name made lowercase.
    branchcostaccount = models.CharField(db_column='BranchCostAccount', max_length=35)  # Field name made lowercase.
    brcstanalysisentry = models.DecimalField(db_column='BrCstAnalysisEntry', max_digits=10, decimal_places=0)  # Field name made lowercase.
    branchcostamount = models.DecimalField(db_column='BranchCostAmount', max_digits=14, decimal_places=2)  # Field name made lowercase.
    timestamp = models.TextField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'ArTrnSummary'
        unique_together = (('trnyear', 'trnyear', 'trnmonth', 'trnmonth', 'register', 'register', 'invoice', 'invoice', 'invoice', 'invoice', 'invoice', 'invoice', 'invoice', 'invoice', 'invoice', 'summaryline', 'summaryline'),)



class InvMasterPlus(models.Model):
    stockcode = models.ForeignKey(InvMaster, models.DO_NOTHING, db_column='StockCode', primary_key=True, max_length=30)  # Field name made lowercase.
    percentofboxlabel = models.DecimalField(db_column='PercentOfBoxLabel', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    finaldescription = models.CharField(db_column='FinalDescription', max_length=60, blank=True, null=True)  # Field name made lowercase.
    customsdescription = models.CharField(db_column='CustomsDescription', max_length=100, blank=True, null=True)  # Field name made lowercase.
    backflushitem = models.CharField(db_column='BackflushItem', max_length=1, blank=True, null=True)  # Field name made lowercase.
    prepackitem = models.CharField(db_column='PrepackItem', max_length=1, blank=True, null=True)  # Field name made lowercase.
    itemweight = models.DecimalField(db_column='ItemWeight', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    fbainstructions = models.CharField(db_column='FbaInstructions', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fbaboxsize = models.CharField(db_column='FbaBoxSize', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fbabagsize = models.CharField(db_column='FbaBagSize', max_length=50, blank=True, null=True)  # Field name made lowercase.
    suspenseitem = models.CharField(db_column='SuspenseItem', max_length=1, blank=True, null=True)  # Field name made lowercase.
    amazonfnsku = models.CharField(db_column='AmazonFnsku', max_length=30, blank=True, null=True)  # Field name made lowercase.
    backordereditem = models.CharField(db_column='BackorderedItem', max_length=100, blank=True, null=True)  # Field name made lowercase.
    orderentrymessage = models.CharField(db_column='OrderEntryMessage', max_length=100, blank=True, null=True)  # Field name made lowercase.
    northshorebrand = models.CharField(db_column='NorthshoreBrand', max_length=1, blank=True, null=True)  # Field name made lowercase.
    discontinueditem = models.CharField(db_column='DiscontinuedItem', max_length=1, blank=True, null=True)  # Field name made lowercase.
    discontinueddate = models.DateTimeField(db_column='DiscontinuedDate', blank=True, null=True)  # Field name made lowercase.
    backorderhold = models.CharField(db_column='BackorderHold', max_length=10, blank=True, null=True)  # Field name made lowercase.
    amazonexclusiveite = models.CharField(db_column='AmazonExclusiveIte', max_length=10, blank=True, null=True)  # Field name made lowercase.
    amazonasin = models.CharField(db_column='AmazonAsin', max_length=30, blank=True, null=True)  # Field name made lowercase.
    excludeshipmentsto = models.CharField(db_column='ExcludeShipmentsTo', max_length=10, blank=True, null=True)  # Field name made lowercase.
    brand = models.CharField(db_column='Brand', max_length=20, blank=True, null=True)  # Field name made lowercase.
    length = models.DecimalField(db_column='Length', max_digits=14, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    width = models.DecimalField(db_column='Width', max_digits=14, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    height = models.DecimalField(db_column='Height', max_digits=14, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    upccode = models.CharField(db_column='UpcCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fbacomments = models.CharField(db_column='FbaComments', max_length=100, blank=True, null=True)  # Field name made lowercase.
    productnotes = models.CharField(db_column='ProductNotes', max_length=100, blank=True, null=True)  # Field name made lowercase.
    avataxcode = models.CharField(db_column='AvataxCode', max_length=15, blank=True, null=True)  # Field name made lowercase.
    lastnotifiedon = models.DateTimeField(db_column='LastNotifiedOn', blank=True, null=True)  # Field name made lowercase.
    pickdescription = models.CharField(db_column='PickDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=30, blank=True, null=True)  # Field name made lowercase.
    prepneeded = models.CharField(db_column='PrepNeeded', max_length=100, blank=True, null=True)  # Field name made lowercase.
    timestamp = models.TextField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    frauditem = models.CharField(db_column='FraudItem', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvMaster+'


class CusSorMaster(models.Model):
    salesorder = models.ForeignKey(SorMaster, models.DO_NOTHING, db_column='SalesOrder', primary_key=True, max_length=20)  # Field name made lowercase.
    invoicenumber = models.CharField(db_column='InvoiceNumber', max_length=20)  # Field name made lowercase.
    chargecode = models.CharField(db_column='ChargeCode', max_length=8, blank=True, null=True)  # Field name made lowercase.
    shippingaccount = models.CharField(db_column='ShippingAccount', max_length=10, blank=True, null=True)  # Field name made lowercase.
    shippingphone = models.CharField(db_column='ShippingPhone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    shippingemail = models.CharField(db_column='ShippingEmail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    onlineorder = models.CharField(db_column='OnlineOrder', max_length=40, blank=True, null=True)  # Field name made lowercase.
    paymentmeth = models.CharField(db_column='PaymentMeth', max_length=50, blank=True, null=True)  # Field name made lowercase.
    requisiton = models.CharField(db_column='Requisiton', max_length=20, blank=True, null=True)  # Field name made lowercase.
    amazonwarehouse = models.CharField(db_column='AmazonWarehouse', max_length=50, blank=True, null=True)  # Field name made lowercase.
    addresstypeoverrid = models.CharField(db_column='AddressTypeOverrid', max_length=20, blank=True, null=True)  # Field name made lowercase.
    suspensereason = models.CharField(db_column='SuspenseReason', max_length=100, blank=True, null=True)  # Field name made lowercase.
    addressvalidation = models.CharField(db_column='AddressValidation', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fedexsignature = models.CharField(db_column='FedexSignature', max_length=30, blank=True, null=True)  # Field name made lowercase.
    shipfromaddress = models.CharField(db_column='ShipFromAddress', max_length=30, blank=True, null=True)  # Field name made lowercase.
    nextaction = models.CharField(db_column='NextAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nextactiondate = models.DateTimeField(db_column='NextActionDate', blank=True, null=True)  # Field name made lowercase.
    recurringorderinte = models.DecimalField(db_column='RecurringOrderInte', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    uspsdeliveryflag = models.CharField(db_column='UspsDeliveryFlag', max_length=20, blank=True, null=True)  # Field name made lowercase.
    shipmentlocator = models.DecimalField(db_column='ShipmentLocator', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    backorder = models.CharField(db_column='Backorder', max_length=1, blank=True, null=True)  # Field name made lowercase.
    originamazonwareho = models.CharField(db_column='OriginAmazonWareho', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ordertaximported = models.DecimalField(db_column='OrderTaxImported', max_digits=16, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amazonprime = models.CharField(db_column='AmazonPrime', max_length=1, blank=True, null=True)  # Field name made lowercase.
    timestamp = models.TextField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    countryship = models.CharField(db_column='CountryShip', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CusSorMaster+'
        unique_together = (('salesorder', 'invoicenumber'),)


class InvMovements(models.Model):
    stockcode = models.ForeignKey(InvMaster, models.DO_NOTHING, db_column='StockCode', primary_key=True)  # Field name made lowercase.
    warehouse = models.TextField(db_column='Warehouse')  # Field name made lowercase.
    trnyear = models.DecimalField(db_column='TrnYear', max_digits=4, decimal_places=0)  # Field name made lowercase.
    trnmonth = models.DecimalField(db_column='TrnMonth', max_digits=2, decimal_places=0)  # Field name made lowercase.
    entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
    trntime = models.DecimalField(db_column='TrnTime', max_digits=8, decimal_places=0)  # Field name made lowercase.
    movementtype = models.CharField(db_column='MovementType', max_length=1)  # Field name made lowercase.
    trnqty = models.DecimalField(db_column='TrnQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    trnvalue = models.DecimalField(db_column='TrnValue', max_digits=14, decimal_places=2)  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=1)  # Field name made lowercase.
    job = models.TextField(db_column='Job')  # Field name made lowercase.
    journal = models.DecimalField(db_column='Journal', max_digits=10, decimal_places=0)  # Field name made lowercase.
    journalentry = models.DecimalField(db_column='JournalEntry', max_digits=10, decimal_places=0)  # Field name made lowercase.
    enteredcost = models.DecimalField(db_column='EnteredCost', max_digits=15, decimal_places=5)  # Field name made lowercase.
    trntype = models.TextField(db_column='TrnType')  # Field name made lowercase.
    reference = models.CharField(db_column='Reference', max_length=30)  # Field name made lowercase.
    addreference = models.CharField(db_column='AddReference', max_length=50)  # Field name made lowercase.
    unitcost = models.DecimalField(db_column='UnitCost', max_digits=15, decimal_places=5)  # Field name made lowercase.
    newwarehouse = models.CharField(db_column='NewWarehouse', max_length=10)  # Field name made lowercase.
    bin = models.TextField(db_column='Bin')  # Field name made lowercase.
    supplier = models.TextField(db_column='Supplier')  # Field name made lowercase.
    glcode = models.CharField(db_column='GlCode', max_length=35)  # Field name made lowercase.
    document = models.DecimalField(db_column='Document', max_digits=9, decimal_places=0)  # Field name made lowercase.
    salesorder = models.ForeignKey(SorMaster, models.DO_NOTHING, db_column='SalesOrder')  # Field name made lowercase.
    invoiceregister = models.DecimalField(db_column='InvoiceRegister', max_digits=10, decimal_places=0)  # Field name made lowercase.
    summaryline = models.DecimalField(db_column='SummaryLine', max_digits=10, decimal_places=0)  # Field name made lowercase.
    invoice = models.ForeignKey(ArInvoice, models.DO_NOTHING, db_column='Invoice')  # Field name made lowercase.
    doctype = models.CharField(db_column='DocType', max_length=1)  # Field name made lowercase.
    customer = models.ForeignKey(ArCustomer, models.DO_NOTHING, db_column='Customer')  # Field name made lowercase.
    costvalue = models.DecimalField(db_column='CostValue', max_digits=14, decimal_places=2)  # Field name made lowercase.
    branch = models.TextField(db_column='Branch')  # Field name made lowercase.
    salesperson = models.TextField(db_column='Salesperson')  # Field name made lowercase.
    salesbin = models.CharField(db_column='SalesBin', max_length=20)  # Field name made lowercase.
    customerponumber = models.CharField(db_column='CustomerPoNumber', max_length=30)  # Field name made lowercase.
    ordertype = models.TextField(db_column='OrderType')  # Field name made lowercase.
    area = models.TextField(db_column='Area')  # Field name made lowercase.
    productclass = models.TextField(db_column='ProductClass')  # Field name made lowercase.
    dispatchnote = models.TextField(db_column='DispatchNote')  # Field name made lowercase.
    detailline = models.DecimalField(db_column='DetailLine', max_digits=10, decimal_places=0)  # Field name made lowercase.
    version = models.TextField(db_column='Version')  # Field name made lowercase.
    release = models.TextField(db_column='Release')  # Field name made lowercase.
    lotserial = models.CharField(db_column='LotSerial', max_length=50)  # Field name made lowercase.
    ioprocessedflag = models.CharField(db_column='IoProcessedFlag', max_length=1)  # Field name made lowercase.
    timestamp = models.TextField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'InvMovements'
        unique_together = (('ioprocessedflag', 'stockcode', 'warehouse', 'entrydate', 'trntime', 'trnyear', 'trnmonth'), ('stockcode', 'stockcode', 'stockcode', 'stockcode', 'stockcode', 'stockcode', 'stockcode', 'stockcode', 'stockcode', 'stockcode', 'stockcode', 'stockcode', 'stockcode', 'warehouse', 'warehouse', 'warehouse', 'warehouse', 'warehouse', 'warehouse', 'warehouse', 'warehouse', 'warehouse', 'warehouse', 'warehouse', 'trnyear', 'trnmonth', 'entrydate', 'trntime'), ('stockcode', 'entrydate', 'trntime', 'warehouse', 'trnyear', 'trnmonth'),)


class InvPrice(models.Model):
    stockcode = models.ForeignKey(InvMaster, models.DO_NOTHING, db_column='StockCode', primary_key=True)  # Field name made lowercase.
    pricecode = models.TextField(db_column='PriceCode')  # Field name made lowercase.
    sellingprice = models.DecimalField(db_column='SellingPrice', max_digits=15, decimal_places=5)  # Field name made lowercase.
    pricebasis = models.CharField(db_column='PriceBasis', max_length=1)  # Field name made lowercase.
    commissioncode = models.TextField(db_column='CommissionCode')  # Field name made lowercase.
    timestamp = models.TextField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'InvPrice'
        unique_together = (('stockcode', 'stockcode', 'pricecode'),)


class InvWarehouse(models.Model):
    stockcode = models.ForeignKey(InvMaster, models.DO_NOTHING, db_column='StockCode', primary_key=True)  # Field name made lowercase.
    warehouse = models.TextField(db_column='Warehouse')  # Field name made lowercase.
    qtyonhand = models.DecimalField(db_column='QtyOnHand', max_digits=18, decimal_places=6)  # Field name made lowercase.
    mtdqtyreceived = models.DecimalField(db_column='MtdQtyReceived', max_digits=18, decimal_places=6)  # Field name made lowercase.
    mtdqtyadjusted = models.DecimalField(db_column='MtdQtyAdjusted', max_digits=18, decimal_places=6)  # Field name made lowercase.
    mtdqtytrf = models.DecimalField(db_column='MtdQtyTrf', max_digits=18, decimal_places=6)  # Field name made lowercase.
    mtdqtyissued = models.DecimalField(db_column='MtdQtyIssued', max_digits=18, decimal_places=6)  # Field name made lowercase.
    mtdqtysold = models.DecimalField(db_column='MtdQtySold', max_digits=18, decimal_places=6)  # Field name made lowercase.
    qtyallocated = models.DecimalField(db_column='QtyAllocated', max_digits=18, decimal_places=6)  # Field name made lowercase.
    qtyonorder = models.DecimalField(db_column='QtyOnOrder', max_digits=18, decimal_places=6)  # Field name made lowercase.
    qtyonbackorder = models.DecimalField(db_column='QtyOnBackOrder', max_digits=18, decimal_places=6)  # Field name made lowercase.
    minimumqty = models.DecimalField(db_column='MinimumQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    maximumqty = models.DecimalField(db_column='MaximumQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    ytdqtysold = models.DecimalField(db_column='YtdQtySold', max_digits=18, decimal_places=6)  # Field name made lowercase.
    prevyearqtysold = models.DecimalField(db_column='PrevYearQtySold', max_digits=18, decimal_places=6)  # Field name made lowercase.
    openingbalance = models.DecimalField(db_column='OpeningBalance', max_digits=18, decimal_places=6)  # Field name made lowercase.
    ytdusagevalue = models.DecimalField(db_column='YtdUsageValue', max_digits=14, decimal_places=2)  # Field name made lowercase.
    abcclass = models.CharField(db_column='AbcClass', max_length=1)  # Field name made lowercase.
    unitcost = models.DecimalField(db_column='UnitCost', max_digits=15, decimal_places=5)  # Field name made lowercase.
    defaultbin = models.CharField(db_column='DefaultBin', max_length=20)  # Field name made lowercase.
    datelastsale = models.DateTimeField(db_column='DateLastSale', blank=True, null=True)  # Field name made lowercase.
    datelaststockmove = models.DateTimeField(db_column='DateLastStockMove', blank=True, null=True)  # Field name made lowercase.
    datelastcostchange = models.DateTimeField(db_column='DateLastCostChange', blank=True, null=True)  # Field name made lowercase.
    datelaststockcnt = models.DateTimeField(db_column='DateLastStockCnt', blank=True, null=True)  # Field name made lowercase.
    datelastpurchase = models.DateTimeField(db_column='DateLastPurchase', blank=True, null=True)  # Field name made lowercase.
    qtyintransit = models.DecimalField(db_column='QtyInTransit', max_digits=18, decimal_places=6)  # Field name made lowercase.
    transfervalue = models.DecimalField(db_column='TransferValue', max_digits=16, decimal_places=4)  # Field name made lowercase.
    safetystockqty = models.DecimalField(db_column='SafetyStockQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    reorderqty = models.DecimalField(db_column='ReOrderQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    qtyallocatedwip = models.DecimalField(db_column='QtyAllocatedWip', max_digits=18, decimal_places=6)  # Field name made lowercase.
    interfaceflag = models.CharField(db_column='InterfaceFlag', max_length=1)  # Field name made lowercase.
    costmultiplier = models.DecimalField(db_column='CostMultiplier', max_digits=9, decimal_places=6)  # Field name made lowercase.
    lastcostentered = models.DecimalField(db_column='LastCostEntered', max_digits=15, decimal_places=5)  # Field name made lowercase.
    mtdsalesvalue = models.DecimalField(db_column='MtdSalesValue', max_digits=14, decimal_places=2)  # Field name made lowercase.
    ytdsalesvalue = models.DecimalField(db_column='YtdSalesValue', max_digits=14, decimal_places=2)  # Field name made lowercase.
    prevytdsalesval = models.DecimalField(db_column='PrevYtdSalesVal', max_digits=14, decimal_places=2)  # Field name made lowercase.
    qtyininspection = models.DecimalField(db_column='QtyInInspection', max_digits=18, decimal_places=6)  # Field name made lowercase.
    palletqty = models.DecimalField(db_column='PalletQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    nummonthshistory = models.DecimalField(db_column='NumMonthsHistory', max_digits=2, decimal_places=0)  # Field name made lowercase.
    ytdqtyissued = models.DecimalField(db_column='YtdQtyIssued', max_digits=18, decimal_places=6)  # Field name made lowercase.
    requisitionflag = models.CharField(db_column='RequisitionFlag', max_length=1)  # Field name made lowercase.
    salesqty1 = models.DecimalField(db_column='SalesQty1', max_digits=18, decimal_places=6)  # Field name made lowercase.
    salesqty2 = models.DecimalField(db_column='SalesQty2', max_digits=18, decimal_places=6)  # Field name made lowercase.
    salesqty3 = models.DecimalField(db_column='SalesQty3', max_digits=18, decimal_places=6)  # Field name made lowercase.
    salesqty4 = models.DecimalField(db_column='SalesQty4', max_digits=18, decimal_places=6)  # Field name made lowercase.
    salesqty5 = models.DecimalField(db_column='SalesQty5', max_digits=18, decimal_places=6)  # Field name made lowercase.
    salesqty6 = models.DecimalField(db_column='SalesQty6', max_digits=18, decimal_places=6)  # Field name made lowercase.
    salesqty7 = models.DecimalField(db_column='SalesQty7', max_digits=18, decimal_places=6)  # Field name made lowercase.
    salesqty8 = models.DecimalField(db_column='SalesQty8', max_digits=18, decimal_places=6)  # Field name made lowercase.
    salesqty9 = models.DecimalField(db_column='SalesQty9', max_digits=18, decimal_places=6)  # Field name made lowercase.
    salesqty10 = models.DecimalField(db_column='SalesQty10', max_digits=18, decimal_places=6)  # Field name made lowercase.
    salesqty11 = models.DecimalField(db_column='SalesQty11', max_digits=18, decimal_places=6)  # Field name made lowercase.
    salesqty12 = models.DecimalField(db_column='SalesQty12', max_digits=18, decimal_places=6)  # Field name made lowercase.
    userfield1 = models.CharField(db_column='UserField1', max_length=1)  # Field name made lowercase.
    userfield2 = models.CharField(db_column='UserField2', max_length=1)  # Field name made lowercase.
    userfield3 = models.CharField(db_column='UserField3', max_length=1)  # Field name made lowercase.
    trfsupplieditem = models.CharField(db_column='TrfSuppliedItem', max_length=1)  # Field name made lowercase.
    defaultsourcewh = models.CharField(db_column='DefaultSourceWh', max_length=10)  # Field name made lowercase.
    trfleadtime = models.DecimalField(db_column='TrfLeadTime', max_digits=10, decimal_places=0)  # Field name made lowercase.
    trfcostglcode = models.CharField(db_column='TrfCostGlCode', max_length=35)  # Field name made lowercase.
    trfcostmultiply = models.DecimalField(db_column='TrfCostMultiply', max_digits=9, decimal_places=6)  # Field name made lowercase.
    qtydispatched = models.DecimalField(db_column='QtyDispatched', max_digits=18, decimal_places=6)  # Field name made lowercase.
    openbalqty1 = models.DecimalField(db_column='OpenBalQty1', max_digits=18, decimal_places=6)  # Field name made lowercase.
    openbalqty2 = models.DecimalField(db_column='OpenBalQty2', max_digits=18, decimal_places=6)  # Field name made lowercase.
    openbalqty3 = models.DecimalField(db_column='OpenBalQty3', max_digits=18, decimal_places=6)  # Field name made lowercase.
    openbalqty4 = models.DecimalField(db_column='OpenBalQty4', max_digits=18, decimal_places=6)  # Field name made lowercase.
    openbalqty5 = models.DecimalField(db_column='OpenBalQty5', max_digits=18, decimal_places=6)  # Field name made lowercase.
    openbalqty6 = models.DecimalField(db_column='OpenBalQty6', max_digits=18, decimal_places=6)  # Field name made lowercase.
    openbalqty7 = models.DecimalField(db_column='OpenBalQty7', max_digits=18, decimal_places=6)  # Field name made lowercase.
    openbalqty8 = models.DecimalField(db_column='OpenBalQty8', max_digits=18, decimal_places=6)  # Field name made lowercase.
    openbalqty9 = models.DecimalField(db_column='OpenBalQty9', max_digits=18, decimal_places=6)  # Field name made lowercase.
    openbalqty10 = models.DecimalField(db_column='OpenBalQty10', max_digits=18, decimal_places=6)  # Field name made lowercase.
    openbalqty11 = models.DecimalField(db_column='OpenBalQty11', max_digits=18, decimal_places=6)  # Field name made lowercase.
    openbalqty12 = models.DecimalField(db_column='OpenBalQty12', max_digits=18, decimal_places=6)  # Field name made lowercase.
    openbalcost1 = models.DecimalField(db_column='OpenBalCost1', max_digits=15, decimal_places=5)  # Field name made lowercase.
    openbalcost2 = models.DecimalField(db_column='OpenBalCost2', max_digits=15, decimal_places=5)  # Field name made lowercase.
    openbalcost3 = models.DecimalField(db_column='OpenBalCost3', max_digits=15, decimal_places=5)  # Field name made lowercase.
    openbalcost4 = models.DecimalField(db_column='OpenBalCost4', max_digits=15, decimal_places=5)  # Field name made lowercase.
    openbalcost5 = models.DecimalField(db_column='OpenBalCost5', max_digits=15, decimal_places=5)  # Field name made lowercase.
    openbalcost6 = models.DecimalField(db_column='OpenBalCost6', max_digits=15, decimal_places=5)  # Field name made lowercase.
    openbalcost7 = models.DecimalField(db_column='OpenBalCost7', max_digits=15, decimal_places=5)  # Field name made lowercase.
    openbalcost8 = models.DecimalField(db_column='OpenBalCost8', max_digits=15, decimal_places=5)  # Field name made lowercase.
    openbalcost9 = models.DecimalField(db_column='OpenBalCost9', max_digits=15, decimal_places=5)  # Field name made lowercase.
    openbalcost10 = models.DecimalField(db_column='OpenBalCost10', max_digits=15, decimal_places=5)  # Field name made lowercase.
    openbalcost11 = models.DecimalField(db_column='OpenBalCost11', max_digits=15, decimal_places=5)  # Field name made lowercase.
    openbalcost12 = models.DecimalField(db_column='OpenBalCost12', max_digits=15, decimal_places=5)  # Field name made lowercase.
    agedqty1 = models.DecimalField(db_column='AgedQty1', max_digits=18, decimal_places=6)  # Field name made lowercase.
    agedqty2 = models.DecimalField(db_column='AgedQty2', max_digits=18, decimal_places=6)  # Field name made lowercase.
    agedqty3 = models.DecimalField(db_column='AgedQty3', max_digits=18, decimal_places=6)  # Field name made lowercase.
    agedqty4 = models.DecimalField(db_column='AgedQty4', max_digits=18, decimal_places=6)  # Field name made lowercase.
    agedqty5 = models.DecimalField(db_column='AgedQty5', max_digits=18, decimal_places=6)  # Field name made lowercase.
    agedqty6 = models.DecimalField(db_column='AgedQty6', max_digits=18, decimal_places=6)  # Field name made lowercase.
    trfreplenishwh = models.DecimalField(db_column='TrfReplenishWh', max_digits=1, decimal_places=0)  # Field name made lowercase.
    trfbuyingrule = models.CharField(db_column='TrfBuyingRule', max_length=1)  # Field name made lowercase.
    trfdocktostock = models.DecimalField(db_column='TrfDockToStock', max_digits=10, decimal_places=0)  # Field name made lowercase.
    trffixtimeperiod = models.DecimalField(db_column='TrfFixTimePeriod', max_digits=2, decimal_places=0)  # Field name made lowercase.
    labourcost = models.DecimalField(db_column='LabourCost', max_digits=15, decimal_places=5)  # Field name made lowercase.
    materialcost = models.DecimalField(db_column='MaterialCost', max_digits=15, decimal_places=5)  # Field name made lowercase.
    fixedoverhead = models.DecimalField(db_column='FixedOverhead', max_digits=15, decimal_places=5)  # Field name made lowercase.
    variableoverhead = models.DecimalField(db_column='VariableOverhead', max_digits=15, decimal_places=5)  # Field name made lowercase.
    stdlabcostsbill = models.DecimalField(db_column='StdLabCostsBill', max_digits=15, decimal_places=5)  # Field name made lowercase.
    subcontractcost = models.DecimalField(db_column='SubContractCost', max_digits=15, decimal_places=5)  # Field name made lowercase.
    datewhadded = models.DateTimeField(db_column='DateWhAdded', blank=True, null=True)  # Field name made lowercase.
    rmaqtyissued = models.DecimalField(db_column='RmaQtyIssued', max_digits=18, decimal_places=6)  # Field name made lowercase.
    lastextendedcost = models.DecimalField(db_column='LastExtendedCost', max_digits=15, decimal_places=5)  # Field name made lowercase.
    orderpolicy = models.CharField(db_column='OrderPolicy', max_length=1)  # Field name made lowercase.
    majorordermult = models.DecimalField(db_column='MajorOrderMult', max_digits=18, decimal_places=6)  # Field name made lowercase.
    minorordermult = models.DecimalField(db_column='MinorOrderMult', max_digits=18, decimal_places=6)  # Field name made lowercase.
    orderminimum = models.DecimalField(db_column='OrderMinimum', max_digits=18, decimal_places=6)  # Field name made lowercase.
    ordermaximum = models.DecimalField(db_column='OrderMaximum', max_digits=18, decimal_places=6)  # Field name made lowercase.
    orderfixperiod = models.DecimalField(db_column='OrderFixPeriod', max_digits=2, decimal_places=0)  # Field name made lowercase.
    manualcostflag = models.CharField(db_column='ManualCostFlag', max_length=1)  # Field name made lowercase.
    leadtime = models.DecimalField(db_column='LeadTime', max_digits=10, decimal_places=0)  # Field name made lowercase.
    manufleadtime = models.DecimalField(db_column='ManufLeadTime', max_digits=10, decimal_places=0)  # Field name made lowercase.
    transfercost = models.DecimalField(db_column='TransferCost', max_digits=15, decimal_places=5)  # Field name made lowercase.
    implosionnum = models.DecimalField(db_column='ImplosionNum', max_digits=5, decimal_places=0)  # Field name made lowercase.
    excludefromsched = models.CharField(db_column='ExcludeFromSched', max_length=1)  # Field name made lowercase.
    qtywipreserved = models.DecimalField(db_column='QtyWipReserved', max_digits=18, decimal_places=6)  # Field name made lowercase.
    supplier = models.TextField(db_column='Supplier')  # Field name made lowercase.
    boughtoutwhslvl = models.CharField(db_column='BoughtOutWhsLvl', max_length=1)  # Field name made lowercase.
    docktostock = models.DecimalField(db_column='DockToStock', max_digits=10, decimal_places=0)  # Field name made lowercase.
    timestamp = models.TextField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    directtopick = models.NullBooleanField(db_column='DirectToPick')  # Field name made lowercase.
    cubicfeetoverride = models.DecimalField(db_column='CubicFeetOverride', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvWarehouse'
        unique_together = (('trfsupplieditem', 'stockcode', 'warehouse'), ('stockcode', 'stockcode', 'stockcode', 'stockcode', 'stockcode', 'warehouse', 'warehouse'), ('warehouse', 'stockcode'),)


class InvWarehousePlus(models.Model):
    stockcode = models.ForeignKey(InvMaster, models.DO_NOTHING, db_column='StockCode', primary_key=True, max_length=30)  # Field name made lowercase.
    warehouse = models.CharField(db_column='Warehouse', max_length=10)  # Field name made lowercase.
    binsize = models.DecimalField(db_column='BinSize', max_digits=6, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    timestamp = models.TextField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'InvWarehouse+'
        unique_together = (('stockcode', 'warehouse'),)


class NorthShoreShipmentMaster(models.Model):
    salesorder = models.CharField(db_column='SalesOrder', max_length=25)  # Field name made lowercase.
    shipmentnumber = models.CharField(db_column='ShipmentNumber', primary_key=True, max_length=25)  # Field name made lowercase.
    shipdate = models.DateTimeField(db_column='ShipDate', blank=True, null=True)  # Field name made lowercase.
    expectedpackcount = models.IntegerField(db_column='ExpectedPackCount')  # Field name made lowercase.
    shipviacode = models.CharField(db_column='ShipViaCode', max_length=10)  # Field name made lowercase.
    shipvia = models.CharField(db_column='ShipVia', max_length=50)  # Field name made lowercase.
    scac = models.CharField(db_column='SCAC', max_length=50)  # Field name made lowercase.
    chargecode = models.CharField(db_column='ChargeCode', max_length=50)  # Field name made lowercase.
    residential = models.CharField(db_column='Residential', max_length=5, blank=True, null=True)  # Field name made lowercase.
    signature = models.CharField(db_column='Signature', max_length=50)  # Field name made lowercase.
    billmethod = models.CharField(db_column='BillMethod', max_length=50)  # Field name made lowercase.
    billtoaccount = models.CharField(db_column='BillToAccount', max_length=50)  # Field name made lowercase.
    customerponumber = models.CharField(db_column='CustomerPoNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customer = models.ForeignKey(ArCustomer, models.DO_NOTHING, db_column='Customer', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customeremail = models.CharField(db_column='CustomerEmail', max_length=100, blank=True, null=True)  # Field name made lowercase.
    branch = models.CharField(db_column='Branch', max_length=5, blank=True, null=True)  # Field name made lowercase.
    salesperson = models.CharField(db_column='Salesperson', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ordertype = models.CharField(db_column='OrderType', max_length=5, blank=True, null=True)  # Field name made lowercase.
    orderitemcount = models.IntegerField(db_column='OrderItemCount', blank=True, null=True)  # Field name made lowercase.
    ordertotalvalue = models.DecimalField(db_column='OrderTotalValue', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    totalweightexpected = models.DecimalField(db_column='TotalWeightExpected', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    totalweightactual = models.DecimalField(db_column='TotalWeightActual', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    insertcodes = models.TextField(db_column='InsertCodes', blank=True, null=True)  # Field name made lowercase.
    notaper = models.NullBooleanField(db_column='NoTaper')  # Field name made lowercase.
    user1 = models.CharField(db_column='User1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    user2 = models.CharField(db_column='User2', max_length=25, blank=True, null=True)  # Field name made lowercase.
    label1tracking = models.CharField(db_column='Label1Tracking', max_length=50, blank=True, null=True)  # Field name made lowercase.
    label1zebra = models.TextField(db_column='Label1Zebra', blank=True, null=True)  # Field name made lowercase.
    label2tracking = models.CharField(db_column='Label2Tracking', max_length=50, blank=True, null=True)  # Field name made lowercase.
    label2zebra = models.TextField(db_column='Label2Zebra', blank=True, null=True)  # Field name made lowercase.
    datetimecreated = models.DateTimeField(db_column='DateTimeCreated', blank=True, null=True)  # Field name made lowercase.
    datetimecompleted = models.DateTimeField(db_column='DateTimeCompleted', blank=True, null=True)  # Field name made lowercase.
    sendername = models.CharField(db_column='SenderName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sendercompanyname = models.CharField(db_column='SenderCompanyName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    senderphone = models.CharField(db_column='SenderPhone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    senderaddress1 = models.CharField(db_column='SenderAddress1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    senderaddress2 = models.CharField(db_column='SenderAddress2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sendercity = models.CharField(db_column='SenderCity', max_length=50, blank=True, null=True)  # Field name made lowercase.
    senderstate = models.CharField(db_column='SenderState', max_length=50, blank=True, null=True)  # Field name made lowercase.
    senderpostalcode = models.CharField(db_column='SenderPostalCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sendercountry = models.CharField(db_column='SenderCountry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    recipientname = models.CharField(db_column='RecipientName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    recipientcompanyname = models.CharField(db_column='RecipientCompanyName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    recipientphone = models.CharField(db_column='RecipientPhone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    recipientaddress1 = models.CharField(db_column='RecipientAddress1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    recipientaddress2 = models.CharField(db_column='RecipientAddress2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    recipientcity = models.CharField(db_column='RecipientCity', max_length=50, blank=True, null=True)  # Field name made lowercase.
    recipientstate = models.CharField(db_column='RecipientState', max_length=50, blank=True, null=True)  # Field name made lowercase.
    recipientpostalcode = models.CharField(db_column='RecipientPostalCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    recipientcountry = models.CharField(db_column='RecipientCountry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastlicenseplateentered = models.CharField(db_column='LastLicensePlateEntered', max_length=25, blank=True, null=True)  # Field name made lowercase.
    orderstockcodes = models.CharField(db_column='OrderStockCodes', max_length=500, blank=True, null=True)  # Field name made lowercase.
    totalshipweightexpected = models.DecimalField(db_column='TotalShipWeightExpected', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bypassweightvalidate = models.NullBooleanField(db_column='BypassWeightValidate')  # Field name made lowercase.
    nousps = models.NullBooleanField(db_column='NoUsps')  # Field name made lowercase.
    archived = models.NullBooleanField(db_column='Archived')  # Field name made lowercase.
    documentformat = models.CharField(db_column='DocumentFormat', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NorthShoreShipmentMaster'


class NorthShoreShipmentPack(models.Model):
    licenseplatenumber = models.CharField(db_column='LicensePlateNumber', primary_key=True, max_length=25)  # Field name made lowercase.
    salesorder = models.ForeignKey(SorMaster, models.DO_NOTHING, db_column='SalesOrder', max_length=25)  # Field name made lowercase.
    shipmentnumber = models.ForeignKey(NorthShoreShipmentMaster, models.DO_NOTHING, db_column='ShipmentNumber', max_length=25)  # Field name made lowercase.
    packnumber = models.IntegerField(db_column='PackNumber')  # Field name made lowercase.
    length = models.DecimalField(db_column='Length', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    width = models.DecimalField(db_column='Width', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    height = models.DecimalField(db_column='Height', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    weight = models.DecimalField(db_column='Weight', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    insertcodes = models.TextField(db_column='InsertCodes', blank=True, null=True)  # Field name made lowercase.
    notaper = models.BooleanField(db_column='NoTaper')  # Field name made lowercase.
    label1tracking = models.CharField(db_column='Label1Tracking', max_length=50, blank=True, null=True)  # Field name made lowercase.
    label1zebra = models.TextField(db_column='Label1Zebra', blank=True, null=True)  # Field name made lowercase.
    label2tracking = models.CharField(db_column='Label2Tracking', max_length=50, blank=True, null=True)  # Field name made lowercase.
    label2zebra = models.TextField(db_column='Label2Zebra', blank=True, null=True)  # Field name made lowercase.
    datetimecreated = models.DateTimeField(db_column='DateTimeCreated', blank=True, null=True)  # Field name made lowercase.
    packinglistenclosed = models.BooleanField(db_column='PackingListEnclosed')  # Field name made lowercase.
    shipdate = models.DateTimeField(db_column='ShipDate', blank=True, null=True)  # Field name made lowercase.
    expectedpackcount = models.IntegerField(db_column='ExpectedPackCount')  # Field name made lowercase.
    shipviacode = models.CharField(db_column='ShipViaCode', max_length=10)  # Field name made lowercase.
    shipvia = models.CharField(db_column='ShipVia', max_length=50)  # Field name made lowercase.
    scac = models.CharField(db_column='SCAC', max_length=50)  # Field name made lowercase.
    chargecode = models.CharField(db_column='ChargeCode', max_length=50)  # Field name made lowercase.
    residential = models.CharField(db_column='Residential', max_length=5, blank=True, null=True)  # Field name made lowercase.
    signature = models.CharField(db_column='Signature', max_length=50)  # Field name made lowercase.
    billmethod = models.CharField(db_column='BillMethod', max_length=50)  # Field name made lowercase.
    billtoaccount = models.CharField(db_column='BillToAccount', max_length=50)  # Field name made lowercase.
    customerponumber = models.CharField(db_column='CustomerPoNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customer = models.CharField(db_column='Customer', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customeremail = models.CharField(db_column='CustomerEmail', max_length=100, blank=True, null=True)  # Field name made lowercase.
    branch = models.CharField(db_column='Branch', max_length=5, blank=True, null=True)  # Field name made lowercase.
    salesperson = models.CharField(db_column='Salesperson', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ordertype = models.CharField(db_column='OrderType', max_length=5, blank=True, null=True)  # Field name made lowercase.
    orderitemcount = models.IntegerField(db_column='OrderItemCount', blank=True, null=True)  # Field name made lowercase.
    ordertotalvalue = models.DecimalField(db_column='OrderTotalValue', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    totalweightexpected = models.DecimalField(db_column='TotalWeightExpected', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sendername = models.CharField(db_column='SenderName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sendercompanyname = models.CharField(db_column='SenderCompanyName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    senderphone = models.CharField(db_column='SenderPhone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    senderaddress1 = models.CharField(db_column='SenderAddress1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    senderaddress2 = models.CharField(db_column='SenderAddress2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sendercity = models.CharField(db_column='SenderCity', max_length=50, blank=True, null=True)  # Field name made lowercase.
    senderstate = models.CharField(db_column='SenderState', max_length=50, blank=True, null=True)  # Field name made lowercase.
    senderpostalcode = models.CharField(db_column='SenderPostalCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sendercountry = models.CharField(db_column='SenderCountry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    recipientname = models.CharField(db_column='RecipientName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    recipientcompanyname = models.CharField(db_column='RecipientCompanyName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    recipientphone = models.CharField(db_column='RecipientPhone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    recipientaddress1 = models.CharField(db_column='RecipientAddress1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    recipientaddress2 = models.CharField(db_column='RecipientAddress2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    recipientcity = models.CharField(db_column='RecipientCity', max_length=50, blank=True, null=True)  # Field name made lowercase.
    recipientstate = models.CharField(db_column='RecipientState', max_length=50, blank=True, null=True)  # Field name made lowercase.
    recipientpostalcode = models.CharField(db_column='RecipientPostalCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    recipientcountry = models.CharField(db_column='RecipientCountry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    enetcreatesuccess = models.BooleanField(db_column='EnetCreateSuccess')  # Field name made lowercase.
    rdslabelconfirm = models.BooleanField(db_column='RdsLabelConfirm')  # Field name made lowercase.
    rdsconfirmmessage = models.CharField(db_column='RdsConfirmMessage', max_length=100, blank=True, null=True)  # Field name made lowercase.
    hasalternatelabels = models.NullBooleanField(db_column='HasAlternateLabels')  # Field name made lowercase.
    rdstimeconfirmed = models.DateTimeField(db_column='RdsTimeConfirmed', blank=True, null=True)  # Field name made lowercase.
    bypassweightvalidate = models.NullBooleanField(db_column='BypassWeightValidate')  # Field name made lowercase.
    user1 = models.CharField(db_column='User1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    user2 = models.CharField(db_column='User2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    shiprate = models.DecimalField(db_column='ShipRate', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nousps = models.NullBooleanField(db_column='NoUsps')  # Field name made lowercase.
    archived = models.NullBooleanField(db_column='Archived')  # Field name made lowercase.
    documentformat = models.CharField(db_column='DocumentFormat', max_length=50, blank=True, null=True)  # Field name made lowercase.
    insertsprocessed = models.NullBooleanField(db_column='InsertsProcessed')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NorthShoreShipmentPack'


class SorAdditions(models.Model):
    trndate = models.TextField(db_column='TrnDate', primary_key=True)  # Field name made lowercase.
    trntime = models.TextField(db_column='TrnTime')  # Field name made lowercase.
    salesorder = models.ForeignKey(SorMaster, models.DO_NOTHING, db_column='SalesOrder')  # Field name made lowercase.
    salesorderline = models.TextField(db_column='SalesOrderLine')  # Field name made lowercase.
    linetype = models.CharField(db_column='LineType', max_length=1)  # Field name made lowercase.
    linevalue = models.DecimalField(db_column='LineValue', max_digits=14, decimal_places=2)  # Field name made lowercase.
    costvalue = models.DecimalField(db_column='CostValue', max_digits=14, decimal_places=2)  # Field name made lowercase.
    productclass = models.TextField(db_column='ProductClass')  # Field name made lowercase.
    customer = models.ForeignKey(ArCustomer, models.DO_NOTHING, db_column='Customer')  # Field name made lowercase.
    branch = models.TextField(db_column='Branch')  # Field name made lowercase.
    documenttype = models.CharField(db_column='DocumentType', max_length=1)  # Field name made lowercase.
    salesperson = models.TextField(db_column='Salesperson')  # Field name made lowercase.
    area = models.TextField(db_column='Area')  # Field name made lowercase.
    taxcode = models.TextField(db_column='TaxCode')  # Field name made lowercase.
    gstcode = models.CharField(db_column='GstCode', max_length=3)  # Field name made lowercase.
    userfield1 = models.CharField(db_column='UserField1', max_length=1)  # Field name made lowercase.
    stockcode = models.ForeignKey(InvMaster, models.DO_NOTHING, db_column='StockCode')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50)  # Field name made lowercase.
    warehouse = models.TextField(db_column='Warehouse')  # Field name made lowercase.
    orderqty = models.DecimalField(db_column='OrderQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    orderuom = models.TextField(db_column='OrderUom')  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=15, decimal_places=5)  # Field name made lowercase.
    priceuom = models.TextField(db_column='PriceUom')  # Field name made lowercase.
    discount = models.DecimalField(db_column='Discount', max_digits=14, decimal_places=2)  # Field name made lowercase.
    shipqty = models.DecimalField(db_column='ShipQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    creditreason = models.CharField(db_column='CreditReason', max_length=6)  # Field name made lowercase.
    operator = models.TextField(db_column='Operator')  # Field name made lowercase.
    timestamp = models.TextField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'SorAdditions'
        unique_together = (('trndate', 'trndate', 'trndate', 'trndate', 'trntime', 'trntime', 'trntime', 'trntime', 'salesorder', 'salesorder', 'salesorder', 'salesorder', 'salesorder', 'salesorderline', 'salesorderline'),)


class SorChanges(models.Model):
    trndate = models.TextField(db_column='TrnDate')  # Field name made lowercase.
    trntime = models.TextField(db_column='TrnTime')  # Field name made lowercase.
    salesorder = models.ForeignKey(SorMaster, models.DO_NOTHING, db_column='SalesOrder', primary_key=True)  # Field name made lowercase.
    salesorderline = models.TextField(db_column='SalesOrderLine')  # Field name made lowercase.
    linetype = models.CharField(db_column='LineType', max_length=1)  # Field name made lowercase.
    changevalue = models.DecimalField(db_column='ChangeValue', max_digits=14, decimal_places=2)  # Field name made lowercase.
    changecost = models.DecimalField(db_column='ChangeCost', max_digits=14, decimal_places=2)  # Field name made lowercase.
    productclass = models.TextField(db_column='ProductClass')  # Field name made lowercase.
    customer = models.ForeignKey(ArCustomer, models.DO_NOTHING, db_column='Customer')  # Field name made lowercase.
    branch = models.TextField(db_column='Branch')  # Field name made lowercase.
    documenttype = models.CharField(db_column='DocumentType', max_length=1)  # Field name made lowercase.
    salesperson = models.TextField(db_column='Salesperson')  # Field name made lowercase.
    area = models.TextField(db_column='Area')  # Field name made lowercase.
    userfield1 = models.CharField(db_column='UserField1', max_length=1)  # Field name made lowercase.
    stockcode = models.ForeignKey(InvMaster, models.DO_NOTHING, db_column='StockCode')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50)  # Field name made lowercase.
    warehouse = models.TextField(db_column='Warehouse')  # Field name made lowercase.
    newwarehouse = models.CharField(db_column='NewWarehouse', max_length=10)  # Field name made lowercase.
    orderqty = models.DecimalField(db_column='OrderQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    orderuom = models.TextField(db_column='OrderUom')  # Field name made lowercase.
    neworderqty = models.DecimalField(db_column='NewOrderQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=15, decimal_places=5)  # Field name made lowercase.
    priceuom = models.TextField(db_column='PriceUom')  # Field name made lowercase.
    newprice = models.DecimalField(db_column='NewPrice', max_digits=15, decimal_places=5)  # Field name made lowercase.
    newpriceuom = models.CharField(db_column='NewPriceUom', max_length=10)  # Field name made lowercase.
    discount = models.DecimalField(db_column='Discount', max_digits=14, decimal_places=2)  # Field name made lowercase.
    newdiscount = models.DecimalField(db_column='NewDiscount', max_digits=14, decimal_places=2)  # Field name made lowercase.
    operator = models.TextField(db_column='Operator')  # Field name made lowercase.
    taxcode = models.TextField(db_column='TaxCode')  # Field name made lowercase.
    reasoncode = models.TextField(db_column='ReasonCode')  # Field name made lowercase.
    timestamp = models.TextField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'SorChanges'
        unique_together = (('trndate', 'trndate', 'trndate', 'trndate', 'trntime', 'trntime', 'trntime', 'trntime', 'salesorder', 'salesorder', 'salesorder', 'salesorder', 'salesorder', 'salesorderline', 'salesorderline'),)
