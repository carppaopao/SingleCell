from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from django.core.files.storage import default_storage
from django.views.decorators.csrf import csrf_exempt
from django.http import FileResponse
from django.shortcuts import redirect, render
import os
from rest_framework import serializers
from .serializers import t3Ser,tliverSer,tliver1Ser,LiterDataSer,UploadSer,LiterIdSer
from app01.models import t3,tliver,tliver1,LiterData,UploadedFile
from rest_framework.viewsets import ModelViewSet
from .paginations import CustomPagination

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
    print(f'attachment; filename={file_name.split("/")[-1].encode().decode("latin-1")}')
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



@api_view(["GET"])
def getTran(request, formar=None):
    paginator = CustomPagination()
    data = tliver1.objects.order_by("id")
    result_page = paginator.paginate_queryset(data, request)
    serializer = tliver1Ser(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)



@api_view(["GET"])
def getTran_all(request, formar=None):
    data = tliver1.objects.all()
    serializer = tliver1Ser(data, many=True)
    return Response(serializer.data)



@api_view(["GET", "POST", "DELETE"])
def getTran_detail(request, id, format=None):
    try:
        tran = tliver1.objects.get(data_id=id)
    except tliver1.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = tliver1Ser(tran)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = tliver1Ser(tran, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == "DELETE":
        tran.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)







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


@api_view(["GET"])
def search(req):
    q = req.GET.get('q')
    print(q)
    data = LiterData.objects.values()
    serializer = LiterIdSer(data, many=True)
    return Response(serializer.data)