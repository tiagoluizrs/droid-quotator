from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

ROLES = (
    ('1', 'Admin'),
    ('2', 'Anunciante')
)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='E-mail', max_length=255, unique=True)
    first_name = models.CharField(verbose_name='Nome', max_length=30, unique=False, null=True, blank=True)
    last_name = models.CharField(verbose_name='Sobrenome', max_length=150, unique=False, null=True, blank=True)
    active = models.BooleanField(default=True, help_text="Estado do usuário ativo/inativo")
    staff = models.BooleanField(default=False, help_text="Caso seja marcado o usuário terá acesso ao painel admin")
    admin = models.BooleanField(default=False, help_text="Administrador do sistema") # a superuser
    role = models.CharField(choices=ROLES, default=ROLES[0][0], verbose_name='Função', max_length=1)

    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active

