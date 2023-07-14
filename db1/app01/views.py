from django.core.paginator import Paginator
from django.shortcuts import render,redirect
from .models import tliver1, LiterData

def home(request):
    logs = [
        {"date": "5.24~5.31", "content": "使用Django框架建立网站的雏形"},
        {"date": "6.1", "content": "实现了在后端对Single_cell_Meta_data.txt中的数据进行绘制，并传回前端页面"},
        {"date": "6.3", "content": "学习使用JavaScript，以便处理数据格式"},
        {"date": "6.4~6.6", "content": "使用echarts.js绘图"},
        {"date": "6.7~6.10", "content": "分页功能实现"},
        {"date": "6.11~15", "content": "尝试前后端分离"},
        {"date": "6.16~6.20", "content": "完善搜索功能和分页按钮"},
        {"date": "6.21~6.27", "content": "使用Databales插件;增加了下载数据功能;Plot增加了筛选功能;上传了summary文件中的数据"},
        {"date": "6.28~7.5", "content": "对数据过滤，允许对数据进行添加或删除"},
    ]
    return render(request, "celldb/home.html", {"logs": logs})

def plotScatter(request):
    return render(request, "celldb/plotScatter.html")

def overview(request):
    liter = LiterData.objects.all()
    data = ""

    return render(request, "celldb/overview.html", {"data": data, "liter":liter})

def browseU(request):
    # data = tliver1.objects.all()
    # items_per_page = 10
    # paginator = Paginator(data, items_per_page)
    # page_number = request.GET.get("page")
    # page_obj = paginator.get_page(page_number)
    liter = LiterData.objects.all()
    

    return render(request, "celldb/browseU.html", {"liter":liter})



def browseG(request):
    liter = LiterData.objects.all()
    data = ""
    return render(request, "celldb/browseG.html", {"data": data, "liter":liter})


def upload(request):
    return render(request, "celldb/upload.html")



def download(request):
    return render(request, "celldb/download.html")



def base(req):
    return render(req,'celldb/base.html')




def analyse(req):
    return render(req,'celldb/analyse.html')





def testli(req):

    link=req.GET.get('link')
    url = f"/test?link={link}"
    print(url)
    # data = LiterData.objects.values()
    # serializer = LiterIdSer(data, many=True)

    # return Response(serializer.data)
    return redirect(url)



def test(req):
    link= req.GET.get('link')
    print(link)
    if link:
        return render(req,'celldb/browseG.html',{'link':link})
    else:
        return render(req,'celldb/test.html')

















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
