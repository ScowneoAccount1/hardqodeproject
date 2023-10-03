from django.shortcuts import render
from .models import *

# Create your views here.
def default_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        user = request.user

        allowed_products = [v.products.all() for i, v in enumerate(user.allowed_products.all())][0]

        context = {
            'page_title': "главная",
            'products': Product.objects.all(),
            'allowed_products': allowed_products,
        }

        return render(request, 'general/starterpage.html', context=context)
    else:
        return render(request, 'general/empty.html', context={'page_title':'404'})