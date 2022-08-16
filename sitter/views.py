from django.shortcuts import render

# Create your views here.
def sitter(request):
    return render(request, 'sitter/sitter.html')