# Arquivo: /apps/users/models.py
#-*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin


class EmailUserManager(BaseUserManager):
    def create_user(self, *args, **kwargs):
        email = kwargs["email"]
        email = self.normalize_email(email)
        password = kwargs["password"]
        kwargs.pop("password")

        if not email:
            raise ValueError(_('USUÁRIOS DEVEM TER OBRIGATORIAMENTE UM ENDEREÇO DE EMAIL!'))

        user = self.model(**kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, *args, **kwargs):
        user = self.create_user(**kwargs)
        user.is_superuser = True
        user.save(using=self._db)
        return user


class MyUser(PermissionsMixin, AbstractBaseUser):
    email = models.EmailField(
        verbose_name=_('Email'),
        unique=True,
	help_text=_('<------------------------------------------------------'),
    )
    first_name = models.CharField(
        verbose_name=_('Nome'),
        max_length=50,
        blank=False,
        help_text=_('Enter your name'),
    )
    last_name = models.CharField(
        verbose_name=_('Sobrenome'),
        max_length=50,
        blank=False,
        help_text=_('Enter your last name'),
    )
    spotify_username = models.CharField(
        verbose_name=_('Usuário do Spotify'),
        max_length=50,
        blank=False,
        help_text=_('Forgot? Go to: <a href ="https://www.spotify.com/us/account/overview">Spotify User</a>')
    )

    USERNAME_FIELD = 'email'
    objects = EmailUserManager()


class IdeaTrack(models.Model):
    name = models.CharField(verbose_name=_('Nome'), max_length=256)
    artist = models.CharField(verbose_name=_('Artista'), max_length=256)
    user = models.ForeignKey(MyUser)

    def __str__(self):  #For Python 2, use __str__ on Python 3
        return self.name

