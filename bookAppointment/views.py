from django.shortcuts import render,HttpResponseRedirect,HttpResponse,redirect
from MediSeApp.models import Setting
from Product.models import Product,Images,Category
from .models import *
from .forms import BookingForm,DoctorRegister
from OrderApp.models import ShopCart
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth import logout, authenticate, login, update_session_auth_hash
from Accounts.models import UserProfile,DoctorProfile,DriverProfile
from .forms import DoctorUserForm
from . import forms,models
from django.conf import settings
User = settings.AUTH_USER_MODEL
# Create your views here.
def base(request):
    context={}
    return render(request,'base.html',context)

def finddoctor(request):
    current_user = request.user
    cart_product = ShopCart.objects.filter(user_id=current_user.id)
    total_amount = 0
    for p in cart_product:
        total_amount += p.product.new_price*p.quantity
    total_quantity =0
    for q in cart_product:
        total_quantity += q.quantity
    setting= Setting.objects.get(id=1)
    category = Category.objects.all()
    context={'cart_product': cart_product,
             'total_amount': total_amount,
             'setting':setting,
             'category':category,
             'total_quantity':total_quantity,
             }
    return render(request,'findDoctor.html',context)
"""
def doctor(request):
    setting= Setting.objects.get(id=1)
    doctors = Doctor.objects.all();
    category=DoctorCategories.objects.all()
    doctor_cat = Doctor.objects.filter(d_s_text__title='Psychiatry')
    doctor_cat1= Doctor.objects.filter(d_s_text__title='Cardiology (Cardiac Imaging)')
    doctor_cat2= Doctor.objects.filter(d_s_text__title='Allergy &amp; Immunology')
    doctor_cat3= Doctor.objects.filter(d_s_text__title='Anesthesiology')
    doctor_cat4= Doctor.objects.filter(d_s_text__title='Anti-Aging Medicine')
    doctor_cat5= Doctor.objects.filter(d_s_text__title='Aviation Medicine')
    doctor_cat6= Doctor.objects.filter(d_s_text__title='Cardiology (Heart)')
    doctor_cat7= Doctor.objects.filter(d_s_text__title='Clinical Nutrition')
    doctor_cat8= Doctor.objects.filter(d_s_text__title='Critical Care Medicine (ICU)')
    doctor_cat9= Doctor.objects.filter(d_s_text__title='Dental')
    doctor_cat10= Doctor.objects.filter(d_s_text__title='Dermatology (Skin)')
    doctor_cat11= Doctor.objects.filter(d_s_text__title='Emergency Medicine')
    doctor_cat12= Doctor.objects.filter(d_s_text__title='Endocrinology (Diabetes &amp; Thyroid &amp; Hormone &amp; Nutrition)')
    doctor_cat13= Doctor.objects.filter(d_s_text__title='Family Medicine (G.P.)')
    doctor_cat14= Doctor.objects.filter(d_s_text__title='Forensic Medicine')
    doctor_cat15= Doctor.objects.filter(d_s_text__title='Gastroenterology &amp; Hepatology')
    doctor_cat16= Doctor.objects.filter(d_s_text__title='General Practice')
    doctor_cat17= Doctor.objects.filter(d_s_text__title='Hematology (Blood)')
    doctor_cat18= Doctor.objects.filter(d_s_text__title='Hyperbaric &amp; Underwater Medicine')
    doctor_cat19= Doctor.objects.filter(d_s_text__title='Infectious Disease')
    doctor_cat20= Doctor.objects.filter(d_s_text__title='Internal Medicine')
    doctor_cat21= Doctor.objects.filter(d_s_text__title='Internal Medicine (Geriatric)')
    doctor_cat22= Doctor.objects.filter(d_s_text__title='Medical Genetics')
    doctor_cat23= Doctor.objects.filter(d_s_text__title='Medicine')
    doctor_cat24= Doctor.objects.filter(d_s_text__title='Nephrology (Kidney)')
    doctor_cat25= Doctor.objects.filter(d_s_text__title='Neurology (Nerve)')
    doctor_cat26= Doctor.objects.filter(d_s_text__title='Neuromedicine')
    doctor_cat27= Doctor.objects.filter(d_s_text__title='Neurosurgery')
    doctor_cat28= Doctor.objects.filter(d_s_text__title='OB/GYN (Women)')
    doctor_cat29= Doctor.objects.filter(d_s_text__title='Oncology (Cancer)')
    doctor_cat30= Doctor.objects.filter(d_s_text__title='Ophthalmology (Eye)')
    doctor_cat31= Doctor.objects.filter(d_s_text__title='Orthopedics (Bone)')
    doctor_cat32= Doctor.objects.filter(d_s_text__title='Otolaryngology (Ear, Nose, Throat)')
    doctor_cat33= Doctor.objects.filter(d_s_text__title='Pathology (Clinical Pathology)')
    doctor_cat34= Doctor.objects.filter(d_s_text__title='Pathology (Surgical Pathology)')
    doctor_cat35= Doctor.objects.filter(d_s_text__title='Pediatrics (Children)')
    doctor_cat36= Doctor.objects.filter(d_s_text__title='Physical Medicine and Rehabilitation (PM&amp;R)')
    doctor_cat37= Doctor.objects.filter(d_s_text__title='Plastic Surgery')
    doctor_cat38= Doctor.objects.filter(d_s_text__title='Preventive Medicine')
    doctor_cat39= Doctor.objects.filter(d_s_text__title='Preventive Medicine (Check up)')
    doctor_cat40= Doctor.objects.filter(d_s_text__title='Pulmonology (Lungs)')
    doctor_cat41= Doctor.objects.filter(d_s_text__title='Radiology')
    doctor_cat42= Doctor.objects.filter(d_s_text__title='Rheumatology (Muscle &amp; Joint)')
    doctor_cat43= Doctor.objects.filter(d_s_text__title='Sleep Medicine')
    doctor_cat44= Doctor.objects.filter(d_s_text__title='Spine')
    doctor_cat45= Doctor.objects.filter(d_s_text__title='Surgery')
    doctor_cat46= Doctor.objects.filter(d_s_text__title='Toxicology &amp; Occupational Medicine')
    doctor_cat47= Doctor.objects.filter(d_s_text__title='Transplant Hepatology')
    doctor_cat48= Doctor.objects.filter(d_s_text__title='Urology (Genito-Urinary)')
    context={'doctors':doctors,
             'setting':setting,
             'category':category,
             'doctor_cat':doctor_cat,
             'doctor_cat1':doctor_cat1,
             'doctor_cat2':doctor_cat2,
             'doctor_cat3':doctor_cat3,
             'doctor_cat4':doctor_cat4,
             'doctor_cat5':doctor_cat5,
             'doctor_cat6':doctor_cat6,
             'doctor_cat7':doctor_cat7,
             'doctor_cat8':doctor_cat8,
             'doctor_cat9':doctor_cat9,
             'doctor_cat10':doctor_cat10,
             'doctor_cat11':doctor_cat11,
             'doctor_cat12':doctor_cat12,
             'doctor_cat13':doctor_cat13,
             'doctor_cat14':doctor_cat14,
             'doctor_cat15':doctor_cat15,
             'doctor_cat16':doctor_cat16,
             'doctor_cat17':doctor_cat17,
             'doctor_cat18':doctor_cat18,
             'doctor_cat19':doctor_cat19,
             'doctor_cat20':doctor_cat20,
             'doctor_cat21':doctor_cat21,
             'doctor_cat22':doctor_cat22,
             'doctor_cat23':doctor_cat23,
             'doctor_cat24':doctor_cat24,
             'doctor_cat25':doctor_cat25,
             'doctor_cat26':doctor_cat26,
             'doctor_cat27':doctor_cat27,
             'doctor_cat28':doctor_cat28,
             'doctor_cat29':doctor_cat29,
             'doctor_cat30':doctor_cat30,
             'doctor_cat31':doctor_cat31,
             'doctor_cat32':doctor_cat32,
             'doctor_cat33':doctor_cat33,
             'doctor_cat34':doctor_cat34,
             'doctor_cat35':doctor_cat35,
             'doctor_cat36':doctor_cat36,
             'doctor_cat37':doctor_cat37,
             'doctor_cat38':doctor_cat38,
             'doctor_cat39':doctor_cat39,
             'doctor_cat40':doctor_cat40,
             'doctor_cat41':doctor_cat41,
             'doctor_cat42':doctor_cat42,
             'doctor_cat43':doctor_cat43,
             'doctor_cat44':doctor_cat44,
             'doctor_cat45':doctor_cat45,
             'doctor_cat46':doctor_cat46,
             'doctor_cat47':doctor_cat47,
             'doctor_cat48':doctor_cat48,
             }
    return render(request,'doctor.html',context)
"""
def doctor(request):
    setting= Setting.objects.get(id=1)
    doctors = Doctor.objects.all();
    category=DoctorCategories.objects.all()
    doctor_cat = DoctorCategories.objects.filter(title='Psychiatry')
    doctor_cat1= DoctorCategories.objects.filter(title='Cardiology (Cardiac Imaging)')
    doctor_cat2= DoctorCategories.objects.filter(title='Allergy &amp; Immunology')
    doctor_cat3= DoctorCategories.objects.filter(title='Anesthesiology')
    doctor_cat4= DoctorCategories.objects.filter(title='Anti-Aging Medicine')
    doctor_cat5= DoctorCategories.objects.filter(title='Aviation Medicine')
    doctor_cat6= DoctorCategories.objects.filter(title='Cardiology (Heart)')
    doctor_cat7= DoctorCategories.objects.filter(title='Clinical Nutrition')
    doctor_cat8= DoctorCategories.objects.filter(title='Critical Care Medicine (ICU)')
    doctor_cat9= DoctorCategories.objects.filter(title='Dental')
    doctor_cat10= DoctorCategories.objects.filter(title='Dermatology (Skin)')
    doctor_cat11= DoctorCategories.objects.filter(title='Emergency Medicine')
    doctor_cat12= DoctorCategories.objects.filter(title='Endocrinology (Diabetes,Thyroid,Hormone,Nutrition)')
    doctor_cat13= DoctorCategories.objects.filter(title='Family Medicine (G.P.)')
    doctor_cat14= DoctorCategories.objects.filter(title='Forensic Medicine')
    doctor_cat15= DoctorCategories.objects.filter(title='Gastroenterology &amp; Hepatology')
    doctor_cat16= DoctorCategories.objects.filter(title='General Practice')
    doctor_cat17= DoctorCategories.objects.filter(title='Hematology (Blood)')
    doctor_cat18= DoctorCategories.objects.filter(title='Hyperbaric &amp; Underwater Medicine')
    doctor_cat19= DoctorCategories.objects.filter(title='Infectious Disease')
    doctor_cat20= DoctorCategories.objects.filter(title='Internal Medicine')
    doctor_cat21= DoctorCategories.objects.filter(title='Internal Medicine (Geriatric)')
    doctor_cat22= DoctorCategories.objects.filter(title='Medical Genetics')
    doctor_cat23= DoctorCategories.objects.filter(title='Medicine')
    doctor_cat24= DoctorCategories.objects.filter(title='Nephrology (Kidney)')
    doctor_cat25= DoctorCategories.objects.filter(title='Neurology (Nerve)')
    doctor_cat26= DoctorCategories.objects.filter(title='Neuromedicine')
    doctor_cat27= DoctorCategories.objects.filter(title='Neurosurgery')
    doctor_cat28= DoctorCategories.objects.filter(title='Gynecologist')
    doctor_cat29= DoctorCategories.objects.filter(title='Oncology (Cancer)')
    doctor_cat30= DoctorCategories.objects.filter(title='Ophthalmology (Eye)')
    doctor_cat31= DoctorCategories.objects.filter(title='Orthopedics (Bone)')
    doctor_cat32= DoctorCategories.objects.filter(title='Otolaryngology (Ear, Nose, Throat)')
    doctor_cat33= DoctorCategories.objects.filter(title='Pathology (Clinical Pathology)')
    doctor_cat34= DoctorCategories.objects.filter(title='Pathology (Surgical Pathology)')
    doctor_cat35= DoctorCategories.objects.filter(title='Pediatrics (Children)')
    doctor_cat36= DoctorCategories.objects.filter(title='Physical Medicine and Rehabilitation (PM&amp;R)')
    doctor_cat37= DoctorCategories.objects.filter(title='Plastic Surgery')
    doctor_cat38= DoctorCategories.objects.filter(title='Preventive Medicine')
    doctor_cat39= DoctorCategories.objects.filter(title='Preventive Medicine (Check up)')
    doctor_cat40= DoctorCategories.objects.filter(title='Pulmonology (Lungs)')
    doctor_cat41= DoctorCategories.objects.filter(title='Radiology')
    doctor_cat42= DoctorCategories.objects.filter(title='Rheumatology (Muscle &amp; Joint)')
    doctor_cat43= DoctorCategories.objects.filter(title='Sleep Medicine')
    doctor_cat44= DoctorCategories.objects.filter(title='Spine')
    doctor_cat45= DoctorCategories.objects.filter(title='Surgery')
    doctor_cat46= DoctorCategories.objects.filter(title='Toxicology &amp; Occupational Medicine')
    doctor_cat47= DoctorCategories.objects.filter(title='Transplant Hepatology')
    doctor_cat48= DoctorCategories.objects.filter(title='Urology (Genito-Urinary) & Andrologist')
    doctor_cat49= DoctorCategories.objects.filter(title='Proctologist')
    context={'doctors':doctors,
             'setting':setting,
             'category':category,
             'doctor_cat':doctor_cat,
             'doctor_cat1':doctor_cat1,
             'doctor_cat2':doctor_cat2,
             'doctor_cat3':doctor_cat3,
             'doctor_cat4':doctor_cat4,
             'doctor_cat5':doctor_cat5,
             'doctor_cat6':doctor_cat6,
             'doctor_cat7':doctor_cat7,
             'doctor_cat8':doctor_cat8,
             'doctor_cat9':doctor_cat9,
             'doctor_cat10':doctor_cat10,
             'doctor_cat11':doctor_cat11,
             'doctor_cat12':doctor_cat12,
             'doctor_cat13':doctor_cat13,
             'doctor_cat14':doctor_cat14,
             'doctor_cat15':doctor_cat15,
             'doctor_cat16':doctor_cat16,
             'doctor_cat17':doctor_cat17,
             'doctor_cat18':doctor_cat18,
             'doctor_cat19':doctor_cat19,
             'doctor_cat20':doctor_cat20,
             'doctor_cat21':doctor_cat21,
             'doctor_cat22':doctor_cat22,
             'doctor_cat23':doctor_cat23,
             'doctor_cat24':doctor_cat24,
             'doctor_cat25':doctor_cat25,
             'doctor_cat26':doctor_cat26,
             'doctor_cat27':doctor_cat27,
             'doctor_cat28':doctor_cat28,
             'doctor_cat29':doctor_cat29,
             'doctor_cat30':doctor_cat30,
             'doctor_cat31':doctor_cat31,
             'doctor_cat32':doctor_cat32,
             'doctor_cat33':doctor_cat33,
             'doctor_cat34':doctor_cat34,
             'doctor_cat35':doctor_cat35,
             'doctor_cat36':doctor_cat36,
             'doctor_cat37':doctor_cat37,
             'doctor_cat38':doctor_cat38,
             'doctor_cat39':doctor_cat39,
             'doctor_cat40':doctor_cat40,
             'doctor_cat41':doctor_cat41,
             'doctor_cat42':doctor_cat42,
             'doctor_cat43':doctor_cat43,
             'doctor_cat44':doctor_cat44,
             'doctor_cat45':doctor_cat45,
             'doctor_cat46':doctor_cat46,
             'doctor_cat47':doctor_cat47,
             'doctor_cat48':doctor_cat48,
             'doctor_cat49':doctor_cat49,
             }
    return render(request,'doctor.html',context)

