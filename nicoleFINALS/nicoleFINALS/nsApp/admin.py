from django.contrib import admin
from .models import Ambassador, Inventory

# Register your models here.

class AmbassadorAdmin(admin.ModelAdmin):
    list_display = ('ambIdV', 'ambNameV', 'ambPosV', 'ambPnumberV', 'ambEmailV', 'ambSocialV', 'ambDateOfHireV', 'ambBirthdateV', 'ambAdrV')

class InventoryAdmin(admin.ModelAdmin):
    list_display = ('itemIdV', 'itemNameV', 'itemQtyV', 'itemPriceV', 'itemDescV')

admin.site.register(Ambassador, AmbassadorAdmin)
admin.site.register(Inventory, InventoryAdmin)
