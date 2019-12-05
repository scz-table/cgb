from django.db import models
from django.contrib.auth.models import User
from User_Extension.models import UserExtension
from django.utils import timezone
from Department.models import Department,Position
from django.urls import reverse
from slugify import slugify

class ArticleColumn(models.Model):
    author=models.ForeignKey(UserExtension,on_delete=models.CASCADE,related_name="article_column",verbose_name="作者")
    column=models.CharField(max_length=200,verbose_name="文章分类")
    notes=models.TextField(null=False,blank=True,verbose_name="备注")
    change_time=models.DateTimeField(auto_now=True,verbose_name="修改时间")
    create_time=models.DateTimeField(auto_now_add=True,verbose_name="创建时间")

    class Meta:
        db_table='article_column'
        verbose_name_plural = '文章分类'
        ordering=("-create_time","-change_time")

    def __str__(self):
        return self.column


class PublishArticle(models.Model):
    author=models.ForeignKey(UserExtension,on_delete=models.CASCADE,related_name="publish_article",verbose_name="作者")
    publish_department=models.CharField(max_length=500,verbose_name="发布部门")
    publish_department_position=models.CharField(max_length=500,verbose_name="发布人职位")
    # contains_department=models.ManyToManyField(Department,related_name="contains_department",null=False,blank=True,verbose_name="查看白名单")
    # excude_department=models.ManyToManyField(Department,related_name="excude_department",null=False,blank=True,verbose_name="查看黑名单")
    slug=models.SlugField(max_length=500)
    title=models.CharField(max_length=300,verbose_name="标题")
    column=models.ForeignKey(ArticleColumn,on_delete=models.CASCADE,related_name="article_column",verbose_name="文章分类")
    body=models.TextField(verbose_name="正文")
    change_time=models.DateTimeField(auto_now=True,verbose_name="修改时间")
    create_time=models.DateTimeField(auto_now_add=True,verbose_name="创建时间")

    class Meta:
        db_table='publish'
        index_together=(('id','slug','title'),)
        verbose_name_plural = '通知'
        ordering=("-create_time","-change_time")

    def __str__(self):
        return self.title


    def save(self, *args, **kargs):
        self.slug = slugify(self.title)
        super(PublishArticle, self).save(*args, **kargs)

    def get_absolute_url(self):
        return reverse("publish:article_detail", args=[self.id, self.slug])

    def get_url_path(self):
        return reverse("publish:article_content", args=[self.id, self.slug])