def bookappointment(request,id):
    doctors = Doctor.objects.all(status=True);
    doctor_profiles=Doctor.objects.get(id=id)
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    context ={'doctor_profiles':doctor_profiles,
              'doctors':doctors,
              'category': category,
              'setting': setting,
              }
    return render(request,'appointment_form.html',context)

def basic(request):
    context={}
    return render(request,'basic.html',context)

def doctorlist(request):
    doctors = Doctor.objects.all();
    context={'doctors':doctors}
    return render(request,'symptomDoctor.html',context)

def doctor_profile(request,id):
    doctor_profiles=Doctor.objects.get(id=id)
    context ={'doctor_profiles':doctor_profiles}
    return render(request,'fdoctor.html',context)

@login_required(login_url='user_logIn')  # Check login
def Appointment_Book(request,id):
    current_user = request.user
    if request.method == "POST":
        form = BookingForm(request.POST, request.FILES)
        if form.is_valid():
            dat = Booking()
            # get product quantity from form
            dat.first_name = form.cleaned_data['first_name']
            dat.last_name = form.cleaned_data['last_name']
            dat.doctor_name = form.cleaned_data['doctor_name']
            dat.phone = form.cleaned_data['phone']
            dat.address = form.cleaned_data['address']
            dat.city = form.cleaned_data['city']
            dat.country = form.cleaned_data['country']
            dat.gender = form.cleaned_data['gender']
            dat.age = form.cleaned_data['age']
            dat.booking_date = form.cleaned_data['booking_date']
            dat.booking_Time = form.cleaned_data['booking_Time']
            dat.user_id = current_user.id
            dat.ip = request.META.get('REMOTE_ADDR')
            dat.save()


            # Now remove all oder data from the shoping cart
            #ShopCart.objects.filter(user_id=current_user.id).delete()
            # request.session['cart_item']=0
            messages.success(request, 'Your Booking has been completed')
            category = Category.objects.all()
            setting = Setting.objects.get(id=1)
            context = {
                # 'category':category,
                'category': category,
                'setting': setting,
            }

            return render(request, 'book_complete.html', context)
        else:
            messages.warning(request, form.errors)
        #  return HttpResponseRedirect("/order/oder_cart")
    form = BookingForm()
    profile = UserProfile.objects.get(user_id=current_user.id)
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    doctors = Doctor.objects.all();
    doctor_profiles=Doctor.objects.get(id=id)


    context = {
        # 'category':category,
        'profile': profile,
        'form': form,
        'category': category,
        'setting': setting,
        'doctor_profiles':doctor_profiles,
        'doctors':doctors,

    }
    return render(request, 'bookAppointment.html', context)

