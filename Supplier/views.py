from django.http import HttpResponse
from django.shortcuts import redirect,reverse,render
from django.views.generic import ListView,View
from .models import *
from .forms import *
from django.utils.timezone import make_aware
from Universalscript.get_paginator import get_pagination_data_ListView

class SupplierListView(ListView):
    model = Supplier
    template_name = 'Supplier/SupplierList.html'
    context_object_name = 'Supplier'
    paginate_by = 50
    ordering = '-id'
    page_kwarg = 'page'
    table_th_name=['序号','供应商等级','供应商编码','供应商单位名称','开户行','账号','行号','税号','备注','合作状态','产品类型','简称','行业地位','委托代理联系人姓名','手机','办公地址','邮编','电话','传真','通信邮箱','注册地址','法人姓名','法人手机','法人固定电话','联系人1姓名','联系人1职务','联系人1手机','联系人1固定电话','联系人1邮箱','联系人2姓名','联系人2职务','联系人2手机','联系人2固定电话','联系人2邮箱','联系人3姓名','联系人3职务','联系人3手机','联系人3固定电话','联系人3邮箱','计划员','物料名称','风险等级','风险说明','最后编辑员工','创建记录员工','创建时间','修改时间']

    def get_queryset(self):
        # qs = super().get_queryset()  # 调用父类方法
        # 获取url 中的值 比如http://127.0.0.1/admin/colortags/?name_text=红色
        search_dict=self.request.GET.dict()
        # 得到这些字段，并转换为字典存储到search_dict
        # name1=and-icontains-supplierName-鞍山
        search_contains={}
        search_exclude={}
        if search_dict.get('page'):
            del search_dict['page']
            # 删除掉p，页码字段
        for tmp_dict_value in search_dict.values():
            tmp_dict_value=tmp_dict_value.split('-')
            if tmp_dict_value[2]=='global':
                pass
            elif tmp_dict_value[1] == 'icontains' and tmp_dict_value[3]:
                search_contains[tmp_dict_value[2]+"__icontains"]=tmp_dict_value[3]
            elif tmp_dict_value[1] == 'exclude' and tmp_dict_value[3]:
                search_exclude[tmp_dict_value[2]+"__icontains"]=tmp_dict_value[3]

        print('查询供应商的条件是：',search_contains,search_exclude)
        return Supplier.objects.filter(**search_contains).exclude(**search_exclude)
        # return Supplier.objects.filter(goodsType__goodsType__icontains="锻造")
        # return Supplier.objects.filter(**self.request.GET.dict())

    def get_context_data(self, **kwargs):
        context = super(SupplierListView, self).get_context_data(**kwargs)
        page_obj = context.get('page_obj')
        paginator = context.get('paginator')
        pagination_data = get_pagination_data_ListView(page_obj, paginator)
        context.update(pagination_data)
        context['table_th_name']=self.table_th_name

        # paginator=context.get('paginator')
        # print('一共有多少条数据：',paginator.count)
        # print('一共有多少页：',paginator.num_pages)
        # print('页码范围：',paginator.page_range)
        #
        # page_obj=context.get('page_obj')
        # print('是否有下一条数据：',page_obj.has_next())
        # print('是否有上一条数据：',page_obj.has_previous())
        # print('下一页页码：',page_obj.next_page_number())
        # print('上一页页码：',page_obj.previous_page_number())
        # print('当前页页码：',page_obj.number)
        # print('当前页的第一条数据索引：',page_obj.start_index())
        # print('当前页的最后一条数据索引：',page_obj.end_index())

        return context
