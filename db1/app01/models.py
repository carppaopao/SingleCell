from django.db import models




# Create your models here.

# tliver=tranmeta
class tliver(models.Model):
    Cell_barcode  = models.CharField(max_length=32)
    cell_type = models.CharField(max_length=20)
    zone = models.IntegerField()
    run_id = models.CharField(max_length=12)
    time_point = models.IntegerField()
    UMAP_X = models.DecimalField(max_digits=32, decimal_places=18)
    UMAP_Y = models.DecimalField(max_digits=32, decimal_places=18)

    class Meta:
        managed = False
        db_table = 'tliver'

class t3(models.Model):
    name = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    pay = models.IntegerField()
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = True
        db_table = 't3'

class tliver1(models.Model):
    Cell_barcode  = models.CharField(max_length=32)
    cell_type = models.CharField(max_length=20)
    zone = models.IntegerField()
    run_id = models.CharField(max_length=12)
    time_point = models.IntegerField()
    UMAP_X = models.CharField(max_length=32)
    UMAP_Y = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'tliver1'

#LiteratureMeta=LiterData
class LiterData(models.Model):
    Liter_pmid = models.CharField(primary_key=True, max_length=100)
    Liter_title = models.CharField(max_length=1000, blank=True, null=True)
    Liter_abstract = models.TextField(blank=True, null=True)
    Liter_publication = models.TextField(blank=True, null=True)
    Liter_content = models.TextField(blank=True, null=True)
    Liter_data = models.TextField(blank=True, null=True)
    Sample_info = models.TextField(blank=True, null=True)
    Species = models.CharField(max_length=1000, blank=True, null=True)
    Tissue = models.CharField(max_length=1000, blank=True, null=True)
    Number_cells = models.CharField(max_length=100, blank=True, null=True)
    Cell_types = models.TextField(blank=True, null=True)
    Method = models.CharField(max_length=1000, blank=True, null=True)
    Markers = models.TextField(blank=True, null=True)
    Note = models.TextField(blank=True, null=True)

    def __self__(self):
        return self.Liter_pmid
    class Meta:
        managed = False 
        db_table = 'celldb_literaturemeta'

    def __self__(self):
        return self.PMID

class UploadedFile(models.Model):
    file = models.FileField(upload_to='data')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    size = models.CharField(max_length=20)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __self__(self):
        return self.name
    class Meta:
        managed = False
        db_table = 'celldb_uploadedfile'


# class gene137537(models.Model):
#     gene  = models.CharField(max_length=255)
#     id = models.IntegerField(primary_key=True)

#     class Meta:
#         managed = False
#         db_table = 'gene137537'


class countsGSE137537(models.Model):
    cell = models.CharField(max_length=255)
    exp = models.CharField(max_length=255)
    genename = models.CharField(max_length=255)
    liter = models.CharField(max_length=255)
    
    class Meta:
        managed = False
        db_table = 'countsGSE137537'

class countsGSE137846(models.Model):
    # gene  = models.CharField(max_length=255)
    cell = models.CharField(max_length=255)
    exp = models.CharField(max_length=255)
    genename = models.CharField(max_length=255)
    liter = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'countsGSE137846'

class AllLiter(models.Model):
    liter = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    gene = models.CharField(max_length=255)
    id = models.IntegerField(primary_key=True)
    class Meta:
        managed = False
        db_table = 'allliter'

class HumanLiter(models.Model):
    liter = models.CharField(max_length=255)
    gene = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'humanliter'

class MouseLiter(models.Model):
    liter = models.CharField(max_length=255)
    gene = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mouseliter'











# class DataSetMeta(models.Model):
#     dataset_id = models.CharField(primary_key=True, max_length=100)
#     subdata_id = models.CharField(max_length=100, blank=True, null=True)
#     dataset_design = models.TextField(blank=True, null=True)
#     dataset_citation = models.TextField(blank=True, null=True)
#     data_platform = models.CharField(max_length=100, blank=True, null=True)
#     data_model = models.CharField(max_length=100, blank=True, null=True)
#     data_library = models.CharField(max_length=100, blank=True, null=True)
#     dataset_sample = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return self.dataset_id

        