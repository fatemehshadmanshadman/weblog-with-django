from django.shortcuts import render
from django.shortcuts import HttpResponse

# def about(request):
#     # return HttpResponse('i,m there')
#     return render(request,'about.html')

def home(request):
    # return HttpResponse("It's home")
    return render(request,'base.html')