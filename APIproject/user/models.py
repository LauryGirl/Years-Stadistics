from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):

    def create_user(self, email, password, name, last_name):
        if not email:
            raise ValueError('The user needs an email')

        user = self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.name = name
        user.last_name = last_name
        user.save()
        return user

    def create_superuser(self, email, password, name, last_name):
        user = self.create_user(
            email=email, password=password, name=name, last_name=last_name)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user

class Role(models.Model):
    name = models.CharField(max_length=120, unique=True)
    admin = models.BooleanField(default=False)
    professor = models.BooleanField(default=False)
    student = models.BooleanField(default=False)
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Rol"
        verbose_name_plural = "Roles"
        ordering = ['-id']

class User(AbstractBaseUser):
    name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=128)
    registration_date = models.DateTimeField(blank=True, null=True)
    email = models.CharField(max_length=128, unique=True)
    
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    blocked = models.BooleanField(default=False)
    verification_code = models.IntegerField(default=0)
    verification_code_created_date = models.DateTimeField(
        blank=True, null=True)

    roles = models.ManyToManyField(Role, related_name='users')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.name + ' ' + self.last_name

    def has_module_perms(self, app_label):
        if self.is_superuser:
            return True

    def has_perm(self, perm, obj=None):
        return True

    def has_perms(self, perm, obj=None):
        return True

    class Meta:
        verbose_name = "User"
        verbose_name_plural = 'Users'
        ordering = ['-id']
