from django.db import models


class GoodsType(models.Model):
    goodsType=models.CharField(max_length=10,unique=True,verbose_name="产品类型")
    Note=models.CharField(max_length=10,null=False,blank=True,verbose_name="备注")

    class Meta:
        db_table='goodstype'
        verbose_name_plural = '产品类型'
    def __str__(self):
        return self.goodsType

class Invoice_partment(models.Model):
    invoice_partment=models.CharField(max_length=10,unique=True,verbose_name="结算单位")
    Note=models.CharField(max_length=10,null=False,blank=True,verbose_name="备注")

    class Meta:
        db_table='invoice_partment'
        verbose_name_plural = '结算单位'
    def __str__(self):
        return self.invoice_partment

class RiskLevel(models.Model):
    riskLevel=models.CharField(max_length=10,unique=True,verbose_name="风险等级")
    Note=models.CharField(max_length=10,null=False,blank=True,verbose_name="备注")

    class Meta:
        db_table='riskLevel'
        verbose_name_plural = '风险等级'
    def __str__(self):
        return self.riskLevel

class ContractEdition(models.Model):
    contractEdition=models.CharField(max_length=10,unique=True,verbose_name="合同版本")
    Note=models.CharField(max_length=10,null=False,blank=True,verbose_name="备注")

    class Meta:
        db_table='contractedition'
        verbose_name_plural = '合同版本'
    def __str__(self):
        return self.contractEdition

class SpecialMark(models.Model):
    specialMark=models.CharField(max_length=10,unique=True,verbose_name="特殊标记")
    Note=models.CharField(max_length=10,null=False,blank=True,verbose_name="备注")

    class Meta:
        db_table='specialmark'
        verbose_name_plural = '特殊标记'
    def __str__(self):
        return self.specialMark

class Grade(models.Model):
    grade=models.CharField(max_length=10,unique=True,verbose_name="供应商等级")
    Note=models.CharField(max_length=10,null=False,blank=True,verbose_name="备注")

    class Meta:
        db_table='grade'
        verbose_name_plural = '供应商等级'
    def __str__(self):
        return self.grade
class CooperationState(models.Model):
    cooperationState=models.CharField(max_length=10,unique=True,verbose_name="合作状态")
    Note=models.CharField(max_length=10,null=False,blank=True,verbose_name="备注")

    class Meta:
        db_table='cooperationstate'
        verbose_name_plural = '合作状态'
    def __str__(self):
        return self.cooperationState
class IndustryStatus(models.Model):
    industryStatus=models.CharField(max_length=10,unique=True,verbose_name="行业地位")
    Note=models.CharField(max_length=10,null=False,blank=True,verbose_name="备注")

    class Meta:
        db_table='industrystatus'
        verbose_name_plural = '行业地位'
    def __str__(self):
        return self.industryStatus