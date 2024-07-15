from django.shortcuts import render, redirect
from .forms import RequestForm

def request(request):
    # フォームの内容をDBに保存
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RequestForm()

    context = {
        'form': form,
    }
    return render(request, 'index.html', context)
