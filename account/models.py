from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from account.cities import City
from category.models import Category


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **kwargs):
        if not email:
            return ValueError('The given email must be set!')
        email = self.normalize_email(email=email)
        user = self.model(email=email, **kwargs)
        user.create_activation_code()
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **kwargs):
        kwargs.setdefault('is_staff', False)
        kwargs.setdefault('is_superuser', False)
        return self._create_user(email, password, **kwargs)

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)
        if kwargs.get('is_staff') is not True:
            raise ValueError('Superuser must have status is_staff=True!')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must have status is_superuser=True!')
        return self._create_user(email, password, **kwargs)


class AccountCategory(models.Model):
    one = 1
    two = 2
    choice = ((one,'client'),(two,'executor'))



class CustomUser(AbstractUser):
    email = models.EmailField('email address', unique=True)
    password = models.CharField(max_length=100)
    activation_code = models.CharField(max_length=255, blank=True)
    username = models.CharField(max_length=100, blank=True)
    # phone = models.CharField(max_length=40,blank=True,null=True)
    # login = models.CharField(max_length=40,blank=True,null=True)
    user = models.PositiveSmallIntegerField(choices=AccountCategory.choice, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_active = models.BooleanField(_('active'), default=False,
                                    help_text=_(
                                        'Designates whether this user should be treated as active.' 
                                        'Unselect this  instead of deleting accounts.'))
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True, blank=True)
    subcategory = models.CharField(max_length=100,blank=True,null=True)
    avatar = models.ImageField(upload_to='media/', null=True, blank=True)
    passwordImage = models.ImageField(upload_to='media/passwordImage',blank=True,null=True)
    city = models.ForeignKey(City,blank=True,null=True,on_delete=models.SET_NULL)
    about_me = models.TextField(blank=True,null=True)
    video = models.FileField(upload_to='media/video_about_me', null=True,blank=True,
                             validators=[
                                 FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    birthday = models.DateTimeField(blank=True,null=True)





    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def create_activation_code(self):
        import uuid
        code = str(uuid.uuid4())
        self.activation_code = code

#  ДЛЯ ТОГО ЧТОБЫ ОТПРАВИТЬ ПИСЬМО СПАМ
class Spam_Contacts(models.Model):
    email = models.EmailField('email address',unique=True)


