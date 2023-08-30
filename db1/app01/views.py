from django.core.paginator import Paginator
from django.shortcuts import render,redirect
from .models import tliver1, LiterData
# from . import models
import json

def home(request):

    return render(request, "celldb/home.html", )

def plotScatter(request):
    return render(request, "celldb/plotScatter.html")

def overview(request):
    liter = LiterData.objects.all()
    return render(request, "celldb/overview.html", {"liter":liter})

# def browseU(request):
    # data = tliver1.objects.all()
    # items_per_page = 10
    # paginator = Paginator(data, items_per_page)
    # page_number = request.GET.get("page")
    # page_obj = paginator.get_page(page_number)

    # liter = LiterData.objects.all()
    # data = ""
    # liter = LiterData.objects.all()
    # return render(request, "celldb/browseU.html", {"liter":liter})
def search(req):
    gene = req.GET.get("gene")
    gene_type = tliver1.objects.filter(run_id=gene).values_list('zone', flat=True).distinct()
    gene_type_list = list(gene_type)

    json_data = json.dumps(gene_type_list)
    print(json_data)
    return render(req, 'celldb/search.html',{"type": gene_type_list})



def upload(request):
    return render(request, "celldb/upload.html")

def download(request):
    return render(request, "celldb/download.html")

def base(req):
    return render(req,'celldb/base.html')

def analyse(req):
    return render(req,'celldb/analyse.html')

def upload(request):
    return render(request, "celldb/upload.html")

def plotLocal(request):
    return render(request, "celldb/plotLocal.html")

def plotR(request):
    return render(request, "celldb/plotR.html")

def runCode(request):
    return render(request, "celldb/runCode.html")

def browseU(request):
    return render(request, "celldb/browseU.html")

def browseE(request):
    return render(request, "celldb/browseE.html")

def searchcelltype(request):
    return render(request, "celldb/searchcelltype.html")

def test(req):
    link= req.GET.get('link')
    print(link)
    if link:
        return render(req,'celldb/plotScatter.html',{'link':link})
    else:
        return render(req,'celldb/test.html')










# def browseG(req):

#     dict ={}
#     search = req.GET.get("q","")
#     # if search:
#     #     dict ["zone"]= search
#     # queryset = models.tliver.objects.filter(**dict).order_by("-cell_type").values()

#     queryset = models.tliver1.objects.all().order_by("-cell_type").values()

#     return render(req, "celldb/browseG.html", {})







# from django.shortcuts import render
# from django.http import HttpResponse
# from django.utils.safestring import mark_safe    #传入格式字符串转为html
# from app01.utils.pagination import Pagination    #导入封装的分页功能
# from django.db.models import Q




# class DSerializer(serializers.ModelSerializer):

#     class Meta:
#             model= t3
#             fields= '__all__'

# class view(ModelViewSet):
#     queryset= t3.objects.all()
#     serializer_class= DSerializer





# # Create your views here.

# def index(req):
#     return render(req,"index.html")

# def home(req):
# #搜索功能：
#     dict ={}
#     search = req.GET.get("q","")
#     if search:
#         dict ["zone"]= search
#     queryset = models.tliver.objects.filter(**dict).order_by("-cell_type").values()

# #分页功能：
# #1. 筛选分页数据
# #2. 实例化分类对象
#     page_object = Pagination(req, queryset)

#     # 调用对象的html方法,生成页码
#     page_object.pagenum()

#     head_page = page_object.head_page
#     end_page = page_object.end_page

#     # data = json.dumps(list(page_object.page_queryset.values()))
#     # print(data)

#     context = {
#         "res": page_object.page_queryset,   # 分页的数据
#         "search": search,                   # 搜索的内容
#         "page_string": page_object.page_string,     # 页码
#         "head_page": head_page,             # 首页
#         "end_page": end_page,               # 尾页
#     }
#     return render(req, "home.html",context)


# def search(req):
#     return render(req,"search.html")

# def browse(req):
#     return render(req,"browse.html")

# def t2(req):
# #搜索功能：
#     dict1 ={}
#     dict2 ={}
#     search = req.GET.get("q","")

#     if search:
        
#         dict1 ["zone"]= search
#         dict2 ["run_id"]=search
#     queryset = models.tliver.objects.filter(Q(**dict1) | Q(**dict2)).order_by("-cell_type").values()

# #分页功能：
# #1. 筛选分页数据
# #2. 实例化分类对象
#     page_object = Pagination(req, queryset)

#     # 调用对象的html方法,生成页码
#     page_object.pagenum()

#     head_page = page_object.head_page
#     end_page = page_object.end_page

#     # data = json.dumps(list(page_object.page_queryset.values()))
#     # print(data)
    
#     context = {
#         "res": page_object.page_queryset,   # 分页的数据
#         "search": search,                   # 搜索的内容
#         "page_string": page_object.page_string,     # 页码
#         "head_page": head_page,             # 首页
#         "end_page": end_page,               # 尾页
#     }
#     return render(req, "t2.html",context)


# def test(req):
#     dict ={}
#     search = req.GET.get("id")

#     if search:
#         dict ["id"]= search

#     res = models.tliver.objects.all(**dict)[10:50]
#     return render(req, "test.html",{"res" : res})






# def test(req):
#     if req.method == "GET":
#         return render(req, "test.html")
    

#     # # # 如果是 POST 请求,获取用户提交的数据

#     # q1 = models.t3.objects.all()     #queryset类型，获取一行数据

#     # q1= models.t3.objects.filter(id=1)

#     # q1= models.t3.objects.all().order_by("-pay")

#     q1= models.t3.objects.filter(id__gt= 1)


#     return render(req,"test.html",{"q1": q1 })
