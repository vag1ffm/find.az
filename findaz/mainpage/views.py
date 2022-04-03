from .models import Items
from django.views.generic import TemplateView


class ShopMainPage(TemplateView):
    model = Items
    template_name = 'mainpage/index.html'
    context_object_name = 'items'

