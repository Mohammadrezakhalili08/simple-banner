from django.shortcuts import render

# Create your views here.
def anothepage (request):
    return render(request,'banner/another_page.html',context={})
def contact (request):
    return render(request,'banner/contact.html',context={})
def examples (request):
    return render(request,'banner/examples.html',context={})
def index (request):
    return render(request,'banner/index.html',context={})
def page (request):
    return render(request,'banner/page.html',context={})
def sign (request):
    return render(request,'banner/sign.html',context={})
