from django.contrib import auth
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core import serializers
from django.core.checks import messages
from django.http import HttpResponse, HttpResponseNotFound, Http404, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

from unidecode import unidecode
from django.template import defaultfilters

# from transliterate import slugify

from TestSite import settings
from .forms import *
from .models import *
from .utils import *


az_to_en_for_slug = {
    'ə': 'e',
    'ğ': 'g',
    'ö': 'o',
    'ş': 'sh',
    'ç': 'c',
    'ı': 'i',
    'ü': 'u'
}


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


# class AddTovar(LoginRequiredMixin, DataMixin, CreateView):
#     form_class = AddTovarForm
#     template_name = 'homepage/adding-tovar.html'
#     login_url = reverse_lazy('home')
#     raise_exception = True
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title="Добавление Товара")
#         return dict(list(context.items()) + list(c_def.items()))
#
#     def form_valid(self, form):
#         text = str(self.request.POST.get('title')).lower()
#
#         for letter in az_to_en_for_slug:
#             if letter in text:
#                 text = text.replace(letter, az_to_en_for_slug[letter])
#
#         try:
#             temp_slug = text + "-pk" + str(Tovar.objects.latest('pk').id + 1)
#         except:
#             temp_slug = text + "-pk0"
#
#         temp_slug2 = unidecode(temp_slug)
#
#         form.instance.slug = defaultfilters.slugify(temp_slug2)
#         form.instance.created_by = self.request.user
#         return super().form_valid(form)


def addtovar(request):
    if request.method == "POST":
        form = AddTovarForm(request.POST, request.FILES)
        cats = Category.objects.all()
        if form.is_valid():

            text = str(request.POST.get('title')).lower()

            for letter in az_to_en_for_slug:
                if letter in text:
                    text = text.replace(letter, az_to_en_for_slug[letter])

            try:
                temp_slug = text + "-pk" + str(Tovar.objects.latest('pk').id + 1)
            except:
                temp_slug = text + "-pk0"

            temp_slug2 = unidecode(temp_slug)

            form.instance.slug = defaultfilters.slugify(temp_slug2)
            form.instance.created_by = request.user

            form.save()
            return redirect("home")
    else:
        form = AddTovarForm()
    data = {
        'form': form,
        'cat': Category.objects.all(),
        'podcat': PodCat.objects.all(),
        'podpodcat': PodPodCat.objects.all(),
        "title": "Добавление статьи"
    }

    return render(request, 'homepage/adding-tovar.html', data)


# class ShowTovar(DataMixin, DetailView):
#     model = Tovar
#     template_name = 'homepage/show-tovar.html'
#     slug_url_kwarg = "tovarslug"
#     context_object_name = "tovar"
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title=context['tovar'], cat_selected=context['tovar'].cat_id)
#         return dict(list(context.items()) + list(c_def.items()))


def show_tovar(request, tovarslug):

    tovar = get_object_or_404(Tovar, slug=tovarslug)
    store = get_object_or_404(User, email=tovar.created_by)

    context = {
        'tovar': tovar,
        'title': tovar.title,
        'store': store
    }
    return render(request, 'homepage/show-tovar.html', context=context)


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
        return Tovar.objects.filter(cat__slug=self.kwargs['catslug'])

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
        # login(self.request, user)
        # return redirect('home')
        send_email_for_verify(self.request, user)
        return redirect('confirm_email')


class RegisterSeller(DataMixin, CreateView):
    form_class = RegisterSellerForm
    template_name = 'homepage/for-salers.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация Продавца")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        form.instance.is_seller = True
        form.instance.city = "Baku"
        user = form.save()
        # login(self.request, user)
        # return redirect('home')
        send_email_for_verify(self.request, user)
        return redirect('confirm_email')
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
    return HttpResponseNotFound("Нет такой страницы")


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
    # Проверка доступности и валидности и заполняемой формы
    email = request.GET.get("email", None)

    response = {
        'is_email': User.objects.filter(email__iexact=email).exists(),
    }

    return JsonResponse(response)


User = get_user_model()


class EmailVerify(View):

    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)

        if user is not None and token_generator.check_token(user, token):
            user.email_verify = True
            user.save()
            login(request, user)
            return redirect('home')
        return redirect('invalid_verify')

    @staticmethod
    def get_user(uidb64):
        try:
            # urlsafe_base64_decode() decodes to bytestring
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (
            TypeError,
            ValueError,
            OverflowError,
            User.DoesNotExist,
            ValidationError,
        ):
            user = None
        return user


def crud_favorites(request):
    print("asjkdghalhbsdlygyugauidgyasgil")
    r = request.GET.get("heart", None)
    # ebat = auth.get_user(request)
    # ebat.favorite_posts.add(Tovar.objects.get(id=1))
    # ebat.favorite_posts.remove(Tovar.objects.get(id=1))
    # ebat.favorite_posts.all()

    # goods = Tovar.objects.all()
    # goods_json = serializers.serialize('json', goods)
    #
    # return HttpResponse(goods_json, content_type='application/json')
