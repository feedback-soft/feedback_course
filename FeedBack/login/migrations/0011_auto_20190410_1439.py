# Generated by Django 2.1.7 on 2019-04-10 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_homework_submitwork'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='courses',
            field=models.ManyToManyField(related_name='users', to='login.course'),
        ),
    ]
