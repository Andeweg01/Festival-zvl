from django.contrib import admin
from .models import Concert
from .models import Edition
from .models import Location


admin.site.register(Concert)
admin.site.register(Edition)
admin.site.register(Location)
