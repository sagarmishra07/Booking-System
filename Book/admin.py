from django.contrib import admin
from .models import Book, Menu, Table, Special
# Register your models here.


class Bookadmin(admin.ModelAdmin):
    list_display = ('username','table','number_of_people','phone','occasion', 'date','time')


class Menuadmin(admin.ModelAdmin):
    list_display = ('title','price','details', 'img')

class Tableadmin(admin.ModelAdmin):
    list_display = ('table','details','title', 'img')

class Specialadmin(admin.ModelAdmin):
    list_display = ('title','price','details', 'img')

admin.site.register(Book,Bookadmin)
admin.site.register(Menu,Menuadmin)
admin.site.register(Table,Tableadmin)
admin.site.register(Special,Specialadmin)

admin.site.site_header= 'Rainbow Cafe'

admin.site.site_title= 'Rainbow Cafe'
admin.site.index_title= 'Admin Dashboard'