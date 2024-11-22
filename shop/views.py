from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')


def base(request):
    return render(request, 'base.html')


def starter_page(request):
    return render(request, 'starter_page.html')


def services(request):
    return render(request, 'services.html')


def appointment(request):
    return render(request, 'appointment.php')


def contact(request):
    return render(request, 'contact.php')