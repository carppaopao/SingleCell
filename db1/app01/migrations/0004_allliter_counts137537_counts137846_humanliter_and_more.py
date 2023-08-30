# Generated by Django 4.2.2 on 2023-08-02 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_literdata_tliver1_uploadedfile_delete_t1'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllLiter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liter', models.CharField(max_length=255)),
                ('species', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'allliter',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='counts137537',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cell', models.CharField(max_length=255)),
                ('exp', models.CharField(max_length=255)),
                ('genename', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'counts137537',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='counts137846',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cell', models.CharField(max_length=255)),
                ('exp', models.CharField(max_length=255)),
                ('genename', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'counts137846',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HumanLiter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liter', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'humanliter',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MouseLiter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liter', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'mouseliter',
                'managed': False,
            },
        ),
    ]
