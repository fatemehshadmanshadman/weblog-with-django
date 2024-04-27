from django.shortcuts import render,redirect,HttpResponse
# from symbol import decorated
from . import models,forms
from django.contrib.auth.decorators import login_required

def list(request):
    articles=models.Articles.objects.all()
    arg={'articles':articles}
    return render(request,'articles/list.html',arg)

def detail(request,slug):
    # return HttpResponse(slug)
    arti=models.Articles.objects.get(slug=slug)
    return render(request,'articles/detail.html',{'arti':arti})

@login_required(login_url="/accounts/login") # type: ignore
def create_article(request):
    if request.method=='POST':
        form=forms.CreateArticle(request.POST,request.FILES)
        if form.is_valid():
            temp=form.save(commit=False)
            temp.author=request.user
            temp.save()
            return redirect('home')    
    else:    
    # elif request.method=='GET': #be khater dokme ijad maghale ino gozashatam
        form=forms.CreateArticle()
        return render(request,'articles/create.html',{'form':form})
