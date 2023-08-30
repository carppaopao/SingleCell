from django.urls import path

from . import views
# from .view import admin,index,home,search,browse,test,t2

urlpatterns = [
    path("", views.home, name="celldb-home"),
    # path("browseU", views.browseU, name="celldb-browseU"),
    path("upload", views.upload, name="celldb-upload"),
    path("download", views.download, name="celldb-download"),
    path("overview", views.overview, name="celldb-overview"),
    path("plot/", views.plotScatter, name="celldb-plot"),
    path("plot/local", views.plotLocal, name="celldb-plot-local"),
    path("plot/r", views.plotR, name="celldb-plot-r"),
    path('base',views.base),
    path('analyse',views.analyse, name="celldb-analyse"),
    path("test", views.test, name="celldb-test"),
    path("runcode/", views.runCode, name="celldb-runcode"),
    path("search", views.search, name='celldb-search'),
    path("browseU/", views.browseU, name='celldb-browseU'),
    path("browseE/", views.browseE, name='celldb-browseE'),
    path("searchcelltype/", views.searchcelltype, name='celldb-searchtype')


]


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('index/',index.index),
#     path('home/',home.home),
#     # 访问www.xxx.com/index/   ->执行函数views.index（写在views.py）
#     path('search/',search.search),
#     path('browse/',browse.browse),
#     path('test/',test.test),
#     path('download/', home.download_file, name='download'),
#     path('t2/', t2.t2),

# # 测试排序
#     path('count/', test.t1),
#     path('test1/', test.test1),
#     path('test2/', test.test2),
# #DRF
# ]