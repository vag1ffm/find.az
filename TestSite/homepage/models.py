from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse


class Tovar(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название Товара")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(verbose_name="Описание Товара")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время загрузки")
    is_published = models.BooleanField(default=True, verbose_name="Статус")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категории")
    created_by = models.ForeignKey("User", on_delete=models.CASCADE, verbose_name="Кем добавлено")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('showtovar', kwargs={"tovarslug": self.slug})

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['-time_create']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категории")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    icon = models.CharField(max_length=255, verbose_name="Класс иконки")
    topic = models.CharField(max_length=255, verbose_name="Класс категории")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={"catslug": self.slug})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['id']


class User(AbstractUser):
    DEFAULT = 'Не указан'
    MALE = 'Мужчина'
    FEMALE = 'Женщина'
    OTHER = 'Другое'
    GENDER_CHOICES = [
        (DEFAULT, 'Не указан'),
        (MALE, 'Мужчина'),
        (FEMALE, 'Женщина'),
        (OTHER, 'Другое'),
    ]
    email = models.EmailField(_("email address"), unique=True)
    email_verify = models.BooleanField(default=False, verbose_name="Подтверждение аккаунта")
    conditions = models.BooleanField(default=False, verbose_name="Условия конфиденциальности")
    is_seller = models.BooleanField(default=False, verbose_name="Продавец или покупатель")
    birth_day = models.DateField(null=True, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$', message="Номер телефона должен быть в формате: '+994 XX XXX XX XX'.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, verbose_name="Номер телефона")
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default=DEFAULT, verbose_name="Пол")
    occupation = models.CharField(max_length=50, verbose_name="Занятие", blank=True)
    address_type = models.CharField(max_length=255, verbose_name="Тип адреса", blank=True)
    city = models.CharField(max_length=50, verbose_name="Город", blank=True)
    place = models.CharField(max_length=255, verbose_name="Место", blank=True)
    block_number = models.CharField(max_length=50, verbose_name="Номер блока", blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
