# Generated by Django 2.0.2 on 2018-03-09 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0028_topic_comment_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='topic.Topic', verbose_name='Go分类'),
        ),
    ]