from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def more(request):
    return render(request,'more.html')

def service(request):
    return render(request,'service.html')

def innerpage(request):
    return render(request,'innerpage.html')
