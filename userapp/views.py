from django.shortcuts import render, redirect
from userapp.models import *
from userapp.utilities import *
import bcrypt
from .decorators import session_required 
from django.contrib.auth import logout
from django.utils import timezone


# Create your views here.

def login_page(request):
    if request.method == 'POST':
        en_email = request.POST.get('Useremail')
        en_pwd = request.POST.get('Password')
        try:
            print('try')
            data = Tblstaff.objects.get(email = en_email)
            stored_hashed_password = data.password  # Retrieve the stored hash from your database
            user_input_password = en_pwd
            if bcrypt.checkpw(user_input_password.encode('utf-8'), stored_hashed_password.encode('utf-8')) and data.role == 2 or data.role == 4:
                request.session['email'] = en_email
                return redirect('dashboard')
            else:
                return redirect('login')
        except:
            print('except')
            return redirect('login')
    return render(request, 'login-page.html')

@session_required
def dashboard(request):
    template_name = 'dashboard.html'
    en_email = request.session.get('email')
    user_id = Tblstaff.objects.get(email=en_email)
    projects_count = Tblprojects.objects.all().count()
    users_count = Tblstaff.objects.all().count()
    clients_count = Tblclients.objects.all().count()
    context = {
        'projects_cou': projects_count,
        'users_cou': users_count,
        'clients_cou': clients_count,
        'u_fname': user_id.firstname,
        'u_lname': user_id.lastname,
        'role': user_id.role,
    }
    return render(request, template_name, context)

@session_required
def logout_view(request):
    logout(request)
    # messages.success(request, 'Logout successfull..!')
    return redirect('login')

@session_required
def send_message(request):
    data = Tblclients.objects.values_list('userid', 'company')
    temp_data = Tbltemplates.objects.filter(type='support')
    en_email = request.session.get('email')
    user_id = Tblstaff.objects.get(email=en_email)
    context = {
        'data': data,
        'temp_data': temp_data,
        'u_fname': user_id.firstname,
        'u_lname': user_id.lastname,
        'role': user_id.role,
    }
    
    if request.method == 'POST':
        cusid = request.POST.get('cusid')
        temp_id = request.POST.get('template')
        dataid = Tblcontacts.objects.get(userid=cusid)
        company_name = Tblclients.objects.get(userid=cusid)
        context['cusid'] = dataid.userid
        context['company'] = company_name.company
        context['email'] = dataid.email
        context['firstname'] = dataid.firstname
        context['lastname'] = dataid.lastname
        context['phonenumber'] = dataid.phonenumber
        context['selected_customer'] = dataid
        cus_activities = Tblnotes.objects.filter(rel_id=cusid)
        tem_data = Tbltemplates.objects.get(id=temp_id)
        context['tempdata'] = tem_data.content
        context['tblnotes_objects'] = cus_activities

    return render(request, 'send-message.html', context)

@session_required
def send_messages_to_whatsapp_email(request):
    current_time = timezone.now()
    en_email = request.session.get('email')
    user_id = Tblstaff.objects.get(email=en_email)
    if request.method == 'POST':
        cus_id = request.POST.get('hdncustomerid')
        message = request.POST.get('message')
        recipients = request.POST.get('mobile').split(',')
        for mobile in recipients:
            send_whatsApp_message(mobile.strip(), message)
            subject = "Test Subject"
            send_email(subject, message, en_email) 
        Tblnotes.objects.create(rel_id=cus_id, rel_type='lead', description=message, addedfrom=user_id.staffid, dateadded=current_time)
        return redirect('send_message')

@session_required
def support(request):
    data = Tblclients.objects.all()
    en_email = request.session.get('email')
    user_id = Tblstaff.objects.get(email=en_email)
    context = {
        'cus_data': data,
        'u_fname': user_id.firstname,
        'u_lname': user_id.lastname,
        'role': user_id.role,
    }
    if request.method == 'POST':
        cus_id = request.POST.get("cusid")
        cus_obj = Tblclients.objects.get(userid = cus_id)
        message = f'Hey Your Issue Link is http://127.0.0.1:8000/customer-issue/{cus_id}/'
        send_whatsApp_message(cus_obj.phonenumber, message)
        gen_link = f'http://127.0.0.1:8000/customer-issue/{cus_id}/'
        context['gen_link'] = gen_link
    return render(request, 'support.html', context)

def customer_issue(request, id):
    en_email = request.session.get('email')
    user_id = Tblstaff.objects.get(email = en_email)
    cus_obj = Tblcontacts.objects.get(userid = id)
    context = {
        'data': cus_obj,
        'u_fname': user_id.firstname,
        'u_lname': user_id.lastname,
        'role': user_id.role,
    }
    if request.method == 'POST':
        current_time = timezone.now()
        # file = request.FILES['file']
        comment = request.POST.get('comments')
        Tblnotes.objects.create(rel_id = id, description = comment, addedfrom = user_id.staffid, dateadded = current_time)
    return render(request, 'support-customer-page.html', context)

@session_required
def template_adding(request):
    en_email = request.session.get('email')
    user_id = Tblstaff.objects.get(email = en_email)
    context = {
        'u_fname': user_id.firstname,
        'u_lname': user_id.lastname,
        'role': user_id.role,
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        type = request.POST.get('type')
        content = request.POST.get('content')
        Tbltemplates.objects.create(name = name, type = type, content = content, addedfrom = user_id.staffid)
        print(Tbltemplates.objects.all().count())
    return render(request, 'template-add.html', context)

@session_required
def sales_send_message(request):
    data = Tblclients.objects.values_list('userid', 'company')
    temp_data = Tbltemplates.objects.filter(type='sales')
    en_email = request.session.get('email')
    user_id = Tblstaff.objects.get(email=en_email)
    context = {
        'data': data,
        'temp_data': temp_data,
        'u_fname': user_id.firstname,
        'u_lname': user_id.lastname,
        'role': user_id.role,
    }
    
    if request.method == 'POST':
        cusid = request.POST.get('cusid')
        temp_id = request.POST.get('template')
        dataid = Tblcontacts.objects.get(userid=cusid)
        company_name = Tblclients.objects.get(userid=cusid)
        context['cusid'] = dataid.userid
        context['company'] = company_name.company
        context['email'] = dataid.email
        context['firstname'] = dataid.firstname
        context['lastname'] = dataid.lastname
        context['phonenumber'] = dataid.phonenumber
        context['selected_customer'] = dataid
        cus_activities = Tblnotes.objects.filter(rel_id=cusid)
        tem_data = Tbltemplates.objects.get(id=temp_id)
        context['tempdata'] = tem_data.content
        context['tblnotes_objects'] = cus_activities
    return render(request, 'sales.html', context)