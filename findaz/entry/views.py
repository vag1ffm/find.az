from django.views.generic import CreateView
from .forms import RegisterUserForm


class EntryPage(CreateView):
    form_class = RegisterUserForm
    template_name = 'entry/voyti.html'
    success_url = 'mainpage/index.html'
