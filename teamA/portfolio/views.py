from django.http import HttpResponse
from django.template import loader

# ホーム画面
def index(request, page=1):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

# 詳細画面
def detail(request, pk):
    template = loader.get_template('detail.html')
    return HttpResponse(template.render({'pk': pk}, request))