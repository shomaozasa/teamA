from django.template import loader
from .models import Work, UsedLang, Image, Language
from django.shortcuts import render


# ホーム画面
def index(request, page=1):
    work = Work.objects.all()
    usedlang = UsedLang.objects.all()
    image = Image.objects.all()

    context = {
        'work':work,
        'usedlang': usedlang,
        'image':image,
    }

    return render(request, 'index.html', context)

# 詳細画面
def detail(request, pk):
    work = Work.objects.filter(id=pk)
    usedlang = UsedLang.objects.filter(work_id=pk)
    image = Image.objects.filter(work_id=pk)

    for i in usedlang:
        print(i)
        print(i.language_id.name)
        # lang.append(Language.objects.filter(id=i.language_id))
    

    context = {
        'work':work,
        'usedlang':usedlang,
        'image':image,
    }
    return render(request, 'detail.html', context)