def Booking_showing(request):
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    current_user = request.user
    books = Booking.objects.filter(user_id=current_user.id)
    context = {
        'category': category,
        'setting': setting,
        'books': books,



    }

    return render(request, 'appointment_booking_show.html', context)

def Doctor_Booking_showing(request):
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    current_user = request.user
    current_user.is_doctor=True
    books = Booking.objects.filter(doctor_name__user_id=current_user.id).order_by('doctor_name__user_id')
    context = {
        'category': category,
        'setting': setting,
        'books': books,



    }

    return render(request, 'doctor_appointment_booking_show.html', context)

def Doctor_Booking_status_change(request):
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    current_user = request.user
    current_user.is_doctor=True
    books = Booking.objects.filter(doctor_name__user_id=current_user.id).order_by('doctor_name__user_id')
    context = {
        'category': category,
        'setting': setting,
        'books': books,



    }

    return render(request, 'status_change.html', context)

"""
def doctor_logIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('fiddoctor')
        else:
            messages.warning(request, 'Your username or password is invalid.')
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    context = {
        'category': category,
        'setting': setting,
    }
    return render(request,'doctor_logIn.html',context)
"""

@login_required(login_url='user_logIn')  # Check login
def Doctor_register(request):
    current_user = request.user
    if request.method == "POST":
        form = DoctorRegister(request.POST, request.FILES)
        if form.is_valid():
            dat = Doctor()
            # get product quantity from form
            dat.name = form.cleaned_data['name']
            dat.d_s_title = form.cleaned_data['d_s_title']
            dat.d_s_text = form.cleaned_data['d_s_text']
            dat.d1 = form.cleaned_data['d1']
            dat.m_t = form.cleaned_data['m_t']
            dat.e_t = form.cleaned_data['e_t']
            dat.m_l = form.cleaned_data['m_l']
            dat.e_l = form.cleaned_data['e_l']
            dat.image = form.cleaned_data['image']
            dat.d2 = form.cleaned_data['d2']
            dat.d3 = form.cleaned_data['d3']
            dat.d4 = form.cleaned_data['d4']
            dat.d5 = form.cleaned_data['d5']
            dat.user_id = current_user.id
            dat.ip = request.META.get('REMOTE_ADDR')
            dat.save()


            # Now remove all oder data from the shoping cart
            #ShopCart.objects.filter(user_id=current_user.id).delete()
            # request.session['cart_item']=0
            messages.success(request, 'Your Register has been completed')
            category = Category.objects.all()
            setting = Setting.objects.get(id=1)

            context = {
                # 'category':category,
                'category': category,
                'setting': setting,

            }

            return render(request, 'doctor_register_complete.html', context)
        else:
            messages.warning(request, form.errors)
        #  return HttpResponseRedirect("/order/oder_cart")
    form = DoctorRegister()
    profile = DoctorProfile.objects.get(user_id=current_user.id)
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    doctor_cat=DoctorCategories.objects.all()


    context = {
        # 'category':category,
        'profile': profile,
        'form': form,
        'category': category,
        'setting': setting,
        'doctor_cat':doctor_cat,

    }
    return render(request, 'doctor_register_Apply.html', context)


