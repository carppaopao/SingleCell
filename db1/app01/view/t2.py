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

def t2(req):
#搜索功能：

    dict ={}
    # search = req.GET.get("q","")
    # if search:
    #     dict ["zone"]= search
    queryset = models.tliver.objects.filter(**dict).order_by("-cell_type").values()

    # search = req.GET.get("q","")
    # field = req.GET.get("field")

    # if field == 'zone':
    #     if search:
    #        queryset = models.tliver1.objects.filter(zone__icontains=search).order_by("-cell_type").values()
    #     else:
    #         queryset = models.tliver1.objects.all().order_by("-cell_type").values()

    # elif field == 'run_id':
    #     if search:
    #         queryset = models.tliver1.objects.filter(run_id__icontains=search).order_by("-cell_type").values()
    #     else:
    #         queryset = models.tliver1.objects.all().order_by("-cell_type").values()

    # elif field == 'cell_type':
    #     if search:
    #         queryset = models.tliver1.objects.filter(cell_type__icontains=search).order_by("-cell_type").values()
    #     else:
    #         queryset = models.tliver1.objects.all().order_by("-cell_type").values()

    # elif field == 'time_point':
    #     if search:
    #         queryset = models.tliver1.objects.filter(time_point__icontains=search).order_by("-cell_type").values()
    #     else:
    #         queryset = models.tliver1.objects.all().order_by("-cell_type").values()

    # else:
    #     queryset = models.tliver1.objects.all().order_by("-cell_type").values()

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
        # "search": search,                   # 搜索的内容
        "page_string": page_object.page_string,     # 页码
        "head_page": head_page,             # 首页
        "end_page": end_page,               # 尾页
        # "field": field,
    }

    return render(req, "t2.html",context)



#科学计数转换
def format_scientific(value):
    return '{:.2e}'.format(value)  # 使用适当的格式化方式进行科学计数转换
























# def download_file(request):

#     with open("D:/22.txt") as file:
#         response = FileResponse(file)
#         response['Content-Disposition'] = 'attachment; filename="22.txt"'
#         return response




# def download(req):
#     # 筛选出表格数据，并将其存储在table_data变量中，你可以根据自己的筛选逻辑进行修改
#     table_data = models.tliver.objects.all().order_by("-cell_type").values()
#     # 生成文本内容，将表格数据格式化成文本文件的形式
#     content = ""
#     for data in table_data:
#         # 根据需要进行数据的格式化
#         row = f"{data.zone}\t{data.cell_type}\n"
#         content += row
#     # 设置响应的内容类型为文本文件
#     response = HttpResponse(content, content_type='text/plain')
#     # 设置响应的头部，指定文件名并设置附件类型
#     response['Content-Disposition'] = 'attachment; filename="table_data.txt"'
#     return response




# def test1(request):
#     def file_itertor(file_name,chunk_size=512):
#         with open(file_name) as f:
#             while True:
#                 c=f.read(chunk_size)
#                 if c:
#                     yield c
#                 else:
#                     break
#     file_name=r"D:\22.txt"
#     download_file='django.txt'
#     response=StreamingHttpResponse(file_itertor(file_name))
#     response['Content-Type'] = 'application/octet-stream'
#     response['Content-Disposition'] = 'attachment;filename="{0}"'.format(download_file)
#     return response


