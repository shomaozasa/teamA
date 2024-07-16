from .models import Work, UsedLang, Image
from django.shortcuts import render
from django.core.paginator import Paginator

# ホーム画面
def index(request, page=1):
    # ページネーション用の変数
    display_num = 4
    page_num = page * display_num
    on_each_side = 2
    works_contents = []

    # DBから作品と画像のデータ取得
    all_works = Work.objects.order_by('-id').all()
    works = all_works[page_num - display_num:page_num]
    for work in works:
        image_path = Image.objects.filter(work_id=work.id).first()
        works_contents.append({
            'work': work,
            'image_path': image_path
        })

    # ページネーションリンク
    data_page = Paginator(all_works, display_num)
    data_p = data_page.get_page(page)
    data_list = data_p.paginator.get_elided_page_range(page, on_each_side=on_each_side)
    
    context = {
        'works': works_contents,
        'data_p': data_p,
        'data_list': data_list,
    }
    return render(request, 'index.html', context)

# 詳細画面
def detail(request, pk):
    work = Work.objects.filter(id=pk).first()
    usedlang = UsedLang.objects.filter(work_id=pk)
    image = Image.objects.filter(work_id=pk)

    context = {
        'work': work,
        'usedlang': usedlang,
        'image': image,
    }
    return render(request, 'detail.html', context)