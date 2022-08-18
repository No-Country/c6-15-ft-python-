from django.shortcuts import render
from sitter.forms import SitterForm
# Create your views here.


def create_sitter(request):
    if request.user.is_authenticated:
        form = SitterForm(request.POST or None)
        if form.is_valid():
            form.save()
        context = {
            'form': form,
        }
        return render(request, 'sitter.html', context)
    else:
        return render(request, 'sitter.html')