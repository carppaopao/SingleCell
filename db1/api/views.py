from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.core.files.storage import default_storage
from django.views.decorators.csrf import csrf_exempt
from django.http import FileResponse
from django.shortcuts import redirect, render
import os
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import serializers
from .serializers import tliverSer,LiterDataSer,UploadSer,LiterIdSer,counts137537Ser,literSer,countsSer
from app01.models import tliver,LiterData,UploadedFile,countsGSE137537,countsGSE137846,AllLiter
from rest_framework.viewsets import ModelViewSet
from .paginations import CustomPagination
from django.views.decorators.cache import cache_page
from datetime import timedelta
from django.apps import apps



def close_view(request):
    print("API is closed.")
    return JsonResponse({"message": "API is closed."})    


# For File download
def download_file(request):
    # 获取文件路径
    file_path = '/home/azureuser/SingleCellDB/Photo/Docker.png'  # 文件的实际路径
    file_name = os.path.basename(file_path)  # 文件名

    # 检查文件是否存在
    if not os.path.exists(file_path):
        raise FileNotFoundError("File not found")

    # 打开文件并创建响应对象
    file = open(file_path, 'rb')
    response = FileResponse(file)

    # 设置响应头，指定文件名和内容类型
    response['Content-Disposition'] = f'attachment; filename={file_name.split("/")[-1].encode().decode("latin-1")}'
    # print(f'attachment; filename={file_name.split("/")[-1].encode().decode("latin-1")}')
    response['Content-Type'] = 'application/png'  # 根据实际文件类型设置

    return response


#For Photo upload
@csrf_exempt
def SaveFiles(request):
    try:
        file = request.FILES['file']
        # 验证文件类型是否为图片
        allowed_extensions = ['txt', 'csv', 'xls', 'xlsx']
        extension = file.name.split('.')[-1].lower()
        if extension not in allowed_extensions:
            return JsonResponse({'error': '只能上传文本文件'}, status=400)
        
        file_name = default_storage.save(file.name, file)
        return JsonResponse({'message': '文件上传成功'}, status=201)
    except KeyError:
        return JsonResponse({'error': '未找到上传的文件'}, status=400)


# For FileUpload
class UploadedFileViewSet(ModelViewSet):
    queryset = UploadedFile.objects.all()
    serializer_class = UploadSer
    parser_classes = (MultiPartParser, FormParser)


#For DataSet
# class DataSetView(ModelViewSet):
#     queryset = DataSetMeta.objects.order_by("dataset_id")
#     serializer_class = DataSetMetaSerializer


# For LiterData
class LiterDataView(ModelViewSet):
    queryset = LiterData.objects.all()
    serializer_class = LiterDataSer

    # def get_permissions(self):
    #     if self.action in ['list', 'retrieve']:
    #         # 列表和详情视图允许任何人访问
    #         permission_classes = [AllowAny]
    #     else:
    #         # 其他视图需要身份验证
    #         permission_classes = [IsAuthenticated]
    #     return [permission() for permission in permission_classes]


@api_view(["GET"])
def getTran(request):
    paginator = CustomPagination()
    data = tliver.objects.order_by("id")
    result_page = paginator.paginate_queryset(data, request)
    serializer = tliverSer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)



@api_view(["GET"])
def getTran_all(request, formart=None):
    fields = request.GET.get("fields")
    if fields:
        fields = fields.split(",")
        data = tliver.objects.order_by("data_id").values(*fields)
    else:
        data = tliver.objects.all()
    serializer = tliverSer(data, many=True, fields=fields)
    import gzip,json
    from django.http import HttpResponse
    # 将序列化后的数据转换为字符串
    serialized_data = serializer.data
    json_str = json.dumps(serialized_data)

    # 使用gzip进行压缩
    compressed_data = gzip.compress(json_str.encode("utf-8"))

    # 构建gzip响应
    response = HttpResponse(content_type="application/json")
    response["Content-Encoding"] = "gzip"
    response["Content-Disposition"] = "attachment; filename=data.json.gz"

    # 将压缩后的数据写入响应
    response.write(compressed_data)

    return response



