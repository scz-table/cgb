from django.urls import path
from . import views
app_name='contract'
urlpatterns = [
    path('',views.index,name='front_index'),


]