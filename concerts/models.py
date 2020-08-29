from django.db import models
from datetime import date, datetime as dt


class Edition(models.Model):
    name = models.CharField(max_length=4)
    friendly_name = models.CharField(max_length=4)

    def __string__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Location(models.Model):
    loc_name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)
    loc_address = models.CharField(max_length=254, null=True, blank=True)
    loc_pc = models.CharField(max_length=8, null=True, blank=True)
    loc_place = models.CharField(max_length=254, null=True, blank=True)

    def __string__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Concert(models.Model):
    edition = models.ForeignKey(
        'Edition', null=True, blank=True, on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=254, null=True, blank=True)
    concert_name = models.CharField(max_length=254, default='name')
    friendly_name = models.CharField(max_length=254, default='the full concert name')
    concert_date = models.DateField(max_length=254, default=date.today)
    concert_subtitle = models.CharField(max_length=254, null=True, blank=True)
    concert_theme = models.CharField(max_length=254, null=True, blank=True)
    concert_conductor = models.CharField(max_length=254, null=True, blank=True)
    concert_soloist = models.CharField(max_length=254, null=True, blank=True)
    concert_program = models.CharField(max_length=254, null=True, blank=True)
    concert_description = models.TextField(null=True, blank=True)
    concert_time = models.CharField(max_length=16, default='20.00 uur')
    concert_price = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    concert_availability = models.DecimalField(
        max_digits=4, decimal_places=0, null=True, blank=True
    )
    concert_url = models.URLField(max_length=1024, null=True, blank=True)
    concert_image = models.ImageField(null=True, blank=True)
    location = models.ForeignKey(
        'Location', null=True, blank=True, on_delete=models.SET_NULL
    )
