# Generated by Django 2.1.7 on 2019-04-06 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_auto_20190402_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='addr',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='number',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='tel',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
    ]
