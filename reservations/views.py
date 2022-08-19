from django.shortcuts import render

# Create your views here.
def create_reservation(request):
    return render(request, 'homepage/homepage.html')