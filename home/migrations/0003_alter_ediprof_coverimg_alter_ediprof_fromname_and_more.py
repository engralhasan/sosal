# Generated by Django 4.2.6 on 2023-10-21 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_ediprof_fromname_alter_ediprof_livename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ediprof',
            name='coverimg',
            field=models.ImageField(blank=True, default='cover.png', null=True, upload_to='product_picture/'),
        ),
        migrations.AlterField(
            model_name='ediprof',
            name='fromName',
            field=models.CharField(blank=True, default='Enter your Home Distik', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ediprof',
            name='job',
            field=models.CharField(blank=True, default='Enter your job titel', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ediprof',
            name='liveName',
            field=models.CharField(blank=True, default='Enter your Live cuntry', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ediprof',
            name='name',
            field=models.CharField(blank=True, default='Enter Your Name', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ediprof',
            name='profimg',
            field=models.ImageField(blank=True, default='def.png', null=True, upload_to='product_picture/'),
        ),
        migrations.AlterField(
            model_name='ediprof',
            name='scholnam',
            field=models.CharField(blank=True, default='Enter your School name', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ediprof',
            name='univarName',
            field=models.CharField(blank=True, default='Enter your Collage or univarciti name', max_length=50, null=True),
        ),
    ]