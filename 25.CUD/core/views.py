from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm,SetPasswordForm,UserChangeForm
from . forms import Register,ChangeUserDetail,ChangeAdminDetail
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.http import HttpResponse

# Create your views here.
def signup(request):
    if request.method == 'POST':
        mf= Register(request.POST)
        if mf.is_valid():
            mf.save()
            messages.success(request,'Registration Successful ! ')
            return redirect('/')
    else:
        mf = Register()
    return render(request,'core/index.html',{'mf':mf})


def log_in(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            mf = AuthenticationForm(request,data=request.POST)
            if mf.is_valid():
                un = mf.cleaned_data['username']
                pw = mf.cleaned_data['password']
                user=authenticate(username=un,password=pw)
                if user is not None:
                    login(request,user)
                    # return HttpResponse('login successful!')
                    # return render(request,'core/success.html')
                    return redirect('/profile/')
        else:
            mf=AuthenticationForm()
        return render(request,'core/log_in.html',{'mf':mf})
    else:
        return redirect('/profile/')


def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.is_superuser == True:
                mf= ChangeAdminDetail(request.POST,instance=request.user)
            else:
                mf=ChangeUserDetail(request.POST,instance=request.user)
            if mf.is_valid():
                mf.save()
                return redirect('/profile/')
        else:
            if request.user.is_superuser == True:
                mf= ChangeAdminDetail(instance=request.user)
            else:
                mf=ChangeUserDetail(instance=request.user)
        return render(request,'core/profile.html',{'mf':mf})
    else:
        return redirect('/login/')

def log_out(request):
    logout(request)
    return redirect('/login/')


def pcf(request):
    if request.method == 'POST':
        mf=PasswordChangeForm(user=request.user,data=request.POST)
        if mf.is_valid():
            mf.save()
            update_session_auth_hash(request,mf.user)   # prevent from automatic logout
            return redirect('/profile/')
    else:
        mf = PasswordChangeForm(user=request.user)
    return render(request,'core/pcf.html',{'mf':mf})

def spf(request):
    if request.method == 'POST':
        mf=SetPasswordForm(user=request.user,data=request.POST)
        if mf.is_valid():
            mf.save()
            update_session_auth_hash(request,mf.user)
            return redirect('/profile/')
    else:
        mf = SetPasswordForm(user=request.user)
    return render(request,'core/spf.html',{'mf':mf})


def success(request):
    return render(request,'core/success.html')



