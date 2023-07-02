from django.shortcuts import render
from django.http import HttpResponse
from app01 import models
from django.utils.safestring import mark_safe    #传入格式字符串转为html
from app01.utils.pagination import Pagination    #导入封装的分页功能
from django.db.models import Q

# # Create your views here.

def browse(req):
    return render(req,"browse.html")
