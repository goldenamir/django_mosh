from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def sayHello(request):
    #return HttpResponse('Hello World')
    #return render(request,'hello.html')
    return render(request,'hello.html',{'name':'Amir'})