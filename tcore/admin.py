from django.contrib import admin
from django.http import HttpRequest
from .models import Contact,About,Service,Slider,Category,Blog,Setting,Page
from modeltranslation.admin import TranslationAdmin
from .admin_mixins import CommonMedia



class BaseAdmin(admin.ModelAdmin):
    def has_add_permission(self,request,obj=None):
        return False
    
    def has_delete_permission(self,request,obj=None):
        return False


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=('full_name','email',)


@admin.register(About)
class AboutAdmin(TranslationAdmin, CommonMedia,BaseAdmin):
    list_display=('title',)

    

    
@admin.register(Service)
class ServiceAdmin(TranslationAdmin, CommonMedia):
    list_display=('title',)

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display=('title','image',)


@admin.register(Category)
class CategoryAdmin(TranslationAdmin,CommonMedia):
    list_display=('name',)

@admin.register(Blog)
class BlogAdmin(TranslationAdmin,CommonMedia):
    list_display=('title','views','created_at','updated_at','category',)


@admin.register(Setting)
class SettingAdmin(TranslationAdmin,CommonMedia,BaseAdmin):
    list_display=('title',)

@admin.register(Page)
class PageAdmin(TranslationAdmin,CommonMedia):
    list_display=('title','slug','slug_url')
    
    def slug_url(self,obj):
        url_path=obj.get_absolute_url()
        return url_path
    slug_url.short_description='Detay Linki'