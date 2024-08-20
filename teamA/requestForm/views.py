from django.shortcuts import render, redirect
from .forms import RequestForm
from django.http import Http404
from django.contrib import messages
from django.core.mail import send_mail

def request(request):
    # フォームの内容をDBに保存
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            
            name = request.POST.get('name')
            mail = request.POST.get('mail')
            system_name = request.POST.get('system_name')
            system_overview = request.POST.get('system_overview')

            # メッセージの内容を作成
            message = f"""
            氏名: {name}
            メールアドレス: {mail}
            システム名: {system_name}
            システム内容:
            {system_overview}
            """
            
            # 確認メールを送信
            send_mail(
                'システム要望依頼',  # 件名
                message,  # メッセージ
                'noreply.figcom@gmail.com',  # 送信元のメールアドレス
                ['figcom@googlegroups.com'],  # 送信先のメールアドレスのリスト
                fail_silently=False,
            )
            
            messages.info(request, f'送信が完了しました！')
            return redirect('index')
    else:
        raise Http404()
    
    messages.info(request, f'送信できませんでした')
    return redirect('index')
