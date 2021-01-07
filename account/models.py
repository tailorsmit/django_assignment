from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, mobile_no, password=None):
        if not email:
            raise ValueError('users must have an email')
        if not username:
            raise ValueError('users must have a username')
        if not mobile_no:
            raise ValueError('users must provide mobile number')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            mobile_no=mobile_no,
            verified=False,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        if not email:
            raise ValueError('users must have an email')
        if not username:
            raise ValueError('users must have a username')

        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='email', max_length=100, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    mobile_no = models.CharField(max_length=11, unique=True)
    verified = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    objects = MyAccountManager()

    def __str__(self):
        return self.username + " " + self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
