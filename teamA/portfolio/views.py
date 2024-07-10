from .models import Work, UsedLang, Image, Language
from django.shortcuts import render

# ホーム画面
def index(request, page=1):
    display_num = 4
    page_num = page * display_num
    work = Work.objects.order_by('-id').all()[page_num - display_num:page_num]
    image = Image.objects.all()

    context = {
        'work': work,
        'image': image,
    }
    return render(request, 'index.html', context)

# 詳細画面
def detail(request, pk):
    work = Work.objects.filter(id=pk)
    usedlang = UsedLang.objects.filter(work_id=pk)
    image = Image.objects.filter(work_id=pk)

    context = {
        'work': work,
        'usedlang': usedlang,
        'image': image,
    }
    return render(request, 'detail.html', context)