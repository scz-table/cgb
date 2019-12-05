from django.contrib import admin
from .models import PublishArticle,ArticleColumn
from django.db import models

# Register your models here.
# Underwriter admin model


class PublishArticleAdmin(admin.ModelAdmin):

    list_max_show_all = 50
    list_per_page = 50         # 分页

    # 设置哪些字段可以点击进入编辑界面，默认是第一个字段
    # list_display_links = list_display
    list_display_links =  ('id',)

    # 是否可以直接编辑
    list_editable = ('title','body')

    # 需要显示的字段信息
    list_display = list_display_links + list_editable + ('author','change_time','create_time')


    search_fields = list_display                           # 搜索字段
    list_filter = ('title','author','create_time','change_time')  # 过滤器
    date_hierarchy = 'create_time'                             # 头部添加  详细时间分层筛选　
    ordering = ('-create_time','-change_time')                               # 排序


# 注册时，在第二个参数写上 admin model
admin.site.register(PublishArticle,PublishArticleAdmin)

class ArticleColumnAdmin(admin.ModelAdmin):

    list_max_show_all = 50
    list_per_page = 50         # 分页

    # 设置哪些字段可以点击进入编辑界面，默认是第一个字段
    # list_display_links = list_display
    list_display_links =  ('id',)

    # 是否可以直接编辑
    list_editable = ('column','notes')

    # 需要显示的字段信息
    list_display = list_display_links + list_editable + ('author','change_time','create_time')


    search_fields = list_display                           # 搜索字段
    list_filter = ('column','author','create_time','change_time')  # 过滤器
    date_hierarchy = 'create_time'                             # 头部添加  详细时间分层筛选　
    ordering = ('-create_time','-change_time')                               # 排序


# 注册时，在第二个参数写上 admin model
admin.site.register(ArticleColumn,ArticleColumnAdmin)
