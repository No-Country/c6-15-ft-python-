from django.shortcuts import render

# Create your views here.
def pets(request):
    return render(request, 'homepage/index.html', )