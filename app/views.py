from django.shortcuts import render

# Create your views here.
def fun(request):
    d={'a':90}
    return render(request,'fun.html',context=d)
