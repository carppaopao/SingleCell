from django.shortcuts import render
from django.http import HttpResponse
from app01 import models
from django.utils.safestring import mark_safe    #传入格式字符串转为html
from app01.utils.pagination import Pagination    #导入封装的分页功能
from django.db.models import Q

# # Create your views here.

def test(req):
    dict ={}
    search = req.GET.get("id")

    if search:
        dict ["id"]= search

    res = models.tliver.objects.all(**dict)[10:50]
    return render(req, "test.html",{"res" : res})


