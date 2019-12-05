from django.contrib import admin
from .models import UserExtension
from django.db import models

# Register your models here.
# Underwriter admin model
class BasicDataAdmin(admin.ModelAdmin):

    list_max_show_all = 50
    list_per_page = 50         # 分页

    # 设置哪些字段可以点击进入编辑界面，默认是第一个字段
    # list_display_links = list_display
    # list_display_links = ('user',)
    # print('list_display')
    # 是否可以直接编辑
    list_editable =('telephone','phone','school')

    # 需要显示的字段信息
    list_display = ('fullname','telephone','phone','school')


    # search_fields = list_editable                           # 搜索字段
    # list_filter =  list_editable   # 过滤器
    # date_hierarchy = 'create_time'                             # 头部添加  详细时间分层筛选　
    # ordering =  list_display                          # 排序



# 注册时，在第二个参数写上 admin model
admin.site.register(UserExtension, BasicDataAdmin)
# admin.site.register(UserExtension)