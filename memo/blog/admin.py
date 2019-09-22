from django.contrib import admin
from .models import Memo
# Register your models here.
class MemoAdmin(admin.ModelAdmin):
    list_display = ('id','image','title','created_datetime','updated_datetime')
    list_display_links = ('id','image','title')

admin.site.register(Memo,MemoAdmin)