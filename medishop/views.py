from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from django.contrib import messages
from MediSeApp.models import Setting,ContactMessage,ContactForm
from medishop.models import Slidding,Cover
from Product.models import Product,Images,Category,Comment
from medishop.forms import SearchForm
from OrderApp.models import ShopCart
from OrderApp.views import *
from django.conf import settings
User = settings.AUTH_USER_MODEL
# Create your views here.
def medihome(request):
    current_user = request.user
    current_user.is_user=True
    cart_product = ShopCart.objects.filter(user_id=current_user.id)
    total_amount = 0
    for p in cart_product:
        total_amount += p.product.new_price*p.quantity
    total_quantity =0
    for q in cart_product:
        total_quantity += q.quantity
    category = Category.objects.all()
    setting= Setting.objects.get(id=1)
    slidding_image = Slidding.objects.all()
    cover = Cover.objects.filter().order_by('id')[:1]
    banner = Cover.objects.filter().order_by('id')[1:]
    latest_product = Product.objects.all().order_by('-id')
    tranding_product = Product.objects.all().order_by('id')[4:8]
    flash_product = Product.objects.all().order_by('id')[8:]
    feature_product = Product.objects.all()

    context={'cart_product': cart_product,
             'total_amount': total_amount,
             'setting':setting,
             'category':category,
             'slidding_image':slidding_image,
             'latest_product':latest_product,
             'feature_product':feature_product,
             'total_quantity':total_quantity,
             'cover':cover,
             'banner':banner,
             'tranding_product':tranding_product,
             'flash_product': flash_product,

             }
    return render(request, 'mediHome.html', context)


def About(request):
    category = Category.objects.all()
    setting= Setting.objects.get(id=1)
    context={'category':category,
        'setting':setting}
    return render(request,'about-us.html',context)

def Contact(request):
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            message.success(request,'Your message has been sent')

            return redirect('Contact')
    setting= Setting.objects.get(pk=1)
    category = Category.objects.all()
    form = ContactForm
    context={'category':category,
             'setting':setting,
             'form':form}
    return render(request,'contact.html',context)

    #setting= Setting.objects.get(id=1)
    #context={'category':category,
        #'setting':setting}
    #return render(request,'contact.html',context)

def SearchView(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            cat_id = form.cleaned_data['cat_id']
            if cat_id == 0:
                product_cat = Product.objects.filter(title__icontains=query)
            else:
                product_cat = Product.objects.filter(
                    title__icontains=query, category_id=cat_id)
            category = Category.objects.all()
            slidding_image = Slidding.objects.all()
            setting = Setting.objects.get(pk=1)
            context = {
                'category': category,
                'query': query,
                'product_cat': product_cat,
                'slidding_image': slidding_image,
                'setting': setting
            }
            return render(request, 'cat.html', context)
    return HttpResponseRedirect('category_product')



def product_single_profile(request,id):
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
    single_product = Product.objects.get(id=id)
    images = Images.objects.filter(product_id=id)
    feature_product = Product.objects.all().order_by('id')[:4]
    product_cat = Product.objects.filter(category_id=id)
    comment_show = Comment.objects.filter(product_id=id, status='True')
    context = {'setting':setting,
               'category':category,
               'product_cat':product_cat,
               'single_product':single_product,'images':images,
               'feature_product':feature_product,
               'cart_product': cart_product,
               'total_amount': total_amount,
               'total_quantity':total_quantity,
               'comment_show': comment_show,
               }
    return render(request,'single-product-profile.html',context)

def category_product(request,id,slug):
    current_user = request.user
    cart_product = ShopCart.objects.filter(user_id=current_user.id)
    total_amount = 0
    for p in cart_product:
        total_amount += p.product.new_price*p.quantity
    total_quantity =0
    for q in cart_product:
        total_quantity += q.quantity
    category = Category.objects.all()
    slidding_image = Slidding.objects.all()
    setting= Setting.objects.get(id=1)
    product_cat = Product.objects.filter(category_id=id)
    context ={'setting':setting,
              'slidding_image':slidding_image,
              'category':category,
              'product_cat':product_cat,
              'cart_product': cart_product,
              'total_amount': total_amount,
              'total_quantity':total_quantity,
              }
    #return render(request,'category_product.html',context)
    return render(request,'cat.html',context)