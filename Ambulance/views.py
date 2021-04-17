from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from django.contrib import messages
from MediSeApp.models import Setting,ContactMessage,ContactForm
from medishop.models import Slidding
from Product.models import Product,Images,Category,Comment
from medishop.forms import SearchForm
from OrderApp.models import ShopCart
from OrderApp.views import *
from django.conf import settings
User = settings.AUTH_USER_MODEL
from .models import *
from .forms import *
from Accounts.models import DriverProfile
# Create your views here.
def ambulanceHome(request):

    category = AmbulanceCategory.objects.all()
    setting = Setting.objects.get(id=1)
    slidding_image = AmbulanceSlidding.objects.all()
    latest_ambulance = Ambulace.objects.all().order_by('-id')
    image_ambulance = Ambulace.objects.all().order_by('id')[:3]
    specific_ambulance = Ambulace.objects.filter().order_by('location')[0::]
    ambulance_cat1 = Ambulace.objects.filter(location__title='Chandonaish')
    ambulance_cat2 = Ambulace.objects.filter(location__title='Chittagong')
    ambulance_cat3= Ambulace.objects.filter(location__title='Dohazari')
    ambulance_cat4 = Ambulace.objects.filter(location__title='Lohagara')
    ambulance_cat5 = Ambulace.objects.filter(location__title='Patiya')
    ambulance_cat6 = Ambulace.objects.filter(location__title='Satkania')

    #ambulance_cat = Ambulace.objects.filter(location_id=id)
    context = {
        'category': category,
        'setting': setting,
        'slidding_image':slidding_image,
        'latest_ambulance':latest_ambulance,
        'image_ambulance':image_ambulance,
        'specific_ambulance':specific_ambulance,
        'ambulance_cat1':ambulance_cat1,
        'ambulance_cat2':ambulance_cat2,
        'ambulance_cat3':ambulance_cat3,
        'ambulance_cat4':ambulance_cat4,
        'ambulance_cat5':ambulance_cat5,
        'ambulance_cat6':ambulance_cat6,


    }
    return render(request,'ambulanceHome.html',context)

@login_required(login_url='driver_logIn')  # Check login
def Ambulance_register(request):
    current_user = request.user
    current_user.is_driver=True
    if request.method == "POST":
        form = AmbulanceRegister(request.POST, request.FILES)
        if form.is_valid():
            dat = Ambulace()
            # get product quantity from form
            dat.name = form.cleaned_data['name']
            dat.driver_name = form.cleaned_data['driver_name']
            dat.location= form.cleaned_data['location']
            #dat.location=AmbulanceCategory.objects.get(id=location_id)
            #dat.form_location = form.cleaned_data['form_location']
            dat.phone = form.cleaned_data['phone']
            dat.image = form.cleaned_data['image']
            dat.discription = form.cleaned_data['discription']
            dat.user_id = current_user.id
            dat.ip = request.META.get('REMOTE_ADDR')
            dat.save()


            # Now remove all oder data from the shoping cart
            #ShopCart.objects.filter(user_id=current_user.id).delete()
            # request.session['cart_item']=0
            messages.success(request, 'Your Register has been completed')
            category = AmbulanceCategory.objects.all()
            setting = Setting.objects.get(id=1)

            context = {
                # 'category':category,
                'category': category,
                'setting': setting,

            }

            return render(request, 'ambulanceregister_complete.html', context)
        else:
            messages.warning(request, form.errors)
        #  return HttpResponseRedirect("/order/oder_cart")
    form = AmbulanceRegister()
    profile = DriverProfile.objects.get(user_id=current_user.id)
    category = AmbulanceCategory.objects.all()
    setting = Setting.objects.get(id=1)
    #doctor_cat=DoctorCategories.objects.all()


    context = {
        # 'category':category,
        'profile': profile,
        'form': form,
        'category': category,
        'setting': setting,
        #'doctor_cat':doctor_cat,

    }
    return render(request, 'driver_register_Apply.html', context)

def ambulance_single_profile(request,id):
    current_user = request.user
    setting= Setting.objects.get(id=1)
    category = AmbulanceCategory.objects.all()
    single_ambulance = Ambulace.objects.get(id=id)
    #images = Images.objects.filter(product_id=id)
    feature_ambulance = Ambulace.objects.all().order_by('id')[:4]
    ambulance_cat = Ambulace.objects.filter(location_id=id)
    comment_show = Comment.objects.filter(product_id=id, status='True')
    context = {'setting':setting,
               'category':category,
               'ambulance_cat':ambulance_cat,
               'single_ambulance':single_ambulance,
               'comment_show': comment_show,
               'feature_ambulance':feature_ambulance,

               }
    return render(request,'single-ambulance-profile.html',context)

def category_ambulance(request,id,slug):
    current_user = request.user
    category = AmbulanceCategory.objects.all()
    slidding_image = AmbulanceSlidding.objects.all()
    setting= Setting.objects.get(id=1)
    ambulance_cat = Ambulace.objects.filter(location_id=id)
    context ={'setting':setting,
              'slidding_image':slidding_image,
              'category':category,
              'ambulance_cat':ambulance_cat,

              }
    #return render(request,'category_product.html',context)
    return render(request,'ambulancecategory.html',context)

