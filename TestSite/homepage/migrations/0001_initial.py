# Generated by Django 4.0.3 on 2022-04-27 16:38

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('email_verify', models.BooleanField(default=False, verbose_name='Подтверждение аккаунта')),
                ('conditions', models.BooleanField(default=False, verbose_name='Условия конфиденциальности')),
                ('is_seller', models.BooleanField(default=False, verbose_name='Продавец или покупатель')),
                ('birth_day', models.DateField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Номер телефона должен быть в формате: '+994 XX XXX XX XX'.", regex='^\\+?1?\\d{9,14}$')], verbose_name='Номер телефона')),
                ('gender', models.CharField(choices=[('Не указан', 'Не указан'), ('Мужчина', 'Мужчина'), ('Женщина', 'Женщина'), ('Другое', 'Другое')], default='Не указан', max_length=20, verbose_name='Пол')),
                ('occupation', models.CharField(blank=True, max_length=50, verbose_name='Занятие')),
                ('address_type', models.CharField(blank=True, max_length=255, verbose_name='Тип адреса')),
                ('city', models.CharField(blank=True, max_length=50, verbose_name='Город')),
                ('place', models.CharField(blank=True, max_length=255, verbose_name='Место')),
                ('block_number', models.CharField(blank=True, max_length=50, verbose_name='Номер блока')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Категории')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('icon', models.CharField(max_length=255, verbose_name='Класс иконки')),
                ('topic', models.CharField(max_length=255, verbose_name='Класс категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Tovar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название Товара')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('content', models.TextField(verbose_name='Описание Товара')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время загрузки')),
                ('is_published', models.BooleanField(default=True, verbose_name='Статус')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='homepage.category', verbose_name='Категории')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Кем добавлено')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['-time_create'],
            },
        ),
    ]
