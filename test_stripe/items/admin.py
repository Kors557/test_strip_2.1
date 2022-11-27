from django.contrib import admin

from .models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'description',
        'price'
    )
    empty_value_display = '-пусто-'
    search_fields = ('name',)


admin.site.register(Item, ItemAdmin)
