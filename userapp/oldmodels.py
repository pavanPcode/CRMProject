# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class TblactivityLog(models.Model):
    description = models.TextField()
    date = models.DateTimeField()
    staffid = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblactivity_log'


class Tblannouncements(models.Model):
    announcementid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    message = models.TextField(blank=True, null=True)
    showtousers = models.IntegerField()
    showtostaff = models.IntegerField()
    showname = models.IntegerField()
    dateadded = models.DateTimeField()
    userid = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tblannouncements'


class Tblclients(models.Model):
    userid = models.AutoField(primary_key=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    vat = models.CharField(max_length=50, blank=True, null=True)
    phonenumber = models.CharField(max_length=30, blank=True, null=True)
    country = models.IntegerField()
    city = models.CharField(max_length=100, blank=True, null=True)
    zip = models.CharField(max_length=15, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=191, blank=True, null=True)
    website = models.CharField(max_length=150, blank=True, null=True)
    datecreated = models.DateTimeField()
    active = models.IntegerField()
    leadid = models.IntegerField(blank=True, null=True)
    billing_street = models.CharField(max_length=200, blank=True, null=True)
    billing_city = models.CharField(max_length=100, blank=True, null=True)
    billing_state = models.CharField(max_length=100, blank=True, null=True)
    billing_zip = models.CharField(max_length=100, blank=True, null=True)
    billing_country = models.IntegerField(blank=True, null=True)
    shipping_street = models.CharField(max_length=200, blank=True, null=True)
    shipping_city = models.CharField(max_length=100, blank=True, null=True)
    shipping_state = models.CharField(max_length=100, blank=True, null=True)
    shipping_zip = models.CharField(max_length=100, blank=True, null=True)
    shipping_country = models.IntegerField(blank=True, null=True)
    longitude = models.CharField(max_length=300, blank=True, null=True)
    latitude = models.CharField(max_length=300, blank=True, null=True)
    default_language = models.CharField(max_length=40, blank=True, null=True)
    default_currency = models.IntegerField()
    show_primary_contact = models.IntegerField()
    stripe_id = models.CharField(max_length=40, blank=True, null=True)
    registration_confirmed = models.IntegerField()
    addedfrom = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tblclients'


class TblconsentPurposes(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblconsent_purposes'


class Tblconsents(models.Model):
    action = models.CharField(max_length=10)
    date = models.DateTimeField()
    ip = models.CharField(max_length=40)
    contact_id = models.IntegerField()
    lead_id = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    opt_in_purpose_description = models.TextField(blank=True, null=True)
    purpose_id = models.IntegerField()
    staff_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblconsents'


class TblcontactPermissions(models.Model):
    permission_id = models.IntegerField()
    userid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tblcontact_permissions'


class Tblcontacts(models.Model):
    userid = models.IntegerField()
    is_primary = models.IntegerField()
    firstname = models.CharField(max_length=191)
    lastname = models.CharField(max_length=191)
    email = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    datecreated = models.DateTimeField()
    password = models.CharField(max_length=255, blank=True, null=True)
    new_pass_key = models.CharField(max_length=32, blank=True, null=True)
    new_pass_key_requested = models.DateTimeField(blank=True, null=True)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    email_verification_key = models.CharField(max_length=32, blank=True, null=True)
    email_verification_sent_at = models.DateTimeField(blank=True, null=True)
    last_ip = models.CharField(max_length=40, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    last_password_change = models.DateTimeField(blank=True, null=True)
    active = models.IntegerField()
    profile_image = models.CharField(max_length=300, blank=True, null=True)
    direction = models.CharField(max_length=3, blank=True, null=True)
    invoice_emails = models.IntegerField()
    estimate_emails = models.IntegerField()
    credit_note_emails = models.IntegerField()
    contract_emails = models.IntegerField()
    task_emails = models.IntegerField()
    project_emails = models.IntegerField()
    ticket_emails = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tblcontacts'


class TblcontractComments(models.Model):
    content = models.TextField(blank=True, null=True)
    contract_id = models.IntegerField()
    staffid = models.IntegerField()
    dateadded = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tblcontract_comments'


class TblcontractRenewals(models.Model):
    contractid = models.IntegerField()
    old_start_date = models.DateField()
    new_start_date = models.DateField()
    old_end_date = models.DateField(blank=True, null=True)
    new_end_date = models.DateField(blank=True, null=True)
    old_value = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    new_value = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    date_renewed = models.DateTimeField()
    renewed_by = models.CharField(max_length=100)
    renewed_by_staff_id = models.IntegerField()
    is_on_old_expiry_notified = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblcontract_renewals'


class Tblcontracts(models.Model):
    content = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    subject = models.CharField(max_length=300, blank=True, null=True)
    client = models.IntegerField()
    datestart = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)
    contract_type = models.IntegerField(blank=True, null=True)
    project_id = models.IntegerField(blank=True, null=True)
    addedfrom = models.IntegerField()
    dateadded = models.DateTimeField()
    isexpirynotified = models.IntegerField()
    contract_value = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    trash = models.IntegerField(blank=True, null=True)
    not_visible_to_client = models.IntegerField()
    hash = models.CharField(max_length=32, blank=True, null=True)
    signed = models.IntegerField()
    signature = models.CharField(max_length=40, blank=True, null=True)
    marked_as_signed = models.IntegerField()
    acceptance_firstname = models.CharField(max_length=50, blank=True, null=True)
    acceptance_lastname = models.CharField(max_length=50, blank=True, null=True)
    acceptance_email = models.CharField(max_length=100, blank=True, null=True)
    acceptance_date = models.DateTimeField(blank=True, null=True)
    acceptance_ip = models.CharField(max_length=40, blank=True, null=True)
    short_link = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblcontracts'


class TblcontractsTypes(models.Model):
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'tblcontracts_types'


class Tblcountries(models.Model):
    country_id = models.AutoField(primary_key=True)
    iso2 = models.CharField(max_length=2, blank=True, null=True)
    short_name = models.CharField(max_length=80)
    long_name = models.CharField(max_length=80)
    iso3 = models.CharField(max_length=3, blank=True, null=True)
    numcode = models.CharField(max_length=6, blank=True, null=True)
    un_member = models.CharField(max_length=12, blank=True, null=True)
    calling_code = models.CharField(max_length=8, blank=True, null=True)
    cctld = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblcountries'


class TblcreditnoteRefunds(models.Model):
    credit_note_id = models.IntegerField()
    staff_id = models.IntegerField()
    refunded_on = models.DateField()
    payment_mode = models.CharField(max_length=40)
    note = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblcreditnote_refunds'


class Tblcreditnotes(models.Model):
    clientid = models.IntegerField()
    deleted_customer_name = models.CharField(max_length=100, blank=True, null=True)
    number = models.IntegerField()
    prefix = models.CharField(max_length=50, blank=True, null=True)
    number_format = models.IntegerField()
    datecreated = models.DateTimeField()
    date = models.DateField()
    adminnote = models.TextField(blank=True, null=True)
    terms = models.TextField(blank=True, null=True)
    clientnote = models.TextField(blank=True, null=True)
    currency = models.IntegerField()
    subtotal = models.DecimalField(max_digits=15, decimal_places=2)
    total_tax = models.DecimalField(max_digits=15, decimal_places=2)
    total = models.DecimalField(max_digits=15, decimal_places=2)
    adjustment = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    addedfrom = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    project_id = models.IntegerField()
    discount_percent = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    discount_total = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    discount_type = models.CharField(max_length=30)
    billing_street = models.CharField(max_length=200, blank=True, null=True)
    billing_city = models.CharField(max_length=100, blank=True, null=True)
    billing_state = models.CharField(max_length=100, blank=True, null=True)
    billing_zip = models.CharField(max_length=100, blank=True, null=True)
    billing_country = models.IntegerField(blank=True, null=True)
    shipping_street = models.CharField(max_length=200, blank=True, null=True)
    shipping_city = models.CharField(max_length=100, blank=True, null=True)
    shipping_state = models.CharField(max_length=100, blank=True, null=True)
    shipping_zip = models.CharField(max_length=100, blank=True, null=True)
    shipping_country = models.IntegerField(blank=True, null=True)
    include_shipping = models.IntegerField()
    show_shipping_on_credit_note = models.IntegerField()
    show_quantity_as = models.IntegerField()
    reference_no = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblcreditnotes'


class Tblcredits(models.Model):
    invoice_id = models.IntegerField()
    credit_id = models.IntegerField()
    staff_id = models.IntegerField()
    date = models.DateField()
    date_applied = models.DateTimeField()
    amount = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'tblcredits'


class Tblcurrencies(models.Model):
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    decimal_separator = models.CharField(max_length=5, blank=True, null=True)
    thousand_separator = models.CharField(max_length=5, blank=True, null=True)
    placement = models.CharField(max_length=10, blank=True, null=True)
    isdefault = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tblcurrencies'


class TblcustomerAdmins(models.Model):
    staff_id = models.IntegerField()
    customer_id = models.IntegerField()
    date_assigned = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tblcustomer_admins'


class TblcustomerGroups(models.Model):
    groupid = models.IntegerField()
    customer_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tblcustomer_groups'


class TblcustomersGroups(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tblcustomers_groups'


class Tblcustomfields(models.Model):
    fieldto = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=150)
    slug = models.CharField(max_length=150)
    required = models.IntegerField()
    type = models.CharField(max_length=20)
    options = models.TextField(blank=True, null=True)
    display_inline = models.IntegerField()
    field_order = models.IntegerField(blank=True, null=True)
    active = models.IntegerField()
    show_on_pdf = models.IntegerField()
    show_on_ticket_form = models.IntegerField()
    only_admin = models.IntegerField()
    show_on_table = models.IntegerField()
    show_on_client_portal = models.IntegerField()
    disalow_client_to_edit = models.IntegerField()
    bs_column = models.IntegerField()
    default_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblcustomfields'


class Tblcustomfieldsvalues(models.Model):
    relid = models.IntegerField()
    fieldid = models.IntegerField()
    fieldto = models.CharField(max_length=15)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'tblcustomfieldsvalues'


class Tbldepartments(models.Model):
    departmentid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    imap_username = models.CharField(max_length=191, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    email_from_header = models.IntegerField()
    host = models.CharField(max_length=150, blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    encryption = models.CharField(max_length=3, blank=True, null=True)
    folder = models.CharField(max_length=191)
    delete_after_import = models.IntegerField()
    calendar_id = models.TextField(blank=True, null=True)
    hidefromclient = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbldepartments'


class TbldismissedAnnouncements(models.Model):
    dismissedannouncementid = models.AutoField(primary_key=True)
    announcementid = models.IntegerField()
    staff = models.IntegerField()
    userid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbldismissed_announcements'


class Tblemaillists(models.Model):
    listid = models.AutoField(primary_key=True)
    name = models.TextField()
    creator = models.CharField(max_length=100)
    datecreated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tblemaillists'


class Tblemailtemplates(models.Model):
    emailtemplateid = models.AutoField(primary_key=True)
    type = models.TextField()
    slug = models.CharField(max_length=100)
    language = models.CharField(max_length=40, blank=True, null=True)
    name = models.TextField()
    subject = models.TextField()
    message = models.TextField()
    fromname = models.TextField()
    fromemail = models.CharField(max_length=100, blank=True, null=True)
    plaintext = models.IntegerField()
    active = models.IntegerField()
    order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tblemailtemplates'


class TblestimateRequestForms(models.Model):
    form_key = models.CharField(max_length=32)
    type = models.CharField(max_length=100)
    name = models.CharField(max_length=191)
    form_data = models.TextField(blank=True, null=True)
    recaptcha = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    submit_btn_name = models.CharField(max_length=100, blank=True, null=True)
    submit_btn_text_color = models.CharField(max_length=10, blank=True, null=True)
    submit_btn_bg_color = models.CharField(max_length=10, blank=True, null=True)
    success_submit_msg = models.TextField(blank=True, null=True)
    submit_action = models.IntegerField(blank=True, null=True)
    submit_redirect_url = models.TextField(blank=True, null=True)
    language = models.CharField(max_length=100, blank=True, null=True)
    dateadded = models.DateTimeField(blank=True, null=True)
    notify_type = models.CharField(max_length=100, blank=True, null=True)
    notify_ids = models.TextField(blank=True, null=True)
    responsible = models.IntegerField(blank=True, null=True)
    notify_request_submitted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tblestimate_request_forms'


class TblestimateRequestStatus(models.Model):
    name = models.CharField(max_length=50)
    statusorder = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)
    flag = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblestimate_request_status'


class TblestimateRequests(models.Model):
    email = models.CharField(max_length=100)
    submission = models.TextField()
    last_status_change = models.DateTimeField(blank=True, null=True)
    date_estimated = models.DateTimeField(blank=True, null=True)
    from_form_id = models.IntegerField(blank=True, null=True)
    assigned = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    default_language = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tblestimate_requests'


class Tblestimates(models.Model):
    sent = models.IntegerField()
    datesend = models.DateTimeField(blank=True, null=True)
    clientid = models.IntegerField()
    deleted_customer_name = models.CharField(max_length=100, blank=True, null=True)
    project_id = models.IntegerField()
    number = models.IntegerField()
    prefix = models.CharField(max_length=50, blank=True, null=True)
    number_format = models.IntegerField()
    hash = models.CharField(max_length=32, blank=True, null=True)
    datecreated = models.DateTimeField()
    date = models.DateField()
    expirydate = models.DateField(blank=True, null=True)
    currency = models.IntegerField()
    subtotal = models.DecimalField(max_digits=15, decimal_places=2)
    total_tax = models.DecimalField(max_digits=15, decimal_places=2)
    total = models.DecimalField(max_digits=15, decimal_places=2)
    adjustment = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    addedfrom = models.IntegerField()
    status = models.IntegerField()
    clientnote = models.TextField(blank=True, null=True)
    adminnote = models.TextField(blank=True, null=True)
    discount_percent = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    discount_total = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    discount_type = models.CharField(max_length=30, blank=True, null=True)
    invoiceid = models.IntegerField(blank=True, null=True)
    invoiced_date = models.DateTimeField(blank=True, null=True)
    terms = models.TextField(blank=True, null=True)
    reference_no = models.CharField(max_length=100, blank=True, null=True)
    sale_agent = models.IntegerField()
    billing_street = models.CharField(max_length=200, blank=True, null=True)
    billing_city = models.CharField(max_length=100, blank=True, null=True)
    billing_state = models.CharField(max_length=100, blank=True, null=True)
    billing_zip = models.CharField(max_length=100, blank=True, null=True)
    billing_country = models.IntegerField(blank=True, null=True)
    shipping_street = models.CharField(max_length=200, blank=True, null=True)
    shipping_city = models.CharField(max_length=100, blank=True, null=True)
    shipping_state = models.CharField(max_length=100, blank=True, null=True)
    shipping_zip = models.CharField(max_length=100, blank=True, null=True)
    shipping_country = models.IntegerField(blank=True, null=True)
    include_shipping = models.IntegerField()
    show_shipping_on_estimate = models.IntegerField()
    show_quantity_as = models.IntegerField()
    pipeline_order = models.IntegerField()
    is_expiry_notified = models.IntegerField()
    acceptance_firstname = models.CharField(max_length=50, blank=True, null=True)
    acceptance_lastname = models.CharField(max_length=50, blank=True, null=True)
    acceptance_email = models.CharField(max_length=100, blank=True, null=True)
    acceptance_date = models.DateTimeField(blank=True, null=True)
    acceptance_ip = models.CharField(max_length=40, blank=True, null=True)
    signature = models.CharField(max_length=40, blank=True, null=True)
    short_link = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblestimates'


class Tblevents(models.Model):
    eventid = models.AutoField(primary_key=True)
    title = models.TextField()
    description = models.TextField(blank=True, null=True)
    userid = models.IntegerField()
    start = models.DateTimeField()
    end = models.DateTimeField(blank=True, null=True)
    public = models.IntegerField()
    color = models.CharField(max_length=10, blank=True, null=True)
    isstartnotified = models.IntegerField()
    reminder_before = models.IntegerField()
    reminder_before_type = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblevents'


class Tblexpenses(models.Model):
    category = models.IntegerField()
    currency = models.IntegerField()
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    tax = models.IntegerField(blank=True, null=True)
    tax2 = models.IntegerField()
    reference_no = models.CharField(max_length=100, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    expense_name = models.CharField(max_length=500, blank=True, null=True)
    clientid = models.IntegerField()
    project_id = models.IntegerField()
    billable = models.IntegerField(blank=True, null=True)
    invoiceid = models.IntegerField(blank=True, null=True)
    paymentmode = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField()
    recurring_type = models.CharField(max_length=10, blank=True, null=True)
    repeat_every = models.IntegerField(blank=True, null=True)
    recurring = models.IntegerField()
    cycles = models.IntegerField()
    total_cycles = models.IntegerField()
    custom_recurring = models.IntegerField()
    last_recurring_date = models.DateField(blank=True, null=True)
    create_invoice_billable = models.IntegerField(blank=True, null=True)
    send_invoice_to_customer = models.IntegerField()
    recurring_from = models.IntegerField(blank=True, null=True)
    dateadded = models.DateTimeField()
    addedfrom = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tblexpenses'


class TblexpensesCategories(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblexpenses_categories'


class Tblfiles(models.Model):
    rel_id = models.IntegerField()
    rel_type = models.CharField(max_length=20)
    file_name = models.CharField(max_length=600)
    filetype = models.CharField(max_length=40, blank=True, null=True)
    visible_to_customer = models.IntegerField()
    attachment_key = models.CharField(max_length=32, blank=True, null=True)
    external = models.CharField(max_length=40, blank=True, null=True)
    external_link = models.TextField(blank=True, null=True)
    thumbnail_link = models.TextField(blank=True, null=True)
    staffid = models.IntegerField()
    contact_id = models.IntegerField(blank=True, null=True)
    task_comment_id = models.IntegerField()
    dateadded = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tblfiles'


class TblformQuestionBox(models.Model):
    boxid = models.AutoField(primary_key=True)
    boxtype = models.CharField(max_length=10)
    questionid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tblform_question_box'


class TblformQuestionBoxDescription(models.Model):
    questionboxdescriptionid = models.AutoField(primary_key=True)
    description = models.TextField()
    boxid = models.TextField()
    questionid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tblform_question_box_description'


class TblformQuestions(models.Model):
    questionid = models.AutoField(primary_key=True)
    rel_id = models.IntegerField()
    rel_type = models.CharField(max_length=20, blank=True, null=True)
    question = models.TextField()
    required = models.IntegerField()
    question_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tblform_questions'


class TblformResults(models.Model):
    resultid = models.AutoField(primary_key=True)
    boxid = models.IntegerField()
    boxdescriptionid = models.IntegerField(blank=True, null=True)
    rel_id = models.IntegerField()
    rel_type = models.CharField(max_length=20, blank=True, null=True)
    questionid = models.IntegerField()
    answer = models.TextField(blank=True, null=True)
    resultsetid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tblform_results'


class TblgdprRequests(models.Model):
    clientid = models.IntegerField()
    contact_id = models.IntegerField()
    lead_id = models.IntegerField()
    request_type = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=40, blank=True, null=True)
    request_date = models.DateTimeField()
    request_from = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblgdpr_requests'


class Tblgoals(models.Model):
    subject = models.CharField(max_length=400)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    goal_type = models.IntegerField()
    contract_type = models.IntegerField()
    achievement = models.IntegerField()
    notify_when_fail = models.IntegerField()
    notify_when_achieve = models.IntegerField()
    notified = models.IntegerField()
    staff_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tblgoals'


class Tblinvoicepaymentrecords(models.Model):
    invoiceid = models.IntegerField()
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    paymentmode = models.CharField(max_length=40, blank=True, null=True)
    paymentmethod = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateField()
    daterecorded = models.DateTimeField()
    note = models.TextField()
    transactionid = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblinvoicepaymentrecords'


class Tblinvoices(models.Model):
    sent = models.IntegerField()
    datesend = models.DateTimeField(blank=True, null=True)
    clientid = models.IntegerField()
    deleted_customer_name = models.CharField(max_length=100, blank=True, null=True)
    number = models.IntegerField()
    prefix = models.CharField(max_length=50, blank=True, null=True)
    number_format = models.IntegerField()
    datecreated = models.DateTimeField()
    date = models.DateField()
    duedate = models.DateField(blank=True, null=True)
    currency = models.IntegerField()
    subtotal = models.DecimalField(max_digits=15, decimal_places=2)
    total_tax = models.DecimalField(max_digits=15, decimal_places=2)
    total = models.DecimalField(max_digits=15, decimal_places=2)
    adjustment = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    addedfrom = models.IntegerField(blank=True, null=True)
    hash = models.CharField(max_length=32)
    status = models.IntegerField(blank=True, null=True)
    clientnote = models.TextField(blank=True, null=True)
    adminnote = models.TextField(blank=True, null=True)
    last_overdue_reminder = models.DateField(blank=True, null=True)
    last_due_reminder = models.DateField(blank=True, null=True)
    cancel_overdue_reminders = models.IntegerField()
    allowed_payment_modes = models.TextField(blank=True, null=True)
    token = models.TextField(blank=True, null=True)
    discount_percent = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    discount_total = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    discount_type = models.CharField(max_length=30)
    recurring = models.IntegerField()
    recurring_type = models.CharField(max_length=10, blank=True, null=True)
    custom_recurring = models.IntegerField()
    cycles = models.IntegerField()
    total_cycles = models.IntegerField()
    is_recurring_from = models.IntegerField(blank=True, null=True)
    last_recurring_date = models.DateField(blank=True, null=True)
    terms = models.TextField(blank=True, null=True)
    sale_agent = models.IntegerField()
    billing_street = models.CharField(max_length=200, blank=True, null=True)
    billing_city = models.CharField(max_length=100, blank=True, null=True)
    billing_state = models.CharField(max_length=100, blank=True, null=True)
    billing_zip = models.CharField(max_length=100, blank=True, null=True)
    billing_country = models.IntegerField(blank=True, null=True)
    shipping_street = models.CharField(max_length=200, blank=True, null=True)
    shipping_city = models.CharField(max_length=100, blank=True, null=True)
    shipping_state = models.CharField(max_length=100, blank=True, null=True)
    shipping_zip = models.CharField(max_length=100, blank=True, null=True)
    shipping_country = models.IntegerField(blank=True, null=True)
    include_shipping = models.IntegerField()
    show_shipping_on_invoice = models.IntegerField()
    show_quantity_as = models.IntegerField()
    project_id = models.IntegerField(blank=True, null=True)
    subscription_id = models.IntegerField()
    short_link = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblinvoices'


class TblitemTax(models.Model):
    itemid = models.IntegerField()
    rel_id = models.IntegerField()
    rel_type = models.CharField(max_length=20)
    taxrate = models.DecimalField(max_digits=15, decimal_places=2)
    taxname = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tblitem_tax'


class Tblitemable(models.Model):
    rel_id = models.IntegerField()
    rel_type = models.CharField(max_length=15)
    description = models.TextField()
    long_description = models.TextField(blank=True, null=True)
    qty = models.DecimalField(max_digits=15, decimal_places=2)
    rate = models.DecimalField(max_digits=15, decimal_places=2)
    unit = models.CharField(max_length=40, blank=True, null=True)
    item_order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblitemable'


class Tblitems(models.Model):
    description = models.TextField()
    long_description = models.TextField(blank=True, null=True)
    rate = models.DecimalField(max_digits=15, decimal_places=2)
    tax = models.IntegerField(blank=True, null=True)
    tax2 = models.IntegerField(blank=True, null=True)
    unit = models.CharField(max_length=40, blank=True, null=True)
    group_id = models.IntegerField()
    rate_currency_1 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblitems'


class TblitemsGroups(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tblitems_groups'


class TblknowedgeBaseArticleFeedback(models.Model):
    articleanswerid = models.AutoField(primary_key=True)
    articleid = models.IntegerField()
    answer = models.IntegerField()
    ip = models.CharField(max_length=40)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tblknowedge_base_article_feedback'


class TblknowledgeBase(models.Model):
    articleid = models.AutoField(primary_key=True)
    articlegroup = models.IntegerField()
    subject = models.TextField()
    description = models.TextField()
    slug = models.TextField()
    active = models.IntegerField()
    datecreated = models.DateTimeField()
    article_order = models.IntegerField()
    staff_article = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tblknowledge_base'


class TblknowledgeBaseGroups(models.Model):
    groupid = models.AutoField(primary_key=True)
    name = models.TextField()
    group_slug = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    active = models.IntegerField()
    color = models.CharField(max_length=10, blank=True, null=True)
    group_order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblknowledge_base_groups'


class TblleadActivityLog(models.Model):
    leadid = models.IntegerField()
    description = models.TextField()
    additional_data = models.CharField(max_length=600, blank=True, null=True)
    date = models.DateTimeField()
    staffid = models.IntegerField()
    full_name = models.CharField(max_length=100, blank=True, null=True)
    custom_activity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbllead_activity_log'


class TblleadIntegrationEmails(models.Model):
    subject = models.TextField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    dateadded = models.DateTimeField()
    leadid = models.IntegerField()
    emailid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbllead_integration_emails'


class Tblleads(models.Model):
    hash = models.CharField(max_length=65, blank=True, null=True)
    name = models.CharField(max_length=300)
    title = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    country = models.IntegerField()
    zip = models.CharField(max_length=15, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    assigned = models.IntegerField()
    dateadded = models.DateTimeField()
    from_form_id = models.IntegerField()
    status = models.IntegerField()
    source = models.IntegerField()
    lastcontact = models.DateTimeField(blank=True, null=True)
    dateassigned = models.DateField(blank=True, null=True)
    last_status_change = models.DateTimeField(blank=True, null=True)
    addedfrom = models.IntegerField()
    email = models.CharField(max_length=150, blank=True, null=True)
    website = models.CharField(max_length=150, blank=True, null=True)
    leadorder = models.IntegerField(blank=True, null=True)
    phonenumber = models.CharField(max_length=50, blank=True, null=True)
    date_converted = models.DateTimeField(blank=True, null=True)
    lost = models.IntegerField()
    junk = models.IntegerField()
    last_lead_status = models.IntegerField()
    is_imported_from_email_integration = models.IntegerField()
    email_integration_uid = models.CharField(max_length=30, blank=True, null=True)
    is_public = models.IntegerField()
    default_language = models.CharField(max_length=40, blank=True, null=True)
    client_id = models.IntegerField()
    lead_value = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblleads'


class TblleadsEmailIntegration(models.Model):
    active = models.IntegerField()
    email = models.CharField(max_length=100)
    imap_server = models.CharField(max_length=100)
    password = models.TextField()
    check_every = models.IntegerField()
    responsible = models.IntegerField()
    lead_source = models.IntegerField()
    lead_status = models.IntegerField()
    encryption = models.CharField(max_length=3, blank=True, null=True)
    folder = models.CharField(max_length=100)
    last_run = models.CharField(max_length=50, blank=True, null=True)
    notify_lead_imported = models.IntegerField()
    notify_lead_contact_more_times = models.IntegerField()
    notify_type = models.CharField(max_length=20, blank=True, null=True)
    notify_ids = models.TextField(blank=True, null=True)
    mark_public = models.IntegerField()
    only_loop_on_unseen_emails = models.IntegerField()
    delete_after_import = models.IntegerField()
    create_task_if_customer = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tblleads_email_integration'


class TblleadsSources(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'tblleads_sources'


class TblleadsStatus(models.Model):
    name = models.CharField(max_length=50)
    statusorder = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)
    isdefault = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tblleads_status'


class Tbllistemails(models.Model):
    emailid = models.AutoField(primary_key=True)
    listid = models.IntegerField()
    email = models.CharField(max_length=250)
    dateadded = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbllistemails'


class TblmailQueue(models.Model):
    engine = models.CharField(max_length=40, blank=True, null=True)
    email = models.CharField(max_length=500)
    cc = models.CharField(max_length=500, blank=True, null=True)
    bcc = models.CharField(max_length=500, blank=True, null=True)
    message = models.TextField()
    alt_message = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=7, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    headers = models.TextField(blank=True, null=True)
    attachments = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblmail_queue'


class Tblmaillistscustomfields(models.Model):
    customfieldid = models.AutoField(primary_key=True)
    listid = models.IntegerField()
    fieldname = models.CharField(max_length=150)
    fieldslug = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tblmaillistscustomfields'


class Tblmaillistscustomfieldvalues(models.Model):
    customfieldvalueid = models.AutoField(primary_key=True)
    listid = models.IntegerField()
    customfieldid = models.IntegerField()
    emailid = models.IntegerField()
    value = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tblmaillistscustomfieldvalues'


class Tblmigrations(models.Model):
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'tblmigrations'


class Tblmilestones(models.Model):
    name = models.CharField(max_length=400)
    description = models.TextField(blank=True, null=True)
    description_visible_to_customer = models.IntegerField(blank=True, null=True)
    due_date = models.DateField()
    project_id = models.IntegerField()
    color = models.CharField(max_length=10, blank=True, null=True)
    milestone_order = models.IntegerField()
    datecreated = models.DateField()
    hide_from_customer = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblmilestones'


class Tblmodules(models.Model):
    module_name = models.CharField(max_length=55)
    installed_version = models.CharField(max_length=11)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tblmodules'


class TblnewsfeedCommentLikes(models.Model):
    postid = models.IntegerField()
    commentid = models.IntegerField()
    userid = models.IntegerField()
    dateliked = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tblnewsfeed_comment_likes'


class TblnewsfeedPostComments(models.Model):
    content = models.TextField(blank=True, null=True)
    userid = models.IntegerField()
    postid = models.IntegerField()
    dateadded = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tblnewsfeed_post_comments'


class TblnewsfeedPostLikes(models.Model):
    postid = models.IntegerField()
    userid = models.IntegerField()
    dateliked = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tblnewsfeed_post_likes'


class TblnewsfeedPosts(models.Model):
    postid = models.AutoField(primary_key=True)
    creator = models.IntegerField()
    datecreated = models.DateTimeField()
    visibility = models.CharField(max_length=100)
    content = models.TextField()
    pinned = models.IntegerField()
    datepinned = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblnewsfeed_posts'


class Tblnotes(models.Model):
    rel_id = models.IntegerField()
    rel_type = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    date_contacted = models.DateTimeField(blank=True, null=True)
    addedfrom = models.IntegerField()
    dateadded = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tblnotes'


class Tblnotifications(models.Model):
    isread = models.IntegerField()
    isread_inline = models.IntegerField()
    date = models.DateTimeField()
    description = models.TextField()
    fromuserid = models.IntegerField()
    fromclientid = models.IntegerField()
    from_fullname = models.CharField(max_length=100)
    touserid = models.IntegerField()
    fromcompany = models.IntegerField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    additional_data = models.CharField(max_length=600, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblnotifications'


class Tbloptions(models.Model):
    name = models.CharField(max_length=150)
    value = models.TextField()
    autoload = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbloptions'


class TblpaymentModes(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    show_on_pdf = models.IntegerField()
    invoices_only = models.IntegerField()
    expenses_only = models.IntegerField()
    selected_by_default = models.IntegerField()
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tblpayment_modes'


class TblpinnedProjects(models.Model):
    project_id = models.IntegerField()
    staff_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tblpinned_projects'


class TblprojectActivity(models.Model):
    project_id = models.IntegerField()
    staff_id = models.IntegerField()
    contact_id = models.IntegerField()
    fullname = models.CharField(max_length=100, blank=True, null=True)
    visible_to_customer = models.IntegerField()
    description_key = models.CharField(max_length=500)
    additional_data = models.TextField(blank=True, null=True)
    dateadded = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tblproject_activity'


class TblprojectFiles(models.Model):
    file_name = models.TextField()
    original_file_name = models.TextField(blank=True, null=True)
    subject = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    filetype = models.CharField(max_length=50, blank=True, null=True)
    dateadded = models.DateTimeField()
    last_activity = models.DateTimeField(blank=True, null=True)
    project_id = models.IntegerField()
    visible_to_customer = models.IntegerField(blank=True, null=True)
    staffid = models.IntegerField()
    contact_id = models.IntegerField()
    external = models.CharField(max_length=40, blank=True, null=True)
    external_link = models.TextField(blank=True, null=True)
    thumbnail_link = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblproject_files'


class TblprojectMembers(models.Model):
    project_id = models.IntegerField()
    staff_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tblproject_members'


class TblprojectNotes(models.Model):
    project_id = models.IntegerField()
    content = models.TextField()
    staff_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tblproject_notes'


class TblprojectSettings(models.Model):
    project_id = models.IntegerField()
    name = models.CharField(max_length=100)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblproject_settings'


class Tblprojectdiscussioncomments(models.Model):
    discussion_id = models.IntegerField()
    discussion_type = models.CharField(max_length=10)
    parent = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)
    content = models.TextField()
    staff_id = models.IntegerField()
    contact_id = models.IntegerField(blank=True, null=True)
    fullname = models.CharField(max_length=300, blank=True, null=True)
    file_name = models.CharField(max_length=300, blank=True, null=True)
    file_mime_type = models.CharField(max_length=70, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblprojectdiscussioncomments'


class Tblprojectdiscussions(models.Model):
    project_id = models.IntegerField()
    subject = models.CharField(max_length=500)
    description = models.TextField()
    show_to_customer = models.IntegerField()
    datecreated = models.DateTimeField()
    last_activity = models.DateTimeField(blank=True, null=True)
    staff_id = models.IntegerField()
    contact_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tblprojectdiscussions'


class Tblprojects(models.Model):
    name = models.CharField(max_length=191)
    description = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    clientid = models.IntegerField()
    billing_type = models.IntegerField()
    start_date = models.DateField()
    deadline = models.DateField(blank=True, null=True)
    project_created = models.DateField()
    date_finished = models.DateTimeField(blank=True, null=True)
    progress = models.IntegerField(blank=True, null=True)
    progress_from_tasks = models.IntegerField()
    project_cost = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    project_rate_per_hour = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    estimated_hours = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    addedfrom = models.IntegerField()
    contact_notification = models.IntegerField(blank=True, null=True)
    notify_contacts = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblprojects'


class TblproposalComments(models.Model):
    content = models.TextField(blank=True, null=True)
    proposalid = models.IntegerField()
    staffid = models.IntegerField()
    dateadded = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tblproposal_comments'


class Tblproposals(models.Model):
    subject = models.CharField(max_length=500, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    addedfrom = models.IntegerField()
    datecreated = models.DateTimeField()
    total = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=15, decimal_places=2)
    total_tax = models.DecimalField(max_digits=15, decimal_places=2)
    adjustment = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    discount_percent = models.DecimalField(max_digits=15, decimal_places=2)
    discount_total = models.DecimalField(max_digits=15, decimal_places=2)
    discount_type = models.CharField(max_length=30, blank=True, null=True)
    show_quantity_as = models.IntegerField()
    currency = models.IntegerField()
    open_till = models.DateField(blank=True, null=True)
    date = models.DateField()
    rel_id = models.IntegerField(blank=True, null=True)
    rel_type = models.CharField(max_length=40, blank=True, null=True)
    assigned = models.IntegerField(blank=True, null=True)
    hash = models.CharField(max_length=32)
    proposal_to = models.CharField(max_length=600, blank=True, null=True)
    country = models.IntegerField()
    zip = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=150, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    allow_comments = models.IntegerField()
    status = models.IntegerField()
    estimate_id = models.IntegerField(blank=True, null=True)
    invoice_id = models.IntegerField(blank=True, null=True)
    date_converted = models.DateTimeField(blank=True, null=True)
    pipeline_order = models.IntegerField()
    is_expiry_notified = models.IntegerField()
    acceptance_firstname = models.CharField(max_length=50, blank=True, null=True)
    acceptance_lastname = models.CharField(max_length=50, blank=True, null=True)
    acceptance_email = models.CharField(max_length=100, blank=True, null=True)
    acceptance_date = models.DateTimeField(blank=True, null=True)
    acceptance_ip = models.CharField(max_length=40, blank=True, null=True)
    signature = models.CharField(max_length=40, blank=True, null=True)
    short_link = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblproposals'


class TblrelatedItems(models.Model):
    rel_id = models.IntegerField()
    rel_type = models.CharField(max_length=30)
    item_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tblrelated_items'


class Tblreminders(models.Model):
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField()
    isnotified = models.IntegerField()
    rel_id = models.IntegerField()
    staff = models.IntegerField()
    rel_type = models.CharField(max_length=40)
    notify_by_email = models.IntegerField()
    creator = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tblreminders'


class Tblroles(models.Model):
    roleid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    permissions = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblroles'


class TblsalesActivity(models.Model):
    rel_type = models.CharField(max_length=20, blank=True, null=True)
    rel_id = models.IntegerField()
    description = models.TextField()
    additional_data = models.TextField(blank=True, null=True)
    staffid = models.CharField(max_length=11, blank=True, null=True)
    full_name = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tblsales_activity'


class TblscheduledEmails(models.Model):
    rel_id = models.IntegerField()
    rel_type = models.CharField(max_length=15)
    scheduled_at = models.DateTimeField()
    contacts = models.CharField(max_length=197)
    cc = models.TextField(blank=True, null=True)
    attach_pdf = models.IntegerField()
    template = models.CharField(max_length=197)

    class Meta:
        managed = False
        db_table = 'tblscheduled_emails'


class Tblservices(models.Model):
    serviceid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tblservices'


class Tblsessions(models.Model):
    id = models.CharField(primary_key=True, max_length=128)
    ip_address = models.CharField(max_length=45)
    timestamp = models.PositiveIntegerField()
    data = models.TextField()

    class Meta:
        managed = False
        db_table = 'tblsessions'


class TblsharedCustomerFiles(models.Model):
    file_id = models.IntegerField()
    contact_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tblshared_customer_files'


class TblspamFilters(models.Model):
    type = models.CharField(max_length=40)
    rel_type = models.CharField(max_length=10)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'tblspam_filters'


class Tblstaff(models.Model):
    staffid = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    facebook = models.TextField(blank=True, null=True)
    linkedin = models.TextField(blank=True, null=True)
    phonenumber = models.CharField(max_length=30, blank=True, null=True)
    skype = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=250)
    datecreated = models.DateTimeField()
    profile_image = models.CharField(max_length=300, blank=True, null=True)
    last_ip = models.CharField(max_length=40, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    last_activity = models.DateTimeField(blank=True, null=True)
    last_password_change = models.DateTimeField(blank=True, null=True)
    new_pass_key = models.CharField(max_length=32, blank=True, null=True)
    new_pass_key_requested = models.DateTimeField(blank=True, null=True)
    admin = models.IntegerField()
    role = models.IntegerField(blank=True, null=True)
    active = models.IntegerField()
    default_language = models.CharField(max_length=40, blank=True, null=True)
    direction = models.CharField(max_length=3, blank=True, null=True)
    media_path_slug = models.CharField(max_length=300, blank=True, null=True)
    is_not_staff = models.IntegerField()
    hourly_rate = models.DecimalField(max_digits=15, decimal_places=2)
    two_factor_auth_enabled = models.IntegerField(blank=True, null=True)
    two_factor_auth_code = models.CharField(max_length=100, blank=True, null=True)
    two_factor_auth_code_requested = models.DateTimeField(blank=True, null=True)
    email_signature = models.TextField(blank=True, null=True)
    google_auth_secret = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblstaff'


class TblstaffDepartments(models.Model):
    staffdepartmentid = models.AutoField(primary_key=True)
    staffid = models.IntegerField()
    departmentid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tblstaff_departments'


class TblstaffPermissions(models.Model):
    staff_id = models.IntegerField()
    feature = models.CharField(max_length=40)
    capability = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tblstaff_permissions'


class Tblsubscriptions(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    description_in_item = models.IntegerField()
    clientid = models.IntegerField()
    date = models.DateField(blank=True, null=True)
    terms = models.TextField(blank=True, null=True)
    currency = models.IntegerField()
    tax_id = models.IntegerField()
    stripe_tax_id = models.CharField(max_length=50, blank=True, null=True)
    tax_id_2 = models.IntegerField()
    stripe_tax_id_2 = models.CharField(max_length=50, blank=True, null=True)
    stripe_plan_id = models.TextField(blank=True, null=True)
    stripe_subscription_id = models.TextField()
    next_billing_cycle = models.BigIntegerField(blank=True, null=True)
    ends_at = models.BigIntegerField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    quantity = models.IntegerField()
    project_id = models.IntegerField()
    hash = models.CharField(max_length=32)
    created = models.DateTimeField()
    created_from = models.IntegerField()
    date_subscribed = models.DateTimeField(blank=True, null=True)
    in_test_environment = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblsubscriptions'


class Tblsurveyresultsets(models.Model):
    resultsetid = models.AutoField(primary_key=True)
    surveyid = models.IntegerField()
    ip = models.CharField(max_length=40)
    useragent = models.CharField(max_length=150)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tblsurveyresultsets'


class Tblsurveys(models.Model):
    surveyid = models.AutoField(primary_key=True)
    subject = models.TextField()
    slug = models.TextField()
    description = models.TextField()
    viewdescription = models.TextField(blank=True, null=True)
    datecreated = models.DateTimeField()
    redirect_url = models.CharField(max_length=100, blank=True, null=True)
    send = models.IntegerField()
    onlyforloggedin = models.IntegerField(blank=True, null=True)
    fromname = models.CharField(max_length=100, blank=True, null=True)
    iprestrict = models.IntegerField()
    active = models.IntegerField()
    hash = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'tblsurveys'


class Tblsurveysemailsendcron(models.Model):
    surveyid = models.IntegerField()
    email = models.CharField(max_length=100)
    emailid = models.IntegerField(blank=True, null=True)
    listid = models.CharField(max_length=11, blank=True, null=True)
    log_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tblsurveysemailsendcron'


class Tblsurveysendlog(models.Model):
    surveyid = models.IntegerField()
    total = models.IntegerField()
    date = models.DateTimeField()
    iscronfinished = models.IntegerField()
    send_to_mail_lists = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblsurveysendlog'


class Tbltaggables(models.Model):
    rel_id = models.IntegerField()
    rel_type = models.CharField(max_length=20)
    tag_id = models.IntegerField()
    tag_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbltaggables'


class Tbltags(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tbltags'


class TbltaskAssigned(models.Model):
    staffid = models.IntegerField()
    taskid = models.IntegerField()
    assigned_from = models.IntegerField()
    is_assigned_from_contact = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbltask_assigned'


class TbltaskChecklistItems(models.Model):
    taskid = models.IntegerField()
    description = models.TextField()
    finished = models.IntegerField()
    dateadded = models.DateTimeField()
    addedfrom = models.IntegerField()
    finished_from = models.IntegerField(blank=True, null=True)
    list_order = models.IntegerField()
    assigned = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbltask_checklist_items'


class TbltaskComments(models.Model):
    content = models.TextField()
    taskid = models.IntegerField()
    staffid = models.IntegerField()
    contact_id = models.IntegerField()
    file_id = models.IntegerField()
    dateadded = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbltask_comments'


class TbltaskFollowers(models.Model):
    staffid = models.IntegerField()
    taskid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbltask_followers'


class Tbltasks(models.Model):
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    dateadded = models.DateTimeField()
    startdate = models.DateField()
    duedate = models.DateField(blank=True, null=True)
    datefinished = models.DateTimeField(blank=True, null=True)
    addedfrom = models.IntegerField()
    is_added_from_contact = models.IntegerField()
    status = models.IntegerField()
    recurring_type = models.CharField(max_length=10, blank=True, null=True)
    repeat_every = models.IntegerField(blank=True, null=True)
    recurring = models.IntegerField()
    is_recurring_from = models.IntegerField(blank=True, null=True)
    cycles = models.IntegerField()
    total_cycles = models.IntegerField()
    custom_recurring = models.IntegerField()
    last_recurring_date = models.DateField(blank=True, null=True)
    rel_id = models.IntegerField(blank=True, null=True)
    rel_type = models.CharField(max_length=30, blank=True, null=True)
    is_public = models.IntegerField()
    billable = models.IntegerField()
    billed = models.IntegerField()
    invoice_id = models.IntegerField()
    hourly_rate = models.DecimalField(max_digits=15, decimal_places=2)
    milestone = models.IntegerField(blank=True, null=True)
    kanban_order = models.IntegerField()
    milestone_order = models.IntegerField()
    visible_to_client = models.IntegerField()
    deadline_notified = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbltasks'


class TbltasksChecklistTemplates(models.Model):
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbltasks_checklist_templates'


class Tbltaskstimers(models.Model):
    task_id = models.IntegerField()
    start_time = models.CharField(max_length=64)
    end_time = models.CharField(max_length=64, blank=True, null=True)
    staff_id = models.IntegerField()
    hourly_rate = models.DecimalField(max_digits=15, decimal_places=2)
    note = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbltaskstimers'


class Tbltaxes(models.Model):
    name = models.CharField(max_length=100)
    taxrate = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'tbltaxes'


class Tbltemplates(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    addedfrom = models.IntegerField()
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbltemplates'


class TblticketAttachments(models.Model):
    ticketid = models.IntegerField()
    replyid = models.IntegerField(blank=True, null=True)
    file_name = models.TextField()
    filetype = models.CharField(max_length=50, blank=True, null=True)
    dateadded = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tblticket_attachments'


class TblticketReplies(models.Model):
    ticketid = models.IntegerField()
    userid = models.IntegerField(blank=True, null=True)
    contactid = models.IntegerField()
    name = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    date = models.DateTimeField()
    message = models.TextField(blank=True, null=True)
    attachment = models.IntegerField(blank=True, null=True)
    admin = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblticket_replies'


class Tbltickets(models.Model):
    ticketid = models.AutoField(primary_key=True)
    adminreplying = models.IntegerField()
    userid = models.IntegerField()
    contactid = models.IntegerField()
    email = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    department = models.IntegerField()
    priority = models.IntegerField()
    status = models.IntegerField()
    service = models.IntegerField(blank=True, null=True)
    ticketkey = models.CharField(max_length=32)
    subject = models.CharField(max_length=300)
    message = models.TextField(blank=True, null=True)
    admin = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField()
    project_id = models.IntegerField()
    lastreply = models.DateTimeField(blank=True, null=True)
    clientread = models.IntegerField()
    adminread = models.IntegerField()
    assigned = models.IntegerField()
    cc = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbltickets'


class TblticketsPipeLog(models.Model):
    date = models.DateTimeField()
    email_to = models.CharField(max_length=500)
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=500)
    message = models.TextField()
    email = models.CharField(max_length=300)
    status = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tbltickets_pipe_log'


class TblticketsPredefinedReplies(models.Model):
    name = models.CharField(max_length=300)
    message = models.TextField()

    class Meta:
        managed = False
        db_table = 'tbltickets_predefined_replies'


class TblticketsPriorities(models.Model):
    priorityid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tbltickets_priorities'


class TblticketsStatus(models.Model):
    ticketstatusid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    isdefault = models.IntegerField()
    statuscolor = models.CharField(max_length=7, blank=True, null=True)
    statusorder = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbltickets_status'


class Tbltodos(models.Model):
    todoid = models.AutoField(primary_key=True)
    description = models.TextField()
    staffid = models.IntegerField()
    dateadded = models.DateTimeField()
    finished = models.IntegerField()
    datefinished = models.DateTimeField(blank=True, null=True)
    item_order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbltodos'


class TbltrackedMails(models.Model):
    uid = models.CharField(max_length=32)
    rel_id = models.IntegerField()
    rel_type = models.CharField(max_length=40)
    date = models.DateTimeField()
    email = models.CharField(max_length=100)
    opened = models.IntegerField()
    date_opened = models.DateTimeField(blank=True, null=True)
    subject = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbltracked_mails'


class TbltwocheckoutLog(models.Model):
    reference = models.CharField(max_length=64)
    invoice = models.ForeignKey(Tblinvoices, models.DO_NOTHING)
    amount = models.CharField(max_length=25)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbltwocheckout_log'


class TbluserAutoLogin(models.Model):
    key_id = models.CharField(max_length=32)
    user_id = models.IntegerField()
    user_agent = models.CharField(max_length=150)
    last_ip = models.CharField(max_length=40)
    last_login = models.DateTimeField()
    staff = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbluser_auto_login'


class TbluserMeta(models.Model):
    umeta_id = models.BigAutoField(primary_key=True)
    staff_id = models.PositiveBigIntegerField()
    client_id = models.PositiveBigIntegerField()
    contact_id = models.PositiveBigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbluser_meta'


class Tblvault(models.Model):
    customer_id = models.IntegerField()
    server_address = models.CharField(max_length=400)
    port = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=300)
    password = models.TextField()
    description = models.TextField(blank=True, null=True)
    creator = models.IntegerField()
    creator_name = models.CharField(max_length=100, blank=True, null=True)
    visibility = models.IntegerField()
    share_in_projects = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    last_updated_from = models.CharField(max_length=100, blank=True, null=True)
    date_created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tblvault'


class TblviewsTracking(models.Model):
    rel_id = models.IntegerField()
    rel_type = models.CharField(max_length=40)
    date = models.DateTimeField()
    view_ip = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'tblviews_tracking'


class TblwebToLead(models.Model):
    form_key = models.CharField(max_length=32)
    lead_source = models.IntegerField()
    lead_status = models.IntegerField()
    notify_lead_imported = models.IntegerField()
    notify_type = models.CharField(max_length=20, blank=True, null=True)
    notify_ids = models.TextField(blank=True, null=True)
    responsible = models.IntegerField()
    name = models.CharField(max_length=400)
    form_data = models.TextField(blank=True, null=True)
    recaptcha = models.IntegerField()
    submit_btn_name = models.CharField(max_length=40, blank=True, null=True)
    submit_btn_text_color = models.CharField(max_length=10, blank=True, null=True)
    submit_btn_bg_color = models.CharField(max_length=10, blank=True, null=True)
    success_submit_msg = models.TextField(blank=True, null=True)
    submit_action = models.IntegerField(blank=True, null=True)
    submit_redirect_url = models.TextField(blank=True, null=True)
    language = models.CharField(max_length=40, blank=True, null=True)
    allow_duplicate = models.IntegerField()
    mark_public = models.IntegerField()
    track_duplicate_field = models.CharField(max_length=20, blank=True, null=True)
    track_duplicate_field_and = models.CharField(max_length=20, blank=True, null=True)
    create_task_on_duplicate = models.IntegerField()
    dateadded = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tblweb_to_lead'


class UserappUserdetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userapp_userdetails'
