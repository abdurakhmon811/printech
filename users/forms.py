from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from django import forms
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UsernameField

from .models import CustomUser
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import RegionalPhoneNumberWidget


class BusinessUserCreationForm(forms.ModelForm):
    """A form for creating a new user for a legal entity."""

    class Meta:

        model = CustomUser
        fields = [
            'first_name', 'last_name', 'middle_name', 'brand_name',
            'phone_number', 'username', 'password', 'password_confirmation',
            'agreed_to_terms',
        ]


class BusinessUserChangeForm(forms.ModelForm):
    """A form for updating user information."""

    password = ReadOnlyPasswordHashField()

    class Meta:

        model = CustomUser
        fields = [
            'logo', 'first_name', 'last_name', 'middle_name',
            'username', 'password', 'phone_number',
            'telegram', 'email',
        ]
        labels = {
            'logo': "Tashkilot logotipi",
            'first_name': "Ism (tashkilot asoschisi)",
            'last_name': "Familiya (tashkilot asoschisi)",
            'middle_name': "Sharif",
            'username': "Foydalanuvchi nomi (login)",
            'password': "Parol",
            'phone_number': "Telefon raqam",
            'email': "Email manzil",
        }
        widgets = {
            'logo': forms.FileInput(attrs={
                # TODO: Make a custom file input class for uploading an avatar.
                'class': '',
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'middle_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'username': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'password': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'phone_number': RegionalPhoneNumberWidget(attrs={
                'class': 'form-control',
                'placeholder': '+998901234567',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'qwerty@example.com',
            }),
        }


class CaptchaForm(forms.Form):
    """A form for recaptcha field."""

    captcha = ReCaptchaField(
        label='',
        widget=ReCaptchaV2Checkbox(attrs={
            'data-theme': 'dark',
        }),
    )


class IndividualUserCreationForm(forms.ModelForm):
    """A form for creating a new user for an individual."""

    class Meta:

        model = CustomUser
        fields = [
            'first_name', 'last_name', 'middle_name', 'phone_number',
            'username', 'password', 'password_confirmation', 'agreed_to_terms',
        ]


class IndividualUserChangeForm(forms.ModelForm):
    """A form for updating user information."""

    password = ReadOnlyPasswordHashField()

    class Meta:

        model = CustomUser
        fields = [
            'avatar', 'first_name', 'last_name', 'middle_name',
            'username', 'password', 'phone_number', 'telegram',
            'email',
        ]
        labels = {
            'avatar': "Foydalanuvchi rasmi",
            'first_name': "Ism",
            'last_name': "Familiya",
            'middle_name': "Sharif",
            'username': "Foydalanuvchi nomi (login)",
            'password': "Parol",
            'phone_number': "Telefon raqam",
            'email': "Email manzil",
        }
        widgets = {
            'avatar': forms.FileInput(attrs={
                # TODO: Make a custom file input class for uploading an avatar.
                'class': '',
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'middle_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'username': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'password': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'phone_number': RegionalPhoneNumberWidget(attrs={
                'class': 'form-control',
                'placeholder': '+998901234567',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'qwerty@example.com',
            })
        }


class PhoneNumberLoginForm(forms.Form):
    """A form for authenticating registered users with their phone_number."""

    phone_number = PhoneNumberField()
    password = forms.CharField()


class UserChangeForm(forms.ModelForm):
    """A form for changing user information in general (for using in the Django admin system)."""

    class Meta:

        model = CustomUser
        fields = [
            'first_name', 'last_name', 'middle_name', 'username',
            'password', 'phone_number', 'telegram', 'email',
            'avatar', 'brand_name', 'logo', 'company_address',
            'orders', 'books_ordered', 'is_legal_entity', 'is_staff',
            'is_superuser', 'is_admin',
        ]
        labels = {
            'first_name': "First name",
            'last_name': "Last name",
            'middle_name': "Middle name",
            'username': "Username",
            'password': "Password",
            'phone_number': "Phone number",
            'telegram': "Telegram",
            'email': "Email",
            'avatar': "Photo",
            'brand_name': "Brand name",
            'logo': "Brand logo",
            'company_address': "Organization address",
            'orders': "The number of orders",
            'books_ordered': "The number of books bought",
            'is_legal_entity': "is-legal-entity",
            'is_staff': "is-staff",
            'is_superuser': "is-superuser",
            'is_admin': "is-admin",
        }


class UserCreationForm(forms.ModelForm):
    """A form for creating a new user in general (for using in the Django admin system)."""

    class Meta:

        model = CustomUser
        fields = [
            'first_name', 'last_name', 'middle_name', 'username',
            'password', 'phone_number', 'telegram', 'email',
            'avatar', 'brand_name', 'logo', 'company_address',
            'orders', 'books_ordered', 'is_legal_entity', 'is_staff',
            'is_superuser', 'is_admin',
        ]
        labels = {
            'first_name': "First name",
            'last_name': "Last name",
            'middle_name': "Middle name",
            'username': "Username",
            'password': "Password",
            'phone_number': "Phone number",
            'telegram': "Telegram",
            'email': "Email",
            'avatar': "Photo",
            'brand_name': "Organization name",
            'logo': "Brand logo",
            'company_address': "Organization address",
            'orders': "The number of orders",
            'books_ordered': "The number of books bought",
            'is_legal_entity': "is-legal-entity",
            'is_staff': "is-staff",
            'is_superuser': "is-superuser",
            'is_admin': "is-admin",
        }


class UserAdmin(BaseUserAdmin):

    # The forms to add and change individual user instances.
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ['first_name', 'last_name', 'username']
    list_filter = []
    fieldsets = [
        ('Sensitive information',
         {'fields': ['username',
                     'password']}),
        ('Personal information',
         {'fields': ['first_name',
                     'last_name',
                     'middle_name',
                     'phone_number',
                     'telegram',
                     'email',
                     'avatar',
                     'brand_name',
                     'logo',
                     'company_address']}),
        ('Server-side properties',
         {'fields': ['orders',
                     'books_ordered',
                     'is_legal_entity',
                     'is_active',
                     'is_staff',
                     'is_superuser',
                     'is_admin',
                     'last_login',
                     'date_joined']}),
    ]
    add_fieldsets = [
        (None, {
            'classes': ['wide'],
            'fields': ['username', 'password'],
        })
    ]
    search_fields = ['username']
    ordering = ['username']
    filter_horizontal = []


class UsernameLoginForm(forms.Form):
    """A form for authenticating registered users with their usernames."""

    username = UsernameField()
    password = forms.CharField()
