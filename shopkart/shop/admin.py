from django.contrib import admin
from .models import *
from .models import product
'''''
class CategoryAdmin(admin.ModelAdmin):
    list_display =('name','image','description')
admin.site.register(Category,CategoryAdmin)
'''
admin.site.register(Category)
admin.site.register(product)

