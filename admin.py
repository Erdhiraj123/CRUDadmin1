from django.contrib import admin
from . models import User
from django.utils.html import format_html

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display=('id','name','email','password','is_staff','is_admin',"Datashow","delete",)
    list_filter=('create_at','is_admin','is_staff',)
    list_display_links=['id',]
    actions = ["Admin","Not_Admin","is_staff","Is_Not_Staff",]
    list_editable=('email','name',)
    search_fields=User.SearchableFields
   
    def Datashow(self,obj):
        return format_html(f'<a href="/admin/enroll/user/{obj.id}/change/" class="default">VIEW</a>')
    
    def delete(self,obj):
         return format_html(f'<a href="/admin/enroll/user/{obj.id}/delete/" class="default">DELETE</a>')
    
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
 
    def Admin(self, request, queryset):
        queryset.update(is_admin=True)

    def Not_Admin(self, request, queryset):
        queryset.update(is_admin=False)

    def is_staff(self,request,queryset):
        queryset.update(is_staff=True)
    
    def Is_Not_Staff(self,request,queryset):
        queryset.update(is_staff=False) 
    
admin.site.register(User,UserAdmin)
