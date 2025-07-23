from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product


class SearchProductView(ListView):
    template_name = "products/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        print(request.GET)
        query = request.GET.get('q')
        print(query)
        if query is not None:
            return Product.objects.filter(title__icontains=query)
        return Product.objects.none()
        '''
        __icontains = field contains this
        __iexact = fields is exactly matching

        '''