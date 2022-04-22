from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.checks import messages
from django.http import HttpResponse, HttpResponseNotFound, Http404, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

from TestSite import settings
from .forms import *
from .models import *
from .utils import *


class MainHome(DataMixin, ListView):
    model = Category
    template_name = "homepage/index.html"
    context_object_name = "categorii"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="FindAz - Главная страница")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        c = Category.objects.all()
        spisok = []
        for i in c:
            t = i.tovar_set.all()
            spisok.append(t)

        # return Tovar.objects.filter(is_published=True)
        return spisok

# def index(request):
#     tovari = Tovar.objects.all()
#     context = {
#         'tovari': tovari,
#         'cat_selected': 0,
#         'menu': menu,
#         'title': 'index homepage'
#     }
#     return render(request, 'homepage/home.html', context=context)


class AddTovar(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddTovarForm
    template_name = 'homepage/addpage.html'
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление Товара")
        return dict(list(context.items()) + list(c_def.items()))

# def addpage(request):
#     if request.method == "POST":
#         form = AddTovarForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect("home")
#     else:
#         form = AddTovarForm()
#
#     return render(request, 'homepage/addpage.html', {'form': form, 'menu': menu, "title": "Добавление статьи"})


class ShowTovar(DataMixin, DetailView):
    model = Tovar
    template_name = 'homepage/show_tovar.html'
    slug_url_kwarg = "tovarslug"
    context_object_name = "tovar"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['tovar'], cat_selected=context['tovar'].cat_id)
        return dict(list(context.items()) + list(c_def.items()))


# def show_tovar(request, tovarslug):
#     tovar = get_object_or_404(Tovar, slug=tovarslug)
#
#     context = {
#         'tovar': tovar,
#         'menu': menu,
#         'title': tovar.title,
#         'cat_selected': tovar.cat_id,
#     }
#     return render(request, 'homepage/show_tovar.html', context=context)


class HomeCategory(DataMixin, ListView):
    model = Tovar
    template_name = "homepage/filter-index.html"
    context_object_name = "tovari"
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="FindAz - Категория - " + str(context['tovari'][0].cat), cat_selected=context["tovari"][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Tovar.objects.filter(cat__slug=self.kwargs['catslug'], is_published=True)

# def show_category(request, catid):
#     tovari = Tovar.objects.filter(cat_id=catid)
#
#     if len(tovari)==0:
#         raise Http404
#
#     context = {
#         'tovari': tovari,
#         'cat_selected': catid,
#         'menu': menu,
#         'title': 'index homepage'
#     }
#     return render(request, 'homepage/home.html', context=context)


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'homepage/register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


# def RegisterUser(request):
#     form = RegisterUserForm()
#
#     if request.method == 'POST':
#         form = RegisterUserForm(request.POST)
#
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home')
#
#     context = {'form': form}
#     return render(request, 'homepage/register.html', context)


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'homepage/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')



def logout_user(request):
    logout(request)
    return redirect('home')


def pageNotFound(request, exception):
    return HttpResponseNotFound("Нет блять такого адреса, пиздуй обратно")


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "password/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    # email_from = settings.EMAIL_HOST_USER
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, "admin@mail.ru", [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="password/password_reset.html", context={"password_reset_form": password_reset_form})


def validate_username(request):
    """Проверка доступности логина"""
    username = request.GET.get('username', None)
    email = request.GET.get("email", None)
    response = {
        'is_taken': User.objects.filter(username__iexact=username).exists(),
        'is_email': User.objects.filter(email__iexact=email).exists()
    }
    print(response)
    return JsonResponse(response)
