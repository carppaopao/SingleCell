from django.shortcuts import render
from django.http import HttpResponse
from app01 import models
from django.utils.safestring import mark_safe    #传入格式字符串转为html
from app01.utils.pagination import Pagination    #导入封装的分页功能
from django.db.models import Q
from django.http import FileResponse
from django.http import StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(req):
#搜索功能：

    # dict ={}
    # search = req.GET.get("q","")
    # if search:
    #     dict ["zone"]= search
    # queryset = models.tliver.objects.filter(**dict).order_by("-cell_type").values()

    search = req.GET.get("q","")
    field = req.GET.get("field")

    if field == 'zone':
        if search:
           queryset = models.tliver1.objects.filter(zone__icontains=search).order_by("-cell_type").values()
        else:
            queryset = models.tliver1.objects.all().order_by("-cell_type").values()

    elif field == 'run_id':
        if search:
            queryset = models.tliver1.objects.filter(run_id__icontains=search).order_by("-cell_type").values()
        else:
            queryset = models.tliver1.objects.all().order_by("-cell_type").values()

    elif field == 'cell_type':
        if search:
            queryset = models.tliver1.objects.filter(cell_type__icontains=search).order_by("-cell_type").values()
        else:
            queryset = models.tliver1.objects.all().order_by("-cell_type").values()

    elif field == 'time_point':
        if search:
            queryset = models.tliver1.objects.filter(time_point__icontains=search).order_by("-cell_type").values()
        else:
            queryset = models.tliver1.objects.all().order_by("-cell_type").values()

    else:
        queryset = models.tliver1.objects.all().order_by("-cell_type").values()

#分页功能：
    #1. 筛选分页数据
    #2. 实例化分类对象
    page_object = Pagination(req, queryset)

    # 调用对象的html方法,生成页码
    page_object.pagenum()

    head_page = page_object.head_page
    end_page = page_object.end_page

    data = list(page_object.page_queryset)

#科学计数法
    for item in data:
        valueX = float(item.get('UMAP_X'))

        valueY = float(item.get('UMAP_Y'))

        formattedX = format_scientific(valueX)
        formattedY = format_scientific(valueY)

        item['UMAP_X'] = formattedX
        item['UMAP_Y'] = formattedY


    context = {
        "res": page_object.page_queryset,   # 分页的数据
        "search": search,                   # 搜索的内容
        "page_string": page_object.page_string,     # 页码
        "head_page": head_page,             # 首页
        "end_page": end_page,               # 尾页
        "field": field,
    }

    return render(req, "home.html",context)

#下载总的
def download_file(req):

    def down_chunk_file_manager(file_path, chuck_size=1024):
        with open(file_path, "rb") as file:
            while True:
                chuck_stream = file.read(chuck_size)
                if chuck_stream:
                    yield chuck_stream
                else:
                    break

    file_path = "D:\Scliver.txt"
    response = StreamingHttpResponse(down_chunk_file_manager(file_path))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file_path)
 
    return response


#科学计数转换
def format_scientific(value):
    return '{:.2e}'.format(value)  # 使用适当的格式化方式进行科学计数转换
