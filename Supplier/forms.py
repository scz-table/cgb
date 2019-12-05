from django import forms
from .models import *
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User
from Universalscript import errorTips,generalVar


class SupplierSearchForm(forms.ModelForm):
    item1 = forms.CharField(required=False)
    item2 = forms.CharField(required=False)
    item3 = forms.CharField(required=False)
    item4 = forms.CharField(required=False)
    item5 = forms.CharField(required=False)

    foritemchoice = (
        ('code', '供应商编码'),
        ('supplierName', '供应商单位名称'),
        ('abbreviation', '简称'),
        ('bankName', '开户行'),
        ('accountNumber', '账号'),
        ('bankNunber', '行号'),
        ('dutyParagraph', '税号'),
        ('Note', '备注'),
        ('state__cooperationState', '合作状态'),
        ('goodsType__goodsType', '产品类型'),
        ('industryStatus__industryStatus', '行业地位'),
        ('entrustName', '委托代理联系人姓名'),
        ('legalName', '法人姓名'),
    )

    and_or_type = (
        ('and-icontains', u'且(包含)'),
        ('or-icontains', u'或(包含)'),
        ('and-exclude', u'且(排除)'),
        ('or-exclude', u'或(排除)'),
    )
    and_or1 = forms.CharField(required=False,widget=forms.widgets.Select(choices=and_or_type,attrs={'class':'form-control'}))
    and_or2 = forms.CharField(required=False,widget=forms.widgets.Select(choices=and_or_type,attrs={'class':'form-control'}))
    and_or3 = forms.CharField(required=False,widget=forms.widgets.Select(choices=and_or_type,attrs={'class':'form-control'}))
    and_or4 = forms.CharField(required=False,widget=forms.widgets.Select(choices=and_or_type,attrs={'class':'form-control'}))
    and_or5 = forms.CharField(required=False,widget=forms.widgets.Select(choices=and_or_type,attrs={'class':'form-control'}))

    # 动态获取下拉菜单
    # queue = forms.ModelChoiceField(label=u'队列', queryset=Queue.objects.all())

    foritem1 = forms.CharField(required=False,widget=forms.widgets.Select(choices=foritemchoice,attrs={'class':'form-control'}))
    foritem2 = forms.CharField(required=False,widget=forms.widgets.Select(choices=foritemchoice,attrs={'class':'form-control'}))
    foritem3 = forms.CharField(required=False,widget=forms.widgets.Select(choices=foritemchoice,attrs={'class':'form-control'}))
    foritem4 = forms.CharField(required=False,widget=forms.widgets.Select(choices=foritemchoice,attrs={'class':'form-control'}))
    foritem5 = forms.CharField(required=False,widget=forms.widgets.Select(choices=foritemchoice,attrs={'class':'form-control'}))

    abbreviation= forms.CharField(required=False)

    class Meta:
        model = Supplier
        fields = ['abbreviation',]