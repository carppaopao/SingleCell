# from django.shortcuts import render
# from django.http import HttpResponse
# from app01 import models
# from django.utils.safestring import mark_safe    #传入格式字符串转为html
# from app01.utils.pagination import Pagination    #导入封装的分页功能
# from django.db.models import Q

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





