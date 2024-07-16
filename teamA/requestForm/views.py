from django.shortcuts import render, redirect
from .forms import RequestForm
from django.http import Http404
from django.contrib import messages

def request(request):
    # フォームの内容をDBに保存
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, f'送信完了しました！')
            return redirect('index')
    else:
        raise Http404()
    
    messages.info(request, f'送信できませんでした。')
    return redirect('index')
