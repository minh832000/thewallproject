from django.shortcuts import render

# Create your views here.
def listCompany(request):
    return render(request,'company-list.html')