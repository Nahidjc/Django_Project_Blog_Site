from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from Login_App.forms import SignUp,UserChange,ProfilePic
def Sign_Up(request):
    form = SignUp()
    registered = False
    if request.method == "POST":
        form = SignUp(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True
    dict = {'form':form,'registered':registered}
    return render(request,'Login_App/sign_up.html',context=dict)
def Login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user= authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
    return render(request,'Login_App/login.html',context={'form':form})
@login_required()
def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
@login_required
def profile(request):
    return render(request,'Login_App/profile.html',context={})
@login_required
def user_change(request):
    current_user = request.user
    form = UserChange(instance=current_user)
    if request.method == "POST":
        form = UserChange(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            form = UserChange(instance=current_user)
    return render(request,'Login_App/change_profile.html',context={'form':form})
@login_required
def pass_change(request):
    current_user = request.user
    changed= False
    form = PasswordChangeForm(current_user)
    if request.method == "POST":
        form = PasswordChangeForm(current_user,data=request.POST)
        if form.is_valid():
            form.save()
            changed = True
    return render(request,'Login_App/pass_change.html',context={'form':form,'changed':changed})
@login_required
def add_pro_pic(request):
    form=ProfilePic()
    if request.method=='POST':
        form=ProfilePic(request.POST,request.FILES)
        if form.is_valid():
            user_obj=form.save(commit=False)
            user_obj.user=request.user
            user_obj.save()
            return HttpResponseRedirect(reverse('Login_App:profile'))
    return render(request,'Login_App/add_pro_pic.html',context={'form':form})
@login_required
def change_pro_pic(request):
    form = ProfilePic(instance=request.user.user_profile)
    if request.method=='POST':
        form=ProfilePic(request.POST,request.FILES,instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Login_App:profile'))
    return render(request,'Login_App/add_pro_pic.html',context={'form':form})
