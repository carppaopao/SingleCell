from django.shortcuts import render
from django.http import HttpResponse
from app01 import models
from django.utils.safestring import mark_safe    #传入格式字符串转为html
from app01.utils.pagination import Pagination    #导入封装的分页功能
from django.db.models import Q
from django.http import FileResponse
from django.http import StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


# Create your views here.

def test(req):
#获取参数：
    search = req.GET.get("q","")
    field = req.GET.get("field")
#调用搜索功能：
    queryset=query(req,search,field)
#调用分页功能：
    page_queryset,data,page_string,head_page,end_page=page(req,queryset)
#调用科学计数法:
    for item in data:
        valueX = float(item.get('UMAP_X'))
        valueY = float(item.get('UMAP_Y'))
        formattedX = format_scientific(valueX)
        formattedY = format_scientific(valueY)
        item['UMAP_X'] = formattedX
        item['UMAP_Y'] = formattedY

    context = {
        "queryset": queryset,
        "res": page_queryset,   # 分页的数据
        "search": search,                   # 搜索的内容
        "page_string": page_string,     # 页码
        "head_page": head_page,             # 首页
        "end_page": end_page,               # 尾页
        "field": field,
    }

    return render(req, "test.html",context)

##搜索功能在此
def query(req,search,field):
    
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

    return queryset
###分页功能在此
def page(req,queryset):
    page_object = Pagination(req, queryset)
    # 调用对象的html方法,生成页码
    page_object.pagenum()

    head_page = page_object.head_page
    end_page = page_object.end_page
    data = list(page_object.page_queryset)
    page_queryset=page_object.page_queryset 
    page_string= page_object.page_string

    return page_queryset,data,page_string,head_page,end_page
##下载总的在此
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
##科学计数在此
def format_scientific(value):
    return '{:.2e}'.format(value)  # 使用适当的格式化方式进行科学计数转换



def t1(req):
    count = int(req.GET.get('count', 0))
    if count % 2 == 0:
        result = 'test1'
    else:
        result = 'test2'
    return JsonResponse({'result': result})


def test1(req):
#获取参数：
#调用搜索功能：
    search=req.GET.get('q')
    field= req.GET.get('field')

    queryset=query(req,search,field)
    queryset = queryset.order_by("cell_type").values()
#调用分页功能：
    page_queryset,data,page_string,head_page,end_page=page(req,queryset)
#调用科学计数法:
    for item in data:
        valueX = float(item.get('UMAP_X'))
        valueY = float(item.get('UMAP_Y'))
        formattedX = format_scientific(valueX)
        formattedY = format_scientific(valueY)
        item['UMAP_X'] = formattedX
        item['UMAP_Y'] = formattedY

    context = {
        "res": page_queryset,   # 分页的数据
        "search": search,                   # 搜索的内容
        "page_string": page_string,     # 页码
        "head_page": head_page,             # 首页
        "end_page": end_page,               # 尾页
        "field": field,
    }
    return render(req, "test.html",context)

def test2(req):
#获取参数：
#调用搜索功能：
    search=req.GET.get('q')
    field= req.GET.get('field')

    queryset=query(req,search,field)
    queryset = queryset.order_by("-cell_type").values()
#调用分页功能：
    page_queryset,data,page_string,head_page,end_page=page(req,queryset)
#调用科学计数法:
    for item in data:
        valueX = float(item.get('UMAP_X'))
        valueY = float(item.get('UMAP_Y'))
        formattedX = format_scientific(valueX)
        formattedY = format_scientific(valueY)
        item['UMAP_X'] = formattedX
        item['UMAP_Y'] = formattedY

    context = {
        "res": page_queryset,   # 分页的数据
        "search": search,                   # 搜索的内容
        "page_string": page_string,     # 页码
        "head_page": head_page,             # 首页
        "end_page": end_page,               # 尾页
        "field": field,
    }
    return render(req, "test.html",context)


    # return render(req, "test.html",{"page_string": page_string,"head_page": head_page,"field": field,})









