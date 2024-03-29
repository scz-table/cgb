# Generated by Django 2.1.10 on 2019-11-05 13:17

import Contract.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Classify', '0001_initial'),
        ('Supplier', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contractMarkTime', models.DateTimeField(default=Contract.models.get_datetime_now, verbose_name='合同登记时间')),
                ('contractSigninTime', models.DateTimeField(default=Contract.models.get_datetime_now, verbose_name='签订时间')),
                ('contractNumberA', models.CharField(max_length=50, unique=True, verbose_name='甲方合同编号')),
                ('contractNumberB', models.CharField(blank=True, max_length=50, unique=True, verbose_name='乙方合同编号')),
                ('totalSum', models.IntegerField(default=0, verbose_name='合同总额')),
                ('code', models.CharField(max_length=30, verbose_name='质保期')),
                ('qualityClause', models.TextField(verbose_name='质量条款')),
                ('Note', models.TextField(blank=True, verbose_name='备注')),
                ('signingPlace', models.CharField(max_length=255, verbose_name='签订地点')),
                ('freight', models.CharField(max_length=10, verbose_name='是否包含运费')),
                ('receivingAddress', models.CharField(max_length=10, verbose_name='收货地址')),
                ('approvalNumber', models.CharField(max_length=10, verbose_name='价格审批编号')),
                ('approvalPerson', models.CharField(max_length=10, verbose_name='价格申请人')),
                ('approvalPrice', models.CharField(max_length=10, verbose_name='审批价格')),
                ('approvalSupplier', models.CharField(max_length=10, verbose_name='价格审批供应商')),
                ('className', models.CharField(max_length=10, verbose_name='录入类别')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('change_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('Contacts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contractContacts', to=settings.AUTH_USER_MODEL, verbose_name='甲方代理人')),
                ('contractEdition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contractContractEdition', to='Classify.ContractEdition', verbose_name='合同版本')),
                ('createName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contractCreateName', to=settings.AUTH_USER_MODEL, verbose_name='创建记录员工')),
                ('goodsType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contractCoodsType', to='Classify.GoodsType', verbose_name='产品类型')),
                ('invoice_partment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contractInvoice_partment', to='Classify.Invoice_partment', verbose_name='结算单位')),
                ('lastEditName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contractLastEditName', to=settings.AUTH_USER_MODEL, verbose_name='最后编辑员工')),
                ('specialMark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contractSpecialMark', to='Classify.SpecialMark', verbose_name='特殊标记')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contractSupplierValue', to='Supplier.Supplier', verbose_name='供应商名称')),
            ],
            options={
                'verbose_name_plural': '合同信息',
                'db_table': 'contract',
            },
        ),
    ]
