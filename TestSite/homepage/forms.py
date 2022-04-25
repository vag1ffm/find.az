from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm as DjangoAuthenticationForm
from django.core.exceptions import ValidationError

from .models import *
from .utils import send_email_for_verify

User = get_user_model()


class AuthenticationForm(DjangoAuthenticationForm):
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username is not None and password:
            self.user_cache = authenticate(
                self.request, username=username, password=password
            )
            if self.user_cache is not None:
                if not self.user_cache.email_verify:
                    send_email_for_verify(self.request, self.user_cache)
                    raise ValidationError(
                        'Аккаунт не подтвержден проверьте свою почту',
                        code='invalid_login'
                    )
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data


class AddTovarForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["cat"].empty_label = "Категория не выбрана"

    class Meta:
        model = Tovar
        fields = ["title", "slug", "content", "photo", "price", "is_published", "cat"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "tovar-form"}),
            "slug": forms.TextInput(attrs={"class": "tovar-form"}),
            "content": forms.Textarea(attrs={"class": "tovar-form"})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превысила 200 символов')
        return title


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Имя Пользователя", widget=forms.TextInput(attrs={"placeholder": "Your Full Name"}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={"placeholder": "E-Mail"}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"placeholder": "Password"}))
    password2 = forms.CharField(label="Повтор пароля", widget=forms.PasswordInput(attrs={"placeholder": "Repeat your password"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Имя Пользователя", widget=forms.TextInput(attrs={"placeholder": "Log in"}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"placeholder": "Password"}))

