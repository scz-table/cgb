# 一.配置路由
# urlpatterns = [
#
#     url(r'^admin/', admin.site.urls),
# ]
#
# 当前配置的路由可以创建一些路由映射关系：
#
# / admin /
# / admin / login /
# / admin / logout /
# / admin / password_change /
# / admin / password_change / done /
#
# / admin / app名称 / model名称 /
# / admin / app名称 / model名称 / add /
# / admin / app名称 / model名称 / ID值 / history /
# / admin / app名称 / model名称 / ID值 / change /
# / admin / app名称 / model名称 / ID值 / delete /
#
# 二.定制Admin
# 在admin.py中只需要讲Mode中的某个类注册，即可在Admin中实现增删改查的功能，如：
#
# admin.site.register(models.UserInfo)
#
# 但是，这种方式比较简单，如果想要进行更多的定制操作，需要利用ModelAdmin进行操作，如：
#
#
# 1
# 方式一：
# 2
#
#
# class UserAdmin(admin.ModelAdmin):
#     3
#     list_display = ('user', 'pwd',)
#
#
# 4
# 5
# admin.site.register(models.UserInfo, UserAdmin)  # 第一个参数可以是列表
# 6
# 7
# 8
# 方式二：
# 9 @ admin.register(models.UserInfo)  # 第一个参数可以是列表
# 10
#
#
# class UserAdmin(admin.ModelAdmin):
#     11
#     list_display = ('user', 'pwd',)
#
#
# ModelAdmin中提供了大量的可定制功能，如
#
# 1.
# list_display，列表时，定制显示的列。
#
# @admin.register(models.UserInfo)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('user', 'pwd', 'xxxxx')
#
#     def xxxxx(self, obj):
#         return "xxxxx"
#
#
# 2.
# list_display_links，列表时，定制列可以点击跳转。
#
# @admin.register(models.UserInfo)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('user', 'pwd', 'xxxxx')
#     list_display_links = ('pwd',)
#
#
# 3.
# list_filter，列表时，定制右侧快速筛选。
#
#
#
# from django.utils.translation import ugettext_lazy as _
#
#
# @admin.register(models.UserInfo)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('user', 'pwd')
#
#     class Ugg(admin.SimpleListFilter):
#         title = _('decade born')
#         parameter_name = 'xxxxxx'
#
#         def lookups(self, request, model_admin):
#             """
#             显示筛选选项
#             :param request:
#             :param model_admin:
#             :return:
#             """
#             return models.UserGroup.objects.values_list('id', 'title')
#
#         def queryset(self, request, queryset):
#             """
#             点击查询时，进行筛选
#             :param request:
#             :param queryset:
#             :return:
#             """
#             v = self.value()
#             return queryset.filter(ug=v)
#
#     list_filter = ('user', Ugg,)
#
#
#
# 4.
# list_select_related，列表时，连表查询是否自动select_related
#
# 5.
# 分页相关
#
#
# # 分页，每页显示条数
# list_per_page = 100
#
# # 分页，显示全部（真实数据<该值时，才会有显示全部）
# list_max_show_all = 200
#
# # 分页插件
# paginator = Paginator
#
# 6.
# list_editable，列表时，可以编辑的列
#
#
# @admin.register(models.UserInfo)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('user', 'pwd', 'ug',)
#     list_editable = ('ug',)
#
#
# 7.
# search_fields，列表时，模糊搜索的功能
#
#
# @admin.register(models.UserInfo)
# class UserAdmin(admin.ModelAdmin):
#     search_fields = ('user', 'pwd')
#
#
# 8.
# date_hierarchy，列表时，对Date和DateTime类型进行搜索
#
#
# @admin.register(models.UserInfo)
# class UserAdmin(admin.ModelAdmin):
#     date_hierarchy = 'ctime'
#
#
# 9.
# preserve_filters，详细页面，删除、修改，更新后跳转回列表后，是否保留原搜索条件
#
# 10.
# save_as = False，详细页面，按钮为“Sava as new” 或 “Sava and add
# another”
#
# 11.
# save_as_continue = True，点击保存并继续编辑
#
# save_as_continue = True
#
# # 如果 save_as=True，save_as_continue = True， 点击Sava as new 按钮后继续编辑。
# # 如果 save_as=True，save_as_continue = False，点击Sava as new 按钮后返回列表。
#
# New in Django
# 1.10.
# 12.
# save_on_top = False，详细页面，在页面上方是否也显示保存删除等按钮
#
# 13.
# inlines，详细页面，如果有其他表和当前表做FK，那么详细页面可以进行动态增加和删除
#
#
#
#
# class UserInfoInline(admin.StackedInline):  # TabularInline
#     extra = 0
#     model = models.UserInfo
#
#
# class GroupAdminMode(admin.ModelAdmin):
#     list_display = ('id', 'title',)
#     inlines = [UserInfoInline, ]
#
#
#
# 14.
# action，列表时，定制action中的操作
#
#
#
#
# @admin.register(models.UserInfo)
# class UserAdmin(admin.ModelAdmin):
#
#     # 定制Action行为具体方法
#     def func(self, request, queryset):
#         print(self, request, queryset)
#         print(request.POST.getlist('_selected_action'))
#
#     func.short_description = "中文显示自定义Actions"
#     actions = [func, ]
#
#     # Action选项都是在页面上方显示
#     actions_on_top = True
#     # Action选项都是在页面下方显示
#     actions_on_bottom = False
#
#     # 是否显示选择个数
#     actions_selection_counter = True
#
#
#
# 15.
# 定制HTML模板
#
# add_form_template = None
# change_form_template = None
# change_list_template = None
# delete_confirmation_template = None
# delete_selected_confirmation_template = None
# object_history_template = None
# 16.
# raw_id_fields，详细页面，针对FK和M2M字段变成以Input框形式
#
#
# @admin.register(models.UserInfo)
# class UserAdmin(admin.ModelAdmin):
#     raw_id_fields = ('FK字段', 'M2M字段',)
#
#
# 17.
# fields，详细页面时，显示字段的字段
#
#
# @admin.register(models.UserInfo)
# class UserAdmin(admin.ModelAdmin):
#     fields = ('user',)
#
#
# 18.
# exclude，详细页面时，排除的字段
#
#
# @admin.register(models.UserInfo)
# class UserAdmin(admin.ModelAdmin):
#     exclude = ('user',)
#
#
# 19.
# readonly_fields，详细页面时，只读字段
#
#
# @admin.register(models.UserInfo)
# class UserAdmin(admin.ModelAdmin):
#     readonly_fields = ('user',)
#
#
# 20.
# fieldsets，详细页面时，使用fieldsets标签对数据进行分割显示
#
#
#
#
# @admin.register(models.UserInfo)
# class UserAdmin(admin.ModelAdmin):
#     fieldsets = (
#         ('基本数据', {
#             'fields': ('user', 'pwd', 'ctime',)
#         }),
#         ('其他', {
#             'classes': ('collapse', 'wide', 'extrapretty'),  # 'collapse','wide', 'extrapretty'
#             'fields': ('user', 'pwd'),
#         }),
#     )
#
#
#
# 21.
# 详细页面时，M2M显示时，数据移动选择（方向：上下和左右）
#
# @admin.register(models.UserInfo)
# class UserAdmin(admin.ModelAdmin):
#     filter_vertical = ("m2m字段",)  # 或filter_horizontal = ("m2m字段",)
#
#
# 22.
# ordering，列表时，数据排序规则
#
#
# @admin.register(models.UserInfo)
# class UserAdmin(admin.ModelAdmin):
#     ordering = ('-id',)
#     或
#
#     def get_ordering(self, request):
#         return ['-id', ]
#
#
# 23.
# view_on_site，编辑时，是否在页面上显示view
# on
# set
#
# view_on_site = False
# 或
#
#
# def view_on_site(self, obj):
#     return 'https://www.baidu.com'
#
#
# 24.
# radio_fields，详细页面时，使用radio显示选项（FK默认使用select）
#
# radio_fields = {"ug": admin.VERTICAL}  # 或admin.HORIZONTAL
# 25.
# show_full_result_count = True，列表时，模糊搜索后面显示的数据个数样式
#
#
# @admin.register(models.UserInfo)
# class UserAdmin(admin.ModelAdmin):
#     # show_full_result_count = True # 1 result (12 total)
#     # show_full_result_count = False  # 1 result (Show all)
#     search_fields = ('user',)
#
#
# 26.
# formfield_overrides = {}，详细页面时，指定现实插件
#
#
# from django.forms import widgets
# from django.utils.html import format_html
#
#
# class MyTextarea(widgets.Widget):
#     def __init__(self, attrs=None):
#         # Use slightly better defaults than HTML's 20x2 box
#         default_attrs = {'cols': '40', 'rows': '10'}
#         if attrs:
#             default_attrs.update(attrs)
#         super(MyTextarea, self).__init__(default_attrs)
#
#     def render(self, name, value, attrs=None):
#         if value is None:
#             value = ''
#         final_attrs = self.build_attrs(attrs, name=name)
#         return format_html('<textarea {}>\r\n{}</textarea>', final_attrs, value)
#
#
# @admin.register(models.UserInfo)
# class UserAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         models.models.CharField: {'widget': MyTextarea},
#     }
#
#
#
# 27.
# prepopulated_fields = {}，添加页面，当在某字段填入值后，自动会将值填充到指定字段。
#
# @admin.register(models.UserInfo)
# class UserAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"email": ("user", "pwd",)}
#
#
# PS: DjangoAdmin中使用js实现功能，页面email字段的值会在输入：user、pwd时自动填充
#
# 28.
# form = ModelForm，用于定制用户请求时候表单验证
#
#
# from app01 import models
# from django.forms import ModelForm
# from django.forms import fields
#
#
# class MyForm(ModelForm):
#     others = fields.CharField()
#
#     class Meta:
#         model = models = models.UserInfo
#         fields = "__all__"
#
#
# @admin.register(models.UserInfo)
# class UserAdmin(admin.ModelAdmin):
#     form = MyForm
#
#
#
#
# 29.
# empty_value_display = "列数据为空时，显示默认值"
#
#
#
#
# @admin.register(models.UserInfo)
# class UserAdmin(admin.ModelAdmin):
#     empty_value_display = "列数据为空时，默认显示"
#
#     list_display = ('user', 'pwd', 'up')
#
#     def up(self, obj):
#         return obj.user
#
#     up.empty_value_display = "指定列数据为空时，默认显示"
#
#
