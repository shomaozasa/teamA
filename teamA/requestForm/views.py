from django.shortcuts import render, redirect
from .forms import RequestForm
from django.http import Http404

def request(request):
    # フォームの内容をDBに保存
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        raise Http404()

    return redirect('index')
