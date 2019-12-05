from django.urls import path
from django.views.generic.base import TemplateView
from . import views
app_name='supplier'
urlpatterns = [
    path('',views.SupplierListView.as_view(),name='SupplierListView'),
    path('search',TemplateView.as_view(template_name='Supplier/SupplierSearch.html'),name='SupplierSearchView'),


]