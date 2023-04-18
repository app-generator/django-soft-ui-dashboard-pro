from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    # Page from the theme 
    return render(request, 'pages/dashboards/default.html')

def wizard(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        # ...
        # here you can send all the information as a post request.
        print(first_name, last_name, email)
    return render(request, 'pages/applications/wizard.html')