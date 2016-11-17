# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class BillingInvoiceDetail(models.Model):
    billing_invoice_id = models.FloatField(primary_key=True)
    billing_program_id = models.IntegerField()
    program_name  = models.CharField(max_length=60)
    status = models.CharField(max_length=20)
    billing_target_id = models.IntegerField()
    target_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'billing_invoice_detail'
        app_label = 'mktplc'

class AccountingCodes(models.Model):
    purchase_form = models.ForeignKey('PurchaseForm', models.DO_NOTHING)
    allocation_amount = models.DecimalField(max_digits=22, decimal_places=2, blank=True, null=True)
    legacy_accounting_code = models.CharField(max_length=60)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    account_code_no = models.FloatField()

    class Meta:
        managed = False
        db_table = 'accounting_codes'
        unique_together = (('purchase_form', 'account_code_no'),)
        app_label = 'mktplc'

class AdministrativeGroup(models.Model):
    administrative_group_id = models.FloatField(primary_key=True)
    admstrve_group_name = models.CharField(max_length=60, blank=True, null=True)
    billing_contact = models.ForeignKey('Contact', related_name='billing_contact',  blank=True, null=True)
    buying_organization = models.ForeignKey('BuyingOrganization', models.DO_NOTHING, blank=True, null=True)
    ship_to_contact = models.ForeignKey('Contact', related_name='shipto_contact', blank=True, null=True)
    group_type = models.CharField(max_length=3, blank=True, null=True)
    delivery_times = models.CharField(max_length=40, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'administrative_group'
        app_label = 'mktplc'

class AdmstrveGroupContact(models.Model):
    administrative_group = models.ForeignKey(AdministrativeGroup, models.DO_NOTHING)
    contact = models.ForeignKey('Contact', models.DO_NOTHING)
    contact_type = models.CharField(max_length=2, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admstrve_group_contact'
        unique_together = (('administrative_group', 'contact'),)
	app_label = 'mktplc'

class Answer(models.Model):
    answer_id = models.FloatField(primary_key=True)
    question = models.ForeignKey('Question', models.DO_NOTHING)
    answer = models.CharField(max_length=4000, blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    owner_id = models.FloatField()
    owner_type = models.CharField(max_length=2)
    sequence = models.FloatField()
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'answer'
	app_label = 'mktplc'

class ApplicationFunction(models.Model):
    application_function_id = models.FloatField(primary_key=True)
    application_name = models.CharField(max_length=80)
    function_name = models.CharField(max_length=80)
    function_description = models.CharField(max_length=400, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'application_function'
	app_label = 'mktplc'

class Article(models.Model):
    article_id = models.FloatField(primary_key=True)
    publisher = models.ForeignKey('Publisher', models.DO_NOTHING)
    publication_date = models.DateField()
    headline = models.CharField(max_length=80)
    blurb = models.CharField(max_length=400, blank=True, null=True)
    article_type = models.CharField(max_length=3, blank=True, null=True)
    article_link = models.CharField(max_length=400, blank=True, null=True)
    article_image = models.CharField(max_length=400, blank=True, null=True)
    visual_priority = models.FloatField(blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article'
	app_label = 'mktplc'

class AssemblyInfo(models.Model):
    master_assmbly_prdt = models.ForeignKey('Product', related_name='master_assmbly_prdt' )
    assembly_part = models.ForeignKey('Product', related_name='assembly_part' )
    assembly_part_quantity = models.FloatField(blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assembly_info'
        unique_together = (('master_assmbly_prdt', 'assembly_part'),)
	app_label = 'mktplc'

class AttributeBin(models.Model):
    attribute_bin_id = models.FloatField(primary_key=True)
    attribute_value = models.CharField(max_length=60)
    value_unit = models.CharField(max_length=20, blank=True, null=True)
    normalized_numeric_value = models.FloatField(blank=True, null=True)
    product_detail = models.ForeignKey('ProductDetail', models.DO_NOTHING)
    meta_attribute = models.ForeignKey('MetaAttribute', models.DO_NOTHING)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attribute_bin'
	app_label = 'mktplc'

class BankStatementTransaction(models.Model):
    bank_statement_transaction_id = models.FloatField(primary_key=True)
    bank_account_id = models.CharField(max_length=40)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    transaction_date = models.DateField()
    transaction_type = models.CharField(max_length=2)
    transaction_amount = models.FloatField()
    transaction_reference_code = models.CharField(max_length=100, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    origin_id = models.FloatField(blank=True, null=True)
    origin_type = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bank_statement_transaction'
	app_label = 'mktplc'

class BatchProcessing(models.Model):
    batch_processing_id = models.FloatField(primary_key=True)
    type = models.CharField(max_length=2, blank=True, null=True)
    status = models.CharField(max_length=2, blank=True, null=True)
    file_path = models.CharField(max_length=200, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'batch_processing'
	app_label = 'mktplc'

class BilltoChangeRequest(models.Model):
    billto_change_request_id = models.FloatField(primary_key=True)
    purchase_form = models.ForeignKey('PurchaseForm', models.DO_NOTHING, blank=True, null=True)
    prev_billto_contact = models.ForeignKey('Contact', related_name='prev_billto_contact' , blank=True, null=True)
    new_billto_contact = models.ForeignKey('Contact', related_name='new_billto_contact'  , blank=True, null=True)
    change_date = models.DateField(blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    request_status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'billto_change_request'
	app_label = 'mktplc'

class BridgesAqQueueTable(models.Model):
    q_name = models.CharField(max_length=30, blank=True, null=True)
    msgid = models.TextField(primary_key=True)  # This field type is a guess.
    corrid = models.CharField(max_length=128, blank=True, null=True)
    priority = models.FloatField(blank=True, null=True)
    state = models.FloatField(blank=True, null=True)
    delay = models.DateTimeField(blank=True, null=True)
    expiration = models.FloatField(blank=True, null=True)
    time_manager_info = models.DateTimeField(blank=True, null=True)
    local_order_no = models.FloatField(blank=True, null=True)
    chain_no = models.FloatField(blank=True, null=True)
    cscn = models.FloatField(blank=True, null=True)
    dscn = models.FloatField(blank=True, null=True)
    enq_time = models.DateTimeField(blank=True, null=True)
    enq_uid = models.FloatField(blank=True, null=True)
    enq_tid = models.CharField(max_length=30, blank=True, null=True)
    deq_time = models.DateTimeField(blank=True, null=True)
    deq_uid = models.FloatField(blank=True, null=True)
    deq_tid = models.CharField(max_length=30, blank=True, null=True)
    retry_count = models.FloatField(blank=True, null=True)
    exception_qschema = models.CharField(max_length=30, blank=True, null=True)
    exception_queue = models.CharField(max_length=30, blank=True, null=True)
    step_no = models.FloatField(blank=True, null=True)
    recipient_key = models.FloatField(blank=True, null=True)
    dequeue_msgid = models.TextField(blank=True, null=True)  # This field type is a guess.
    sender_name = models.CharField(max_length=30, blank=True, null=True)
    sender_address = models.CharField(max_length=1024, blank=True, null=True)
    sender_protocol = models.FloatField(blank=True, null=True)
    user_data = models.BinaryField(blank=True, null=True)
    user_prop = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'bridges_aq_queue_table'
	app_label = 'mktplc'

class BridgesQueueTable(models.Model):
    q_name = models.CharField(max_length=30, blank=True, null=True)
    msgid = models.TextField(primary_key=True)  # This field type is a guess.
    corrid = models.CharField(max_length=128, blank=True, null=True)
    priority = models.FloatField(blank=True, null=True)
    state = models.FloatField(blank=True, null=True)
    delay = models.DateTimeField(blank=True, null=True)
    expiration = models.FloatField(blank=True, null=True)
    time_manager_info = models.DateTimeField(blank=True, null=True)
    local_order_no = models.FloatField(blank=True, null=True)
    chain_no = models.FloatField(blank=True, null=True)
    cscn = models.FloatField(blank=True, null=True)
    dscn = models.FloatField(blank=True, null=True)
    enq_time = models.DateTimeField(blank=True, null=True)
    enq_uid = models.FloatField(blank=True, null=True)
    enq_tid = models.CharField(max_length=30, blank=True, null=True)
    deq_time = models.DateTimeField(blank=True, null=True)
    deq_uid = models.FloatField(blank=True, null=True)
    deq_tid = models.CharField(max_length=30, blank=True, null=True)
    retry_count = models.FloatField(blank=True, null=True)
    exception_qschema = models.CharField(max_length=30, blank=True, null=True)
    exception_queue = models.CharField(max_length=30, blank=True, null=True)
    step_no = models.FloatField(blank=True, null=True)
    recipient_key = models.FloatField(blank=True, null=True)
    dequeue_msgid = models.TextField(blank=True, null=True)  # This field type is a guess.
    sender_name = models.CharField(max_length=30, blank=True, null=True)
    sender_address = models.CharField(max_length=1024, blank=True, null=True)
    sender_protocol = models.FloatField(blank=True, null=True)
    user_data = models.TextField(blank=True, null=True)  # This field type is a guess.
    user_prop = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'bridges_queue_table'
	app_label = 'mktplc'

class BuyerContact(models.Model):
    buying_organization = models.ForeignKey('BuyingOrganization', models.DO_NOTHING)
    contact = models.ForeignKey('Contact', models.DO_NOTHING)
    contact_type = models.CharField(max_length=4)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buyer_contact'
        unique_together = (('buying_organization', 'contact', 'contact_type'),)
	app_label = 'mktplc'

class BuyerLogEntry(models.Model):
    buyer_log_entry_id = models.FloatField(primary_key=True)
    user = models.ForeignKey('EpylonUser', models.DO_NOTHING)
    buyer_log_entry_type = models.CharField(max_length=2)
    buyer_request = models.ForeignKey('BuyerRequest', models.DO_NOTHING, blank=True, null=True)
    entry_date = models.DateField(blank=True, null=True)
    supplier_rspns_offer = models.ForeignKey('SupplierResponse', models.DO_NOTHING, blank=True, null=True)
    purchase_form = models.ForeignKey('PurchaseForm', models.DO_NOTHING, blank=True, null=True)
    user_name = models.CharField(max_length=80)
    comments = models.CharField(max_length=2000)
    user_type = models.CharField(max_length=2, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    group_code = models.FloatField(blank=True, null=True)
    format_type = models.CharField(max_length=4, blank=True, null=True)
    real_user_id = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buyer_log_entry'
	app_label = 'mktplc'

class BuyerLvpParticipation(models.Model):
    buying_organization_id = models.FloatField(blank=True, null=True)
    large_vendor_program_id = models.FloatField(blank=True, null=True)
    small_business_org_id = models.FloatField(blank=True, null=True)
    buyer_lvp_participation_id = models.FloatField(primary_key=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    sequence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'buyer_lvp_participation'
        unique_together = (('buying_organization_id', 'large_vendor_program_id', 'small_business_org_id'),)
	app_label = 'mktplc'

class BuyerRegResponses(models.Model):
    initial_interest = models.OneToOneField('InitialInterest')
    organization_contact = models.ForeignKey('Contact', models.DO_NOTHING, blank=True, null=True)
    federal_tax_id = models.CharField(max_length=20, blank=True, null=True)
    purchase_order_count = models.FloatField(blank=True, null=True)
    organization_size = models.CharField(max_length=40, blank=True, null=True)
    heard_of_epylon = models.CharField(max_length=400, blank=True, null=True)
    receive_epylon_news = models.FloatField(blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buyer_reg_responses'
	app_label = 'mktplc'

class BuyerRequest(models.Model):
    buyer_request_id = models.FloatField(primary_key=True)
    template = models.FloatField()
    buyer_request_type = models.CharField(max_length=2)
    awarded_spplr_offer = models.ForeignKey('SupplierResponse', models.DO_NOTHING, blank=True, null=True)
    buyer_request_status = models.CharField(max_length=2)
    legacy_no = models.CharField(max_length=20, blank=True, null=True)
    title = models.CharField(max_length=256, blank=True, null=True)
    template_name = models.CharField(max_length=20, blank=True, null=True)
    structured = models.FloatField()
    unstructured_text = models.CharField(max_length=400, blank=True, null=True)
    substitution_allowed = models.FloatField()
    date_submitted = models.DateField(blank=True, null=True)
    item_count = models.FloatField(blank=True, null=True)
    rush_response = models.FloatField()
    date_response_due = models.DateField(blank=True, null=True)
    date_delivery_expected = models.DateField(blank=True, null=True)
    terms_and_conditions = models.CharField(max_length=400, blank=True, null=True)
    rush_delivery = models.FloatField(blank=True, null=True)
    freight_on_board = models.CharField(max_length=20, blank=True, null=True)
    shipto_org_name = models.CharField(max_length=60, blank=True, null=True)
    shipto_contact = models.ForeignKey('Contact', models.DO_NOTHING, blank=True, null=True)
    shipto_contact_name = models.CharField(max_length=80, blank=True, null=True)
    shipto_addr_line1 = models.CharField(max_length=80, blank=True, null=True)
    shipto_addr_line2 = models.CharField(max_length=80, blank=True, null=True)
    shipto_city = models.CharField(max_length=30, blank=True, null=True)
    shipto_state = models.CharField(max_length=20, blank=True, null=True)
    shipto_zip = models.CharField(max_length=20, blank=True, null=True)
    shipto_notes = models.CharField(max_length=400, blank=True, null=True)
    initiator_user = models.ForeignKey('EpylonUser', models.DO_NOTHING)
    initiator_name = models.CharField(max_length=80, blank=True, null=True)
    initiator_phone = models.CharField(max_length=20, blank=True, null=True)
    shipping_method = models.CharField(max_length=20, blank=True, null=True)
    inttr_buying_org = models.ForeignKey('BuyingOrganization', models.DO_NOTHING, blank=True, null=True)
    inttr_buying_org_name = models.CharField(max_length=80, blank=True, null=True)
    initiator_email = models.CharField(max_length=80, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    spot_price_check = models.FloatField()
    shipto_mail_stop = models.CharField(max_length=80, blank=True, null=True)
    opening_date = models.DateField(blank=True, null=True)
    meeting_date = models.DateField(blank=True, null=True)
    meeting_notes = models.CharField(max_length=2000, blank=True, null=True)
    unweighted_scoring = models.FloatField(blank=True, null=True)
    scratchpad = models.CharField(max_length=4000, blank=True, null=True)
    attachment_path_name = models.CharField(max_length=200, blank=True, null=True)
    reveal_award = models.FloatField(blank=True, null=True)
    shipto_county = models.CharField(max_length=30, blank=True, null=True)
    program = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buyer_request'
	app_label = 'mktplc'

class BuyerSpplrRelshp(models.Model):
    buying_organization = models.ForeignKey('BuyingOrganization', models.DO_NOTHING)
    supplier = models.ForeignKey('SupplierOrganization', models.DO_NOTHING)
    product_category = models.ForeignKey('ProductCategory', models.DO_NOTHING, blank=True, null=True)
    relationship_type = models.CharField(max_length=4, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buyer_spplr_relshp'
        unique_together = (('buying_organization', 'supplier'),)
 	app_label = 'mktplc'

class BuyingGroup(models.Model):
    buying_group_id = models.FloatField(primary_key=True)
    buying_group_name = models.CharField(max_length=80)
    buying_group_type = models.CharField(max_length=2)
    buying_group_code = models.CharField(max_length=20, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buying_group'
	app_label = 'mktplc'

class BuyingGroupHierarchy(models.Model):
    parent_buying_group = models.ForeignKey(BuyingGroup, related_name='parent_buying_group')
    child_buying_group = models.ForeignKey(BuyingGroup, related_name='child_buying_group')
    browsable = models.FloatField()
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buying_group_hierarchy'
        unique_together = (('parent_buying_group', 'child_buying_group'),)
	app_label = 'mktplc'

class BuyingOrganization(models.Model):
    buying_organization_id = models.FloatField(primary_key=True)
    organization_type = models.CharField(max_length=8, blank=True, null=True)
    buying_org_name = models.CharField(max_length=80)
    preferred_carrier = models.CharField(max_length=20, blank=True, null=True)
    prfrd_shpmnt_method = models.CharField(max_length=3, blank=True, null=True)
    date_registered = models.DateField(blank=True, null=True)
    quote_rules = models.CharField(max_length=20, blank=True, null=True)
    bid_rules = models.CharField(max_length=20, blank=True, null=True)
    buyer_otgng_quote_terms = models.CharField(max_length=400, blank=True, null=True)
    buyer_otgng_bid_terms = models.CharField(max_length=400, blank=True, null=True)
    buyer_dlvr_times = models.CharField(max_length=400, blank=True, null=True)
    buying_group = models.ForeignKey('BuyingGroup', models.DO_NOTHING, blank=True, null=True)
    status = models.CharField(max_length=2, blank=True, null=True)
    order_reaprvl_thrhld = models.FloatField(blank=True, null=True)
    buying_group_code = models.CharField(max_length=20, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    initial_interest = models.ForeignKey('InitialInterest', models.DO_NOTHING, blank=True, null=True)
    integration_type = models.CharField(max_length=2, blank=True, null=True)
    external_map_code = models.CharField(max_length=20, blank=True, null=True)
    ssc_subscriber = models.FloatField(blank=True, null=True)
    generic_config =  models.ForeignKey('GenericConfig', models.DO_NOTHING, blank=True, null=True)
    federal_tax_id = models.CharField(max_length=20, blank=True, null=True)
    activation_date = models.DateField(blank=True, null=True)
    punchin_integration = models.CharField(max_length=2)
    fiscal_rollover_start = models.DateField(blank=True, null=True)
    default_tax_rate = models.DecimalField(max_digits=30, decimal_places=10, blank=True, null=True)
    agency_billing_code = models.CharField(max_length=100, blank=True, null=True)
    lvp_session_restricted = models.NullBooleanField()
    sales_tax_handler_name = models.CharField(max_length=100, blank=True, null=True)
    expire_lists = models.FloatField(blank=True, null=True)
    list_days_to_live = models.FloatField(blank=True, null=True)
    list_expiration_date = models.DateField(blank=True, null=True)
    express_page = models.TextField(blank=True, null=True)
    segment_count = models.FloatField(blank=True, null=True)
    program = models.CharField(max_length=80, blank=True, null=True)
    testing = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buying_organization'
	app_label = 'mktplc'

class Category(models.Model):
    category_id = models.FloatField(primary_key=True)
    category_name = models.CharField(max_length=150)
    category_status = models.CharField(max_length=2)
    ui_short_name = models.CharField(max_length=100, blank=True, null=True)
    browsable = models.FloatField()
    top_category = models.FloatField()
    shelf_category = models.FloatField()
    item_count = models.FloatField(blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    supplier_equote_count = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'
	app_label = 'mktplc'

class CategoryMetaAttributes(models.Model):
    meta_attrb = models.ForeignKey('MetaAttribute', models.DO_NOTHING)
    product_category = models.ForeignKey('ProductCategory', models.DO_NOTHING)
    attribute_default_value = models.CharField(max_length=60, blank=True, null=True)
    attribute_default_unit = models.CharField(max_length=20, blank=True, null=True)
    visual_priority = models.FloatField(blank=True, null=True)
    section = models.ForeignKey('SpecificationSection', models.DO_NOTHING, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    category = models.ForeignKey(Category, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category_meta_attributes'
        unique_together = (('meta_attrb', 'product_category'),)
	app_label = 'mktplc'

class CategoryPath(models.Model):
    category_id = models.FloatField(unique=True)
    category_path = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category_path'
	app_label = 'mktplc'

class CategoryPromotion(models.Model):
    promotion = models.ForeignKey('Promotion', models.DO_NOTHING)
    promotion_type = models.CharField(max_length=2)
    position_no = models.IntegerField()
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    category = models.ForeignKey(Category, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'category_promotion'
        unique_together = (('category', 'position_no', 'promotion_type'),)
	app_label = 'mktplc'

class CategoryTree(models.Model):
    parent_category = models.ForeignKey(Category, related_name='parent_category')
    child_category = models.ForeignKey(Category, related_name='child_category')
    visual_priority = models.FloatField(blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    letter_code = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'category_tree'
        unique_together = (('parent_category', 'child_category'),)
	app_label = 'mktplc'
	
class CitySalesTaxArea(models.Model):
    city_sales_tax_area_id = models.FloatField(primary_key=True)
    city_name = models.CharField(max_length=100, blank=True, null=True)
    county_name = models.CharField(max_length=100, blank=True, null=True)
    state_abbreviated_name = models.CharField(max_length=5, blank=True, null=True)
    tax_area_status = models.CharField(max_length=5, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    city_alias = models.CharField(max_length=100, blank=True, null=True)
    franchise_tax_board_city_name = models.CharField(max_length=100, blank=True, null=True)
    zip = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'city_sales_tax_area'
	app_label = 'mktplc'

class CitySalesTaxRate(models.Model):
    city_sales_tax_rate_id = models.FloatField(primary_key=True)
    city_sales_tax_area = models.ForeignKey(CitySalesTaxArea, models.DO_NOTHING, blank=True, null=True)
    total_tax_rate = models.FloatField(blank=True, null=True)
    effective_date = models.DateField(blank=True, null=True)
    ending_date = models.DateField(blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'city_sales_tax_rate'
	app_label = 'mktplc'

class CleanupSupplierCategory(models.Model):
    supplier_id = models.FloatField()
    category_id = models.FloatField()
    accepts_equotes = models.FloatField(blank=True, null=True)
    accepts_ebids = models.FloatField(blank=True, null=True)
    category_path = models.CharField(max_length=40, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cleanup_supplier_category'
	app_label = 'mktplc'

class CodeTable(models.Model):
    code_type = models.CharField(max_length=20, blank=True, null=True)
    code_value = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    code_group_1 = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'code_table'
	app_label = 'mktplc'

class Contact(models.Model):
    contact_id = models.FloatField(primary_key=True)
    contact_title = models.CharField(max_length=32, blank=True, null=True)
    contact_first_name = models.CharField(max_length=40, blank=True, null=True)
    contact_middle_name = models.CharField(max_length=40, blank=True, null=True)
    contact_last_name = models.CharField(max_length=40, blank=True, null=True)
    contact_suffix = models.CharField(max_length=20, blank=True, null=True)
    contact_job_title = models.CharField(max_length=40, blank=True, null=True)
    contact_org_name = models.CharField(max_length=80, blank=True, null=True)
    contact_street_line1 = models.CharField(max_length=60, blank=True, null=True)
    contact_street_line2 = models.CharField(max_length=60, blank=True, null=True)
    contact_city = models.CharField(max_length=30, blank=True, null=True)
    contact_state = models.CharField(max_length=400, blank=True, null=True)
    contact_zip = models.CharField(max_length=20, blank=True, null=True)
    contact_country = models.CharField(max_length=20, blank=True, null=True)
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    contact_fax = models.CharField(max_length=20, blank=True, null=True)
    contact_email = models.CharField(max_length=80, blank=True, null=True)
    contact_url = models.CharField(max_length=400, blank=True, null=True)
    contact_assistant_email = models.CharField(max_length=80, blank=True, null=True)
    contact_notes = models.CharField(max_length=4000, blank=True, null=True)
    contact_location = models.CharField(max_length=400, blank=True, null=True)
    contact_mail_stop = models.CharField(max_length=80, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    contact_status = models.CharField(max_length=2)
    county = models.CharField(max_length=30, blank=True, null=True)
    contact_timezone = models.ForeignKey('Timezone', models.DO_NOTHING)
    site_location_type = models.CharField(max_length=40, blank=True, null=True)
    elevator_access_type = models.CharField(max_length=40, blank=True, null=True)
    external_id = models.CharField(max_length=24, blank=True, null=True)
    version = models.FloatField(blank=True, null=True)
    city_sales_tax_area = models.ForeignKey(CitySalesTaxArea, models.DO_NOTHING, blank=True, null=True)
    twitter = models.CharField(max_length=80, blank=True, null=True)
    facebook = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contact'
	app_label = 'mktplc'

class Contract(models.Model):
    contract_spplr_offer = models.OneToOneField('SupplierOffer')
    disctd_spplr_ctlg_offer = models.ForeignKey('SupplierOffer', related_name='disctd_spplr_ctlg_offer' , db_column='disctd_spplr_ctlg_offer', blank=True, null=True)
    coop_contract = models.FloatField()
    discount_percentage = models.FloatField(blank=True, null=True)
    legacy_vendor_no = models.CharField(max_length=20, blank=True, null=True)
    scndry_buyer_contact = models.ForeignKey(Contact, related_name='scndry_buyer_contact'  , blank=True, null=True)
    scndry_spplr_contact = models.ForeignKey(Contact, related_name='scndry_spplr_contact'  , blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    bundle = models.FloatField()
    title = models.CharField(max_length=400, blank=True, null=True)
    subtitle = models.CharField(max_length=400, blank=True, null=True)
    last_update_date = models.DateField(blank=True, null=True)
    distribution = models.CharField(max_length=2000, blank=True, null=True)
    terms_of_payment = models.CharField(max_length=2000, blank=True, null=True)
    fob = models.FloatField(blank=True, null=True)
    fob_destination = models.CharField(max_length=2000, blank=True, null=True)
    minimum_order = models.CharField(max_length=2000, blank=True, null=True)
    scope_of_contract = models.CharField(max_length=2000, blank=True, null=True)
    delivery = models.CharField(max_length=2000, blank=True, null=True)
    assignment_of_payment = models.CharField(max_length=2000, blank=True, null=True)
    taxes = models.CharField(max_length=2000, blank=True, null=True)
    abnormal_quantities = models.CharField(max_length=2000, blank=True, null=True)
    placement_of_orders = models.CharField(max_length=2000, blank=True, null=True)
    order_confirmation = models.CharField(max_length=2000, blank=True, null=True)
    invoicing_requirement = models.CharField(max_length=2000, blank=True, null=True)
    awardee_commodity_code = models.CharField(max_length=400, blank=True, null=True)
    contract_group = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contract'
	app_label = 'mktplc'

class ContractChanges(models.Model):
    supplier_offer_id = models.FloatField(blank=True, null=True)
    change_type = models.CharField(max_length=20, blank=True, null=True)
    change_date = models.DateField(blank=True, null=True)
    change_done = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contract_changes'
	app_label = 'mktplc'

class Cooperative(models.Model):
    coop_buying_org = models.OneToOneField(BuyingOrganization)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cooperative'
	app_label = 'mktplc'


class CreditCard(models.Model):
    credit_card_id = models.FloatField(primary_key=True)
    user = models.ForeignKey('EpylonUser', models.DO_NOTHING)
    credit_card_status = models.CharField(max_length=2)
    procurement_card = models.FloatField(blank=True, null=True)
    credit_card_type = models.CharField(max_length=2)
    credit_card_number = models.CharField(max_length=50)
    bank_name = models.CharField(max_length=60, blank=True, null=True)
    credit_card_usage_type = models.CharField(max_length=2, blank=True, null=True)
    cardholder_name = models.CharField(max_length=80, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    avs_street = models.CharField(max_length=200, blank=True, null=True)
    avs_zip = models.CharField(max_length=9, blank=True, null=True)
    obscured_card_number = models.CharField(max_length=20, blank=True, null=True)
    allow_external_export_flag = models.FloatField(blank=True, null=True)
    credit_card_exp_month = models.CharField(max_length=30, blank=True, null=True)
    credit_card_exp_year = models.CharField(max_length=30, blank=True, null=True)
    routing_number = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'credit_card'
	app_label = 'mktplc'

class CreditCardRefund(models.Model):
    credit_card_refund_id = models.FloatField(primary_key=True)
    refund_transaction_id = models.FloatField(blank=True, null=True)
    sale_transaction_id = models.FloatField(blank=True, null=True)
    amount = models.DecimalField(max_digits=22, decimal_places=2)
    owner_id = models.FloatField(blank=True, null=True)
    owner_type = models.CharField(max_length=2, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'credit_card_refund'
	app_label = 'mktplc'

class CreditCardTransaction(models.Model):
    credit_card_transaction_id = models.FloatField(primary_key=True)
    purchase_order_form_id = models.FloatField(blank=True, null=True)
    entire_paramlist = models.CharField(max_length=2000)
    entire_response = models.CharField(max_length=4000)
    pnref = models.CharField(max_length=12)
    trxtype = models.CharField(max_length=1)
    authcode = models.CharField(max_length=18, blank=True, null=True)
    result = models.CharField(max_length=25)
    respmsg = models.CharField(max_length=500, blank=True, null=True)
    transaction_amount = models.FloatField(blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    purchase_order_invoice_id = models.FloatField(blank=True, null=True)
    manual_adjustment_id = models.FloatField(blank=True, null=True)
    void = models.FloatField(blank=True, null=True)
    note = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'credit_card_transaction'
	app_label = 'mktplc'

class Customization(models.Model):
    cust_id = models.FloatField(primary_key=True)
    cust_type = models.CharField(max_length=10)
    selector_type = models.CharField(max_length=10)
    selector_id = models.FloatField()
    cust_class = models.CharField(max_length=100)
    configuration = models.CharField(max_length=4000, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customization'
	app_label = 'mktplc'

class DirectPurchase(models.Model):
    direct_purchase_form = models.OneToOneField('PurchaseForm')
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'direct_purchase'
	app_label = 'mktplc'

class DistrictSpendingLimits(models.Model):
    school_dist_buying_org = models.OneToOneField('SchoolDistrict')
    spndng_limit_period_type = models.CharField(max_length=20)
    spending_limit_amount = models.DecimalField(max_digits=22, decimal_places=2, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'district_spending_limits'
	app_label = 'mktplc'

class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=510, blank=True, null=True)
    name = models.CharField(max_length=510, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
	app_label = 'mktplc'

class DrKenTempIdxI(models.Model):
    token_text = models.CharField(max_length=64)
    token_type = models.IntegerField()
    token_first = models.IntegerField()
    token_last = models.IntegerField()
    token_count = models.IntegerField()
    token_info = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dr$ken_temp_idx$i'
	app_label = 'mktplc'

class DrKenTempIdxK(models.Model):
    docid = models.BigIntegerField(blank=True, null=True)
    textkey = models.TextField(primary_key=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'dr$ken_temp_idx$k'
	app_label = 'mktplc'

class DrKenTempIdxN(models.Model):
    nlt_docid = models.BigIntegerField(primary_key=True)
    nlt_mark = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'dr$ken_temp_idx$n'
	app_label = 'mktplc'
	
class DrKenTempIdxR(models.Model):
    row_no = models.IntegerField(blank=True, null=True)
    data = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dr$ken_temp_idx$r'
	app_label = 'mktplc'

class DrSearchImIdxI(models.Model):
    token_text = models.CharField(max_length=64)
    token_type = models.IntegerField()
    token_first = models.IntegerField()
    token_last = models.IntegerField()
    token_count = models.IntegerField()
    token_info = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dr$search_im_idx$i'
	app_label = 'mktplc'

class DrSearchImIdxK(models.Model):
    docid = models.BigIntegerField(blank=True, null=True)
    textkey = models.TextField(primary_key=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'dr$search_im_idx$k'
	app_label = 'mktplc'

class DrSearchImIdxN(models.Model):
    nlt_docid = models.BigIntegerField(primary_key=True)
    nlt_mark = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'dr$search_im_idx$n'
	app_label = 'mktplc'

class DrSearchImIdxR(models.Model):
    row_no = models.IntegerField(blank=True, null=True)
    data = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dr$search_im_idx$r'
	app_label = 'mktplc'

class DrSearchableItemCtx01I(models.Model):
    token_text = models.CharField(max_length=64)
    token_type = models.IntegerField()
    token_first = models.IntegerField()
    token_last = models.IntegerField()
    token_count = models.IntegerField()
    token_info = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dr$searchable_item_ctx_01$i'
	app_label = 'mktplc'

class DrSearchableItemCtx01K(models.Model):
    docid = models.BigIntegerField(blank=True, null=True)
    textkey = models.TextField(primary_key=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'dr$searchable_item_ctx_01$k'
	app_label = 'mktplc'

class DrSearchableItemCtx01N(models.Model):
    nlt_docid = models.BigIntegerField(primary_key=True)
    nlt_mark = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'dr$searchable_item_ctx_01$n'
	app_label = 'mktplc'

class DrSearchableItemCtx01R(models.Model):
    row_no = models.IntegerField(blank=True, null=True)
    data = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dr$searchable_item_ctx_01$r'
	app_label = 'mktplc'

class EbidTcLibrary(models.Model):
    ebid_tc_library_id = models.FloatField(primary_key=True)
    file_attachment = models.ForeignKey('FileAttachment', models.DO_NOTHING, blank=True, null=True)
    buying_organization = models.ForeignKey(BuyingOrganization, models.DO_NOTHING, blank=True, null=True)
    buyer_request = models.ForeignKey(BuyerRequest, models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=400, blank=True, null=True)
    sort_order = models.FloatField(blank=True, null=True)
    text = models.CharField(max_length=2500, blank=True, null=True)
    created_by_user = models.ForeignKey('EpylonUser', models.DO_NOTHING, blank=True, null=True)
    status = models.CharField(max_length=2, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ebid_tc_library'
	app_label = 'mktplc'

class EmailNotice(models.Model):
    email_notice_id = models.FloatField(primary_key=True)
    email_destination = models.CharField(max_length=80, blank=True, null=True)
    email_source = models.CharField(max_length=80, blank=True, null=True)
    email_body = models.CharField(max_length=4000, blank=True, null=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    email_footer = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=3, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    email_appln = models.CharField(max_length=2, blank=True, null=True)
    email_appln_id = models.FloatField(blank=True, null=True)
    email_body_clob = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_notice'
	app_label = 'mktplc'

class EpylonSupplierCtgryMap(models.Model):
    supplier_prdt_ctgry = models.ForeignKey('SpplrPrdtCtgry', models.DO_NOTHING)
    product_category = models.ForeignKey('ProductCategory', models.DO_NOTHING)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'epylon_supplier_ctgry_map'
        unique_together = (('supplier_prdt_ctgry', 'product_category'),)
	app_label = 'mktplc'


class EpylonUser(models.Model):
    user_id = models.FloatField(primary_key=True)
    user_role = models.ForeignKey('UserRole', models.DO_NOTHING)
    user_status = models.CharField(max_length=2, blank=True, null=True)
    user_type = models.CharField(max_length=2, blank=True, null=True)
    supplier = models.ForeignKey('SupplierOrganization', models.DO_NOTHING, blank=True, null=True)
    buying_organization = models.ForeignKey(BuyingOrganization, models.DO_NOTHING, blank=True, null=True)
    administrative_group = models.ForeignKey(AdministrativeGroup, models.DO_NOTHING, blank=True, null=True)
    user_contact = models.ForeignKey(Contact, models.DO_NOTHING)
    date_created = models.DateField(blank=True, null=True)
    date_last_login = models.DateField(blank=True, null=True)
    date_password_changed = models.DateField(blank=True, null=True)
    user_name = models.CharField(unique=True, max_length=80, blank=True, null=True)
    user_password = models.CharField(max_length=36, blank=True, null=True)
    password_hint = models.CharField(max_length=50, blank=True, null=True)
    email_requested = models.FloatField(blank=True, null=True)
    fax_requested = models.FloatField(blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    external_map_code = models.CharField(max_length=20, blank=True, null=True)
    change_password = models.FloatField(blank=True, null=True)
    view_accounting_codes = models.FloatField()
    po_limit = models.FloatField(blank=True, null=True)
    approvers_defined = models.FloatField(blank=True, null=True)
    department_name = models.CharField(max_length=100, blank=True, null=True)
    authorization_code = models.CharField(max_length=15, blank=True, null=True)
    supervisor_first_name = models.CharField(max_length=40, blank=True, null=True)
    supervisor_last_name = models.CharField(max_length=40, blank=True, null=True)
    supervisor_title = models.CharField(max_length=40, blank=True, null=True)
    supervisor_phone = models.CharField(max_length=20, blank=True, null=True)
    supervisor_email = models.CharField(max_length=80, blank=True, null=True)
    registration_request_billto = models.ForeignKey(Contact, related_name='registration_request_billto' , db_column='registration_request_billto', blank=True, null=True)
    registration_request_shipto = models.ForeignKey(Contact, related_name='registration_request_shipto' , db_column='registration_request_shipto', blank=True, null=True)
    billing_code = models.CharField(max_length=5, blank=True, null=True)
    registration_req_org_name = models.CharField(max_length=100, blank=True, null=True)
    login_fail_time = models.BigIntegerField(blank=True, null=True)
    login_fail_count = models.FloatField(blank=True, null=True)
    user_status_reason = models.CharField(max_length=2, blank=True, null=True)
    accepted = models.FloatField(blank=True, null=True)
    accepted_time = models.DateField(blank=True, null=True)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)
    program = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'epylon_user'
	app_label = 'mktplc'


class Events(models.Model):
    event_id = models.FloatField(primary_key=True)
    event_name = models.CharField(max_length=160)
    event_begin_date = models.DateField()
    event_end_date = models.DateField()
    begin_display_date = models.DateField(blank=True, null=True)
    end_display_date = models.DateField(blank=True, null=True)
    event_description = models.CharField(max_length=2000)
    event_location = models.CharField(max_length=4000)
    event_url = models.CharField(max_length=400)
    visual_priority = models.FloatField()
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'events'
	app_label = 'mktplc'


class FaxNotice(models.Model):
    fax_notice_id = models.FloatField(primary_key=True)
    fax_destination = models.CharField(max_length=40, blank=True, null=True)
    fax_source = models.CharField(max_length=40, blank=True, null=True)
    fax_body = models.CharField(max_length=2000, blank=True, null=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    fax_footer = models.CharField(max_length=2000, blank=True, null=True)
    status = models.CharField(max_length=3, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    fax_appln = models.CharField(max_length=2, blank=True, null=True)
    fax_appln_id = models.FloatField(blank=True, null=True)
    fax_body_clob = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fax_notice'
	app_label = 'mktplc'

class FederalGovernmentInfo(models.Model):
    initial_interest = models.ForeignKey('SupplierRegResponses', models.DO_NOTHING)
    business_type = models.CharField(max_length=2)
    certification_number = models.CharField(max_length=40, blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'federal_government_info'
        unique_together = (('initial_interest', 'business_type'),)
	app_label = 'mktplc'

class Fee(models.Model):
    fee_id = models.FloatField(primary_key=True)
    owner_id = models.FloatField(blank=True, null=True)
    owner_type = models.CharField(max_length=2, blank=True, null=True)
    charge_amount = models.DecimalField(max_digits=22, decimal_places=2)
    charge_event = models.CharField(max_length=25, blank=True, null=True)
    charge_per = models.CharField(max_length=25, blank=True, null=True)
    charge_description = models.CharField(max_length=2000, blank=True, null=True)
    charge_credit_card = models.FloatField(blank=True, null=True)
    charge_ach = models.FloatField(blank=True, null=True)
    charge_attachment = models.FloatField(blank=True, null=True)
    charge_upon_open = models.FloatField(blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fee'
	app_label = 'mktplc'

class FileAttachment(models.Model):
    file_attachment_id = models.FloatField(primary_key=True)
    file_sequence_no = models.FloatField(blank=True, null=True)
    user_type = models.CharField(max_length=2, blank=True, null=True)
    file_path_name = models.CharField(max_length=200, blank=True, null=True)
    url = models.CharField(max_length=80, blank=True, null=True)
    buyer_request_id = models.FloatField(blank=True, null=True)
    purchase_form_id = models.FloatField(blank=True, null=True)
    file_content = models.BinaryField(blank=True, null=True)
    supplier_offer_id = models.FloatField(blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    product_line_response_id = models.FloatField(blank=True, null=True)
    answer_id = models.FloatField(blank=True, null=True)
    type = models.CharField(max_length=4, blank=True, null=True)
    product_line_request_id = models.FloatField(blank=True, null=True)
    batch_processing_id = models.FloatField(blank=True, null=True)
    payment_id = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'file_attachment'
	app_label = 'mktplc'


class FixupInvoiceDate(models.Model):
    purchase_order_invoice_id = models.FloatField(blank=True, null=True)
    cxml_date = models.DateField(blank=True, null=True)
    invoice_date = models.DateField(blank=True, null=True)
    deferred_process_time = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fixup_invoice_date'
	app_label = 'mktplc'


class Folder(models.Model):
    folder_id = models.FloatField(primary_key=True)
    name = models.CharField(max_length=80, blank=True, null=True)
    owner_id = models.FloatField()
    folder_type = models.CharField(max_length=2)
    sequence = models.FloatField(blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'folder'
	app_label = 'mktplc'


class Function(models.Model):
    user_function_id = models.FloatField(primary_key=True)
    user_function_code = models.CharField(max_length=8, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'function'
	app_label = 'mktplc'


class FunctionRole(models.Model):
    user_role = models.ForeignKey('UserRole', models.DO_NOTHING)
    user_function = models.ForeignKey(Function, models.DO_NOTHING)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'function_role'
        unique_together = (('user_role', 'user_function'),)
	app_label = 'mktplc'


class GenericConfig(models.Model):
    generic_config_id = models.FloatField(primary_key=True)
    generic_config_title = models.CharField(max_length=60, blank=True, null=True)
    generic_config_type = models.CharField(max_length=2, blank=True, null=True)
    generic_config_data = models.CharField(max_length=4000, blank=True, null=True)
    parent_config = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'generic_config'
	app_label = 'mktplc'

class InitialInterest(models.Model):
    initial_interest_id = models.FloatField(primary_key=True)
    contact = models.ForeignKey(Contact, models.DO_NOTHING)
    interest_type = models.CharField(max_length=4, blank=True, null=True)
    district_name = models.CharField(max_length=40, blank=True, null=True)
    institution_name = models.CharField(max_length=80, blank=True, null=True)
    school_name = models.CharField(max_length=40, blank=True, null=True)
    school_department_name = models.CharField(max_length=60, blank=True, null=True)
    refered_by = models.CharField(max_length=100, blank=True, null=True)
    interest_status = models.CharField(max_length=2, blank=True, null=True)
    business_type = models.CharField(max_length=2, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    registration_date = models.DateField(blank=True, null=True)
    tcversion = models.CharField(max_length=40, blank=True, null=True)
    archived_date = models.DateField(blank=True, null=True)
    nc_hub = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'initial_interest'
	app_label = 'mktplc'

class InitialInterestAnswers(models.Model):
    initial_intrst_ans_id = models.FloatField()
    initial_intrst_qstn = models.ForeignKey('InitialInterestQstn', models.DO_NOTHING)
    answer = models.CharField(max_length=800, blank=True, null=True)
    text_input = models.FloatField(blank=True, null=True)
    visual_priority = models.FloatField(blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'initial_interest_answers'
        unique_together = (('initial_intrst_ans_id', 'initial_intrst_qstn'),)
	app_label = 'mktplc'


class InitialInterestCtgry(models.Model):
    initial_interest = models.ForeignKey(InitialInterest, models.DO_NOTHING)
    product_category = models.ForeignKey(Category, models.DO_NOTHING)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'initial_interest_ctgry'
        unique_together = (('initial_interest', 'product_category'),)
	app_label = 'mktplc'


class InitialInterestQstn(models.Model):
    initial_intrst_qstn_id = models.FloatField(primary_key=True)
    question = models.CharField(max_length=200, blank=True, null=True)
    required = models.FloatField(blank=True, null=True)
    type = models.CharField(max_length=2, blank=True, null=True)
    visual_priority = models.FloatField(blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'initial_interest_qstn'
	app_label = 'mktplc'


class InitialInterestRspns(models.Model):
    initial_interest_rspns = models.FloatField(primary_key=True)
    initial_interest = models.ForeignKey(InitialInterest, models.DO_NOTHING)
    initial_intrst_ans = models.ForeignKey(InitialInterestAnswers, models.DO_NOTHING, blank=True, null=True)
    initial_intrst_qstn = models.ForeignKey(InitialInterestQstn, models.DO_NOTHING, blank=True, null=True)
    response = models.CharField(max_length=800, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'initial_interest_rspns'
	app_label = 'mktplc'


class InterfaceDocArchive(models.Model):
    interface_doc_archive_id = models.FloatField(primary_key=True)
    interface_request_document = models.TextField(blank=True, null=True)
    interface_response_document = models.TextField(blank=True, null=True)
    external_doc_id = models.CharField(unique=True, max_length=1000)
    document_status = models.CharField(max_length=40, blank=True, null=True)
    document_type = models.CharField(max_length=40, blank=True, null=True)
    remote_hostname = models.CharField(max_length=200, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    local_reference_id = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'interface_doc_archive'
	app_label = 'mktplc'


class InvExceptionPodInfo(models.Model):
    external_invoice_id = models.CharField(max_length=40, blank=True, null=True)
    order_research_note = models.CharField(max_length=400, blank=True, null=True)
    pod_available = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inv_exception_pod_info'
	app_label = 'mktplc'


class InviteSupplier(models.Model):
    invite_supplier_id = models.FloatField(primary_key=True)
    issuer_user = models.ForeignKey(EpylonUser, models.DO_NOTHING)
    supplier_company_name = models.CharField(max_length=60, blank=True, null=True)
    supplier_contact_name = models.CharField(max_length=60, blank=True, null=True)
    supplier_contact_phone = models.CharField(max_length=20, blank=True, null=True)
    supplier_contact_fax = models.CharField(max_length=20, blank=True, null=True)
    supplier_contact_email = models.CharField(max_length=80, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invite_supplier'
	app_label = 'mktplc'


class ItemAccountingCodes(models.Model):
    purchase_item = models.ForeignKey('PurchaseItem', models.DO_NOTHING)
    allocation_amount = models.DecimalField(max_digits=22, decimal_places=2, blank=True, null=True)
    legacy_accounting_code = models.CharField(max_length=60)
    account_code_no = models.FloatField()
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_accounting_codes'
        unique_together = (('purchase_item', 'account_code_no'),)
	app_label = 'mktplc'


class KenAaa(models.Model):
    user_id = models.FloatField(blank=True, null=True)
    supplier = models.CharField(max_length=80, blank=True, null=True)
    spend_2008 = models.FloatField(blank=True, null=True)
    spend_2015 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ken_aaa'
	app_label = 'mktplc'


class KenBbb(models.Model):
    user_id = models.FloatField(blank=True, null=True)
    supplier = models.CharField(max_length=80, blank=True, null=True)
    spend_2008 = models.FloatField(blank=True, null=True)
    spend_2015 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ken_bbb'
	app_label = 'mktplc'


class KenCcc(models.Model):
    user_id = models.FloatField(blank=True, null=True)
    supplier_2008 = models.CharField(max_length=4000, blank=True, null=True)
    supplier_2015 = models.CharField(max_length=4000, blank=True, null=True)
    spend_2008 = models.FloatField(blank=True, null=True)
    spend_2015 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ken_ccc'
	app_label = 'mktplc'


class KenEbidProgram(models.Model):
    buyer_request_id = models.FloatField(blank=True, null=True)
    program = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ken_ebid_program'
	app_label = 'mktplc'


class KenRcPo(models.Model):
    po_id = models.FloatField()
    inv_id = models.FloatField(blank=True, null=True)
    od_inv_id = models.CharField(max_length=100, blank=True, null=True)
    invoice_status = models.CharField(max_length=30, blank=True, null=True)
    invoice_type = models.CharField(max_length=20, blank=True, null=True)
    reconcile_type = models.CharField(max_length=20, blank=True, null=True)
    inv_amount = models.FloatField(blank=True, null=True)
    po_amount = models.DecimalField(max_digits=22, decimal_places=2, blank=True, null=True)
    inv_count = models.FloatField(blank=True, null=True)
    charged_amount = models.FloatField(blank=True, null=True)
    return_amount = models.FloatField(blank=True, null=True)
    unknown_amount = models.FloatField(blank=True, null=True)
    net_amount = models.FloatField(blank=True, null=True)
    rc_count = models.FloatField(blank=True, null=True)
    invoice_date = models.DateField(blank=True, null=True)
    reconciled_date = models.DateField(blank=True, null=True)
    po_date = models.DateField(blank=True, null=True)
    po_legacy = models.CharField(max_length=25, blank=True, null=True)
    od_legacy = models.CharField(max_length=40, blank=True, null=True)
    po_count = models.FloatField(blank=True, null=True)
    user_id = models.FloatField()
    supplier_name = models.CharField(max_length=80, blank=True, null=True)
    deliver_to = models.CharField(max_length=400, blank=True, null=True)
    street1 = models.CharField(max_length=80, blank=True, null=True)
    street2 = models.CharField(max_length=80, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    zip = models.CharField(max_length=20, blank=True, null=True)
    buying_org = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'ken_rc_po'
	app_label = 'mktplc'


class KenRcPoItems(models.Model):
    item_no = models.FloatField(blank=True, null=True)
    manufacturer_name = models.CharField(max_length=60, blank=True, null=True)
    manufacturer_sku = models.CharField(max_length=60, blank=True, null=True)
    price_origin_descriptor = models.CharField(max_length=20, blank=True, null=True)
    price_origin_type = models.CharField(max_length=2, blank=True, null=True)
    price_per_uom = models.DecimalField(max_digits=30, decimal_places=10, blank=True, null=True)
    price_uom = models.CharField(max_length=20, blank=True, null=True)
    product_description = models.CharField(max_length=400)
    product_name = models.CharField(max_length=80, blank=True, null=True)
    purchase_form_id = models.FloatField(blank=True, null=True)
    purchase_item_id = models.FloatField()
    purchase_item_type = models.CharField(max_length=2)
    quantity = models.FloatField()
    supplier_aux_sku = models.CharField(max_length=200, blank=True, null=True)
    supplier_id = models.FloatField(blank=True, null=True)
    supplier_name = models.CharField(max_length=80, blank=True, null=True)
    supplier_sku = models.CharField(max_length=60, blank=True, null=True)
    item_count = models.FloatField(blank=True, null=True)
    date_issued = models.DateField(blank=True, null=True)
    subtotal_price = models.DecimalField(max_digits=22, decimal_places=2, blank=True, null=True)
    shipping_cost = models.DecimalField(max_digits=22, decimal_places=2, blank=True, null=True)
    tax = models.DecimalField(max_digits=22, decimal_places=2, blank=True, null=True)
    credit_card_id = models.FloatField(blank=True, null=True)
    legacy_no = models.CharField(max_length=20, blank=True, null=True)
    unique_legacy_no = models.CharField(max_length=25, blank=True, null=True)
    ap_price = models.DecimalField(max_digits=30, decimal_places=10, blank=True, null=True)
    start_valid_date = models.DateField(blank=True, null=True)
    end_valid_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ken_rc_po_items'
	app_label = 'mktplc'


class KenSisProgram(models.Model):
    supplier_name = models.CharField(max_length=80, blank=True, null=True)
    program = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ken_sis_program'
	app_label = 'mktplc'


class KenTemp(models.Model):
    real_user = models.CharField(max_length=80, blank=True, null=True)
    ghosted_user = models.CharField(max_length=80, blank=True, null=True)
    cs_created = models.FloatField(blank=True, null=True)
    terms = models.CharField(max_length=400, blank=True, null=True)
    pam = models.FloatField(blank=True, null=True)
    carol = models.FloatField(blank=True, null=True)
    other = models.FloatField(blank=True, null=True)
    epylon = models.FloatField(blank=True, null=True)
    buyer_name = models.CharField(max_length=80, blank=True, null=True)
    buyer = models.CharField(max_length=80, blank=True, null=True)
    buyer_city = models.CharField(max_length=30, blank=True, null=True)
    buyer_state = models.CharField(max_length=20, blank=True, null=True)
    buyer_zip = models.CharField(max_length=20, blank=True, null=True)
    issue_date = models.DateField(blank=True, null=True)
    epylon_po_id = models.FloatField(blank=True, null=True)
    po_value = models.FloatField(blank=True, null=True)
    item_count = models.FloatField(blank=True, null=True)
    supplier = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ken_temp'
	app_label = 'mktplc'


class LargeVendorProgram(models.Model):
    large_vendor_program_id = models.FloatField(primary_key=True)
    supplier_organization = models.ForeignKey('SupplierOrganization', models.DO_NOTHING)
    program_code = models.CharField(max_length=20)
    program_name = models.CharField(max_length=80)
    login_url = models.CharField(max_length=1000, blank=True, null=True)
    logout_url = models.CharField(max_length=1000, blank=True, null=True)
    failed_login_url = models.CharField(max_length=1000, blank=True, null=True)
    buyer_landing_url = models.CharField(max_length=1000, blank=True, null=True)
    contracts_active_flag = models.CharField(max_length=5, blank=True, null=True)
    logo_url = models.CharField(max_length=1000, blank=True, null=True)
    http_host_name = models.CharField(max_length=200, blank=True, null=True)
    punchout_receiving_url = models.CharField(max_length=1000, blank=True, null=True)
    contract_number = models.CharField(max_length=100, blank=True, null=True)
    default_reg_buy_org = models.ForeignKey(BuyingOrganization, models.DO_NOTHING)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    acknowledgement_url = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'large_vendor_program'
	app_label = 'mktplc'


class LegacyPayloadStage(models.Model):
    local_reference_id = models.FloatField()
    payloadid = models.CharField(max_length=200, blank=True, null=True)
    legacyno = models.CharField(max_length=200, blank=True, null=True)
    orderdate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'legacy_payload_stage'
	app_label = 'mktplc'


class ManualAdjustment(models.Model):
    manual_adjustment_id = models.FloatField(primary_key=True)
    type = models.CharField(max_length=2, blank=True, null=True)
    status = models.CharField(max_length=2, blank=True, null=True)
    description = models.CharField(max_length=400, blank=True, null=True)
    purchase_order_id = models.FloatField(blank=True, null=True)
    purchase_order_invoice_id = models.FloatField(blank=True, null=True)
    amount = models.DecimalField(max_digits=22, decimal_places=2, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    user_id = models.FloatField(blank=True, null=True)
    payment_id = models.FloatField(blank=True, null=True)
    buyer_request_id = models.FloatField(blank=True, null=True)
    product_line_response_id = models.FloatField(blank=True, null=True)
    notification = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manual_adjustment'
	app_label = 'mktplc'


class ManualReconcile(models.Model):
    manual_reconcile_id = models.FloatField(primary_key=True)
    type = models.CharField(max_length=2, blank=True, null=True)
    status = models.CharField(max_length=2, blank=True, null=True)
    description = models.CharField(max_length=400, blank=True, null=True)
    invoice_id = models.FloatField(blank=True, null=True)
    purchase_order_id = models.FloatField(blank=True, null=True)
    override_uom = models.FloatField(blank=True, null=True)
    override_sku = models.FloatField(blank=True, null=True)
    override_price = models.FloatField(blank=True, null=True)
    override_overbill = models.FloatField(blank=True, null=True)
    override_overreturn = models.FloatField(blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    clear_credit_card_id = models.FloatField(blank=True, null=True)
    result = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manual_reconcile'
	app_label = 'mktplc'


class MetaAttrbConstraints(models.Model):
    meta_attrb = models.OneToOneField('MetaAttribute')
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meta_attrb_constraints'
	app_label = 'mktplc'


class MetaAttrbTranslator(models.Model):
    meta_attrb = models.OneToOneField('MetaAttribute')
    translator_procedure = models.CharField(max_length=20, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meta_attrb_translator'
	app_label = 'mktplc'


class MetaAttrbValidRange(models.Model):
    meta_attrb = models.OneToOneField('MetaAttribute')
    high_value = models.CharField(max_length=20, blank=True, null=True)
    low_value = models.CharField(max_length=20, blank=True, null=True)
    max_value = models.FloatField(blank=True, null=True)
    min_value = models.FloatField(blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meta_attrb_valid_range'
	app_label = 'mktplc'


class MetaAttrbValidValues(models.Model):
    meta_attrb = models.OneToOneField('MetaAttribute')
    valid_value = models.CharField(max_length=20, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meta_attrb_valid_values'
	app_label = 'mktplc'


class MetaAttrbValidator(models.Model):
    meta_attrb = models.OneToOneField('MetaAttribute')
    validator_procedure = models.CharField(max_length=20, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meta_attrb_validator'
	app_label = 'mktplc'


class MetaAttribute(models.Model):
    meta_attrb_id = models.FloatField(primary_key=True)
    attribute_name = models.CharField(unique=True, max_length=40)
    browsable = models.FloatField()
    attribute_type = models.CharField(max_length=2)
    searchable = models.FloatField()
    attribute_description = models.CharField(max_length=400, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meta_attribute'
	app_label = 'mktplc'


class MikeInvoiceExtract(models.Model):
    archive_id = models.FloatField(blank=True, null=True)
    req_payload_id = models.CharField(max_length=200, blank=True, null=True)
    order_payload_id = models.CharField(max_length=200, blank=True, null=True)
    order_id = models.CharField(max_length=200, blank=True, null=True)
    order_date = models.DateField(blank=True, null=True)
    supplier_order_id = models.CharField(max_length=200, blank=True, null=True)
    supplier_invoice_id = models.CharField(max_length=200, blank=True, null=True)
    invoice_date = models.DateField(blank=True, null=True)
    subtotal = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mike_invoice_extract'
	app_label = 'mktplc'


class MikeInvoiceReplay(models.Model):
    interface_doc_archive_id = models.FloatField(blank=True, null=True)
    interface_request_document = models.TextField(blank=True, null=True)
    interface_response_document = models.TextField(blank=True, null=True)
    external_doc_id = models.CharField(max_length=1000)
    document_status = models.CharField(max_length=40, blank=True, null=True)
    document_type = models.CharField(max_length=40, blank=True, null=True)
    remote_hostname = models.CharField(max_length=200, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    local_reference_id = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mike_invoice_replay'
 	app_label = 'mktplc'

class MikeOldInvoicesNov29(models.Model):
    interface_doc_archive_id = models.FloatField(blank=True, null=True)
    interface_request_document = models.TextField(blank=True, null=True)
    interface_response_document = models.TextField(blank=True, null=True)
    external_doc_id = models.CharField(max_length=1000)
    document_status = models.CharField(max_length=40, blank=True, null=True)
    document_type = models.CharField(max_length=40, blank=True, null=True)
    remote_hostname = models.CharField(max_length=200, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    local_reference_id = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mike_old_invoices_nov_29'
	app_label = 'mktplc'


class MikePoItemNoIssues(models.Model):
    purchase_form_id = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mike_po_item_no_issues'
	app_label = 'mktplc'


class OdActivePricing(models.Model):
    sku = models.CharField(max_length=60, blank=True, null=True)
    price = models.DecimalField(max_digits=30, decimal_places=10, blank=True, null=True)
    start_valid_date = models.DateField(blank=True, null=True)
    core = models.CharField(max_length=4, blank=True, null=True)
    end_valid_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'od_active_pricing'
	app_label = 'mktplc'


class OdInvoiceAudit(models.Model):
    od_invoice_number = models.CharField(unique=True, max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'od_invoice_audit'
	app_label = 'mktplc'


class OddgsSalesDump(models.Model):
    customer_no = models.CharField(max_length=40, blank=True, null=True)
    customer_name = models.CharField(max_length=100, blank=True, null=True)
    product_description = models.CharField(max_length=1000, blank=True, null=True)
    product_code = models.CharField(max_length=40, blank=True, null=True)
    wholesaler_product_code = models.CharField(max_length=40, blank=True, null=True)
    customer_product_code = models.CharField(max_length=40, blank=True, null=True)
    ship_date = models.DateField(blank=True, null=True)
    order_number = models.CharField(max_length=40, blank=True, null=True)
    order_date = models.DateField(blank=True, null=True)
    unit_of_measure = models.CharField(max_length=10, blank=True, null=True)
    quantity = models.FloatField(blank=True, null=True)
    unit_price = models.FloatField(blank=True, null=True)
    extended_price = models.FloatField(blank=True, null=True)
    currency = models.CharField(max_length=10, blank=True, null=True)
    reconcile_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oddgs_sales_dump'
	app_label = 'mktplc'


class OfferDistributorScope(models.Model):
    supplier_offer = models.ForeignKey('SupplierOffer', models.DO_NOTHING)
    supplier = models.ForeignKey('SupplierOrganization', models.DO_NOTHING)
    buying_group = models.ForeignKey(BuyingGroup, models.DO_NOTHING)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'offer_distributor_scope'
        unique_together = (('supplier_offer', 'buying_group', 'supplier'),)
	app_label = 'mktplc'


class OfficeSolutions(models.Model):
    description = models.CharField(max_length=200, blank=True, null=True)
    supplier_sku = models.CharField(max_length=100, blank=True, null=True)
    supplier_uom = models.CharField(max_length=20, blank=True, null=True)
    od_sku = models.CharField(max_length=100, blank=True, null=True)
    od_price = models.DecimalField(max_digits=24, decimal_places=2, blank=True, null=True)
    od_uom = models.CharField(max_length=20, blank=True, null=True)
    od_uom_units = models.CharField(max_length=20, blank=True, null=True)
    manufacturer_sku = models.CharField(max_length=100, blank=True, null=True)
    min_sup_price = models.FloatField(blank=True, null=True)
    max_sup_price = models.FloatField(blank=True, null=True)
    min_uom = models.CharField(max_length=20, blank=True, null=True)
    max_uom = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'office_solutions'
	app_label = 'mktplc'


class OfficeSolutionsTemp(models.Model):
    description = models.CharField(max_length=200, blank=True, null=True)
    supplier_sku = models.CharField(max_length=100, blank=True, null=True)
    supplier_uom = models.CharField(max_length=20, blank=True, null=True)
    supplier_price = models.DecimalField(max_digits=24, decimal_places=2, blank=True, null=True)
    od_sku = models.CharField(max_length=100, blank=True, null=True)
    od_price = models.DecimalField(max_digits=24, decimal_places=2, blank=True, null=True)
    od_uom = models.CharField(max_length=20, blank=True, null=True)
    od_uom_units = models.CharField(max_length=20, blank=True, null=True)
    manufacturer_sku = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'office_solutions_temp'
	app_label = 'mktplc'


class OnBehalfOf(models.Model):
    on_behalf_of_id = models.FloatField(primary_key=True)
    delegate_user_id = models.FloatField(blank=True, null=True)
    organization_id = models.FloatField(blank=True, null=True)
    organization_name = models.CharField(max_length=80, blank=True, null=True)
    user = models.ForeignKey(EpylonUser, models.DO_NOTHING, blank=True, null=True)
    user_name = models.CharField(max_length=80, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'on_behalf_of'
	app_label = 'mktplc'

class OnBehalfOfPrivilege(models.Model):
    on_behalf_of = models.ForeignKey(OnBehalfOf, models.DO_NOTHING)
    privilege = models.CharField(max_length=40)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'on_behalf_of_privilege'
        unique_together = (('on_behalf_of', 'privilege'),)
	app_label = 'mktplc'


class PartnerExtrinsics(models.Model):
    extrinsic_id = models.FloatField(primary_key=True)
    purchase_form = models.ForeignKey('PurchaseForm', models.DO_NOTHING, blank=True, null=True)
    extrinsic_name = models.CharField(max_length=4000, blank=True, null=True)
    extrinsic_value = models.CharField(max_length=4000, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'partner_extrinsics'
	app_label = 'mktplc'


class Party(models.Model):
    party_id = models.FloatField(primary_key=True)
    party_type = models.CharField(max_length=2)
    internal_party_id = models.FloatField()
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party'
	app_label = 'mktplc'


class PartyFunction(models.Model):
    party_function_id = models.FloatField(primary_key=True)
    application_function = models.ForeignKey(ApplicationFunction, models.DO_NOTHING)
    party = models.ForeignKey(Party, models.DO_NOTHING)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_function'
	app_label = 'mktplc'


class PayloadLookup(models.Model):
    payloadid = models.CharField(max_length=200, blank=True, null=True)
    legacyno = models.CharField(max_length=200, blank=True, null=True)
    orderdate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payload_lookup'
	app_label = 'mktplc'


class Payment(models.Model):
    payment_id = models.FloatField(primary_key=True)
    fee = models.ForeignKey(Fee, models.DO_NOTHING)
    owner_id = models.FloatField(blank=True, null=True)
    owner_type = models.CharField(max_length=2, blank=True, null=True)
    payment_type = models.CharField(max_length=4, blank=True, null=True)
    credit_card_id = models.FloatField(blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment'
	app_label = 'mktplc'


class PaymentCredential(models.Model):
    payment_credential_id = models.FloatField(primary_key=True)
    owner_id = models.FloatField(blank=True, null=True)
    owner_type = models.CharField(max_length=2, blank=True, null=True)
    gateway = models.CharField(max_length=50, blank=True, null=True)
    merchant_name = models.CharField(max_length=50, blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_credential'
	app_label = 'mktplc'


class PoInvoiceItem(models.Model):
    po_invoice_item_id = models.FloatField(primary_key=True)
    purchase_order_invoice = models.ForeignKey('PurchaseOrderInvoice', models.DO_NOTHING, blank=True, null=True)
    po_line_number = models.FloatField(blank=True, null=True)
    invoice_line_number = models.FloatField(blank=True, null=True)
    item_type = models.CharField(max_length=20, blank=True, null=True)
    quantity = models.FloatField(blank=True, null=True)
    price_uom = models.CharField(max_length=20, blank=True, null=True)
    price_per_uom = models.FloatField(blank=True, null=True)
    supplier_sku = models.CharField(max_length=60, blank=True, null=True)
    product_description = models.CharField(max_length=400, blank=True, null=True)
    unspsc_code = models.CharField(max_length=20, blank=True, null=True)
    discount_rate = models.FloatField(blank=True, null=True)
    extended_price = models.FloatField(blank=True, null=True)
    reconcile_status = models.CharField(max_length=20, blank=True, null=True)
    reconcile_note = models.CharField(max_length=1000, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'po_invoice_item'
	app_label = 'mktplc'


class PrchseOrderItem(models.Model):
    purchase_order_item = models.OneToOneField('PurchaseItem')
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prchse_order_item'
	app_label = 'mktplc'


class Product(models.Model):
    product_id = models.FloatField(primary_key=True)
    product_name = models.CharField(max_length=80, blank=True, null=True)
    product_status = models.CharField(max_length=2)
    manufacturer_name = models.CharField(max_length=60, blank=True, null=True)
    manufacturer_sku = models.CharField(max_length=60, blank=True, null=True)
    upc = models.CharField(max_length=60, blank=True, null=True)
    unspsc = models.CharField(max_length=60, blank=True, null=True)
    price_uom = models.CharField(max_length=20, blank=True, null=True)
    dimensions = models.CharField(max_length=20, blank=True, null=True)
    color = models.CharField(max_length=20, blank=True, null=True)
    weight = models.CharField(max_length=10, blank=True, null=True)
    weight_uom = models.CharField(max_length=20, blank=True, null=True)
    manufacturer_warranty = models.CharField(max_length=60, blank=True, null=True)
    prdt_shelf_ctgry = models.ForeignKey('ProductCategory', models.DO_NOTHING, blank=True, null=True)
    dimensions_uom = models.CharField(max_length=20, blank=True, null=True)
    manuf_sug_rtl_price = models.DecimalField(max_digits=22, decimal_places=2, blank=True, null=True)
    mtl_safety_data_sheet = models.CharField(max_length=200, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    shelf_category = models.ForeignKey(Category, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'
	app_label = 'mktplc'


class ProductCategory(models.Model):
    product_category_id = models.FloatField(primary_key=True)
    product_category_name = models.CharField(unique=True, max_length=100)
    ui_short_name = models.CharField(max_length=8, blank=True, null=True)
    short_description = models.CharField(max_length=400, blank=True, null=True)
    long_description = models.CharField(max_length=2000, blank=True, null=True)
    browsable = models.FloatField(blank=True, null=True)
    shelf_page = models.FloatField(blank=True, null=True)
    shelf_page_spnsr_prd_img = models.CharField(max_length=80, blank=True, null=True)
    leftnav_sponsor_image = models.CharField(max_length=80, blank=True, null=True)
    rightnav_sponsor_image1 = models.CharField(max_length=80, blank=True, null=True)
    rightnav_sponsor_image2 = models.CharField(max_length=80, blank=True, null=True)
    rightnav_sponsor_image3 = models.CharField(max_length=80, blank=True, null=True)
    prsntby_sponsor_image = models.CharField(max_length=80, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_category'
	app_label = 'mktplc'


class ProductCategoryTree(models.Model):
    parent_category = models.ForeignKey(ProductCategory, related_name='parent_category')
    child_category = models.ForeignKey(ProductCategory, related_name='child_category')
    letter_code = models.CharField(max_length=2, blank=True, null=True)
    visual_priority = models.FloatField(blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_category_tree'
        unique_together = (('parent_category', 'child_category'),)
	app_label = 'mktplc'


class ProductDetail(models.Model):
    product_detail_id = models.FloatField(primary_key=True)
    short_description = models.CharField(max_length=400, blank=True, null=True)
    long_description = models.CharField(max_length=2000, blank=True, null=True)
    thumbnail_image = models.CharField(max_length=200, blank=True, null=True)
    fullscale_image = models.CharField(max_length=200, blank=True, null=True)
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    parent_description = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_detail'
	app_label = 'mktplc'


class ProductLineRequestItem(models.Model):
    item_id = models.FloatField(primary_key=True)
    product_line = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=400, blank=True, null=True)
    owner_id = models.FloatField()
    owner_type = models.CharField(max_length=2)
    sequence = models.FloatField()
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    awarded_prodline_respitem = models.ForeignKey('ProductLineResponseItem', models.DO_NOTHING, blank=True, null=True)
    awardee_notification_status = models.FloatField(blank=True, null=True)
    award_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_line_request_item'
	app_label = 'mktplc'


class ProductLineResponseItem(models.Model):
    item_id = models.FloatField(primary_key=True)
    request_item = models.ForeignKey(ProductLineRequestItem, models.DO_NOTHING, blank=True, null=True)
    owner_id = models.FloatField()
    owner_type = models.CharField(max_length=2)
    type = models.CharField(max_length=2)
    sequence = models.FloatField()
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    all_sku_count = models.FloatField(blank=True, null=True)
    common_sku_count = models.FloatField(blank=True, null=True)
    all_sku_value = models.FloatField(blank=True, null=True)
    common_sku_value = models.FloatField(blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    percentage_from_low_bidder = models.FloatField(blank=True, null=True)
    analyzed = models.FloatField(blank=True, null=True)
    common_sku_score = models.FloatField(blank=True, null=True)
    product_score = models.FloatField(blank=True, null=True)
    current_product_score = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_line_response_item'
	app_label = 'mktplc'


class Promotion(models.Model):
    promotion_id = models.FloatField(primary_key=True)
    supplier = models.ForeignKey('SupplierOrganization', models.DO_NOTHING)
    promotion_type = models.CharField(max_length=2)
    date_issued = models.DateField(blank=True, null=True)
    date_expires = models.DateField(blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    promotion_title = models.CharField(max_length=60, blank=True, null=True)
    promotion_status = models.CharField(max_length=2, blank=True, null=True)
    promotion_text = models.CharField(max_length=400, blank=True, null=True)
    promotion_graphic = models.BinaryField(blank=True, null=True)
    top_shelf_graphic = models.BinaryField(blank=True, null=True)
    well_graphic = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'promotion'
	app_label = 'mktplc'

class PromotionElement(models.Model):
    container_promotion = models.ForeignKey(Promotion, related_name='container_promotion')
    promotion_element_no = models.FloatField(blank=True, null=True)
    promotion_element_type = models.CharField(max_length=2)
    graphic = models.BinaryField(blank=True, null=True)
    display_text = models.CharField(max_length=400, blank=True, null=True)
    supplier_item = models.ForeignKey('SupplierItem', models.DO_NOTHING, blank=True, null=True)
    url = models.CharField(max_length=80, blank=True, null=True)
    nested_promotion = models.ForeignKey(Promotion, related_name='nested_promotion' , blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    link_text = models.CharField(max_length=60, blank=True, null=True)
    promotion_element_id = models.FloatField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'promotion_element'
	app_label = 'mktplc'


class Publisher(models.Model):
    publisher_id = models.FloatField(primary_key=True)
    publisher_name = models.CharField(max_length=200)
    publisher_category = models.CharField(max_length=20, blank=True, null=True)
    logo = models.CharField(max_length=400)
    publisher_link = models.CharField(max_length=400, blank=True, null=True)
    archive_frequency = models.FloatField(blank=True, null=True)
    publisher_description = models.CharField(max_length=400)
    parent_publisher = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'publisher'
	app_label = 'mktplc'


class PunchinIntegration(models.Model):
    supplier = models.ForeignKey('SupplierOrganization', models.DO_NOTHING)
    integration_type = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'punchin_integration'
        unique_together = (('supplier', 'integration_type'),)
	app_label = 'mktplc'


class PunchoutSite(models.Model):
    punchout_supplier_offer = models.OneToOneField('SupplierOffer')
    url = models.CharField(max_length=80)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'punchout_site'
	app_label = 'mktplc'


class PurchaseForm(models.Model):
    purchase_form_id = models.FloatField(primary_key=True)
    purchase_form_type = models.CharField(max_length=2)
    supplier = models.ForeignKey('SupplierOrganization', models.DO_NOTHING, blank=True, null=True)
    purchase_form_status = models.CharField(max_length=2)
    structured = models.FloatField()
    unstructured_text = models.CharField(max_length=400, blank=True, null=True)
    separable = models.FloatField()
    substitution_allowed = models.FloatField()
    item_count = models.FloatField(blank=True, null=True)
    date_created = models.DateField()
    date_issued = models.DateField(blank=True, null=True)
    date_delivery_expected = models.DateField(blank=True, null=True)
    terms_and_conditions = models.CharField(max_length=400, blank=True, null=True)
    freight_on_board = models.CharField(max_length=20, blank=True, null=True)
    shipto_contact = models.ForeignKey(Contact, models.DO_NOTHING, blank=True, null=True)
    shipto_org_name = models.CharField(max_length=60, blank=True, null=True)
    shipto_contact_name = models.CharField(max_length=80, blank=True, null=True)
    shipto_addr_line1 = models.CharField(max_length=80, blank=True, null=True)
    shipto_addr_line2 = models.CharField(max_length=80, blank=True, null=True)
    shipto_city = models.CharField(max_length=30, blank=True, null=True)
    shipto_state = models.CharField(max_length=20, blank=True, null=True)
    shipto_zip = models.CharField(max_length=20, blank=True, null=True)
    shipto_notes = models.CharField(max_length=400, blank=True, null=True)
    shipping_method = models.CharField(max_length=20, blank=True, null=True)
    initiator_name = models.CharField(max_length=80)
    initiator_phone = models.CharField(max_length=20, blank=True, null=True)
    inttr_buying_org_name = models.CharField(max_length=80)
    accounting_method = models.CharField(max_length=3, blank=True, null=True)
    initiator_email = models.CharField(max_length=80, blank=True, null=True)
    user = models.ForeignKey(EpylonUser, models.DO_NOTHING)
    buying_organization = models.ForeignKey(BuyingOrganization, models.DO_NOTHING)
    legacy_no = models.CharField(max_length=20, blank=True, null=True)
    title = models.CharField(max_length=256, blank=True, null=True)
    subtotal_price = models.DecimalField(max_digits=22, decimal_places=2, blank=True, null=True)
    tax = models.DecimalField(max_digits=22, decimal_places=2, blank=True, null=True)
    shipping_cost = models.DecimalField(max_digits=22, decimal_places=2, blank=True, null=True)
    total_price = models.DecimalField(max_digits=22, decimal_places=2, blank=True, null=True)
    buyer_request = models.ForeignKey(BuyerRequest, related_name='buyer_request', blank=True, null=True)
    supplier_name = models.CharField(max_length=80, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    encumber_status = models.CharField(max_length=2, blank=True, null=True)
    outstandingpo = models.FloatField(blank=True, null=True)
    shipto_mail_stop = models.CharField(max_length=80, blank=True, null=True)
    fiscal_year = models.IntegerField(blank=True, null=True)
    ebid_buyer_request = models.ForeignKey(BuyerRequest, related_name='ebid_buyer_request' , blank=True, null=True)
    ereq_budget_check = models.NullBooleanField()
    billto_contact_id = models.FloatField(blank=True, null=True)
    billto_addr_line1 = models.CharField(max_length=80, blank=True, null=True)
    billto_addr_line2 = models.CharField(max_length=80, blank=True, null=True)
    billto_city = models.CharField(max_length=30, blank=True, null=True)
    billto_contact_name = models.CharField(max_length=80, blank=True, null=True)
    billto_state = models.CharField(max_length=20, blank=True, null=True)
    billto_zip = models.CharField(max_length=20, blank=True, null=True)
    billto_phone = models.CharField(max_length=20, blank=True, null=True)
    discount = models.DecimalField(max_digits=22, decimal_places=2, blank=True, null=True)
    schedule_time = models.DateField(blank=True, null=True)
    schedule_type = models.CharField(max_length=2, blank=True, null=True)
    schedule_param = models.FloatField(blank=True, null=True)
    schedule_limit = models.DateField(blank=True, null=True)
    schedule_parent_id = models.FloatField(blank=True, null=True)
    shipto_external_id = models.CharField(max_length=24, blank=True, null=True)
    billto_external_id = models.CharField(max_length=24, blank=True, null=True)
    agency_billing_code = models.CharField(max_length=5, blank=True, null=True)
    authorization_code = models.CharField(max_length=15, blank=True, null=True)
    scprs_code = models.CharField(max_length=14, blank=True, null=True)
    customer_service_created = models.FloatField(blank=True, null=True)
    shipto_sales_tax_area_id = models.FloatField(blank=True, null=True)
    payment_type = models.CharField(max_length=5, blank=True, null=True)
    customer_service_id = models.FloatField(blank=True, null=True)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)
    accounting_code_type = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'purchase_form'
	app_label = 'mktplc'


class PurchaseItem(models.Model):
    purchase_item_id = models.FloatField(primary_key=True)
    purchase_item_type = models.CharField(max_length=2)
    supplier = models.ForeignKey('SupplierOrganization', models.DO_NOTHING, blank=True, null=True)
    item_no = models.FloatField(blank=True, null=True)
    saved_list = models.ForeignKey('SavedList', models.DO_NOTHING, blank=True, null=True)
    product_description = models.CharField(max_length=400)
    manufacturer_sku = models.CharField(max_length=60, blank=True, null=True)
    supplier_sku = models.CharField(max_length=60, blank=True, null=True)
    quantity = models.FloatField()
    manufacturer_name = models.CharField(max_length=60, blank=True, null=True)
    product_name = models.CharField(max_length=80, blank=True, null=True)
    extended_price = models.DecimalField(max_digits=30, decimal_places=10, blank=True, null=True)
    price_origin_type = models.CharField(max_length=2, blank=True, null=True)
    supplier_terms = models.CharField(max_length=80, blank=True, null=True)
    item_specific_text = models.CharField(max_length=20, blank=True, null=True)
    supplier_name = models.CharField(max_length=80, blank=True, null=True)
    price_uom = models.CharField(max_length=20, blank=True, null=True)
    purchase_form = models.ForeignKey(PurchaseForm, models.DO_NOTHING, blank=True, null=True)
    price_per_uom = models.DecimalField(max_digits=30, decimal_places=10, blank=True, null=True)
    rfnce_spplr_item = models.ForeignKey('SupplierItem', models.DO_NOTHING, blank=True, null=True)
    product_detail = models.ForeignKey(ProductDetail, models.DO_NOTHING, blank=True, null=True)
    requested_item = models.ForeignKey('RequestedItem', models.DO_NOTHING, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    need_distributor = models.FloatField()
    price_origin_descriptor = models.CharField(max_length=20, blank=True, null=True)
    product_url = models.CharField(max_length=400, blank=True, null=True)
    supplier_aux_sku = models.CharField(max_length=200, blank=True, null=True)
    extrinsic_name = models.CharField(max_length=60, blank=True, null=True)
    extrinsic_value = models.CharField(max_length=4000, blank=True, null=True)
    discount = models.DecimalField(max_digits=22, decimal_places=2, blank=True, null=True)
    taxable = models.FloatField(blank=True, null=True)
    is_distributor = models.NullBooleanField()
    program = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'purchase_item'
	app_label = 'mktplc'


class PurchaseOrder(models.Model):
    purchase_order_form = models.OneToOneField(PurchaseForm)
    updated_delivery_date = models.DateField(blank=True, null=True)
    rqstn_prchs_form = models.ForeignKey(PurchaseForm, related_name='rqstn_prchs_form', blank=True, null=True)
    credit_card = models.ForeignKey(CreditCard, models.DO_NOTHING, blank=True, null=True)
    date_shipped = models.DateField(blank=True, null=True)
    legacy_no = models.CharField(max_length=20, blank=True, null=True)
    supplier_legacy_no = models.CharField(max_length=20, blank=True, null=True)
    supplier_user = models.ForeignKey(EpylonUser, models.DO_NOTHING, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    eorder_type = models.CharField(max_length=2, blank=True, null=True)
    account_number = models.CharField(max_length=20, blank=True, null=True)
    unique_legacy_no = models.CharField(unique=True, max_length=25, blank=True, null=True)
    notification_email = models.CharField(max_length=400, blank=True, null=True)
    use_unique_legacy_no = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'purchase_order'
	app_label = 'mktplc'


class PurchaseOrderInvoice(models.Model):
    purchase_order_invoice_id = models.FloatField(primary_key=True)
    purchase_form = models.ForeignKey(PurchaseForm, models.DO_NOTHING, blank=True, null=True)
    external_invoice_id = models.CharField(max_length=100, blank=True, null=True)
    external_order_id = models.CharField(max_length=100, blank=True, null=True)
    supplier_id = models.FloatField(blank=True, null=True)
    invoice_type = models.CharField(max_length=20, blank=True, null=True)
    invoice_date = models.DateField(blank=True, null=True)
    invoice_status = models.CharField(max_length=30, blank=True, null=True)
    subtotal_amount = models.FloatField(blank=True, null=True)
    gross_amount = models.FloatField(blank=True, null=True)
    net_amount = models.FloatField(blank=True, null=True)
    shipping_amount = models.FloatField(blank=True, null=True)
    special_handling_amount = models.FloatField(blank=True, null=True)
    discount_rate = models.FloatField(blank=True, null=True)
    tax_rate = models.FloatField(blank=True, null=True)
    sales_tax_area_id = models.FloatField(blank=True, null=True)
    adjusted_total_price = models.FloatField(blank=True, null=True)
    adjusted_subtotal_amount = models.FloatField(blank=True, null=True)
    adjusted_net_amount = models.FloatField(blank=True, null=True)
    adjusted_tax_amount = models.FloatField(blank=True, null=True)
    reconcile_note = models.CharField(max_length=1000, blank=True, null=True)
    deferred_process_time = models.DateField(blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    reconcile_type = models.CharField(max_length=20, blank=True, null=True)
    external_invoice_reference = models.CharField(max_length=50, blank=True, null=True)
    reconciled_date = models.DateField(blank=True, null=True)
    purchaser_notification_date = models.DateField(blank=True, null=True)
    purchaser_notification_type = models.CharField(max_length=20, blank=True, null=True)
    order_reference_id = models.CharField(max_length=40, blank=True, null=True)
    order_match_type = models.CharField(max_length=40, blank=True, null=True)
    order_document_reference_id = models.CharField(max_length=200, blank=True, null=True)
    fee_rate = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'purchase_order_invoice'
	app_label = 'mktplc'


class Question(models.Model):
    question_id = models.FloatField(primary_key=True)
    question = models.CharField(max_length=2000, blank=True, null=True)
    choices = models.CharField(max_length=1000, blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    owner_id = models.FloatField()
    owner_type = models.CharField(max_length=2)
    sequence = models.FloatField()
    required = models.FloatField(blank=True, null=True)
    buyer_side = models.FloatField(blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    no_attachments = models.FloatField(blank=True, null=True)
    product_line = models.FloatField(blank=True, null=True)
    header = models.FloatField(blank=True, null=True)
    suppressed = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'question'
	app_label = 'mktplc'


class ReceivablesAllocation(models.Model):
    receivables_allocation_id = models.FloatField(blank=True, null=True)
    receivables_payment = models.ForeignKey('ReceivablesPayment', models.DO_NOTHING, blank=True, null=True)
    allocation_document_id = models.CharField(max_length=20, blank=True, null=True)
    allocation_document_type = models.CharField(max_length=20, blank=True, null=True)
    payment_type = models.CharField(max_length=10, blank=True, null=True)
    allocation_amount = models.FloatField(blank=True, null=True)
    allocation_description = models.CharField(max_length=400, blank=True, null=True)
    internal_notes = models.CharField(max_length=400, blank=True, null=True)
    allocation_status = models.CharField(max_length=20, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    payee_supplier_id = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'receivables_allocation'
	app_label = 'mktplc'


class ReceivablesPayment(models.Model):
    receivables_payment_id = models.FloatField(primary_key=True)
    bank_transaction_id = models.CharField(max_length=100, blank=True, null=True)
    credit_card_transaction = models.ForeignKey(CreditCardTransaction, models.DO_NOTHING, blank=True, null=True)
    transaction_date = models.DateField()
    transaction_type = models.CharField(max_length=2)
    transaction_amount = models.FloatField()
    payment_type = models.CharField(max_length=40)
    payment_description = models.CharField(max_length=400, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    payment_status = models.CharField(max_length=20, blank=True, null=True)
    deposit_account_id = models.CharField(max_length=40, blank=True, null=True)
    check_number = models.CharField(max_length=40, blank=True, null=True)
    check_date = models.DateField(blank=True, null=True)
    batch_total = models.FloatField(blank=True, null=True)
    claim_schedule_no = models.CharField(max_length=80, blank=True, null=True)
    internal_notes = models.CharField(max_length=400, blank=True, null=True)
    transaction_id = models.CharField(max_length=20, blank=True, null=True)
    receivable_account_id = models.FloatField(blank=True, null=True)
    bank_account_id = models.CharField(max_length=20, blank=True, null=True)
    external_document_id = models.CharField(max_length=20, blank=True, null=True)
    payer_buy_org_id = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'receivables_payment'
	app_label = 'mktplc'


class Referals(models.Model):
    buyer_referals_id = models.FloatField(primary_key=True)
    refered_by_user = models.ForeignKey(EpylonUser, models.DO_NOTHING, db_column='refered_by_user')
    contact = models.ForeignKey(Contact, models.DO_NOTHING)
    is_a_buyer = models.FloatField(blank=True, null=True)
    is_a_supplier = models.FloatField(blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'referals'
	app_label = 'mktplc'


class RelatedProduct(models.Model):
    product = models.ForeignKey(Product, related_name='product')
    related_product = models.ForeignKey(Product, related_name='related_product')
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'related_product'
        unique_together = (('product', 'related_product'),)
	app_label = 'mktplc'


class RequestedItem(models.Model):
    requested_item_id = models.FloatField(primary_key=True)
    item_no = models.FloatField(blank=True, null=True)
    buyer_request = models.ForeignKey(BuyerRequest, models.DO_NOTHING)
    manufacturer_sku = models.CharField(max_length=60, blank=True, null=True)
    product_name = models.CharField(max_length=80, blank=True, null=True)
    product_description = models.CharField(max_length=400)
    item_specific_text = models.CharField(max_length=20, blank=True, null=True)
    product_detail = models.ForeignKey(ProductDetail, models.DO_NOTHING, blank=True, null=True)
    manufacturer_name = models.CharField(max_length=60, blank=True, null=True)
    price_uom = models.CharField(max_length=20)
    quantity = models.FloatField()
    price_per_uom = models.FloatField(blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    price_origin_descriptor = models.CharField(max_length=20, blank=True, null=True)
    price_origin_type = models.CharField(max_length=2)
    rfnce_spplr_item = models.ForeignKey('SupplierItem', models.DO_NOTHING, blank=True, null=True)
    classify_id = models.FloatField(blank=True, null=True)
    classify_type = models.CharField(max_length=2, blank=True, null=True)
    program = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requested_item'
	app_label = 'mktplc'


class RfpCompliance(models.Model):
    rfp_compliance_id = models.FloatField(primary_key=True)
    school = models.ForeignKey('School', models.DO_NOTHING, unique=True)
    school_dist_buying_org = models.ForeignKey('SchoolDistrict', models.DO_NOTHING, db_column='school_dist_buying_org')
    rfp_compliance_name = models.CharField(max_length=200, blank=True, null=True)
    rfp_compliance_value = models.CharField(max_length=200, blank=True, null=True)
    rfp_compliance_desc = models.CharField(max_length=200, blank=True, null=True)
    rfp_compliance_html = models.CharField(max_length=20, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rfp_compliance'
	app_label = 'mktplc'


class RpOverride(models.Model):
    rp_override_id = models.FloatField(primary_key=True)
    receivables_payment = models.ForeignKey(ReceivablesPayment, models.DO_NOTHING, blank=True, null=True)
    override_exception = models.CharField(max_length=20, blank=True, null=True)
    note = models.CharField(max_length=1000, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    redistribution_id = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rp_override'
	app_label = 'mktplc'


class SalesTaxStage(models.Model):
    zip = models.CharField(max_length=5, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    county = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state_sales_tax = models.FloatField(blank=True, null=True)
    state_use_tax = models.FloatField(blank=True, null=True)
    county_sales_tax = models.FloatField(blank=True, null=True)
    county_use_tax = models.FloatField(blank=True, null=True)
    city_sales_tax = models.FloatField(blank=True, null=True)
    city_use_tax = models.FloatField(blank=True, null=True)
    total_sales_tax = models.FloatField(blank=True, null=True)
    total_use_tax = models.FloatField(blank=True, null=True)
    tax_shipping_alone = models.CharField(max_length=1, blank=True, null=True)
    tax_shipping_and_handling = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_tax_stage'
	app_label = 'mktplc'


class SavedList(models.Model):
    saved_list_id = models.FloatField(primary_key=True)
    saved_list_name = models.CharField(max_length=80)
    saved_list_description = models.CharField(max_length=400, blank=True, null=True)
    creation_date = models.DateField()
    item_count = models.FloatField(blank=True, null=True)
    last_modified_date = models.DateField()
    buying_organization = models.ForeignKey(BuyingOrganization, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(EpylonUser, models.DO_NOTHING, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    saved_list_alias = models.CharField(max_length=12, blank=True, null=True)
    user_email = models.CharField(max_length=80, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    price_updated_date = models.DateField(blank=True, null=True)
    access_code = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'saved_list'
	app_label = 'mktplc'


class School(models.Model):
    school_id = models.FloatField(primary_key=True)
    school_name = models.CharField(max_length=60, blank=True, null=True)
    school_dist_buying_org = models.ForeignKey('SchoolDistrict', models.DO_NOTHING, db_column='school_dist_buying_org')
    parent_university = models.ForeignKey('University', models.DO_NOTHING, db_column='parent_university')
    general_contact = models.ForeignKey(Contact, related_name='general_contact' )
    receiving_contact = models.ForeignKey(Contact, related_name='receiving_contact' )
    school_location_v2 = models.FloatField(blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'school'
	app_label = 'mktplc'


class SchoolDistrict(models.Model):
    school_dist_buying_org = models.ForeignKey(BuyingOrganization, models.DO_NOTHING, db_column='school_dist_buying_org', primary_key=True)
    coop_buying_org = models.ForeignKey(Cooperative, models.DO_NOTHING, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'school_district'
        app_label = 'mktplc'


class SchoolSpendingLimits(models.Model):
    school = models.ForeignKey(School, models.DO_NOTHING, primary_key=True)
    spndng_limit_period_type = models.CharField(max_length=20, blank=True, null=True)
    spndng_limit_amount = models.DecimalField(max_digits=22, decimal_places=2, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'school_spending_limits'
        app_label = 'mktplc'


class Search(models.Model):
    search_id = models.FloatField(primary_key=True)
    contract_bundle = models.FloatField(blank=True, null=True)
    contract_legacy_vendor_no = models.CharField(max_length=20, blank=True, null=True)
    offer_buyer_contact = models.ForeignKey(Contact, related_name='offer_buyer_contact' , blank=True, null=True)
    offer_buying_org_name = models.CharField(max_length=80, blank=True, null=True)
    offer_date_expires = models.DateField(blank=True, null=True)
    offer_date_issued = models.DateField(blank=True, null=True)
    offer_item_count = models.FloatField(blank=True, null=True)
    offer_legacy_no = models.CharField(max_length=20, blank=True, null=True)
    offer_legacy_request_no = models.CharField(max_length=80, blank=True, null=True)
    offer_notes = models.CharField(max_length=2000, blank=True, null=True)
    offer_piggybackable = models.FloatField(blank=True, null=True)
    offer_supplier_contact = models.ForeignKey(Contact, related_name='offer_supplier_contact' , blank=True, null=True)
    offer_supplier_offer =  models.ForeignKey('SupplierOffer' ,  models.DO_NOTHING)
    offer_supplier_offer_type = models.CharField(max_length=2, blank=True, null=True)
    offer_supplier_name = models.CharField(max_length=80)
    offer_unstructured_text = models.CharField(max_length=400, blank=True, null=True)
    supplier_offer_category = models.CharField(max_length=2000, blank=True, null=True)
    search_type = models.CharField(max_length=80, blank=True, null=True)
    item_bundle_base_unit = models.FloatField(blank=True, null=True)
    item_product_description = models.CharField(max_length=400, blank=True, null=True)
    item_current_price_method = models.CharField(max_length=2, blank=True, null=True)
    item_supplier_item = models.ForeignKey('SupplierItem', models.DO_NOTHING, blank=True, null=True)
    item_manufacturer_name = models.CharField(max_length=80, blank=True, null=True)
    item_current_price_per_uom = models.FloatField(blank=True, null=True)
    item_has_distributors = models.FloatField(blank=True, null=True)
    item_product_name = models.CharField(max_length=80, blank=True, null=True)
    item_supplier_sku = models.CharField(max_length=60, blank=True, null=True)
    item_item_no = models.FloatField(blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    search_text = models.TextField(blank=True, null=True)
    item_product_url = models.CharField(max_length=400, blank=True, null=True)
    item_price_uom = models.CharField(max_length=20, blank=True, null=True)
    product_line = models.CharField(max_length=255, blank=True, null=True)
    offer_description = models.CharField(max_length=2000, blank=True, null=True)
    shelf_category_id = models.FloatField(blank=True, null=True)
    supplier_id = models.FloatField(blank=True, null=True)
    item_manufacturer_sku = models.CharField(max_length=60, blank=True, null=True)
    scope_of_contract = models.CharField(max_length=2000, blank=True, null=True)
    attributes = models.CharField(max_length=80, blank=True, null=True)
    program = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'search'
        app_label = 'mktplc'

class SearchDirtyRows(models.Model):
    on_which_table = models.CharField(max_length=50)
    on_which_id = models.FloatField()
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'search_dirty_rows'
        unique_together = (('on_which_table', 'on_which_id'),)
        app_label = 'mktplc'

class SearchLog(models.Model):
    search_log_id = models.FloatField(primary_key=True)
    search_query_string = models.TextField(blank=True, null=True)  # This field type is a guess.
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'search_log'
        app_label = 'mktplc'

class SearchableItem(models.Model):
    searchable_item_id = models.FloatField(primary_key=True)
    supplier_offer_id = models.FloatField()
    supplier_item = models.ForeignKey('SupplierItem', models.DO_NOTHING)
    shelf_prdt_cat_id = models.FloatField(blank=True, null=True)
    supplier_item_type = models.CharField(max_length=2)
    piggybackable_segment = models.CharField(max_length=2, blank=True, null=True)
    supplier_id = models.FloatField()
    price_uom = models.CharField(max_length=20, blank=True, null=True)
    buying_group = models.ForeignKey(BuyingGroup, models.DO_NOTHING)
    supplier_terms = models.CharField(max_length=80, blank=True, null=True)
    product_detail_id = models.FloatField(blank=True, null=True)
    price_per_uom = models.FloatField(blank=True, null=True)
    item_search_text = models.CharField(max_length=1000, blank=True, null=True)
    category_path_name = models.CharField(max_length=20, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    shelf_category = models.ForeignKey(Category, models.DO_NOTHING, blank=True, null=True)
    category_path = models.CharField(max_length=40, blank=True, null=True)
    bundle_base_unit = models.FloatField()
    price_method = models.CharField(max_length=2)
    has_distributors = models.FloatField()
    offer_descriptor = models.CharField(max_length=20, blank=True, null=True)
    item_descriptor = models.CharField(max_length=20, blank=True, null=True)
    product_url = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'searchable_item'
        app_label = 'mktplc'

class SecurityLog(models.Model):
    security_log_id = models.FloatField(primary_key=True)
    user = models.ForeignKey(EpylonUser, related_name='user', blank=True, null=True)
    apparent_user = models.ForeignKey(EpylonUser, related_name='apparent_user' , blank=True, null=True)
    log_type = models.CharField(max_length=4, blank=True, null=True)
    ip_address = models.CharField(max_length=20, blank=True, null=True)
    session_id = models.CharField(max_length=40, blank=True, null=True)
    aux_id_1 = models.FloatField(blank=True, null=True)
    aux_id_2 = models.FloatField(blank=True, null=True)
    aux_text_1 = models.CharField(max_length=100, blank=True, null=True)
    aux_text_2 = models.CharField(max_length=100, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'security_log'
        app_label = 'mktplc'

class SegmentCodeStage(models.Model):
    seg_code = models.CharField(max_length=20, blank=True, null=True)
    seg_desc = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'segment_code_stage'
        app_label = 'mktplc'

class SiteProperties(models.Model):
    poweredby_sponsor_image = models.CharField(max_length=400, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'site_properties'
        app_label = 'mktplc'

class SmallBusinessVendor(models.Model):
    large_vendor_program_id = models.FloatField(blank=True, null=True)
    small_business_org_id = models.FloatField(blank=True, null=True)
    customer_support_phone = models.CharField(max_length=20, blank=True, null=True)
    logo_url = models.CharField(max_length=2000, blank=True, null=True)
    credit_processing_username = models.CharField(max_length=50, blank=True, null=True)
    credit_processing_password = models.CharField(max_length=50, blank=True, null=True)
    credit_processing_vendor = models.CharField(max_length=50, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    small_business_vendor_id = models.FloatField(blank=True, null=True)
    interface_user_name = models.CharField(max_length=80, blank=True, null=True)
    interface_user_password = models.CharField(max_length=36, blank=True, null=True)
    small_bus_cert_no = models.CharField(max_length=40, blank=True, null=True)
    dvbe_cert_no = models.CharField(max_length=40, blank=True, null=True)
    contract_id = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=2, blank=True, null=True)
    fee_rate = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'small_business_vendor'
        app_label = 'mktplc'

class SpecificationSection(models.Model):
    section_id = models.FloatField(primary_key=True)
    section_name = models.CharField(max_length=20)
    visual_priority = models.FloatField(blank=True, null=True)
    product_category = models.ForeignKey(ProductCategory, models.DO_NOTHING)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    category = models.ForeignKey(Category, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'specification_section'
	app_label = 'mktplc'

class SpplrInterfaceAccess(models.Model):
    spplr_interface_access_id = models.FloatField(primary_key=True)
    supplier = models.ForeignKey('SupplierOrganization', models.DO_NOTHING, blank=True, null=True)
    interface_type = models.CharField(max_length=3, blank=True, null=True)
    account_no = models.CharField(max_length=20, blank=True, null=True)
    supplier_credential = models.ForeignKey('SpplrIntfCredential', related_name='supplier_credential', blank=True, null=True)
    buyer_credential = models.ForeignKey('SpplrIntfCredential', related_name='buyer_credential', blank=True, null=True)
    epylon_credential = models.ForeignKey('SpplrIntfCredential', related_name='epylon_credential', blank=True, null=True)
    buying_organization = models.ForeignKey(BuyingOrganization, models.DO_NOTHING, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    program = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spplr_interface_access'
	app_label = 'mktplc'

class SpplrIntfCredential(models.Model):
    spplr_intf_credential_id = models.FloatField(primary_key=True)
    supplier = models.ForeignKey('SupplierOrganization', models.DO_NOTHING)
    interface_type =  models.CharField(max_length=3, blank=True, null=True)
    user_name = models.CharField(max_length=80)
    user_password = models.CharField(max_length=36, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spplr_intf_credential'
	app_label = 'mktplc'

class SpplrOffrdPrdtCtgry(models.Model):
    product_category = models.ForeignKey(ProductCategory, models.DO_NOTHING)
    supplier = models.ForeignKey('SupplierOrganization', models.DO_NOTHING)
    accept_equotes = models.FloatField(blank=True, null=True)
    accept_bids = models.FloatField(blank=True, null=True)
    premier_priority = models.FloatField(blank=True, null=True)
    punchout_offer = models.ForeignKey(PunchoutSite, models.DO_NOTHING, blank=True, null=True)
    product_detail = models.ForeignKey(ProductDetail, models.DO_NOTHING, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spplr_offrd_prdt_ctgry'
        unique_together = (('supplier', 'product_category'),)
	app_label = 'mktplc'

class SpplrPrdtCtgry(models.Model):
    supplier_prdt_ctgry_id = models.FloatField(primary_key=True)
    supplier_prdt_ctgry_name = models.CharField(max_length=100)
    supplier = models.ForeignKey('SupplierOrganization', models.DO_NOTHING)
    supplier_prdt_ctgry_dsc = models.CharField(max_length=400, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spplr_prdt_ctgry'
	app_label = 'mktplc'

class SpplrRprsntTrtry(models.Model):
    supplier_represented_territory = models.FloatField(primary_key=True)
    supplier = models.ForeignKey('SupplierOrganization', models.DO_NOTHING)
    territory_name = models.CharField(max_length=60)
    sales_contact_user = models.ForeignKey(EpylonUser, related_name='sales_contact_user',  blank=True, null=True)
    purchase_order_contact_user = models.ForeignKey(EpylonUser, related_name='purchase_order_contact_user', blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spplr_rprsnt_trtry'
	app_label = 'mktplc'

class StagingTaxRateInfo(models.Model):
    city = models.CharField(max_length=100, blank=True, null=True)
    total_tax_rate = models.FloatField(blank=True, null=True)
    county = models.CharField(max_length=100, blank=True, null=True)
    effective_date = models.DateField(blank=True, null=True)
    load_status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staging_tax_rate_info'
	app_label = 'mktplc'

class SupplierBuyerRelshp(models.Model):
    supplier = models.ForeignKey('SupplierOrganization', models.DO_NOTHING)
    buying_organization = models.ForeignKey(BuyingOrganization, models.DO_NOTHING)
    preferred_supplier = models.FloatField()
    buyer_excluded = models.FloatField()
    supplier_excluded = models.FloatField()
    supplier_contact = models.ForeignKey(Contact, models.DO_NOTHING, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    account_no = models.CharField(max_length=20, blank=True, null=True)
    local_supplier = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_buyer_relshp'
        unique_together = (('buying_organization', 'supplier'),)
	app_label = 'mktplc'

class SupplierCategory(models.Model):
    supplier = models.ForeignKey('SupplierOrganization', models.DO_NOTHING)
    category = models.ForeignKey(Category, models.DO_NOTHING)
    accepts_equotes = models.FloatField(blank=True, null=True)
    accepts_ebids = models.FloatField(blank=True, null=True)
    category_path = models.CharField(max_length=40, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_category'
        unique_together = (('supplier', 'category'),)
	app_label = 'mktplc'

class SupplierCategoryMap(models.Model):
    buyer = models.ForeignKey(BuyingOrganization, models.DO_NOTHING, blank=True, null=True)
    supplier = models.ForeignKey('SupplierOrganization', models.DO_NOTHING, blank=True, null=True)
    target_supplier_id = models.FloatField(blank=True, null=True)
    category = models.CharField(max_length=60, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    extrinsic = models.CharField(max_length=20, blank=True, null=True)
    default_category = models.CharField(max_length=20, blank=True, null=True)
    supplier_name = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_category_map'
	app_label = 'mktplc'

class SupplierCategoryShadow(models.Model):
    supplier_category_id = models.FloatField(primary_key=True)
    supplier = models.ForeignKey('SupplierOrganization', models.DO_NOTHING)
    category = models.ForeignKey(Category, models.DO_NOTHING)
    accepts_equotes = models.FloatField(blank=True, null=True)
    accepts_ebids = models.FloatField(blank=True, null=True)
    category_path = models.CharField(max_length=40, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_category_shadow'
	app_label = 'mktplc'

class SupplierCtlgItem(models.Model):
    supplier_catalog_item = models.ForeignKey('SupplierItem', models.DO_NOTHING, primary_key=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_ctlg_item'
	app_label = 'mktplc'

class SupplierInterfaceSpec(models.Model):
    interface_type = models.CharField(max_length=3)
    interface_status = models.CharField(max_length=2, blank=True, null=True)
    supplier = models.ForeignKey('SupplierOrganization', models.DO_NOTHING)
    url = models.CharField(max_length=200, blank=True, null=True)
    interface_handler = models.CharField(max_length=120, blank=True, null=True)
    user_domain = models.CharField(max_length=60, blank=True, null=True)
    inactive_reason = models.CharField(max_length=400, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    require_credential = models.NullBooleanField()
    program = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_interface_spec'
        unique_together = (('supplier', 'interface_type'),)
	app_label = 'mktplc'

class SupplierItem(models.Model):
    supplier_item_id = models.FloatField(primary_key=True)
    supplier_offer = models.ForeignKey('SupplierOffer', models.DO_NOTHING)
    shelf_prdt_cat = models.ForeignKey(ProductCategory, models.DO_NOTHING, blank=True, null=True)
    supplier_item_type = models.CharField(max_length=2)
    supplier = models.ForeignKey('SupplierOrganization', models.DO_NOTHING)
    manufacturer_sku = models.CharField(max_length=60, blank=True, null=True)
    item_no = models.FloatField(blank=True, null=True)
    product_description = models.CharField(max_length=400)
    supplier_sku = models.CharField(max_length=60, blank=True, null=True)
    manufacturer_name = models.CharField(max_length=60, blank=True, null=True)
    item_specific_text = models.CharField(max_length=20, blank=True, null=True)
    price_uom = models.CharField(max_length=20, blank=True, null=True)
    supplier_terms = models.CharField(max_length=80, blank=True, null=True)
    product_detail = models.ForeignKey(ProductDetail, models.DO_NOTHING, blank=True, null=True)
    supplier_item_status = models.CharField(max_length=2)
    current_price_per_uom = models.DecimalField(max_digits=30, decimal_places=10, blank=True, null=True)
    product_name = models.CharField(max_length=80, blank=True, null=True)
    current_price_method = models.CharField(max_length=2)
    supplier_name = models.CharField(max_length=80)
    quantity = models.FloatField(blank=True, null=True)
    extended_price = models.DecimalField(max_digits=30, decimal_places=10, blank=True, null=True)
    legacy_buying_code = models.CharField(max_length=60, blank=True, null=True)
    no_response = models.FloatField(blank=True, null=True)
    substitute = models.FloatField(blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    shelf_category = models.ForeignKey(Category, models.DO_NOTHING, blank=True, null=True)
    requested_item = models.ForeignKey(RequestedItem, models.DO_NOTHING, blank=True, null=True)
    response_item_type = models.CharField(max_length=2, blank=True, null=True)
    bundle_base_unit = models.FloatField()
    has_distributors = models.FloatField()
    offer_descriptor = models.CharField(max_length=20, blank=True, null=True)
    product_url = models.CharField(max_length=400, blank=True, null=True)
    nigp = models.CharField(max_length=20, blank=True, null=True)
    unspsc = models.CharField(max_length=60, blank=True, null=True)
    extended_description = models.CharField(max_length=2000, blank=True, null=True)
    classify_id = models.FloatField(blank=True, null=True)
    classify_type = models.CharField(max_length=4, blank=True, null=True)
    accepted = models.FloatField(blank=True, null=True)
    attributes = models.CharField(max_length=80, blank=True, null=True)
    program = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_item'
        app_label = 'mktplc'

class SupplierOffer(models.Model):
    supplier_offer_id = models.FloatField(primary_key=True)
    supplier_offer_type = models.CharField(max_length=2)
    supplier_contact = models.ForeignKey(Contact, related_name='supplier_contact', blank=True, null=True)
    supplier = models.ForeignKey('SupplierOrganization' ,  models.DO_NOTHING)
    supplier_offer_status = models.CharField(max_length=2)
    piggybackable = models.FloatField(blank=True, null=True)
    terms_and_conditions = models.CharField(max_length=800, blank=True, null=True)
    date_issued = models.DateField(blank=True, null=True)
    date_expires = models.DateField(blank=True, null=True)
    structured = models.FloatField(blank=True, null=True)
    notes = models.CharField(max_length=2000, blank=True, null=True)
    separable_strctrd_items = models.FloatField(blank=True, null=True)
    item_count = models.FloatField(blank=True, null=True)
    unstructured_text = models.CharField(max_length=400, blank=True, null=True)
    piggybackable_segment = models.CharField(max_length=2, blank=True, null=True)
    buying_organization = models.ForeignKey(BuyingOrganization, models.DO_NOTHING, blank=True, null=True)
    buying_org_name = models.CharField(max_length=80, blank=True, null=True)
    supplier_name = models.CharField(max_length=80)
    buyer_contact = models.ForeignKey(Contact, related_name='buyer_contact', blank=True, null=True)
    legacy_no = models.CharField(max_length=20, blank=True, null=True)
    legacy_request_no = models.CharField(max_length=80, blank=True, null=True)
    legacy_name = models.CharField(max_length=256, blank=True, null=True)
    supplier_issuer_user = models.ForeignKey(EpylonUser, models.DO_NOTHING, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    has_distributors = models.FloatField()
    product_line = models.CharField(max_length=255, blank=True, null=True)
    awarding_institution_name = models.CharField(max_length=80, blank=True, null=True)
    eligible_buyer = models.CharField(max_length=400, blank=True, null=True)
    offer_description = models.CharField(max_length=2000, blank=True, null=True)
    date_updated = models.DateField(blank=True, null=True)
    catalog_site_url = models.CharField(max_length=400, blank=True, null=True)
    program = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_offer'
        app_label = 'mktplc'

class SupplierOfferCategory(models.Model):
    spplr_offer_cat_id = models.FloatField(primary_key=True)
    supplier_offer = models.ForeignKey(SupplierOffer, models.DO_NOTHING, blank=True, null=True)
    product_category_0 = models.ForeignKey(ProductCategory, related_name='product_category_0', db_column='product_category_0', blank=True, null=True)
    buyer_request = models.ForeignKey(BuyerRequest, models.DO_NOTHING, blank=True, null=True)
    product_category_1 = models.ForeignKey(ProductCategory, related_name='product_category_1', db_column='product_category_1', blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    category = models.ForeignKey(Category, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_offer_category'
	app_label = 'mktplc'

class SupplierOfferContact(models.Model):
    supplier_offer = models.ForeignKey(SupplierOffer, models.DO_NOTHING)
    contact = models.ForeignKey(Contact, models.DO_NOTHING)
    buying_group = models.ForeignKey(BuyingGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'supplier_offer_contact'
        unique_together = (('supplier_offer', 'buying_group'),)
	app_label = 'mktplc'

class SupplierOfferScope(models.Model):
    buying_group = models.ForeignKey(BuyingGroup, models.DO_NOTHING)
    supplier_offer = models.ForeignKey(SupplierOffer, models.DO_NOTHING)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_offer_scope'
        unique_together = (('supplier_offer', 'buying_group'),)
	app_label = 'mktplc'

class SupplierOrganization(models.Model):
    supplier_id = models.FloatField(primary_key=True)
    company_name = models.CharField(max_length=80)
    initial_interest_id = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=2)
    oem = models.FloatField()
    distributor = models.FloatField()
    reseller = models.FloatField(blank=True, null=True)
    supplier_description = models.CharField(max_length=4000, blank=True, null=True)
    minority_bsnss_entity = models.FloatField(blank=True, null=True)
    women_bsnss_entity = models.FloatField(blank=True, null=True)
    disadv_bsnss_entity = models.FloatField(blank=True, null=True)
    small_bsnss_entity = models.FloatField(blank=True, null=True)
    dis_vet_bsnss_entity = models.FloatField(blank=True, null=True)
    supplier_general_contact = models.ForeignKey(Contact, related_name='supplier_general_contact', blank=True, null=True)
    sales_contact = models.ForeignKey(Contact, models.DO_NOTHING, blank=True, null=True)
    bonded = models.FloatField(blank=True, null=True)
    supplier_billing_contact = models.ForeignKey(Contact, related_name='supplier_billing_contact', blank=True, null=True)
    customer_service_contact = models.ForeignKey(Contact, related_name='customer_service_contact', blank=True, null=True)
    federal_tax_id = models.CharField(max_length=20, blank=True, null=True)
    supplier_shipping_contact = models.ForeignKey(Contact, related_name='supplier_shipping_contact', blank=True, null=True)
    supplier_represented_corporate = models.ForeignKey(SpplrRprsntTrtry, models.DO_NOTHING, db_column='supplier_represented_corporate', blank=True, null=True)
    email_requested = models.FloatField()
    fax_notices_requested = models.FloatField()
    new_order_notification = models.FloatField()
    li_detail_notification = models.FloatField()
    order_email = models.CharField(max_length=80, blank=True, null=True)
    order_fax = models.CharField(max_length=20, blank=True, null=True)
    seller_dflt_quote_terms = models.CharField(max_length=400, blank=True, null=True)
    email_digest_requested = models.FloatField(blank=True, null=True)
    seller_default_bid_terms = models.CharField(max_length=400, blank=True, null=True)
    seller_dflt_strfrnt_term = models.CharField(max_length=400, blank=True, null=True)
    dflt_shppng_cost_rule = models.FloatField(blank=True, null=True)
    dflt_rtn_policy_short_dsc = models.CharField(max_length=20, blank=True, null=True)
    dflt_dlvr_terms_shrt_dsc = models.CharField(max_length=400, blank=True, null=True)
    dunbrad_universal_numb = models.CharField(max_length=40, blank=True, null=True)
    supplier_code = models.CharField(unique=True, max_length=20, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    issues_rush_responses = models.FloatField(blank=True, null=True)
    supplier_main_contact = models.ForeignKey(Contact, related_name='supplier_main_contact', blank=True, null=True)
    eighta_bsnss_entity = models.FloatField(blank=True, null=True)
    hub_zone_bsnss_entity = models.FloatField(blank=True, null=True)
    activation_date = models.DateField(blank=True, null=True)
    nc_hub = models.FloatField(blank=True, null=True)
    po_cxml_requested = models.FloatField(blank=True, null=True)
    external_supplier_id = models.CharField(max_length=20, blank=True, null=True)
    external_domain = models.CharField(max_length=80, blank=True, null=True)
    fl_wmb_equote = models.FloatField(blank=True, null=True)
    fl_cmb_equote = models.CharField(max_length=1, blank=True, null=True)
    testing = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_organization'
	app_label = 'mktplc'

class SupplierPrdtCtgryTree(models.Model):
    parent_supplier_cat = models.ForeignKey(SpplrPrdtCtgry, related_name='parent_supplier_cat')
    child_supplier_cat = models.ForeignKey(SpplrPrdtCtgry, related_name='child_supplier_cat')
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_prdt_ctgry_tree'
        unique_together = (('parent_supplier_cat', 'child_supplier_cat'),)
	app_label = 'mktplc'

class SupplierPrice(models.Model):
    price_id = models.FloatField(primary_key=True)
    price_per_uom = models.DecimalField(max_digits=22, decimal_places=2, blank=True, null=True)
    vrsnd_price_list = models.ForeignKey('VersionedPriceList', models.DO_NOTHING)
    is_current_price = models.FloatField()
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_price'
	app_label = 'mktplc'

class SupplierProfile(models.Model):
    supplier = models.ForeignKey(SupplierOrganization, models.DO_NOTHING, primary_key=True)
    jump_page_text_type = models.CharField(max_length=4, blank=True, null=True)
    about_text = models.CharField(max_length=1000, blank=True, null=True)
    supplier_logo = models.CharField(max_length=200, blank=True, null=True)
    supplier_jump_page_icon = models.CharField(max_length=200, blank=True, null=True)
    supplier_home_page = models.CharField(max_length=80, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    supplier_logo_content = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_profile'
	app_label = 'mktplc'

class SupplierReceivingRequest(models.Model):
    buyer_request = models.ForeignKey(BuyerRequest, models.DO_NOTHING)
    supplier = models.ForeignKey(SupplierOrganization, models.DO_NOTHING)
    user = models.ForeignKey(EpylonUser, models.DO_NOTHING, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_receiving_request'
        unique_together = (('buyer_request', 'supplier'),)
	app_label = 'mktplc'

class SupplierRegResponses(models.Model):
    initial_interest = models.ForeignKey(InitialInterest, models.DO_NOTHING, primary_key=True)
    billing_contact = models.ForeignKey(Contact, related_name='supplier_reg_resp_billing_contact', blank=True, null=True)
    main_contact = models.ForeignKey(Contact, related_name='supplier_reg_resp_main_contact', blank=True, null=True)
    federal_tax_id = models.CharField(max_length=20, blank=True, null=True)
    accept_purchase_order = models.FloatField(blank=True, null=True)
    accept_procurement_card = models.FloatField(blank=True, null=True)
    accept_credit_card = models.FloatField(blank=True, null=True)
    shipping_charge_method = models.CharField(max_length=400, blank=True, null=True)
    order_process_period = models.CharField(max_length=400, blank=True, null=True)
    company_description = models.CharField(max_length=400, blank=True, null=True)
    receive_epylon_news = models.FloatField(blank=True, null=True)
    heard_of_epylon = models.CharField(max_length=400, blank=True, null=True)
    promotion_code = models.CharField(max_length=80, blank=True, null=True)
    company_website = models.CharField(max_length=80, blank=True, null=True)
    manufacturer_developer = models.FloatField(blank=True, null=True)
    wholesaler = models.FloatField(blank=True, null=True)
    service_provider = models.FloatField(blank=True, null=True)
    distributor_var = models.FloatField(blank=True, null=True)
    retailer = models.FloatField(blank=True, null=True)
    other = models.FloatField(blank=True, null=True)
    us_regional = models.FloatField(blank=True, null=True)
    us_national = models.FloatField(blank=True, null=True)
    us_canada = models.FloatField(blank=True, null=True)
    additional_comments = models.CharField(max_length=400, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    dunbrad_universal_numb = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_reg_responses'
	app_label = 'mktplc'

class SupplierRequestScope(models.Model):
    supplier = models.ForeignKey(SupplierOrganization, models.DO_NOTHING)
    buying_group = models.ForeignKey(BuyingGroup, models.DO_NOTHING)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_request_scope'
        unique_together = (('supplier', 'buying_group'),)
	app_label = 'mktplc'

class SupplierResponse(models.Model):
    supplier_rspns_offer = models.ForeignKey(SupplierOffer, models.DO_NOTHING, primary_key=True)
    partial_response = models.FloatField(blank=True, null=True)
    supplier_response_status = models.CharField(max_length=2)
    subtotal_price = models.DecimalField(max_digits=22, decimal_places=2, blank=True, null=True)
    tax = models.DecimalField(max_digits=22, decimal_places=2, blank=True, null=True)
    shipping_cost = models.DecimalField(max_digits=22, decimal_places=2, blank=True, null=True)
    buyer_request = models.ForeignKey(BuyerRequest, models.DO_NOTHING)
    total_price = models.DecimalField(max_digits=22, decimal_places=2, blank=True, null=True)
    freight_on_board = models.CharField(max_length=20, blank=True, null=True)
    shipping_method = models.CharField(max_length=20, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    includes_shipping = models.FloatField(blank=True, null=True)
    account_number = models.CharField(max_length=20, blank=True, null=True)
    awarded_status = models.FloatField(blank=True, null=True)
    late_status = models.FloatField(blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    score_comment = models.CharField(max_length=2000, blank=True, null=True)
    sign_name = models.CharField(max_length=80, blank=True, null=True)
    sign_time = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_response'
	app_label = 'mktplc'

class SupplierTerritoryScope(models.Model):
    supplier_represented_territory = models.ForeignKey(SpplrRprsntTrtry, models.DO_NOTHING, db_column='supplier_represented_territory')
    buying_group = models.ForeignKey(BuyingGroup, models.DO_NOTHING)
    supplier = models.ForeignKey(SupplierOrganization, models.DO_NOTHING)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_territory_scope'
        unique_together = (('supplier_represented_territory', 'buying_group'),)
	app_label = 'mktplc'

class SupplierXrefIdev1(models.Model):
    supplier_id = models.FloatField()
    objectid = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'supplier_xref_idev1'
	app_label = 'mktplc'

class TahoeCompanyIdev1(models.Model):
    compname = models.CharField(max_length=64, blank=True, null=True)
    objectid = models.TextField()  # This field type is a guess.
    comppersonname = models.CharField(max_length=32, blank=True, null=True)
    comppersonrole = models.CharField(max_length=20, blank=True, null=True)
    compdescription1 = models.CharField(max_length=4000, blank=True, null=True)
    compdescription2 = models.CharField(max_length=4000, blank=True, null=True)
    compeeostatuscode = models.CharField(max_length=18, blank=True, null=True)
    compaddedby = models.CharField(max_length=24, blank=True, null=True)
    compaddeddate = models.DateField(blank=True, null=True)
    complogo = models.CharField(max_length=32, blank=True, null=True)
    compcurrentstatus = models.IntegerField(blank=True, null=True)
    compfedtaxid = models.CharField(max_length=60, blank=True, null=True)
    compdandbrating = models.CharField(max_length=18, blank=True, null=True)
    compdandbnumber = models.CharField(max_length=18, blank=True, null=True)
    comptaxexempt = models.TextField(blank=True, null=True)  # This field type is a guess.
    compbankname = models.CharField(max_length=18, blank=True, null=True)
    compsavingaccount = models.CharField(max_length=32, blank=True, null=True)
    compcheckingaccount = models.CharField(max_length=32, blank=True, null=True)
    comptypeofcorporation = models.CharField(max_length=20, blank=True, null=True)
    compcreditreference1 = models.CharField(max_length=64, blank=True, null=True)
    compcreditreference2 = models.CharField(max_length=64, blank=True, null=True)
    compyearsinbusiness = models.FloatField(blank=True, null=True)
    compbankofficer = models.CharField(max_length=18, blank=True, null=True)
    financialstatement = models.CharField(max_length=32, blank=True, null=True)
    compmargins = models.CharField(max_length=18, blank=True, null=True)
    compdeliverycost1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    compdeliverycost2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    compdeliverycost3 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    compdeliverytime1 = models.DateField(blank=True, null=True)
    compdeliverytime2 = models.DateField(blank=True, null=True)
    compdeliverytime3 = models.DateField(blank=True, null=True)
    comppicture1 = models.CharField(max_length=32, blank=True, null=True)
    comppicture2 = models.CharField(max_length=32, blank=True, null=True)
    comppicture3 = models.CharField(max_length=32, blank=True, null=True)
    comppicture4 = models.CharField(max_length=32, blank=True, null=True)
    comppicture5 = models.CharField(max_length=32, blank=True, null=True)
    compaudio1 = models.CharField(max_length=32, blank=True, null=True)
    compaudio2 = models.CharField(max_length=32, blank=True, null=True)
    compvideo1 = models.CharField(max_length=32, blank=True, null=True)
    compvideo2 = models.CharField(max_length=32, blank=True, null=True)
    compothers1 = models.CharField(max_length=4000, blank=True, null=True)
    compothers2 = models.CharField(max_length=4000, blank=True, null=True)
    compemail = models.CharField(max_length=64, blank=True, null=True)
    compupdateddate = models.DateField(blank=True, null=True)
    comprenewdate = models.DateField(blank=True, null=True)
    compcomment = models.CharField(max_length=4000, blank=True, null=True)
    compapproveddate = models.DateField(blank=True, null=True)
    compnoprop = models.IntegerField(blank=True, null=True)
    compnorooms = models.IntegerField(blank=True, null=True)
    comphomepagetype = models.IntegerField(blank=True, null=True)
    compfreeemail = models.CharField(max_length=32, blank=True, null=True)
    comppic6 = models.CharField(max_length=32, blank=True, null=True)
    comppic7 = models.CharField(max_length=32, blank=True, null=True)
    comptext1 = models.CharField(max_length=4000, blank=True, null=True)
    comptext2 = models.CharField(max_length=4000, blank=True, null=True)
    comptext3 = models.CharField(max_length=4000, blank=True, null=True)
    compid = models.CharField(max_length=5, blank=True, null=True)
    accepts_rush_orders = models.IntegerField()
    requires_fax = models.IntegerField()
    visual_priority = models.IntegerField()
    school_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tahoe_company_idev1'
	app_label = 'mktplc'

class TaxonomyTranslations(models.Model):
    category_code = models.CharField(max_length=60)
    category = models.ForeignKey(Category, models.DO_NOTHING)
    domain = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'taxonomy_translations'
	app_label = 'mktplc'

class TempInvOrderReferences(models.Model):
    purchase_order_invoice_id = models.FloatField(blank=True, null=True)
    payloadid = models.CharField(max_length=4000, blank=True, null=True)
    orderrefid = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_inv_order_references'
	app_label = 'mktplc'


class TempSupplierInfo(models.Model):
    supplier_part_id = models.CharField(db_column='supplier part id', max_length=60, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    manufacturer_part_id = models.CharField(db_column='manufacturer part id', max_length=60, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    product_description = models.CharField(db_column='product description', max_length=400, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    unit_price = models.DecimalField(db_column='unit price', max_digits=22, decimal_places=2, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    unit_of_measure = models.CharField(db_column='unit of measure', max_length=20, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    manufacturer_name = models.CharField(db_column='manufacturer name', max_length=60, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    short_name = models.CharField(db_column='short name', max_length=80, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    expiration_date = models.DateField(db_column='expiration date', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    effective_date = models.DateField(db_column='effective date', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    contract_id = models.FloatField(db_column='contract id', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    supplier_url = models.CharField(db_column='supplier url', max_length=400, blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'temp_supplier_info'
	app_label = 'mktplc'

class TempVendorMap(models.Model):
    user_id = models.FloatField()
    actual_supplier = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_vendor_map'
	app_label = 'mktplc'

class TempWriteoffPoi(models.Model):
    purchase_order_invoice_id = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_writeoff_poi'
	app_label = 'mktplc'

class Temprequest(models.Model):
    q_name = models.CharField(max_length=30, blank=True, null=True)
    msgid = models.TextField(blank=True, null=True)  # This field type is a guess.
    corrid = models.CharField(max_length=128, blank=True, null=True)
    priority = models.FloatField(blank=True, null=True)
    state = models.FloatField(blank=True, null=True)
    delay = models.DateField(blank=True, null=True)
    expiration = models.FloatField(blank=True, null=True)
    time_manager_info = models.DateField(blank=True, null=True)
    local_order_no = models.FloatField(blank=True, null=True)
    chain_no = models.FloatField(blank=True, null=True)
    cscn = models.FloatField(blank=True, null=True)
    dscn = models.FloatField(blank=True, null=True)
    enq_time = models.DateField(blank=True, null=True)
    enq_uid = models.FloatField(blank=True, null=True)
    enq_tid = models.CharField(max_length=30, blank=True, null=True)
    deq_time = models.DateField(blank=True, null=True)
    deq_uid = models.FloatField(blank=True, null=True)
    deq_tid = models.CharField(max_length=30, blank=True, null=True)
    retry_count = models.FloatField(blank=True, null=True)
    exception_qschema = models.CharField(max_length=30, blank=True, null=True)
    exception_queue = models.CharField(max_length=30, blank=True, null=True)
    step_no = models.FloatField(blank=True, null=True)
    recipient_key = models.FloatField(blank=True, null=True)
    dequeue_msgid = models.TextField(blank=True, null=True)  # This field type is a guess.
    sender_name = models.CharField(max_length=30, blank=True, null=True)
    sender_address = models.CharField(max_length=1024, blank=True, null=True)
    sender_protocol = models.FloatField(blank=True, null=True)
    user_data = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temprequest'
	app_label = 'mktplc'

class Timezone(models.Model):
    timezone_id = models.FloatField(primary_key=True)
    java_timezone_value = models.CharField(max_length=40)
    ui_description = models.CharField(max_length=80, blank=True, null=True)
    status = models.CharField(max_length=2)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'timezone'
	app_label = 'mktplc'

class ToolAccess(models.Model):
    tool_name = models.CharField(max_length=60, blank=True, null=True)
    owner = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tool_access'
	app_label = 'mktplc'


class University(models.Model):
    university_id = models.FloatField(primary_key=True)
    university_name = models.CharField(max_length=20, blank=True, null=True)
    general_contact = models.ForeignKey(Contact, related_name='university_general_contact')
    receving_contact = models.ForeignKey(Contact, related_name='university_receving_contact')
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'university'
	app_label = 'mktplc'


class UserAccountingCodes(models.Model):
    owner_id = models.FloatField()
    legacy_accounting_code = models.CharField(max_length=60)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    legacy_description = models.CharField(max_length=60, blank=True, null=True)
    owner_type = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'user_accounting_codes'
        unique_together = (('owner_id', 'legacy_accounting_code', 'owner_type'),)
	app_label = 'mktplc'


class UserComment(models.Model):
    user_comment_id = models.FloatField(primary_key=True)
    contact = models.ForeignKey(Contact, models.DO_NOTHING)
    user = models.ForeignKey(EpylonUser, models.DO_NOTHING)
    area_of_comment = models.CharField(max_length=40)
    comment_text = models.CharField(max_length=2000)
    contact_via = models.CharField(max_length=2)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_comment'
	app_label = 'mktplc'


class UserContact(models.Model):
    user = models.ForeignKey(EpylonUser, models.DO_NOTHING)
    contact = models.ForeignKey(Contact, models.DO_NOTHING)
    contact_type = models.CharField(max_length=2)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_contact'
        unique_together = (('user', 'contact'),)
	app_label = 'mktplc'


class UserFieldData(models.Model):
    doc_type = models.CharField(max_length=2)
    doc_id = models.FloatField()
    meta = models.ForeignKey('UserFieldMeta', models.DO_NOTHING)
    text_value = models.CharField(max_length=100, blank=True, null=True)
    numeric_value = models.FloatField(blank=True, null=True)
    date_value = models.DateField(blank=True, null=True)
    sequence_no = models.FloatField(blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_field_data'
        unique_together = (('doc_type', 'doc_id', 'meta'),)
	app_label = 'mktplc'


class UserFieldMeta(models.Model):
    meta_id = models.FloatField(primary_key=True)
    doc_type = models.CharField(max_length=2)
    buyer_id = models.FloatField()
    name = models.CharField(max_length=40)
    length = models.FloatField()
    validation = models.CharField(max_length=2)
    required = models.FloatField()
    sequence_no = models.FloatField()
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    default_value = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_field_meta'
	app_label = 'mktplc'


class UserFunction(models.Model):
    user = models.ForeignKey(EpylonUser, models.DO_NOTHING)
    user_function = models.ForeignKey(Function, models.DO_NOTHING)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_function'
        unique_together = (('user', 'user_function'),)
	app_label = 'mktplc'


class UserLvpParticipation(models.Model):
    epylon_user = models.ForeignKey(EpylonUser, models.DO_NOTHING)
    large_vendor_program = models.ForeignKey(LargeVendorProgram, models.DO_NOTHING)
    small_business_org_id = models.FloatField()
    user_lvp_participation_id = models.FloatField(primary_key=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    sequence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_lvp_participation'
        unique_together = (('epylon_user', 'large_vendor_program', 'small_business_org_id'),)
	app_label = 'mktplc'


class UserRelationship(models.Model):
    base_user = models.ForeignKey(EpylonUser, related_name='base_user')
    related_user = models.ForeignKey(EpylonUser, related_name='related_user')
    relationship_type = models.CharField(max_length=2)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_relationship'
        unique_together = (('base_user', 'related_user', 'relationship_type'),)
	app_label = 'mktplc'


class UserRole(models.Model):
    user_role_id = models.FloatField(primary_key=True)
    user_role_code = models.CharField(max_length=8)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_role'
	app_label = 'mktplc'


class VendorCategoryWork(models.Model):
    federal_tax_id = models.CharField(max_length=20, blank=True, null=True)
    category_code = models.CharField(max_length=60, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    external_supplier_id = models.CharField(max_length=20)
    registration_site = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vendor_category_work'
	app_label = 'mktplc'


class VendorRegWork(models.Model):
    initial_interest_id = models.FloatField(blank=True, null=True)
    company_name = models.CharField(max_length=80, blank=True, null=True)
    address1 = models.CharField(max_length=60, blank=True, null=True)
    address2 = models.CharField(max_length=60, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    state = models.CharField(max_length=30, blank=True, null=True)
    zip = models.CharField(max_length=20, blank=True, null=True)
    county = models.CharField(max_length=30, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    company_website = models.CharField(max_length=400, blank=True, null=True)
    federal_tax_id = models.CharField(max_length=20, blank=True, null=True)
    dunbrad_universal_numb = models.CharField(max_length=40, blank=True, null=True)
    accepted_epylon_tc = models.FloatField(blank=True, null=True)
    has_hub_status = models.FloatField(blank=True, null=True)
    mc_first_name = models.CharField(max_length=40, blank=True, null=True)
    mc_middle_name = models.CharField(max_length=40, blank=True, null=True)
    mc_last_name = models.CharField(max_length=40, blank=True, null=True)
    mc_title = models.CharField(max_length=32, blank=True, null=True)
    mc_phone = models.CharField(max_length=20, blank=True, null=True)
    mc_other_phone = models.CharField(max_length=20, blank=True, null=True)
    mc_email = models.CharField(max_length=80, blank=True, null=True)
    bc_first_name = models.CharField(max_length=40, blank=True, null=True)
    bc_middle_name = models.CharField(max_length=40, blank=True, null=True)
    bc_last_name = models.CharField(max_length=40, blank=True, null=True)
    bc_title = models.CharField(max_length=32, blank=True, null=True)
    bc_phone = models.CharField(max_length=20, blank=True, null=True)
    bc_other_phone = models.CharField(max_length=20, blank=True, null=True)
    bc_email = models.CharField(max_length=80, blank=True, null=True)
    processed = models.FloatField(blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)
    vendor_reg_work_id = models.FloatField(primary_key=True)
    vendor_status = models.CharField(max_length=2, blank=True, null=True)
    object_status = models.CharField(max_length=2, blank=True, null=True)
    message_type = models.CharField(max_length=5, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    registration_site = models.CharField(max_length=2)
    external_supplier_id = models.CharField(max_length=20)
    fl_cmb_equote = models.CharField(max_length=40, blank=True, null=True)
    fl_wmb_equote = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vendor_reg_work'
	app_label = 'mktplc'


class VersionedPriceList(models.Model):
    vrsnd_price_list_id = models.FloatField(primary_key=True)
    spplr_cat_offer = models.ForeignKey(SupplierOffer, models.DO_NOTHING)
    version = models.CharField(max_length=10, blank=True, null=True)
    date_issued = models.DateField(blank=True, null=True)
    date_expires = models.DateField(blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'versioned_price_list'
	app_label = 'mktplc'


class VolumePriceSchedule(models.Model):
    supplier_item = models.ForeignKey(SupplierItem, models.DO_NOTHING)
    lower_limit = models.FloatField()
    upper_limit = models.FloatField(blank=True, null=True)
    price_value_type = models.CharField(max_length=2)
    current_price_per_uom = models.DecimalField(max_digits=30, decimal_places=10)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'volume_price_schedule'
        unique_together = (('supplier_item', 'lower_limit'),)
	app_label = 'mktplc'


class Workflow(models.Model):
    workflow_id = models.FloatField(primary_key=True)
    purchase_form = models.ForeignKey(PurchaseForm, models.DO_NOTHING, blank=True, null=True)
    buyer_request = models.ForeignKey(BuyerRequest, models.DO_NOTHING, blank=True, null=True)
    responsible_user = models.ForeignKey(EpylonUser, related_name='responsible_user', blank=True, null=True)
    action_date = models.DateField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    supplier_response_offer = models.ForeignKey(SupplierResponse, models.DO_NOTHING, blank=True, null=True)
    buying_organization = models.ForeignKey(BuyingOrganization, models.DO_NOTHING)
    supplier = models.ForeignKey(SupplierOrganization, models.DO_NOTHING, blank=True, null=True)
    number_issued = models.FloatField(blank=True, null=True)
    object_type = models.CharField(max_length=20)
    number_responded = models.FloatField(blank=True, null=True)
    object_description = models.CharField(max_length=256, blank=True, null=True)
    object_status = models.CharField(max_length=20)
    user_type = models.CharField(max_length=2)
    sender_name = models.CharField(max_length=80, blank=True, null=True)
    insert_user = models.CharField(max_length=40, blank=True, null=True)
    insert_time = models.DateField(blank=True, null=True)
    update_user = models.CharField(max_length=40, blank=True, null=True)
    update_time = models.DateField(blank=True, null=True)
    delete_user = models.CharField(max_length=40, blank=True, null=True)
    delete_time = models.DateField(blank=True, null=True)
    last_update_tmstmp = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)
    eorder_type = models.CharField(max_length=2, blank=True, null=True)
    eorder_retry_count = models.FloatField(blank=True, null=True)
    encumber_status = models.CharField(max_length=2, blank=True, null=True)
    previous_user = models.ForeignKey(EpylonUser, related_name='previous_user', blank=True, null=True)
    owner = models.NullBooleanField()
    opening_date = models.DateField(blank=True, null=True)
    folder = models.ForeignKey(Folder, models.DO_NOTHING, blank=True, null=True)
    saved_object_status = models.CharField(max_length=20, blank=True, null=True)
    archive_date = models.DateField(blank=True, null=True)
    markers = models.CharField(max_length=20, blank=True, null=True)
    identifier = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workflow'
	app_label = 'mktplc'