def category_doctor(request,id,slug):
    current_user = request.user
    category = DoctorCategories.objects.all()
    #slidding_image = AmbulanceSlidding.objects.all()
    setting= Setting.objects.get(id=1)
    doctor_cat = Doctor.objects.filter(d_s_text_id=id)
    context ={'setting':setting,
              #'slidding_image':slidding_image,
              'category':category,
              'doctor_cat':doctor_cat,

              }
    #return render(request,'category_product.html',context)
    return render(request,'doctorcategory.html',context)


def appointment_delete(request, id):
    url = request.META.get('HTTP_REFERER') #For Redirect
    current_user = request.user
    books = Booking.objects.filter(id=id, doctor_name__user_id=current_user.id)
    books.delete()
    messages.warning(request, 'Your Appointment has been deleted.')
    return HttpResponseRedirect(url)

def user_appointment_delete(request, id):
    url = request.META.get('HTTP_REFERER') #For Redirect
    current_user = request.user
    books = Booking.objects.filter(id=id, user_id=current_user.id)
    books.delete()
    messages.warning(request, 'Your Appointment has been deleted.')
    return HttpResponseRedirect(url)
#def doctor_show_categorywise(request):
    #current_user = request.user
    #category = DoctorCategories.objects.all()
    #slidding_image = AmbulanceSlidding.objects.all()
    #setting= Setting.objects.get(id=1)
    #doctors = Doctor.objects.all();
    #doctor_cat = Doctor.objects.filter(d_s_text__title='Cardiology (Cardiac Imaging)')
    #context ={#'setting':setting,
              #'slidding_image':slidding_image,
              #'category':category,
              #'doctor_cat':doctor_cat,

              #}
    #return render(request,'category_product.html',context)
    #return render(request,'doctor.html',context)




"""
def doctor_signUp(request):
    userForm=forms.DoctorUserForm()
    doctorForm=forms.DoctorRegister()
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    mydict={'userForm':userForm,'doctorForm':doctorForm,'category': category,
            'setting': setting}
    if request.method=='POST':
        userForm=forms.DoctorUserForm(request.POST)
        doctorForm=forms.DoctorRegister(request.POST,request.FILES)
        if userForm.is_valid() and doctorForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            user = authenticate(username=username, password=password_raw)
            if user is not None:
                login(request, user)
            current_user = request.user
            doctor=doctorForm.save(commit=False)
            doctor.user=user
            doctor=doctor.save()
            my_doctor_group = Group.objects.get_or_create(name='DOCTOR')
            my_doctor_group[0].user_set.add(user)
        return HttpResponseRedirect('doctor_logIn')
    return render(request,'doctorsignup.html',context=mydict)

def is_doctor(user):
    return user.groups.filter(name='DOCTOR').exists()

def afterlogin_view(request):
    if is_doctor(request.user):
        accountapproval=models.Doctor.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('doctor-dashboard')


def doctorclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'doctor_logIn.html')
"""