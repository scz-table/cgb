from django.contrib import admin
from .models import BasicData
from django.db import models

# Register your models here.
# Underwriter admin model


class BasicDataAdmin(admin.ModelAdmin):

    list_max_show_all = 50
    list_per_page = 50         # 分页

    # 设置哪些字段可以点击进入编辑界面，默认是第一个字段
    # list_display_links = list_display
    list_display_links =  ('id','groupName')

    # 是否可以直接编辑
    list_editable = ('groupNameRemarks', 'projectName','projectNameRemarks', 'projectDict', 'projectKey', 'projectValue','projectValueRemarks')

    # 需要显示的字段信息
    list_display = list_display_links + list_editable


    search_fields = list_display                           # 搜索字段
    list_filter = ('groupName', 'projectName', 'projectDict', 'projectKey', 'projectValue')  # 过滤器
    # date_hierarchy = 'create_time'                             # 头部添加  详细时间分层筛选　
    # ordering = ('groupName','projectName','projectDict','projectKey','projectValue')                               # 排序


# 注册时，在第二个参数写上 admin model
admin.site.register(BasicData, BasicDataAdmin)