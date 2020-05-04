from django.views.generic.list import ListView
from django.shortcuts import render

from .models import Product

class ProductListview(ListView):
    queryset = Product.objects.all()
    template_name = "products/list.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListview, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context

def product_list_view(request):
    querset = Product.objects.all()
    context = {
        "object_list": querset
    }
    return render(request, "products/list.html", context)
