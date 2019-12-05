from django.contrib import admin
from .models import Supplier
from django.db import models

# Register your models here.
# Underwriter admin model


class SupplierAdmin(admin.ModelAdmin):

    list_max_show_all = 50
    list_per_page = 50         # 分页

    # 设置哪些字段可以点击进入编辑界面，默认是第一个字段
    # list_display_links = list_display
    list_display_links =  ('id',)

    # 是否可以直接编辑
    list_editable = ('grade','code','supplierName','bankName','accountNumber','bankNunber','dutyParagraph','Note','state','abbreviation','industryStatus','entrustName','entrustTelephone','entrustAddress','entrustZipCode','entrustPhone','entrustFax','entrustEmail','registeredAddress','legalName','legalTelephone','legalPhone','contact1Name','contact1Post','contact1Telephone','contact1Phone','contact1Email','contact2Name','contact2Post','contact2Telephone','contact2Phone','contact2Email','contact3Name','contact3Post','contact3Telephone','contact3Phone','contact3Email','goodsTypeName','riskLevel','riskStatement','lastEditName','createName')

    # 需要显示的字段信息
    list_display = list_display_links + list_editable


    search_fields = list_display                           # 搜索字段
    list_filter = list_display  # 过滤器
    # date_hierarchy = 'create_time'                             # 头部添加  详细时间分层筛选　
    ordering = ('goodsType','supplierName')                               # 排序


# 注册时，在第二个参数写上 admin model
admin.site.register(Supplier,SupplierAdmin)
