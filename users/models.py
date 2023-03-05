from django.db import models
from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
import time

# Third party fields
from phonenumber_field.modelfields import PhoneNumberField


class CustomUserManager(BaseUserManager):
    """A custom manager for the custom user."""

    def create_individual_user(self, first_name, last_name, username, password):
        """Create an individual account."""

        if not first_name:
            raise ValueError("Foydalanuvchi ismi kiritilmadi!")

        if not last_name:
            raise ValueError("Foydalanuvchi familiyasi kiritilmadi!")

        if not username:
            raise ValueError("Foydalanuvchi nomi kiritilmadi!")

        if not password:
            raise ValueError("Parol kiritilmadi!")

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            password_confirmation=password,
            last_login=f'{time.strftime("%Y-%m-%d", time.localtime())}',
            date_joined=f'{time.strftime("%Y-%m-%d", time.localtime())}',
        )

        user.is_active = True
        user.save(using=self._db)
        return user

    def create_legal_entity_user(self,
                                 first_name,
                                 last_name,
                                 brand_name,
                                 username,
                                 password):
        """Create a business account."""

        if not first_name:
            raise ValueError("Foydalanuvchi ismi kiritilmadi!")

        if not last_name:
            raise ValueError("Foydalanuvchi familiyasi kiritilmadi!")

        if not username:
            raise ValueError("Foydalanuvchi nomi kiritilmadi!")

        if not brand_name:
            raise ValueError("Kompaniya nomi kiritilmadi!")

        if not password:
            raise ValueError("Parol kiritilmadi!")

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            brand_name=brand_name,
            username=username,
            password=password,
            password_confirmation=password,
            last_login=f'{time.strftime("%Y-%m-%d", time.localtime())}',
            date_joined=f'{time.strftime("%Y-%m-%d", time.localtime())}',
        )

        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, username, password, phone_number):
        """Create a super user."""

        if not first_name:
            raise ValueError("Foydalanuvchi ismi kiritilmadi!")

        if not last_name:
            raise ValueError("Foydalanuvchi familiyasi kiritilmadi!")

        if not username:
            raise ValueError("Foydalanuvchi nomi kiritilmadi!")

        if not password:
            raise ValueError("Parol kiritilmadi!")

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            password_confirmation=password,
            phone_number=phone_number,
            last_login=f'{time.strftime("%Y-%m-%d", time.localtime())}',
            date_joined=f'{time.strftime("%Y-%m-%d", time.localtime())}',
        )

        user.is_active = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    """A custom user model."""

    # Attributes for both individuals and legal entities
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=30)
    password_confirmation = models.CharField(max_length=30, null=True)
    phone_number = PhoneNumberField(region=settings.PHONENUMBER_DEFAULT_REGION, max_length=13, null=True)
    telegram = models.URLField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True, unique=True)
    agreed_to_terms = models.BooleanField(default=False)

    # Attributes for individuals
    avatar = models.ImageField(null=True, blank=True, upload_to='media/user_loaded_images')

    # Attributes for legal entities
    brand_name = models.CharField(max_length=70, unique=True, null=True, blank=True)
    logo = models.ImageField(null=True, blank=True, upload_to='media/user_loaded_images')
    company_address = models.CharField(max_length=100, null=True, blank=True)

    # Attributes used mostly in server side
    orders = models.PositiveIntegerField(null=True, blank=True, default=0)
    books_ordered = models.PositiveIntegerField(null=True, blank=True, default=0)
    is_legal_entity = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now_add=False, null=True)
    date_joined = models.DateField(auto_now_add=False, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']

    PERMISSIONS = []

    def __str__(self):

        return self.username

    def get_full_name(self):
        """
        Gets the full name of a user.
        """

        if self.middle_name:
            return f'{self.first_name} {self.middle_name} {self.last_name}'
        else:
            return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        """
        Gets the first name only.
        """

        return self.first_name

    def add_permission(self, perm_name):
        """
        Adds the permission passed in to the list PERMISSIONS.
        """

        self.PERMISSIONS.append(perm_name)

    def has_perm(self, perm_name):
        """
        Checks whether a user has the permission passed in.
        """

        return True

    def has_module_perms(self, app_label):
        """
        Checks whether the user has a permission to view the app.
        """

        return True
