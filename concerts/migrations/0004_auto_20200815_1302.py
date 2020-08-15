# Generated by Django 3.1 on 2020-08-15 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concerts', '0003_concert_concert_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='concert',
            name='concert_availability',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='concert',
            name='concert_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='concert',
            name='concert_date',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='concert',
            name='concert_image',
            field=models.ImageField(blank=True, max_length=254, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='concert',
            name='concert_name',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='concert',
            name='concert_time',
            field=models.TimeField(blank=True, max_length=254, null=True),
        ),
    ]
