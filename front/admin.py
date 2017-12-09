from django.contrib import admin
from front import models


# Register your models here.

class managerAdmin(admin.ModelAdmin):
    list_display = ('M_id','M_name', 'M_pwd','M_sex','M_phone','M_type')
    search_fields = ('M_id','M_name', 'M_pwd','M_sex','M_phone','M_type')

class userAdmin(admin.ModelAdmin):
    list_display = ('U_id','U_name', 'U_phone','U_pwd','M_sex', 'U_addr','U_school')
    search_fields = ('U_id','U_name', 'U_phone','U_pwd','M_sex', 'U_addr','U_school')

class trainAdmin(admin.ModelAdmin):
    list_display = ('T_id','T_name', 'R_id','T_starttime','T_arrttime', 'T_price','T_num','T_yp','T_car')
    search_fields = ('T_id','T_name', 'R_id','T_starttime','T_arrttime', 'T_price','T_num','T_yp','T_car')

class routeAdmin(admin.ModelAdmin):
    list_display = ('R_id','R_startcity', 'R_arrtcity','R_startplace','R_arrtplace')
    search_fields = ('R_id','R_startcity', 'R_arrtcity','R_startplace','R_arrtplace')

class orderAdmin(admin.ModelAdmin):
    list_display = ('O_id','U_id','T_id','O_num','O_totalpri','O_orderstates','O_paystates','O_paymode','O_ordertime')
    search_fields = ('O_id','U_id','T_id','O_num','O_totalpri','O_orderstates','O_paystates','O_paymode','O_ordertime')

class suggestionAdmin(admin.ModelAdmin):
    list_display = ('SU_id','U_id', 'SU_time','SU_content')
    search_fields = ('SU_id','U_id', 'SU_time','SU_content')

class informAdmin(admin.ModelAdmin):
    list_display = ('I_id','T_id', 'I_content')
    search_fields = ('I_id','T_id', 'I_content')

class helpAdmin(admin.ModelAdmin):
    list_display = ('H_id','H_content')
    search_fields = ('H_id','H_content')

admin.site.register(models.manager,managerAdmin)
admin.site.register(models.user,userAdmin)
admin.site.register(models.train,trainAdmin)
admin.site.register(models.route,routeAdmin)
admin.site.register(models.order,orderAdmin)
admin.site.register(models.suggestion,suggestionAdmin)
admin.site.register(models.inform,informAdmin)
admin.site.register(models.help,helpAdmin)

