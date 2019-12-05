from django.contrib import admin
from .models import GoodsType,Invoice_partment,RiskLevel,ContractEdition,SpecialMark,Grade,CooperationState,IndustryStatus
from django.db import models

# Register your models here.
# Underwriter admin model


class GoodsTypeAdmin(admin.ModelAdmin):

    list_max_show_all = 50
    list_per_page = 50         # 分页

    # 设置哪些字段可以点击进入编辑界面，默认是第一个字段
    # list_display_links = list_display
    list_display_links =  ('id',)

    # 是否可以直接编辑
    list_editable = ('goodsType', 'Note')

    # 需要显示的字段信息
    list_display = list_display_links + list_editable

    search_fields = list_display                           # 搜索字段
    list_filter = list_display  # 过滤器
    # date_hierarchy = 'create_time'                             # 头部添加  详细时间分层筛选　
    ordering = list_editable                              # 排序


# 注册时，在第二个参数写上 admin model
admin.site.register(GoodsType,GoodsTypeAdmin)

class Invoice_partmentAdmin(admin.ModelAdmin):

    list_max_show_all = 50
    list_per_page = 50         # 分页

    # 设置哪些字段可以点击进入编辑界面，默认是第一个字段
    # list_display_links = list_display
    list_display_links =  ('id',)

    # 是否可以直接编辑
    list_editable = ('invoice_partment', 'Note')

    # 需要显示的字段信息
    list_display = list_display_links + list_editable

    search_fields = list_display                           # 搜索字段
    list_filter = list_display  # 过滤器
    # date_hierarchy = 'create_time'                             # 头部添加  详细时间分层筛选　
    ordering = list_editable                              # 排序


# 注册时，在第二个参数写上 admin model
admin.site.register(Invoice_partment,Invoice_partmentAdmin)


class RiskLevelAdmin(admin.ModelAdmin):

    list_max_show_all = 50
    list_per_page = 50         # 分页

    # 设置哪些字段可以点击进入编辑界面，默认是第一个字段
    # list_display_links = list_display
    list_display_links =  ('id',)

    # 是否可以直接编辑
    list_editable = ('riskLevel', 'Note')

    # 需要显示的字段信息
    list_display = list_display_links + list_editable

    search_fields = list_display                           # 搜索字段
    list_filter = list_display  # 过滤器
    # date_hierarchy = 'create_time'                             # 头部添加  详细时间分层筛选　
    # ordering = list_editable                              # 排序


# 注册时，在第二个参数写上 admin model
admin.site.register(RiskLevel,RiskLevelAdmin)

class ContractEditionAdmin(admin.ModelAdmin):

    list_max_show_all = 50
    list_per_page = 50         # 分页

    # 设置哪些字段可以点击进入编辑界面，默认是第一个字段
    # list_display_links = list_display
    list_display_links =  ('id',)

    # 是否可以直接编辑
    list_editable = ('contractEdition', 'Note')

    # 需要显示的字段信息
    list_display = list_display_links + list_editable

    search_fields = list_display                           # 搜索字段
    list_filter = list_display  # 过滤器
    # date_hierarchy = 'create_time'                             # 头部添加  详细时间分层筛选　
    ordering = list_editable                              # 排序


# 注册时，在第二个参数写上 admin model
admin.site.register(ContractEdition,ContractEditionAdmin)

class SpecialMarkAdmin(admin.ModelAdmin):

    list_max_show_all = 50
    list_per_page = 50         # 分页

    # 设置哪些字段可以点击进入编辑界面，默认是第一个字段
    # list_display_links = list_display
    list_display_links =  ('id',)

    # 是否可以直接编辑
    list_editable = ('specialMark', 'Note')

    # 需要显示的字段信息
    list_display = list_display_links + list_editable

    search_fields = list_display                           # 搜索字段
    list_filter = list_display  # 过滤器
    # date_hierarchy = 'create_time'                             # 头部添加  详细时间分层筛选　
    ordering = list_editable                              # 排序


# 注册时，在第二个参数写上 admin model
admin.site.register(SpecialMark,SpecialMarkAdmin)

class GradeAdmin(admin.ModelAdmin):

    list_max_show_all = 50
    list_per_page = 50         # 分页

    # 设置哪些字段可以点击进入编辑界面，默认是第一个字段
    # list_display_links = list_display
    list_display_links =  ('id',)

    # 是否可以直接编辑
    list_editable = ('grade', 'Note')

    # 需要显示的字段信息
    list_display = list_display_links + list_editable

    search_fields = list_display                           # 搜索字段
    list_filter = list_display  # 过滤器
    # date_hierarchy = 'create_time'                             # 头部添加  详细时间分层筛选　
    ordering = list_editable                              # 排序


# 注册时，在第二个参数写上 admin model
admin.site.register(Grade,GradeAdmin)

class CooperationStateAdmin(admin.ModelAdmin):

    list_max_show_all = 50
    list_per_page = 50         # 分页

    # 设置哪些字段可以点击进入编辑界面，默认是第一个字段
    # list_display_links = list_display
    list_display_links =  ('id',)

    # 是否可以直接编辑
    list_editable = ('cooperationState', 'Note')

    # 需要显示的字段信息
    list_display = list_display_links + list_editable

    search_fields = list_display                           # 搜索字段
    list_filter = list_display  # 过滤器
    # date_hierarchy = 'create_time'                             # 头部添加  详细时间分层筛选　
    ordering = list_editable                              # 排序


# 注册时，在第二个参数写上 admin model
admin.site.register(CooperationState,CooperationStateAdmin)

class IndustryStatusAdmin(admin.ModelAdmin):

    list_max_show_all = 50
    list_per_page = 50         # 分页

    # 设置哪些字段可以点击进入编辑界面，默认是第一个字段
    # list_display_links = list_display
    list_display_links =  ('id',)

    # 是否可以直接编辑
    list_editable = ('industryStatus', 'Note')

    # 需要显示的字段信息
    list_display = list_display_links + list_editable

    search_fields = list_display                           # 搜索字段
    list_filter = list_display  # 过滤器
    # date_hierarchy = 'create_time'                             # 头部添加  详细时间分层筛选　
    ordering = list_editable                              # 排序


# 注册时，在第二个参数写上 admin model
admin.site.register(IndustryStatus,IndustryStatusAdmin)