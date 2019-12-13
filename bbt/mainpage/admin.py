from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *
from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import *


class BusAdmin(admin.ModelAdmin):
    list_display = ('id','from_city', 'to_city','bus_manufacturer','bus_service','bus_type',
                    'bus_amount_seats','bus_number')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name','surname','email','identity_card_number','card_number')

class DateGoingOutAdmin(admin.ModelAdmin):
    list_display = ('id','date_going_out','date_arriving','bus')

class SeatsAdmin(admin.ModelAdmin):
    list_display = ('id','date','status','number')

class ImageAdmin(admin.ModelAdmin):
    list_display = ('id','images')


admin.site.register(Bus,BusAdmin)
admin.site.register(Client,ClientAdmin)
admin.site.register(DateGoingOut,DateGoingOutAdmin)
admin.site.register(Seats,SeatsAdmin)
admin.site.register(Image,ImageAdmin)