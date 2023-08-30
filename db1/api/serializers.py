from rest_framework import serializers
from django import forms
from app01.models import t3,tliver,tliver1,LiterData,UploadedFile,countsGSE137537,HumanLiter,AllLiter,MouseLiter

# tranmeta=tliver1
class tliver1Ser(serializers.ModelSerializer):
    class Meta:
        model = tliver1
        fields = (
            # "data_id",
            "Cell_barcode",
            "cell_type",
            "zone",
            "run_id",
            "time_point",
            "UMAP_X",
            "UMAP_Y",
        )

class tliverSer(serializers.ModelSerializer):
    class Meta:
        model = tliver
        fields = "__all__"
        
class t3Ser(serializers.ModelSerializer):
    class Meta:
        model = t3
        fields = "__all__"


class LiterDataSer(serializers.ModelSerializer):
    class Meta:
        model = LiterData
        fields = "__all__"

class counts137537Ser(serializers.ModelSerializer):
    class Meta:
        model = countsGSE137537
        fields = "gene","cell","exp"



class countsSer(serializers.Serializer):

    genename = serializers.CharField()
    cell = serializers.CharField()
    exp = serializers.CharField()
    liter = serializers.CharField()
    # fields = "gene","cell","exp"
        
class UploadSer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = "__all__"


class LiterIdSer(serializers.ModelSerializer):
    class Meta:
        model = LiterData
        fields = ( 'Liter_pmid' ,)



class literSer(serializers.ModelSerializer):
    class Meta:
        model = AllLiter
        fields = "__all__"