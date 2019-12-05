from django.contrib import admin
from .models import GoodsType,Contract
from django.db import models

# Register your models here.
# Underwriter admin model

class ContractAdmin(admin.ModelAdmin):

    list_max_show_all = 50
    list_per_page = 50         # 分页

    # 设置哪些字段可以点击进入编辑界面，默认是第一个字段
    # list_display_links = list_display
    list_display_links =  ('id',)

    # 是否可以直接编辑
    list_editable = ('goodsType','invoice_partment','contractEdition','specialMark','contractMarkTime','contractSigninTime','contractNumberA','contractNumberB','Contacts','supplier','totalSum','code','qualityClause','Note','signingPlace','freight','receivingAddress','approvalNumber','approvalPerson','approvalPrice','approvalSupplier','className','lastEditName','createName')

    # 需要显示的字段信息
    list_display = list_display_links + list_editable

    search_fields = list_display                           # 搜索字段
    list_filter =  ('goodsType','invoice_partment','contractEdition','specialMark','Contacts','approvalPerson','approvalPrice','approvalSupplier','className','lastEditName','createName')  # 过滤器
    # date_hierarchy = 'create_time'                             # 头部添加  详细时间分层筛选　
    ordering = ('goodsType','invoice_partment','supplier')                              # 排序


# 注册时，在第二个参数写上 admin model
admin.site.register(Contract,ContractAdmin)
