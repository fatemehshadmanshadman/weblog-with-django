from email.mime import audio
from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login as log_in , logout as log_out

# def accounts(request):
#     return HttpResponse("accounts list")

def signup(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=UserCreationForm()
        return render(request,'accounts/signup.html',{'form':form})
    
def login(request):
    if request.method=="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            log_in(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else :
                return redirect('accounts:login')
        else:
            return HttpResponse("password not corecct")
    else:
        form=AuthenticationForm()
        return render(request,'accounts/login.html',{'form':form})
    
def logout(request):
    if request.method=="POST":
        log_out(request)
        return redirect('home')
        # return HttpResponse("logout")
    else:
        log_out(request)
        return redirect('home')
        # return HttpResponse("logout")