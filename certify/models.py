# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model
from django.utils import timezone
import uuid


class AccountManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, name, phone, password, **extra_fields):
        values = [email, name, phone]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
        for field_name, value in field_value_map.items():
            if not value:
                raise ValueError('The {} value must be set'.format(field_name))

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            name=name,
            phone=phone,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, name, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, name, phone, password, **extra_fields)

    def create_superuser(self, email, name, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, name, phone, password, **extra_fields)


class Account(AbstractBaseUser, PermissionsMixin):
    

    CHOICES_GENDER=(
        ('MALE','MALE'),
        ('FEMALE','FEMALE'),
        ('OTHERS','OTHERS')
        )

    CHOICES_LEVEL = (
        ('BASIC', 'BASIC'),
        ('SECONDARY', 'SECONDARY'),
        ('TERTIARY','TERTIARY'),
        ('OTHERS','OTHERS'),
    )
    
   
    CHOICES_FIELD=(
    
            ('ART','ART'),
            ('PHYSICS','PHYSICS'),
            ('CHEMISTRY','CHEMISTRY'),
            ('BIOLOGY','BIOLOGY'),
            ('MATHEMATICS','MATHEMATICS'),
            ('OTHERS','OTHERS'),
    
            )
   

    
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=50)
    date_of_birth = models.DateField(blank=True, null=True)
    gender=models.CharField(max_length=20, choices=CHOICES_GENDER)
    picture = models.ImageField(blank=True, null=True,upload_to='uploads/picture')
    #edu_other = models.CharField(max_length=100,blank=True, null=True)
    education_level= models.CharField(max_length=20, choices=CHOICES_LEVEL,null=True, blank=True)
    #field_other = models.CharField(max_length=100,blank=True, null=True)
    field_of_interest=models.CharField(max_length=100, choices=CHOICES_FIELD,null=True,blank=True)   
    update_me_on_my_field=models.BooleanField(default=False,null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(null=True)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name.split()[0]
       

class Captcha(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    value=models.CharField(max_length=30)
    image=models.ImageField(upload_to="captcha")

    def __str__(self):
        return 'Captcha {} with value - {}'.format(self.id, self.value)