# Generated by Django 2.1.7 on 2019-04-15 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20190415_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submitwork',
            name='myfile',
            field=models.FileField(upload_to='%Y/%m/%d/'),
        ),
    ]