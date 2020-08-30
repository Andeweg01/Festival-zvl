from django.contrib import admin
from .models import Concert, Edition, Location


class ConcertAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'concert_name',
        'friendly_name',
        'concert_date',
        'edition',
        'concert_subtitle',
        'concert_theme',
        'concert_conductor',
        'concert_soloist',
        'concert_program',
        'concert_description',
        'concert_time',
        'concert_price',
        'concert_availability',
        'concert_url'
        'concert_image',
        'location',
    )

    ordering = ('sku',)


class EditionAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'loc_name',
        'friendly_name',
        'loc_address',
        'loc_pc',
        'loc_place',
    )


admin.site.register(Concert, ConcertAdmin)
admin.site.register(Edition, EditionAdmin)
admin.site.register(Location, LocationAdmin)
