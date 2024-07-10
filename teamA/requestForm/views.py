from django.shortcuts import render, redirect
from .forms import RequestForm

def request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RequestForm()
    
    return render(request, 'index.html', {'form': form})
