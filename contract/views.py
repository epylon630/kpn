from django.shortcuts import get_object_or_404, render
import httplib, urllib2
import xml.dom.minidom
import csv

# Create your views here.
from .models import Search, Contract, BuyingOrganization, SupplierOffer, SupplierItem
from django.contrib.auth.models import User
from django.views import generic
from .tables import ContractTable, ItemListTable
from django.db.models import Q
from django.views.generic import TemplateView

def index(request):
    pPEPPMPVSTCode = 'EP-02040-CA-PVPM'
    queryset = BuyingOrganization.objects.filter(buying_group_code=pPEPPMPVSTCode)
    pBuyingGroupId = queryset[0].buying_group_id
    pBuyingGroupId = str(pBuyingGroupId)

    pSearchQueryXml = '<Request payloadID="2016-05-25T11:22:58-07:00.15073085.5886691126459456@VBDEV" xmlns="epylon/searchxml"><RequestType>GroupOffers</RequestType><RequestSubType>Offer</RequestSubType><SortType>None</SortType><GroupId>' + pBuyingGroupId + '</GroupId><HitLimit>2000</HitLimit></Request>'

    r = urllib2.Request("http://dev-search.epylon.hq:8088/searchWebApp/search", data=pSearchQueryXml, headers={'Content-Type': 'application/xml'})
    req = urllib2.urlopen(r)
    data = req.read()
    req.close()

    dom = xml.dom.minidom.parseString(data)

    Ids = dom.getElementsByTagName("Id")
    iDCount = len(Ids)

    print iDCount
    idArray = [0] * iDCount

    i = 0
    for id in Ids:
        value = id.firstChild.nodeValue
        idArray[i] = int(value)
        i += 1

    args = {'offer_supplier_offer_id__in':idArray}

    table = ContractTable(Search.objects.filter(**args).filter(search_type='ContractHeader').
                          values('search_id', 'offer_legacy_no', 'offer_unstructured_text', 'offer_supplier_name','offer_supplier_offer', 'offer_legacy_request_no'))
    #RequestConfig(request).configure(table)
    return render(request, 'contract/index.html', {'table': table})

def category(request, category):
    print category
    pPEPPMPVSTCode = 'EP-02040-CA-PVPM'
    queryset = BuyingOrganization.objects.filter(buying_group_code=pPEPPMPVSTCode)
    pBuyingGroupId = queryset[0].buying_group_id
    pBuyingGroupId = str(pBuyingGroupId)

    pSearchQueryXml = '<Request payloadID="2016-05-25T11:22:58-07:00.15073085.5886691126459456@VBDEV" xmlns="epylon/searchxml"><RequestType>GroupOffers</RequestType><RequestSubType>Offer</RequestSubType><SortType>None</SortType><GroupId>' + pBuyingGroupId + '</GroupId><HitLimit>2000</HitLimit></Request>'

    r = urllib2.Request("http://dev-search.epylon.hq:8088/searchWebApp/search", data=pSearchQueryXml,
                        headers={'Content-Type': 'application/xml'})
    req = urllib2.urlopen(r)
    data = req.read()
    req.close()

    dom = xml.dom.minidom.parseString(data)

    Ids = dom.getElementsByTagName("Id")
    iDCount = len(Ids)

    print iDCount
    idArray = [0] * iDCount

    i = 0
    for id in Ids:
        value = id.firstChild.nodeValue
        idArray[i] = int(value)
        i += 1

    args = {'offer_supplier_offer_id__in': idArray}

    table = ContractTable(Search.objects.filter(**args).filter(search_type='ContractHeader').filter(offer_supplier_name__icontains=category).
                          values('search_id', 'offer_legacy_no', 'offer_unstructured_text', 'offer_supplier_name',
                                 'offer_supplier_offer', 'offer_legacy_request_no'))
    return render(request, 'contract/index.html', {'table': table})

def detail(request, offer_id):
    offer = get_object_or_404(SupplierOffer, pk=offer_id)
    return render(request, 'contract/detail.html',  {'offer': offer} )

def item_list(request, offer_id):
        
    table = ItemListTable(SupplierItem.objects.filter(supplier_offer_id=offer_id).filter(supplier_item_status='CU').order_by('item_no').values('supplier_item_id', 'manufacturer_sku', 'product_description', 'price_uom', 'current_price_per_uom', 'supplier_name'))
#    RequestConfig(request).configure(table)
    return render(request, 'contract/item_list.html', {'table': table})

def item_detail(request, item_id):
         item = get_object_or_404(SupplierItem, pk=item_id)
         return render(request, 'contract/item_detail.html',  {'item': item} )