@api_view(["GET", "POST", "DELETE"])
def getTran_detail(request, id, format=None):
    try:
        tran = tliver.objects.get(data_id=id)
    except tliver.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = tliverSer(tran)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = tliverSer(tran, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == "DELETE":
        tran.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# @cache_page(60 * 60)
@api_view(["GET"])
def search(req):
    genes = req.GET.get('gene', '').split(',')
    species = int(req.GET.get("species"))
    res = AllLiter.objects.none()  # 创建空的 queryset
    for gene in genes:
        if gene:
            if species == 1:
                res |= AllLiter.objects.filter(gene = gene)  
                # res = AllLiter.objects.filter(gene = gene)

            elif species == 2:
                # res = AllLiter.objects.filter(gene = gene, species='mouse')
                res |= AllLiter.objects.filter(gene = gene, species='mouse')  

            else:
                # res = AllLiter.objects.filter(gene = gene, species='human')
                res |= AllLiter.objects.filter(gene = gene, species='human')  

    serializer = literSer(res, many=True)

    return Response(serializer.data)


def searchexcel(req):


    # current_directory = os.getcwd()
    # print("当前工作目录：", current_directory)



    data1 = {'message': 'true'}
    data2= {'message': 'false'}

    genes = req.GET.get('gene', '').split(',')
    print(genes)
# 搜索当前目录下的所有文件
    for filename in os.listdir('.'):
        if filename.endswith('.tsv') and 'barcodes' in filename:
            with open(filename, 'r') as file:
                for line in file:
                    for gene in genes:  # 遍历基因列表
                        if gene in line:
                            return Response(data1,format='json')

    return Response(data2,format='json')
    genes = req.GET.get('gene', '').split(',')
    # species = int(req.GET.get("species"))
    print(genes)
    # 搜索当前目录下的所有文件
    for filename in os.listdir('.'):
        if filename.endswith('.tsv') and 'barcodes' in filename:
            with open(filename, 'r') as file:
                for line in file:
                    if genes in line:
                        return Response("true")

    return Response("false")

    serializer=()
    return Response(serializer.data)

def downloadexcel(req):


    return Response("")


def searchtype(req):

    return Response("ok")


@api_view(["GET"])
def download(req):
    genes = req.GET.get('params').split(',')
    res = countsGSE137537.objects.none() 
    serializer = []

    for param in genes:
        x, y = param.split('&')[0].split('=')[1], param.split('&')[1].split('=')[1]
        y = 'counts' + y
        model = apps.get_model(app_label='app01', model_name=y)
        res = model.objects.filter(genename = x)  
        resse = countsSer(res, many=True)
        serializer= resse.data + serializer  # 将结果添加到列表中

    return Response(serializer)







@api_view(["GET"])
def getTran_id(req):
    data = LiterData.objects.values()
    serializer = LiterIdSer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def browseUmap_view(req):
    select_value = req.GET.get('selectedOption')  # 获取请求参数 select 的值

    return Response({'select': select_value})


# @api_view(["GET"])
# def gettest_id(req):
#     data = LiterData.objects.values()
#     serializer = LiterIdSer(data, many=True)
#     print(serializer)
#     return Response(serializer.data)


# @api_view(["GET"])
# def gettest_id(req):
#     # link = request.query_params.get("link")  # 获取超链接内容数据
#     # print("请求名:", request.META.get("HTTP_X_REQUEST_NAME"))  # 打印请求名

    
#     link=req.GET.get('link')
#     target_url = f"/destination?link={link}"

#     # data = LiterData.objects.values()
#     # serializer = LiterIdSer(data, many=True)

#     # return Response(serializer.data)
#     return redirect("celldb-browseG")


