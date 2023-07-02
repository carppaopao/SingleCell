from django.db import models




# Create your models here.

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

# create table tliver1(
#     -> Cell_barcode varchar(32),
#     -> cell_type varchar(20),
#     -> zone int,
#     -> run_id varchar(12),
#     -> time_point int,   
#     -> UMAP_X decimal(32,18),
#     -> UMAP_Y float)default charset=utf8
#     -> ;