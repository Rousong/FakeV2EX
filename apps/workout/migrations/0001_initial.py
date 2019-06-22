# Generated by Django 2.0.6 on 2019-06-22 12:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BodyManage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('height', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='身高')),
                ('weightMb', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='目标体重')),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='体重')),
                ('BMI', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='BMI(kg/m²)')),
                ('fat_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='体脂率(%)')),
                ('fat_rateMb', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='目标体脂率(%)')),
                ('xiongwei', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='胸围(cm)')),
                ('biwei', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='臂围(cm)')),
                ('jiankaun', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='肩宽(cm)')),
                ('yaowei', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='腰围(cm)')),
                ('tunwei', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='臀围(cm)')),
                ('datuiwei', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='腿围(cm)')),
                ('jiaohuai', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='脚踝(cm)')),
                ('shouwan', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='手腕(cm)')),
                ('bowei', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='脖围(cm)')),
                ('jiaochang', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='脚长(cm)')),
                ('BMR', models.DecimalField(blank=True, decimal_places=0, max_digits=4, null=True, verbose_name='基础代谢(kcal)')),
                ('TDEE', models.DecimalField(blank=True, decimal_places=0, max_digits=4, null=True, verbose_name='每日热量总消耗(kcal)')),
                ('zt', models.SmallIntegerField(choices=[(0, '保持体型'), (1, '增肌'), (2, '减脂'), (3, '增重'), (4, '增强心肺'), (5, '改善体态')], default=0, verbose_name='当前状态')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='所属用户')),
            ],
            options={
                'verbose_name': '身材记录管理',
                'verbose_name_plural': '身材记录管理',
                'db_table': 'body_bodymanage',
            },
        ),
        migrations.CreateModel(
            name='WeightManage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('rm', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='rm')),
                ('wotui', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='卧推')),
                ('shendun', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='深蹲')),
                ('yingla', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='硬拉')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='所属用户')),
            ],
            options={
                'verbose_name': '配重记录管理',
                'verbose_name_plural': '配重记录管理',
                'db_table': 'body_weightmanage',
            },
        ),
    ]
