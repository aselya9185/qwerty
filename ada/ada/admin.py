from django.contrib import admin
from .models import *




class UserBuyer(admin.ModelAdmin):
    list_display = [field.name for field in Buyer._meta.fields]
    list_filter = ('name',)
    search_fields = ["name", "login"]

    class Meta:
        model = Buyer


admin.site.register(Buyer,UserBuyer)

