# Generated by Django 2.1.7 on 2019-04-06 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_auto_20190402_1606'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='board',
            options={'verbose_name': '反馈区', 'verbose_name_plural': '反馈区'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': '帖子', 'verbose_name_plural': '帖子'},
        ),
        migrations.AlterModelOptions(
            name='topic',
            options={'verbose_name': '课程反馈区', 'verbose_name_plural': '课程反馈区'},
        ),
    ]