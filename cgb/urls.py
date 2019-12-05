"""cgb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse


def index(request):
    return HttpResponse("战略采购部--首页")

urlpatterns = [
    path('admin/', admin.site.urls,name='home'),
# 首页代码
    path('',include('Front.urls',namespace="front")),
# 发布公告Publish
    path('publish/',include('Publish.urls',namespace="publish")),
# 用户拓展userextension
    path('user_extension/',include('User_Extension.urls',namespace="userextension")),
# 战略采购部合同、请款、发票
    path('contract/',include('Contract.urls',namespace="contract")),
# 供应商信息
    path('supplier/',include('Supplier.urls',namespace="supplier")),
]
