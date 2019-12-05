from django.db import models
from django.contrib.auth.models import User
from Classify.models import *

class Supplier(models.Model):
    grade=models.ForeignKey(Grade,on_delete=models.CASCADE,related_name='suppelierGrade',verbose_name="供应商等级")
    code=models.CharField(max_length=10,unique=True,verbose_name="供应商编码")
    supplierName=models.CharField(max_length=50,unique=True,verbose_name="供应商单位名称")
    bankName=models.CharField(max_length=50,verbose_name="开户行")
    accountNumber=models.CharField(max_length=50,unique=True,verbose_name="账号")
    bankNunber=models.CharField(max_length=50,verbose_name="行号")
    dutyParagraph=models.CharField(max_length=50,unique=True,null=False,blank=True,verbose_name="税号")
    Note=models.TextField(null=False,blank=True,verbose_name="备注")
    state=models.ForeignKey(CooperationState,on_delete=models.CASCADE,related_name='suppelierCooperationState',verbose_name="合作状态")
    goodsType=models.ManyToManyField(GoodsType,related_name='supplierGoodsType',verbose_name="产品类型")
    abbreviation=models.CharField(max_length=50,unique=True,verbose_name="简称")
    industryStatus=models.ForeignKey(IndustryStatus,on_delete=models.CASCADE,related_name='suppelierIndustryStatus',verbose_name="行业地位")
    entrustName=models.CharField(max_length=10,verbose_name="委托代理联系人姓名")
    entrustTelephone=models.CharField(max_length=11,verbose_name="手机")
    entrustAddress=models.TextField(verbose_name="办公地址")
    entrustZipCode=models.CharField(max_length=10,null=False,blank=True,verbose_name="邮编")
    entrustPhone=models.CharField(max_length=13,null=False,blank=True,verbose_name="电话")
    entrustFax=models.CharField(max_length=13,null=False,blank=True,verbose_name="传真")
    entrustEmail=models.EmailField(max_length=255,verbose_name="通信邮箱")
    registeredAddress=models.TextField(verbose_name="注册地址")
    legalName=models.CharField(max_length=5,verbose_name="法人姓名")
    legalTelephone=models.CharField(max_length=11,null=False,blank=True,verbose_name="法人手机")
    legalPhone=models.CharField(max_length=13,null=False,blank=True,verbose_name="法人固定电话")
    contact1Name=models.CharField(max_length=5,null=False,blank=True,verbose_name="联系人1姓名")
    contact1Post=models.CharField(max_length=10,null=False,blank=True,verbose_name="联系人1职务")
    contact1Telephone=models.CharField(max_length=11,null=False,blank=True,verbose_name="联系人1手机")
    contact1Phone=models.CharField(max_length=13,null=False,blank=True,verbose_name="联系人1固定电话")
    contact1Email=models.EmailField(max_length=255,null=False,blank=True,verbose_name="联系人1邮箱")
    contact2Name=models.CharField(max_length=5,null=False,blank=True,verbose_name="联系人2姓名")
    contact2Post=models.CharField(max_length=10,null=False,blank=True,verbose_name="联系人2职务")
    contact2Telephone=models.CharField(max_length=11,null=False,blank=True,verbose_name="联系人2手机")
    contact2Phone=models.CharField(max_length=13,null=False,blank=True,verbose_name="联系人2固定电话")
    contact2Email=models.EmailField(max_length=255,null=False,blank=True,verbose_name="联系人2邮箱")
    contact3Name=models.CharField(max_length=5,null=False,blank=True,verbose_name="联系人3姓名")
    contact3Post=models.CharField(max_length=10,null=False,blank=True,verbose_name="联系人3职务")
    contact3Telephone=models.CharField(max_length=11,null=False,blank=True,verbose_name="联系人3手机")
    contact3Phone=models.CharField(max_length=13,null=False,blank=True,verbose_name="联系人3固定电话")
    contact3Email=models.EmailField(max_length=255,null=False,blank=True,verbose_name="联系人3邮箱")
    Planner=models.ManyToManyField(User,related_name='supplierUser',verbose_name="计划员")
    goodsTypeName=models.CharField(max_length=100,null=False,blank=True,verbose_name="物料名称")
    riskLevel=models.ForeignKey(RiskLevel,on_delete=models.CASCADE,related_name='suppelierriskLevel',verbose_name="风险等级")
    riskStatement=models.TextField(null=False,blank=True,verbose_name="风险说明")
    lastEditName=models.ForeignKey(User,on_delete=models.CASCADE,related_name='suppelierLastEditName',verbose_name="最后编辑员工")
    createName=models.ForeignKey(User,on_delete=models.CASCADE,related_name='suppelierCreateName',verbose_name="创建记录员工")
    create_time=models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    change_time=models.DateTimeField(auto_now=True,verbose_name="修改时间")

    class Meta:
        db_table='supplier'
        verbose_name_plural = '供应商信息'
        ordering=("-create_time",)

    def __str__(self):
        return self.abbreviation