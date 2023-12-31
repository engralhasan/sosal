# Generated by Django 4.2.6 on 2023-10-16 19:05

from django.db import migrations, models
import video.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='videoinput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(blank=True, max_length=250, null=True)),
                ('video', models.FileField(upload_to='video/%y', validators=[video.validators.file_size])),
            ],
        ),
    ]
