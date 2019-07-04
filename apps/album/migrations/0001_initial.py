# Generated by Django 2.0.6 on 2019-07-04 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('url', models.URLField(blank=True)),
                ('slug', models.SlugField(blank=True, max_length=500)),
                ('title', models.CharField(max_length=300, verbose_name='标题')),
                ('description', models.TextField(blank=True, verbose_name='简介')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/album/%Y%m%d')),
                ('total_likes', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': '照片墙',
                'ordering': ('-create_time',),
            },
        ),
    ]
