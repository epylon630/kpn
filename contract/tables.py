from table import Table
from table.columns import Column
from table.utils import A
from table.columns import LinkColumn, Link

from .models import Search, SupplierOffer

class ContractTable(Table):
    contractList = LinkColumn(header='Contracts',   links=[Link( text=(A('offer_supplier_offer')) , viewname='contract:item_list' , args=(A('offer_supplier_offer'),)), ])
    offer_unstructured_text = Column(field='offer_unstructured_text' , header='Contract Line Description')
    offer_supplier_name = Column(field='offer_supplier_name',  header='Awarded Vendor')
  #  ItemList  = LinkColumn( 'contract:item_list', text= lambda record: record['offer_legacy_no'] , args=[A('offer_supplier_offer')], verbose_name='Item List')
    itemList = LinkColumn(header='Contract Number', links=[
        Link(text=(A('offer_legacy_no')), viewname='contract:detail', args=(A('offer_supplier_offer'),)), ])


class ItemListTable(Table):
    supplier = Column(field='supplier_name', header='Supplier')
    detail = LinkColumn(header='Manufacturer Sku', links=[
        Link(text=(A('manufacturer_sku')), viewname='contract:item_detail', args=(A('supplier_item_id'),)), ])
    product_description = Column(field='product_description' ,  header='Product Description' )
    price_uom = Column(field='price_uom' ,  header='Price UOM')
    current_price_per_uom = Column(field='current_price_per_uom' ,  header='Unit Price' )
