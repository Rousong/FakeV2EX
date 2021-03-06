# Generated by Django 2.0.6 on 2019-07-04 14:26

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('avatar_thumbnail', imagekit.models.fields.ProcessedImageField(upload_to='image/image_source/%Y%m%d', verbose_name='图片')),
            ],
            options={
                'verbose_name_plural': '图库',
                'ordering': ('-create_time',),
            },
        ),
    ]
