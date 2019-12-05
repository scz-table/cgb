from django.views.generic import DetailView,ListView,CreateView,UpdateView,FormView,DeleteView,View
from django.http import Http404
# from .models import Article
from Supplier.models import Supplier
from django.utils import timezone


class IndexView(ListView):
    model = Supplier #等同于queryset = Supplier.objects.all().order_by("-pub_date")
    template_name = 'blog/Supplier_list.html'
    context_object_name = 'latest_Suppliers'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()  # 只有这行代码有用
        return context

    def get_queryset(self):
        qs = super().get_queryset()  # 调用父类方法
        return qs.filter(author=self.request.user).order_by('-pub_date')


class SupplierDetailView(DetailView):
    queryset = Supplier.objects.all().order_by("-pub_date")
    template_name = 'blog/Supplier_detail.html'
    context_object_name = 'Supplier'
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)

     if obj.author != self.request.user:
          raise Http404()
     return obj
