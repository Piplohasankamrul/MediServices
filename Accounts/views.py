from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth import logout, authenticate, login, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from MediSeApp.models import Setting
from Product.models import Product,Images,Category,Comment

# Create your views here.
def home(request):
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    slidding = HomeSlidding.objects.all()
    context = {
        'category': category,
        'setting': setting,
        'slidding': slidding,
    }
    return render(request,'home.html',context)
def doctorDashboard(request):
    context={}
    return render(request,'doctorDashboard.html',context)
def driverDashboard(request):
    context={}
    return render(request,'driverDashboard.html',context)

def user_logIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, 'Your username or password is invalid.')
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    context = {
        'category': category,
        'setting': setting,
    }
    return render(request,'userlogin.html',context)

def doctor_logIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('doctorDashboard')
        else:
            messages.warning(request, 'Your username or password is invalid.')
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    context = {
        'category': category,
        'setting': setting,
    }
    return render(request,'doctorlogin.html',context)

def driver_logIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('driverDashboard')
        else:
            messages.warning(request, 'Your username or password is invalid.')
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    context = {
        'category': category,
        'setting': setting,
    }
    return render(request,'driverlogin.html',context)

def user_logout(request):
    logout(request)
    return redirect('home')

def doctor_logout(request):
    logout(request)
    return redirect('home')

def driver_logout(request):
    logout(request)
    return redirect('home')



def user_register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password_raw = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password_raw)
            #user = super().save(commit=False)
            user.is_user=True
            if user is not None:
                login(request, user)
            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.image = "user_img/avatar.jpg"
            data.save()
            return redirect('home')

        else:
            messages.warning(request, "Your new and reset password is not matching")
    else:
        form = SignUpForm()
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    context = {'category': category,
               'setting': setting,#
               'form': form}
    return render(request, 'userRegister.html', context)

def doctor_register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password_raw = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password_raw)
            #user = super().save(commit=False)
            user.is_doctor=True
            if user is not None:
                login(request, user)
            current_user = request.user
            data = DoctorProfile()
            data.user_id = current_user.id
            data.image = "user_img/avatar.jpg"
            data.save()
            return redirect('doctorDashboard')

        else:
            messages.warning(request, "Your new and reset password is not matching")
    else:
        form = SignUpForm()
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    context = {'category': category,
               'setting': setting,
               'form': form}
    return render(request, 'userRegister.html', context)

def driver_register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password_raw = form.cleaned_data.get('password1')
            #user = super().save(commit=False)

            user = authenticate(username=username, password=password_raw)
            user.is_driver=True
            if user is not None:
                login(request, user)
            current_user = request.user
            data = DriverProfile()
            data.user_id = current_user.id
            data.image = "user_img/avatar.jpg"
            data.save()
            return redirect('driverDashboard')

        else:
            messages.warning(request, "Your new and reset password is not matching")
    else:
        form = SignUpForm()
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    context = {'category': category,
               'setting': setting,
               'form': form}
    return render(request, 'userRegister.html', context)

def userprofile(request):
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)

    context = {'category': category,
               'setting': setting,
               'profile': profile}
    return render(request, 'user_profile.html', context)

def doctorprofile(request):
    #category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    current_user = request.user
    profiles = DoctorProfile.objects.get(user_id=current_user.id)

    context = {#'category': category,
        'setting': setting,
        'profiles': profiles}
    return render(request, 'doctorDashboard.html', context)


def driverprofile(request):
    #category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    current_user = request.user
    profiles = DriverProfile.objects.get(user_id=current_user.id)

    context = {#'category': category,
        'setting': setting,
        'profiles': profiles}
    return render(request, 'driverDashboard.html', context)

@login_required(login_url='user_logIn')  # Check login
def user_update(request):
    if request.method == 'POST':
        # request.user is user  data
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('userprofile')
    else:
        # category = Category.objects.all()
        user_form = UserUpdateForm(instance=request.user)
        # "userprofile" model -> OneToOneField relatinon with user
        profile_form = ProfileUpdateForm(instance=request.user)
        category = Category.objects.all()
        setting = Setting.objects.get(id=1)
        context = {
            # 'category': category,
            'user_form': user_form,
            'profile_form': profile_form,
            'category': category,
            'setting': setting,
        }
        return render(request, 'userupdate.html', context)


@login_required(login_url='/user_logIn')  # Check login
def user_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('userprofile')
        else:
            messages.error(
                request, 'Please correct the error below.<br>' + str(form.errors))
            return redirect('user_password')
    else:
        category = Category.objects.all()
        setting = Setting.objects.get(id=1)
        form = PasswordChangeForm(request.user)
        return render(request, 'userpasswordupdate.html', {'form': form,
                                                           'category': category,
                                                           'setting': setting,

                                                           })

@login_required(login_url='doctor_logIn')  # Check login
def doctor_update(request):
    if request.method == 'POST':
        # request.user is user  data
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = DoctorProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.doctorprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('doctorprofile')
    else:
        # category = Category.objects.all()
        user_form = UserUpdateForm(instance=request.user)
        # "userprofile" model -> OneToOneField relatinon with user
        profile_form = DoctorProfileUpdateForm(instance=request.user)
        category = Category.objects.all()
        setting = Setting.objects.get(id=1)
        context = {
            # 'category': category,
            'user_form': user_form,
            'profile_form': profile_form,
            'category': category,
            'setting': setting,
        }
        return render(request, 'doctorupdate.html', context)


@login_required(login_url='doctor_logIn')  # Check login
def doctor_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('doctorprofile')
        else:
            messages.error(
                request, 'Please correct the error below.<br>' + str(form.errors))
            return redirect('doctor_password')
    else:
        category = Category.objects.all()
        setting = Setting.objects.get(id=1)
        form = PasswordChangeForm(request.user)
        return render(request, 'doctorpasswordupdate.html', {'form': form,
                                                           'category': category,
                                                           'setting': setting,

                                                           })

@login_required(login_url='driver_logIn')  # Check login
def driver_update(request):
    if request.method == 'POST':
        # request.user is user  data
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = DriverProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.driverprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('driverprofile')
    else:
        # category = Category.objects.all()
        user_form = UserUpdateForm(instance=request.user)
        # "userprofile" model -> OneToOneField relatinon with user
        profile_form = DriverProfileUpdateForm(instance=request.user)
        category = Category.objects.all()
        setting = Setting.objects.get(id=1)
        context = {
            # 'category': category,
            'user_form': user_form,
            'profile_form': profile_form,
            'category': category,
            'setting': setting,
        }
        return render(request, 'driverupdate.html', context)



@login_required(login_url='driver_logIn')  # Check login
def driver_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('driverprofile')
        else:
            messages.error(
                request, 'Please correct the error below.<br>' + str(form.errors))
            return redirect('driver_password')
    else:
        category = Category.objects.all()
        setting = Setting.objects.get(id=1)
        form = PasswordChangeForm(request.user)
        return render(request, 'driverpasswordupdate.html', {'form': form,
                                                           'category': category,
                                                           'setting': setting,

                                                           })


@login_required(login_url='user_logIn')
def usercomment(request):
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    current_user = request.user
    comment = Comment.objects.filter(user_id=current_user.id)
    context = {
        'category': category,
        'setting': setting,
        'comment': comment

    }
    return render(request, 'usercomment.html', context)


def comment_delete(request, id):
    current_user = request.user
    comment = Comment.objects.filter(user_id=current_user.id, id=id)
    comment.delete()
    messages.success(request, 'Your comment is successfully deleted')
    return redirect('usercomment')