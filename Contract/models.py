from django.db import models
from django.contrib.auth.models import User
from Classify.models import *
from Supplier.models import *
from django.utils.timezone import now
import pytz
def get_datetime_now():
    # return now().replace(tzinfo=pytz.timezone("Asia/Shanghai"))
    return now()

class Contract(models.Model):
    goodsType=models.ForeignKey(GoodsType,on_delete=models.CASCADE,related_name='contractCoodsType',verbose_name="产品类型")
    invoice_partment=models.ForeignKey(Invoice_partment,on_delete=models.CASCADE,related_name='contractInvoice_partment',verbose_name="结算单位")
    contractEdition=models.ForeignKey(ContractEdition,on_delete=models.CASCADE,related_name='contractContractEdition',verbose_name="合同版本")
    specialMark=models.ForeignKey(SpecialMark,on_delete=models.CASCADE,related_name='contractSpecialMark',verbose_name="特殊标记")
    # contractEdition=models.ForeignKey(ContractEdition,on_delete=models.CASCADE,related_name='contractContractEdition',verbose_name="合同版本")
    # specialMark=models.ForeignKey(SpecialMark,on_delete=models.CASCADE,related_name='contractSpecialMark',verbose_name="特殊标记")
    contractMarkTime=models.DateTimeField(default=get_datetime_now,verbose_name="合同登记时间")
    contractSigninTime=models.DateTimeField(default=get_datetime_now,verbose_name="签订时间")
    contractNumberA=models.CharField(max_length=50,unique=True,verbose_name="甲方合同编号")
    contractNumberB=models.CharField(max_length=50,unique=True,null=False,blank=True,verbose_name="乙方合同编号")
    Contacts=models.ForeignKey(User,on_delete=models.CASCADE,related_name='contractContacts',verbose_name="甲方代理人")
    supplier=models.ForeignKey(Supplier,on_delete=models.CASCADE,related_name='contractSupplierValue',verbose_name="供应商名称")
    totalSum=models.IntegerField(default=0,verbose_name="合同总额")
    code=models.CharField(max_length=30,verbose_name="质保期")
    qualityClause=models.TextField(verbose_name="质量条款")
    Note=models.TextField(null=False,blank=True,verbose_name="备注")
    signingPlace=models.CharField(max_length=255,verbose_name="签订地点")
    freight=models.CharField(max_length=10,verbose_name="是否包含运费")
    receivingAddress=models.CharField(max_length=10,verbose_name="收货地址")
    approvalNumber=models.CharField(max_length=10,verbose_name="价格审批编号")
    approvalPerson=models.CharField(max_length=10,verbose_name="价格申请人")
    approvalPrice=models.CharField(max_length=10,verbose_name="审批价格")
    approvalSupplier=models.CharField(max_length=10,verbose_name="价格审批供应商")
    className=models.CharField(max_length=10,verbose_name="录入类别")
    lastEditName=models.ForeignKey(User,on_delete=models.CASCADE,related_name='contractLastEditName',verbose_name="最后编辑员工")
    createName=models.ForeignKey(User,on_delete=models.CASCADE,related_name='contractCreateName',verbose_name="创建记录员工")
    create_time=models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    change_time=models.DateTimeField(auto_now=True,verbose_name="修改时间")

    class Meta:
        db_table='contract'
        verbose_name_plural = '合同信息'
        ordering=("-create_time",)
    def __str__(self):
        return self.contractNumberA