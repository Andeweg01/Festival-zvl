# Generated by Django 3.1 on 2020-08-29 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concerts', '0008_auto_20200829_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concert',
            name='concert_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]