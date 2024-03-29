from django import forms
from .models import Account, \
    BindingPrice, BlogPost, Book, \
    CategoryEx, CategoryIn, ColorPrice, Complaint, Contact, Coupon, CoverPrice, \
    Expense, \
    GluePrice, \
    Income, \
    LType, Loss, \
    News, \
    Order, OrderOptions, OuterPrice, \
    PagePrice, PaperPrice, PlaceToGet, Printer, \
    RefillAndPageCount, Resource, RingPrice, RType, \
    SubCategoryEx, SubCategoryIn, \
    Transaction, \
    Workforce, \
    YarnPrice
import time

# Third party application widgets
from bootstrap_datepicker_plus.widgets import DateTimePickerInput, DatePickerInput
from djmoney.forms.widgets import MoneyWidget


class AccountForm(forms.ModelForm):
    """A form for adding money accounts (available to admins only)."""

    class Meta:

        currencies = [
            ('EUR', 'EUR'),
            ('RUB', 'RUB'),
            ('USD', 'USD'),
            ('UZS', 'UZS'),
        ]

        model = Account
        fields = [
            'name', 'means',
        ]
        labels = {
            'name': "Hisob raqam nomi",
            'means': "Summa",
        }
        error_messages = {
            'name': {
                'required': "Forma to'lirilmadi!",
            },
            'means': {
                'invalid': "Forma noto'g'ri to'ldirildi!",
                'required': "Forma to'lirilmadi!",
            }
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'means': MoneyWidget(
                amount_widget=forms.NumberInput(
                    attrs={
                        'class': 'form-control',
                        'placeholder': "Mavjud miqdor",
                        'style': 'border-radius: .7rem .7rem .0rem .0rem;',
                    }),
                currency_widget=forms.Select(
                    attrs={
                        'class': 'form-select form-control',
                        'style': 'border-radius: .0rem .0rem .7rem .7rem; ',
                    },
                    choices=currencies)
            ),
        }


class BindingPriceForm(forms.ModelForm):
    """A form for adding binding types and prices (available to admins only)."""

    class Meta:

        model = BindingPrice
        fields = [
            'date', 'type', 'size',
        ]
        labels = {
            'date': "Sana",
            'type': "Ulash turi",
            'size': "O'lchami",
        }
        error_messages = {
            'date': {
                'invalid': "Forma noto'g'ri to'ldirildi!",
                'required': "Forma to'ldirilmadi!",
            },
            'type': {
                'required': "Forma to'ldirilmadi!",
            },
            'size': {
                'required': "Forma to'ldirilmadi!",
            },
        }
        widgets = {
            'date': DatePickerInput(attrs={
                'class': 'form-control',
                'placeholder': f'{time.strftime("%Y-%m-%d", time.localtime())}',
            }),
            'type': forms.Select(attrs={
                'class': 'form-control',
            }),
            'size': forms.Select(attrs={
                'class': 'form-control',
            }),
        }


class BlogPostForm(forms.ModelForm):
    """A form for adding blog posts (available to admins only)."""

    class Meta:

        model = BlogPost
        fields = [
            'title', 'subtitle_1', 'subtitle_2', 'subtitle_3',
            'picture_1', 'picture_2', 'picture_3', 'body_1',
            'body_2', 'body_3', 'conclusion', 'publisher_tg',
            'publisher_li', 'publisher_gm', 'publisher_tw', 'ref_links',
        ]
        labels = {
            'title': "Sarlavha",
            'subtitle_1': "Kichik sarlavha №1 (Majburiy)",
            'subtitle_2': "Kichik sarlavha №2 (Ixtiyoriy)",
            'subtitle_3': "Kichik sarlavha №3 (Ixtiyoriy)",
            'picture_1': "Fotorasm №1 (Majburiy)",
            'picture_2': "Fotorasm №2 (Ixtiyoriy)",
            'picture_3': "Fotorasm №3 (Ixtiyoriy)",
            'body_1': "Tafsilotlar №1 (Majburiy)",
            'body_2': "Tafsilotlar №2 (Ixtiyoriy)",
            'body_3': "Tafsilotlar №3 (Ixtiyoriy)",
            'conclusion': "Xulosa",
            'publisher_tg': "Nashriyotchining Telegram sahifasi",
            'publisher_li': "Nashriyotchining LinkedIn sahifasi",
            'publisher_gm': "Nashriyotchining Gmail pochta quttisi",
            'publisher_tw': "Nashriyotchining Twitter sahifasi",
            'ref_links': "Foydalanilgan axborot vositalari",
        }
        error_messages = {
            'title': {
                'required': "Forma to'ldirilmadi!",
            },
            'subtitle_1': {
                'required': "Forma to'ldirilmadi!",
            },
            'picture_1': {
                'required': "Forma to'ldirilmadi!",
            },
            'body_1': {
                'required': "Forma to'ldirilmadi!",
            },
            'conclusion': {
                'required': "Forma to'ldirilmadi!",
            },
            'publisher_tg': {
                'invalid': "Telegram manzil noto'g'ri kiritildi!",
                'required': "Forma to'ldirilmadi!",
            },
            'publisher_li': {
                'invalid': "LinkedIn manzil noto'g'ri kiritildi!",
                'required': "Forma to'ldirilmadi!",
            },
            'publisher_gm': {
                'invalid': "Gmail manzil noto'g'ri kiritildi!",
                'required': "Forma to'ldirilmadi!",
            },
            'publisher_tw': {
                'invalid': "Twitter manzil noto'g'ri kiritildi!",
                'required': "Forma to'ldirilmadi!",
            },
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'subtitle_1': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'subtitle_2': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'subtitle_3': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'picture_1': forms.FileInput(attrs={
                'class': 'custom-file-input',
                'style': 'padding: 0;',
            }),
            'picture_2': forms.FileInput(attrs={
                'class': 'custom-file-input',
                'style': 'padding: 0;',
            }),
            'picture_3': forms.FileInput(attrs={
                'class': 'custom-file-input',
                'style': 'padding: 0;',
            }),
            'body_1': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10,
            }),
            'body_2': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10,
            }),
            'body_3': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10,
            }),
            'conclusion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
            }),
            'publisher_tg': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://telegram.me/foydalanuvchi-nomi',
            }),
            'publisher_li': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://www.linkedin.com/in/foydalanuvchi-nomi-000000000',
            }),
            'publisher_gm': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'qwerty@example.com',
            }),
            'publisher_tw': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://twitter.com/foydalanuvchi-nomi',
            }),
            'ref_links': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'https://www.wikipedia.com/...',
            }),
        }


class BookForm(forms.ModelForm):
    """A form for adding books (available to admins only)."""

    class Meta:

        model = Book
        fields = [
            'category', 'name_coded', 'picture', 'pages', 'chars', 'telegram_link',
        ]
        labels = {
            'category': "Janri",
            'name_coded': "Kodi",
            'picture': "Muqovasi",
            'pages': "Betlar soni",
            'chars': "Kitob haqida qisqacha",
            'telegram_link': "Telegram havolasi",
        }
        error_messages = {
            'category': {
                'required': "Forma to'ldirilmadi!",
            },
            'name_coded': {
                'required': "Forma to'ldirilmadi!",
            },
            'pages': {
                'invalid': "Butun son kiriting!",
                'required': "Forma to'ldirilmadi!",
            },
            'chars': {
                'required': "Forma to'ldirilmadi!",
            },
            'telegram_link': {
                'invalid': "Telegram manzil noto'g'ri kiritildi!",
                'required': "Forma to'ldirilmadi!",
            },
        }
        widgets = {
            'category': forms.Select(attrs={
                'class': 'form-control',
            }),
            'name_coded': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '#100',
            }),
            'picture': forms.FileInput(attrs={
                'class': 'custom-file-input',
                'style': 'padding: 0;',
            }),
            'pages': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0',
            }),
            'chars': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
            }),
            'telegram_link': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://telegram.me/kitob-xabari-havolasi',
            })
        }


class CategoryExForm(forms.ModelForm):
    """A form handling expense categories (available to admins only)."""

    class Meta:

        model = CategoryEx
        fields = [
            'category',
        ]
        labels = {
            'category': "Xarajat kategoriyasi",
        }
        error_messages = {
            'category': {
                'required': "Forma to'lidirilmadi!",
            }
        }
        widgets = {
            'category': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Transport",
            }),
        }


class CategoryInForm(forms.ModelForm):
    """A form handling expense categories (available to admins only)."""

    class Meta:
        model = CategoryIn
        fields = [
            'category',
        ]
        labels = {
            'category': "Daromad kategoriyasi",
        }
        error_messages = {
            'category': {
                'required': "Forma to'lidirilmadi!",
            }
        }
        widgets = {
            'category': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Biznes',
            }),
        }


class ColorPriceForm(forms.ModelForm):
    """A form for adding prices to colors based on color (available to admins only)."""

    class Meta:

        currencies = [
            ('EUR', 'EUR'),
            ('RUB', 'RUB'),
            ('USD', 'USD'),
            ('UZS', 'UZS'),
        ]

        model = ColorPrice
        fields = [
            'date', 'color', 'size', 'price',
        ]
        labels = {
            'date': "Sana",
            'color': "Rang",
            'size': "Kitob o'lchami",
            'price': "Narx (bir bet uchun)",
        }
        error_messages = {
            'date': {
                'invalid': "Forma noto'g'ri to'ldirildi!",
                'required': "Forma to'ldirilmadi!",
            },
            'color': {
                'required': "Forma to'ldirilmadi!",
            },
            'size': {
                'required': "Forma to'ldirilmadi!",
            },
            'price': {
                'invalid': "Forma noto'g'ri to'ldirildi!",
                'required': "Forma to'ldirilmadi!",
            },
        }
        widgets = {
            'date': DatePickerInput(attrs={
                'class': 'form-control',
                'placeholder': f"{time.strftime('%Y-%m-%d', time.localtime())}",
            }),
            'color': forms.Select(attrs={
                'class': 'form-control',
            }),
            'size': forms.Select(attrs={
                'class': 'form-control',
            }),
            'price': MoneyWidget(
                amount_widget=forms.NumberInput(
                    attrs={
                        'class': 'form-control',
                        'placeholder': '0',
                        'style': 'border-radius: .7rem .7rem .0rem .0rem;',
                    }),
                currency_widget=forms.Select(
                    attrs={
                        'class': 'form-select form-control',
                        'style': 'border-radius: .0rem .0rem .7rem .7rem; ',
                    },
                    choices=currencies)
            ),
        }


class ComplaintForm(forms.ModelForm):
    """A form for receiving complaints from users."""

    class Meta:

        model = Complaint
        fields = [
            'title', 'book', 'time_bought', 'problem',
        ]
        labels = {
            'title': "Sarlavha",
            'book': "Kitob",
            'time_bought': "Sotib olingan vaqt",
            'problem': "Muammo",
        }
        error_messages = {
            'title': {
                'required': "Forma to'ldirilmadi!",
            },
            'book': {
                'required': "Forma to'ldirilmadi!",
            },
            'time_bought': {
                'invalid': "Vaqt noto'g'ri formatda kiritildi!",
                'required': "Forma to'ldirilmadi!"
            },
            'problem': {
                'required': "Forma to'ldirilmadi!",
            },
        }
        widgets = {
              'title': forms.TextInput(attrs={
                  'class': 'form-control',
                  'placeholder': "Sarlavha",
              }),
              'book': forms.Select(attrs={
                  'class': 'form-control',
              }),
              'time_bought': DatePickerInput(attrs={
                  'class': 'form-control',
                  'placeholder': f'{time.strftime("%Y-%m-%d", time.localtime())}',
              }),
              'problem': forms.Textarea(attrs={
                  'class': 'form-control',
                  'placeholder': "Muammo...",
                  'cols': 50,
                  'rows': 10,
              }),
        }


class ComplaintBookForm(forms.ModelForm):
    """A form for receiving special complaints about books from users."""

    class Meta:

        model = Complaint
        fields = [
            'book', 'time_bought', 'problem',
        ]
        labels = {
            'book': "Kitob",
            'time_bought': "Sotib olingan vaqt",
            'problem': "Xabar",
        }
        error_messages = {
            'book': {
                'required': "Forma to'ldirilmadi!",
            },
            'time_bought': {
                'invalid': "Vaqt noto'g'ri formatda kiritildi!",
                'required': "Forma to'ldirilmadi!",
            },
            'problem': {
                'required': "Forma to'ldirilmadi!",
            },
        }
        widgets = {
            'book': forms.Select(attrs={
                'class': 'form-control',
            }),
            'time_bought': DatePickerInput(attrs={
                'class': 'form-control',
                'placeholder': f'{time.strftime("%Y-%m-%d", time.localtime())}',
            }),
            'problem': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Muammo...",
            })
        }


class ComplaintOtherForm(forms.ModelForm):
    """A form for receiving special complaints about other topics from users."""

    class Meta:

        model = Complaint
        fields = [
            'title', 'problem',
        ]
        labels = {
            'title': "Sarlavha",
            'problem': "Xabar",
        }
        error_messages = {
            'title': {
                'required': "Forma to'ldirilmadi!",
            },
            'problem': {
                'required': "Forma to'ldirilmadi!",
            },
        }
        widgets = {
            'custom_category': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Yetkazib berish",
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Sarlavha",
            }),
            'problem': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Xabar...",
            }),
        }


class ComplaintSiteForm(forms.ModelForm):
    """A form for receiving special complaints about the website from users."""

    class Meta:

        model = Complaint
        fields = [
            'title', 'problem',
        ]
        labels = {
            'title': "Sarlavha",
            'problem': "Xabar",
        }
        error_messages = {
            'title': {
                'required': "Forma to'ldirilmadi!",
            },
            'problem': {
                'required': "Forma to'ldirilmadi!",
            },
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Sarlavha",
            }),
            'problem': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Muammo...",
                'cols': 50,
                'rows': 10,
            }),
        }


class ContactForm(forms.ModelForm):
    """A form for receiving inquires from users."""

    class Meta:

        model = Contact
        fields = [
            'telegram', 'title', 'message',
        ]
        labels = {
            'telegram': "Telegram manzilingiz (ixtiyoriy)",
            'title': "Sarlavha",
            'message': "Xabar",
        }
        error_messages = {
            'telegram': {
                'invalid': "Telegram manzil noto'g'ri kiritildi!",
                'required': "Forma to'ldirilmadi!",
            },
            'title': {
                'required': "Forma to'ldirilmadi!",
            },
            'message': {
                'required': "Forma to'ldirilmadi!",
            },
        }
        widgets = {
            'telegram': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': "https://telegram.me/foydalanuvchi-nomi",
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Xabar...",
            }),
        }


class CouponForm(forms.ModelForm):
    """A form for adding coupons for discounts (available to admins only)."""

    class Meta:

        model = Coupon
        fields = [
            'date_release', 'type', 'lifetime', 'for_books',
            'minus', 'status', 'owner', 'for_retail',
            'sold_given',
        ]
        labels = {
            'date_release': "Chiqarilgan sana",
            'type': "Turi",
            'lifetime': "Muddati",
            'for_books': "Kitoblar soni (kuponni olish uchun xarid qilish kerak bo'lgan)",
            'minus': "Chegirma foizi",
            'status': "Holati",
            'owner': "Egasi",
            'for_retail': "Sotuv uchun",
            'sold_given': "Sotildi/Berildi",
        }
        error_messages = {
            'date_release': {
                'invalid': "Forma noto'g'ri to'ldirildi!",
                'required': "Forma to'ldirilmadi!",
            },
            'type': {
                'required': "Forma to'ldirilmadi!",
            },
            'lifetime': {
                'invalid': "Forma noto'g'ri to'ldirildi!",
                'required': "Forma to'ldirilmadi!",
            },
            'for_books': {
                'invalid': "Butun son kiriting!"
            },
            'minus': {
                'required': "Forma to'ldirilmadi!",
            },
            'status': {
                'required': "Forma to'ldirilmadi!",
            },
        }
        widgets = {
            'date_release': DatePickerInput(attrs={
                'class': 'form-control',
                'placeholder': f'{time.strftime("%Y-%m-%d", time.localtime())}',
            }),
            'type': forms.Select(attrs={
                'class': 'form-control',
            }),
            'lifetime': DatePickerInput(attrs={
                'class': 'form-control',
                'placeholder': f'{time.strftime("%Y-%m-%d", time.localtime())}',
            }),
            'for_books': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0',
            }),
            'minus': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0',
            }),
            'status': forms.Select(attrs={
                'class': 'form-control',
            }),
            'owner': forms.Select(attrs={
                'class': 'form-control',
            }),
            'for_retail': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
            'sold_given': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }


class CoverPriceForm(forms.ModelForm):
    """A form for adding prices to covers based on type and size (available to admins only)."""

    class Meta:
        currencies = [
            ('EUR', 'EUR'),
            ('RUB', 'RUB'),
            ('USD', 'USD'),
            ('UZS', 'UZS'),
        ]

        model = CoverPrice
        fields = [
            'date', 'type', 'size', 'price',
        ]
        labels = {
            'date': "Sana",
            'type': "Turi",
            'size': "O'lchami",
            'price': "Narx",
        }
        error_messages = {
            'date': {
                'invalid': "Forma noto'g'ri to'ldirildi!",
                'required': "Forma to'ldirilmadi!",
            },
            'type': {
                'required': "Forma to'ldirilmadi!",
            },
            'size': {
                'required': "Forma to'ldirilmadi!",
            },
            'price': {
                'invalid': "Forma noto'g'ri to'ldirildi!",
                'required': "Forma to'ldirilmadi!",
            },
        }
        widgets = {
            'date': DatePickerInput(attrs={
                'class': 'form-control',
                'placeholder': f"{time.strftime('%Y-%m-%d', time.localtime())}",
            }),
            'type': forms.Select(attrs={
                'class': 'form-control',
            }),
            'size': forms.Select(attrs={
                'class': 'form-control',
            }),
            'price': MoneyWidget(
                amount_widget=forms.NumberInput(
                    attrs={
                        'class': 'form-control',
                        'placeholder': '0',
                        'style': 'border-radius: .7rem .7rem .0rem .0rem;',
                    }),
                currency_widget=forms.Select(
                    attrs={
                        'class': 'form-select form-control',
                        'style': 'border-radius: .0rem .0rem .7rem .7rem; ',
                    },
                    choices=currencies)
            ),
        }


class ExpenseForm(forms.ModelForm):
    """A form for making expenses related to business (available to admins only)."""

    class Meta:

        currencies = [
            ('EUR', 'EUR'),
            ('RUB', 'RUB'),
            ('USD', 'USD'),
            ('UZS', 'UZS'),
        ]

        model = Expense
        fields = [
            'category', 'subcategory', 'user', 'account',
            'date_made', 'comment', 'amount',
        ]
        labels = {
            'category': "Kategoriya",
            'subcategory': "Quyi kategoriya",
            'user': "Foydalanuvchi",
            'account': "Hisob",
            'date_made': "Sana",
            'comment': "Izoh",
            'amount': "Miqdor",
        }
        error_messages = {
            'category': {
                'required': "Forma to'ldirilmadi!",
            },
            'subcategory': {
                'required': "Forma to'ldirilmadi!",
            },
            'user': {
                'required': "Forma to'ldirilmadi!",
            },
            'account': {
                'required': "Forma to'ldirilmadi!",
            },
            'date_made': {
                'invalid': "Vaqt noto'g'ri formatda kiritildi!",
                'required': "Forma to'ldirilmadi!",
            },
            'comment': {
                'required': "Forma to'ldirilmadi!",
            },
            'amount': {
                'invalid': "Forma noto'g'ri to'ldirildi!",
                'required': "Forma to'ldirilmadi!",
            },
        }
        widgets = {
            'category': forms.Select(attrs={
                'class': 'form-control',
            }),
            'subcategory': forms.Select(attrs={
                'class': 'form-control',
            }),
            'user': forms.Select(attrs={
                'class': 'form-control',
            }),
            'account': forms.Select(attrs={
                'class': 'form-control',
            }),
            'date_made': DateTimePickerInput(attrs={
                'class': 'form-control',
                'placeholder': f'{time.strftime("%Y-%m-%d %H:%I", time.localtime())}',
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
            }),
            'amount': MoneyWidget(
                amount_widget=forms.NumberInput(
                    attrs={
                        'class': 'form-control',
                        'placeholder': '0',
                        'style': 'border-radius: .7rem .7rem .0rem .0rem;',
                    }),
                currency_widget=forms.Select(
                    attrs={
                        'class': 'form-select form-control',
                        'style': 'border-radius: .0rem .0rem .7rem .7rem; ',
                    },
                    choices=currencies)
            ),
        }


class GluePriceForm(forms.ModelForm):
    """A form for adding prices to glue based on type (available to admins only)."""

    class Meta:
        currencies = [
            ('EUR', 'EUR'),
            ('RUB', 'RUB'),
            ('USD', 'USD'),
            ('UZS', 'UZS'),
        ]

        model = GluePrice
        fields = [
            'date', 'type', 'size', 'price',
        ]
        labels = {
            'date': "Sana",
            'type': "Turi",
            'size': "Kitob o'lchami",
            'price': "Narx",
        }
        error_messages = {
            'date': {
                'invalid': "Forma noto'g'ri to'ldirildi!",
                'required': "Forma to'ldirilmadi!",
            },
            'type': {
                'required': "Forma to'ldirilmadi!",
            },
            'size': {
                'required': "Forma to'ldirilmadi!",
            },
            'price': {
                'invalid': "Forma noto'g'ri to'ldirildi!",
                'required': "Forma to'ldirilmadi!",
            },
        }
        widgets = {
            'date': DatePickerInput(attrs={
                'class': 'form-control',
                'placeholder': f"{time.strftime('%Y-%m-%d', time.localtime())}",
            }),
            'type': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'PVA Standard/PVA Jade 403/...',
            }),
            'size': forms.Select(attrs={
                'class': 'form-control',
            }),
            'price': MoneyWidget(
                amount_widget=forms.NumberInput(
                    attrs={
                        'class': 'form-control',
                        'placeholder': '0',
                        'style': 'border-radius: .7rem .7rem .0rem .0rem;',
                    }),
                currency_widget=forms.Select(
                    attrs={
                        'class': 'form-select form-control',
                        'style': 'border-radius: .0rem .0rem .7rem .7rem; ',
                    },
                    choices=currencies)
            ),
        }


class IncomeForm(forms.ModelForm):
    """A form for making expenses related to business (available to admins only)."""

    class Meta:

        currencies = [
            ('EUR', 'EUR'),
            ('RUB', 'RUB'),
            ('USD', 'USD'),
            ('UZS', 'UZS'),
        ]

        model = Income
        fields = [
            'category', 'subcategory', 'user', 'account',
            'date_made', 'comment', 'amount',
        ]
        labels = {
            'category': "Kategoriya",
            'subcategory': "Quyi kategoriya",
            'user': "Foydalanuvchi",
            'account': "Hisob",
            'date_made': "Sana",
            'comment': "Izoh",
            'amount': "Miqdor",
        }
        error_messages = {
            'category': {
                'required': "Forma to'ldirilmadi!",
            },
            'subcategory': {
                'required': "Forma to'ldirilmadi!",
            },
            'user': {
                'required': "Forma to'ldirilmadi!",
            },
            'account': {
                'required': "Forma to'ldirilmadi!",
            },
            'date_made': {
                'invalid': "Vaqt noto'g'ri formatda kiritildi!",
                'required': "Forma to'ldirilmadi!",
            },
            'comment': {
                'required': "Forma to'ldirilmadi!",
            },
            'amount': {
                'invalid': "Forma noto'g'ri to'ldirildi!",
                'required': "Forma to'ldirilmadi!",
            },
        }
        widgets = {
            'category': forms.Select(attrs={
                'class': 'form-control',
            }),
            'subcategory': forms.Select(attrs={
                'class': 'form-control',
            }),
            'user': forms.Select(attrs={
                'class': 'form-control',
            }),
            'account': forms.Select(attrs={
                'class': 'form-control',
            }),
            'date_made': DateTimePickerInput(attrs={
                'class': 'form-control',
                'placeholder': f'{time.strftime("%Y-%m-%d %H:%I", time.localtime())}',
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
            }),
            'amount': MoneyWidget(
                amount_widget=forms.NumberInput(
                    attrs={
                        'class': 'form-control',
                        'placeholder': '0',
                        'style': 'border-radius: .7rem .7rem .0rem .0rem;',
                    }),
                currency_widget=forms.Select(
                    attrs={
                        'class': 'form-select form-control',
                        'style': 'border-radius: .0rem .0rem .7rem .7rem; ',
                    },
                    choices=currencies)
            ),
        }


class LossForm(forms.ModelForm):
    """A form for adding losses happened in business (available to admins only)."""

    class Meta:

        currencies = [
            ('EUR', 'EUR'),
            ('RUB', 'RUB'),
            ('USD', 'USD'),
            ('UZS', 'UZS'),
        ]

        model = Loss
        fields = [
            'ltype', 'name', 'size', 'type',
            'color', 'amount', 'reason', 'time_loss',
            'loser', 'worth',
        ]
        labels = {
            'ltype': "Zararga tushgan resurs nomi",
            'name': "Kitob nomi",
            'size': "O'lchami",
            'type': "Turi",
            'color': "Ranggi",
            'amount': "Miqdori/Soni",
            'reason': "Sabab",
            'time_loss': "Sana",
            'loser': "Ma'sul shaxs",
            'worth': "Qiymati"
        }
        error_messages = {
            'ltype': {
                'required': "Forma to'ldirilmadi!",
            },
            'amount': {
                'required': "Forma to'ldirilmadi!",
            },
            'reason': {
                'required': "Forma to'ldirilmadi!",
            },
            'time_loss': {
                'invalid': "Vaqt noto'g'ri formatda kiritildi!",
                'required': "Forma to'ldirilmadi!",
            },
            'loser': {
                'required': "Forma to'ldirilmadi!",
            },
            'worth': {
                'invalid': "Forma noto'g'ri to'ldirildi!",
                'required': "Forma to'ldirilmadi!",
            }
        }
        widgets = {
            'ltype': forms.Select(attrs={
                'class': 'form-control',
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Factfulness'
            }),
            'size': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'A4/20mm/...'
            }),
            'type': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Classic/Plastic/Type-2/...',
            }),
            'color': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Ko'k/Qora/Yashil/..."
            }),
            'amount': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '50 gram/50ta/...'
            }),
            'reason': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Elektr tarmoqdan uzilishi/E'tiborsizlik/..."
            }),
            'time_loss': DatePickerInput(attrs={
                'class': 'form-control',
                'placeholder': f'{time.strftime("%Y-%m-%d", time.localtime())}',
            }),
            'loser': forms.Select(attrs={
                'class': 'form-control',
            }),
            'worth': MoneyWidget(
                amount_widget=forms.NumberInput(
                    attrs={
                        'class': 'form-control',
                        'placeholder': '0',
                        'style': 'border-radius: .7rem .7rem .0rem .0rem;',
                    }),
                currency_widget=forms.Select(
                    attrs={
                        'class': 'form-select form-control',
                        'style': 'border-radius: .0rem .0rem .7rem .7rem; ',
                    },
                    choices=currencies)
            ),
        }


class LTypeForm(forms.ModelForm):
    """A form for adding loss types to the model Loss (available to admins only)."""

    class Meta:

        model = LType
        fields = [
            'type', 'size', 'color',
        ]
        labels = {
            'type': "Zararga tushgan resurs nomi",
            'size': "Turli o'lchamlari mavjud/O'lchamlari mavjud",
            'color': "Turli ranglari mavjud",
        }
        error_messages = {
            'type': {
                'required': "Forma to'ldirilmadi!",
            }
        }
        widgets = {
            'type': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Kitob/Qog'oz/Rang/...",
            }),
            'size': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
            'color': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }


class NewsForm(forms.ModelForm):
    """A form for publishing news about the service (or something else / available to admins only)."""

    class Meta:

        model = News
        fields = [
            'title', 'subtitle_1', 'subtitle_2', 'subtitle_3',
            'picture_1', 'picture_2', 'picture_3', 'short_body',
            'body_1', 'body_2', 'body_3', 'publisher_tg',
            'publisher_li', 'publisher_gm', 'publisher_tw',
        ]
        labels = {
            'title': "Sarlavha",
            'subtitle_1': "Kichik sarlavha №1 (Majburiy)",
            'subtitle_2': "Kichik sarlavha №2 (Ixtiyoriy)",
            'subtitle_3': "Kichik sarlavha №3 (Ixtiyoriy)",
            'picture_1': "Fotorasm №1 (Majburiy)",
            'picture_2': "Fotorasm №2 (Ixtiyoriy)",
            'picture_3': "Fotorasm №3 (Ixtiyoriy)",
            'short_body': "Yangilik haqida qisqacha",
            'body_1': "Tafsilotlar №1 (Majburiy)",
            'body_2': "Tafsilotlar №2 (Ixtiyoriy)",
            'body_3': "Tafsilotlar №3 (Ixtiyoriy)",
            'publisher_tg': "Nashriyotchining Telegram sahifasi",
            'publisher_li': "Nashriyotchining LinkedIn sahifasi",
            'publisher_gm': "Nashriyotchining Gmail pochta quttisi",
            'publisher_tw': "Nashriyotchining Twitter sahifasi",
        }
        error_messages = {
            'title': {
                'required': "Forma to'ldirilmadi!",
            },
            'subtitle_1': {
                'required': "Forma to'ldirilmadi!",
            },
            'picture_1': {
                'required': "Forma to'ldirilmadi!",
            },
            'short_body': {
                'required': "Forma to'ldirilmadi!",
            },
            'body_1': {
                'required': "Forma to'ldirilmadi!",
            },
            'publisher_tg': {
                'invalid': "Telegram manzil noto'g'ri kiritildi!",
                'required': "Forma to'ldirilmadi!",
            },
            'publisher_li': {
                'invalid': "LinkedIn manzil noto'g'ri kiritildi!",
                'required': "Forma to'ldirilmadi!",
            },
            'publisher_gm': {
                'invalid': "Gmail manzil noto'g'ri kiritildi!",
                'required': "Forma to'ldirilmadi!",
            },
            'publisher_tw': {
                'invalid': "Twitter manzil noto'g'ri kiritildi!",
                'required': "Forma to'ldirilmadi!",
            },
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'subtitle_1': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'subtitle_2': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'subtitle_3': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'picture_1': forms.FileInput(attrs={
                'class': 'custom-file-input',
                'style': 'padding: 0;',
            }),
            'picture_2': forms.FileInput(attrs={
                'class': 'custom-file-input',
                'style': 'padding: 0;',
            }),
            'picture_3': forms.FileInput(attrs={
                'class': 'custom-file-input',
                'style': 'padding: 0;',
            }),
            'short_body': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
            }),
            'body_1': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10,
            }),
            'body_2': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10,
            }),
            'body_3': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10,
            }),
            'publisher_tg': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://telegram.me/foydalanuvchi-nomi',
            }),
            'publisher_li': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://www.linkedin.com/in/foydalanuvchi-nomi-000000000',
            }),
            'publisher_gm': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'qwerty@example.com',
            }),
            'publisher_tw': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://twitter.com/foydalanuvchi-nomi',
            })
        }


class OrderOptionsForm(forms.ModelForm):
    """A form for defining the available resources for making orders (available to admins only)."""

    class Meta:

        model = OrderOptions
        fields = [
            'date', 'ringed_colorless', 'ringed_color', 'metal_ringed_colorless',
            'metal_ringed_color', 'g_soft_colorless', 'g_soft_color', 'g_hard_colorless',
            'g_hard_color',  'stapled_colorless', 'stapled_color', 'blue',
            'red', 'black', 'transparent', 'yellow',
            'green',
        ]
        labels = {
            'date': 'Sana',
            'ringed_colorless': "Plastik prujinalangan (rangsiz)",
            'ringed_color': "Plastik prujinalangan (rangli)",
            'metal_ringed_colorless': "Metal prujinalangan (rangsiz)",
            'metal_ringed_color': "Metal prujinalangan (rangli)",
            'g_soft_colorless': "Yelimlangan yumshoq muqovali (rangsiz)",
            'g_soft_color': "Yelimlangan yumshoq muqovali (rangli)",
            'g_hard_colorless': "Yelimlangan qattiq muqovali (rangsiz)",
            'g_hard_color': "Yelimlangan qattiq muqovali (rangli)",
            'stapled_colorless': "Steplerlangan (rangsiz)",
            'stapled_color': "Steplerlangan (rangli)",
            'black': "Qora",
            'blue': "Ko`k",
            'green': "Yashil",
            'red': "Qizil",
            'transparent': "Rangsiz",
            'yellow': "Sariq",
        }
        error_messages = {
            'date': {
                'invalid': "Vaqt noto'g'ri formatda kiritildi!",
                'required': "Forma to'ldirilmadi!",
            }
        }
        widgets = {
            'date': DatePickerInput(attrs={
                'class': 'form-control',
                'placeholder': f'{time.strftime("%Y-%m-%d", time.localtime())}',
            })
        }


class OrderSelfForm(forms.ModelForm):
    """A form for receiving orders by users for books provided by them."""

    class Meta:

        model = Order
        fields = [
            'custom_book', 'book_type', 'ring_color', 'front_cover_color',
            'back_cover_color', 'size', 'custom_page_number', 'number',
            'user_needs', 'place_to_get', 'payment',
        ]
        labels = {
            'custom_book': 'Kitob',
            'book_type': 'Kitob shakli',
            'ring_color': 'Prujina ranggi',
            'front_cover_color': 'Old muqova ranggi',
            'back_cover_color': 'Orqa muqova ranggi',
            'size': "O'lchami",
            'custom_page_number': "Betlari soni",
            'number': "Soni",
            'user_needs': "Kitob kerak bo'ladigan vaqt",
            'place_to_get': "Buyurtmani olish mumkin bo'lgan joylar",
            'payment': "To'lov usuli",
        }
        error_messages = {
            'custom_book': {
                'required': "Forma to'ldirilmadi!",
            },
            'book_type': {
                'required': "Forma to'ldirilmadi!",
            },
            'ring_color': {
                'required': "Forma to'ldirilmadi!",
            },
            'front_cover_color': {
                'required': "Forma to'ldirilmadi!",
            },
            'back_cover_color': {
                'required': "Forma to'ldirilmadi!",
            },
            'size': {
                'required': "Forma to'ldirilmadi!",
            },
            'custom_page_number': {
                'invalid': "Butun son kiriting!",
                'required': "Forma to'ldirilmadi!",
            },
            'number': {
                'invalid': "Butun son kiriting!",
                'required': "Forma to'ldirilmadi!",
            },
            'user_needs': {
                'invalid': "Vaqt noto'g'ri formatda kiritildi!",
                'required': "Forma to'ldirilmadi!",
            },
            'place_to_get': {
                'required': "Forma to'ldirilmadi!",
            },
            'payment': {
                'required': "Forma to'ldirilmadi!",
            },
        }
        widgets = {
            'custom_book': forms.FileInput(attrs={
                'class': 'custom-file-input',
                'style': 'padding: 0;',
            }),
            'book_type': forms.Select(attrs={
                'class': 'form-control',
            }),
            'ring_color': forms.Select(attrs={
                'class': 'form-control',
            }),
            'front_cover_color': forms.Select(attrs={
                'class': 'form-control',
            }),
            'back_cover_color': forms.Select(attrs={
                'class': 'form-control',
            }),
            'size': forms.Select(attrs={
                'class': 'form-control',
            }),
            'custom_page_number': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0',
            }),
            'number': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0',
            }),
            'user_needs': DateTimePickerInput(attrs={
                'class': 'form-control',
                'placeholder': f'{time.strftime("%Y-%m-%d %H:%I", time.localtime())}',
            }),
            'place_to_get': forms.Select(attrs={
                'class': 'form-control',
            }),
            'payment': forms.Select(attrs={
                'class': 'form-control',
            }),
        }


class OrderSiteForm(forms.ModelForm):
    """A form for receiving orders by users for books available in the base."""

    class Meta:

        model = Order
        fields = [
            'book', 'book_type', 'ring_color', 'front_cover_color',
            'back_cover_color', 'size', 'number', 'user_needs',
            'place_to_get', 'payment',
        ]
        labels = {
            'book': "Kitob",
            'book_type': 'Kitob shakli',
            'ring_color': 'Prujina ranggi',
            'front_cover_color': 'Old muqova ranggi',
            'back_cover_color': 'Orqa muqova ranggi',
            'size': "O'lchami",
            'number': "Soni",
            'user_needs': "Kitob kerak bo'ladigan vaqt",
            'place_to_get': "Buyurtmani olish mumkin bo'lgan joylar",
            'payment': "To'lov usuli",
        }
        error_messages = {
            'book': {
                'required': "Forma to'ldirilmadi!",
            },
            'book_type': {
                'required': "Forma to'ldirilmadi!",
            },
            'ring_color': {
                'required': "Forma to'ldirilmadi!",
            },
            'front_cover_color': {
                'required': "Forma to'ldirilmadi!",
            },
            'back_cover_color': {
                'required': "Forma to'ldirilmadi!",
            },
            'size': {
                'required': "Forma to'ldirilmadi!",
            },
            'number': {
                'invalid': "Butun son kiriting!",
                'required': "Forma to'ldirilmadi!",
            },
            'user_needs': {
                'invalid': "Vaqt noto'g'ri formatda kiritildi!",
                'required': "Forma to'ldirilmadi!",
            },
            'place_to_get': {
                'required': "Forma to'ldirilmadi!",
            },
            'payment': {
                'required': "Forma to'ldirilmadi!",
            },
        }
        widgets = {
            'book': forms.Select(attrs={
                'class': 'form-control',
            }),
            'book_type': forms.Select(attrs={
                'class': 'form-control',
            }),
            'ring_color': forms.Select(attrs={
                'class': 'form-control',
            }),
            'front_cover_color': forms.Select(attrs={
                'class': 'form-control',
            }),
            'back_cover_color': forms.Select(attrs={
                'class': 'form-control',
            }),
            'size': forms.Select(attrs={
                'class': 'form-control',
            }),
            'number': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0',
            }),
            'user_needs': DateTimePickerInput(attrs={
                'class': 'form-control',
                'placeholder': f'{time.strftime("%Y-%m-%d %H:%I", time.localtime())}',
            }),
            'place_to_get': forms.Select(attrs={
                'class': 'form-control',
            }),
            'payment': forms.Select(attrs={
                'class': 'form-control',
            }),
        }


class OuterPriceForm(forms.ModelForm):
    """A form for adding prices to external expenses spent on making books (available to admins only)."""

    class Meta:

        currencies = [
            ('EUR', 'EUR'),
            ('RUB', 'RUB'),
            ('USD', 'USD'),
            ('UZS', 'UZS'),
        ]

        model = OuterPrice
        fields = [
            'date', 'staple_price', 'packaging_expenses', 'delivery_expenses',
            'workforce_expenses', 'electricity_expenses', 'printer_expenses', 'profit',
        ]
        labels = {
            'date': "Sana",
            'staple_price': "Stepler o'qi narxi",
            'packaging_expenses': "Qadoqlash xarajati",
            'delivery_expenses': "Yetkazib berish xarajatlari",
            'workforce_expenses': "Ishchi kuchi xarajatlari",
            'electricity_expenses': "Elektr toki xarajatlari",
            'printer_expenses': "Printer xarajatlari (A4)",
            'profit': "Sof foyda (%)",
        }
        error_messages = {
            'date': {
                'invalid': "Forma noto'g'ri to'ldirildi!",
                'required': "Forma to'ldirilmadi!",
            },
            'staple_price': {
                'invalid': "Forma noto'g'ri to'ldirildi!",
                'required': "Forma to'ldirilmadi!",
            },
            'packaging_expenses': {
                'invalid': "Forma noto'g'ri to'ldirildi!",
                'required': "Forma to'ldirilmadi!",
            },
            'delivery_expenses': {
                'invalid': "Forma noto'g'ri to'ldirildi!",
                'required': "Forma to'ldirilmadi!",
            },
            'workforce_expenses': {
                'invalid': "Forma noto'g'ri to'ldirildi!",
                'required': "Forma to'ldirilmadi!",
            },
            'electricity_expenses': {
                'invalid': "Forma noto'g'ri to'ldirildi!",
                'required': "Forma to'ldirilmadi!",
            },
            'printer_expenses': {
                'invalid': "Forma noto'g'ri to'ldirildi!",
                'required': "Forma to'ldirilmadi!",
            },
            'profit': {
                'required': "Forma to'ldirilmadi!",
            },
        }
        widgets = {
            'date': DatePickerInput(attrs={
                'class': 'form-control',
                'placeholder': f'{time.strftime("%Y-%m-%d", time.localtime())}',
            }),
            'staple_price': MoneyWidget(
                amount_widget=forms.NumberInput(
                    attrs={
                        'class': 'form-control',
                        'placeholder': "Bir o'qi",
                        'style': 'border-radius: .7rem .7rem .0rem .0rem;',
                    }),
                currency_widget=forms.Select(
                    attrs={
                        'class': 'form-select form-control',
                        'style': 'border-radius: .0rem .0rem .7rem .7rem; ',
                    },
                    choices=currencies)
            ),
            'packaging_expenses': MoneyWidget(
                amount_widget=forms.NumberInput(
                    attrs={
                        'class': 'form-control',
                        'placeholder': "Bir kitob uchun (o'rtacha narxi)",
                        'style': 'border-radius: .7rem .7rem .0rem .0rem;',
                    }),
                currency_widget=forms.Select(
                    attrs={
                        'class': 'form-select form-control',
                        'style': 'border-radius: .0rem .0rem .7rem .7rem; ',
                    },
                    choices=currencies)
            ),
            'delivery_expenses': MoneyWidget(
                amount_widget=forms.NumberInput(
                    attrs={
                        'class': 'form-control',
                        'placeholder': "Bir kitob uchun",
                        'style': 'border-radius: .7rem .7rem .0rem .0rem;',
                    }),
                currency_widget=forms.Select(
                    attrs={
                        'class': 'form-select form-control',
                        'style': 'border-radius: .0rem .0rem .7rem .7rem; ',
                    },
                    choices=currencies)
            ),
            'workforce_expenses': MoneyWidget(
                amount_widget=forms.NumberInput(
                    attrs={
                        'class': 'form-control',
                        'placeholder': "Bir kitob uchun",
                        'style': 'border-radius: .7rem .7rem .0rem .0rem;',
                    }),
                currency_widget=forms.Select(
                    attrs={
                        'class': 'form-select form-control',
                        'style': 'border-radius: .0rem .0rem .7rem .7rem; ',
                    },
                    choices=currencies)
            ),
            'electricity_expenses': MoneyWidget(
                amount_widget=forms.NumberInput(
                    attrs={
                        'class': 'form-control',
                        'placeholder': "Bir kitob uchun",
                        'style': 'border-radius: .7rem .7rem .0rem .0rem;',
                    }),
                currency_widget=forms.Select(
                    attrs={
                        'class': 'form-select form-control',
                        'style': 'border-radius: .0rem .0rem .7rem .7rem; ',
                    },
                    choices=currencies)
            ),
            'printer_expenses': MoneyWidget(
                amount_widget=forms.NumberInput(
                    attrs={
                        'class': 'form-control',
                        'placeholder': "Bir bet uchun",
                        'style': 'border-radius: .7rem .7rem .0rem .0rem;',
                    }),
                currency_widget=forms.Select(
                    attrs={
                        'class': 'form-select form-control',
                        'style': 'border-radius: .0rem .0rem .7rem .7rem; ',
                    },
                    choices=currencies)
            ),
            'profit': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0',
            }),
        }


class PagePriceForm(forms.ModelForm):
    """A form for adding prices to single page based on size (available to admins only)."""

    class Meta:
        currencies = [
            ('EUR', 'EUR'),
            ('RUB', 'RUB'),
            ('USD', 'USD'),
            ('UZS', 'UZS'),
        ]

        model = PagePrice
        fields = [
            'date', 'type', 'size',
        ]
        labels = {
            'date': "Sana",
            'type': "Qog'oz turi",
            'size': "O'lchami",
        }
        error_messages = {
            'date': {
                'invalid': "Forma noto'g'ri to'ldirildi!",
                'required': "Forma to'ldirilmadi!",
            },
            'type': {
                'required': "Forma to'ldirilmadi!",
            },
            'size': {
                'required': "Forma to'ldirilmadi!",
            },
        }
        widgets = {
            'date': DatePickerInput(attrs={
                'class': 'form-control',
                'placeholder': f"{time.strftime('%Y-%m-%d', time.localtime())}",
            }),
            'type': forms.Select(attrs={
                'class': 'form-control',
            }),
            'size': forms.Select(attrs={
                'class': 'form-control',
            }),
        }


class PaperPriceForm(forms.ModelForm):
    """A form for adding prices to paper based on size (available to admins only)."""

    class Meta:

        currencies = [
            ('EUR', 'EUR'),
            ('RUB', 'RUB'),
            ('USD', 'USD'),
            ('UZS', 'UZS'),
        ]

        model = PaperPrice
        fields = [
            'date', 'type', 'size', 'price',
        ]
        labels = {
            'date': "Sana",
            'type': "Turi",
            'size': "O'lchami",
            'price': "Narxi  (bir bet uchun)",
        }
        error_messages = {
            'date': {
                'invalid': "Forma noto'g'ri to'ldirildi!",
                'required': "Forma to'ldirilmadi!",
            },
            'type': {
                'required': "Forma to'ldirilmadi!",
            },
            'size': {
                'required': "Forma to'ldirilmadi!",
            },
            'price': {
                'invalid': "Forma noto'g'ri to'ldirildi!",
                'required': "Forma to'dirilmadi!",
            },
        }
        widgets = {
            'date': DatePickerInput(attrs={
                'class': 'form-control',
                'placeholder': f"{time.strftime('%Y-%m-%d', time.localtime())}",
            }),
            'type': forms.Select(attrs={
                'class': 'form-control',
            }),
            'size': forms.Select(attrs={
                'class': 'form-control',
            }),
            'price': MoneyWidget(
                amount_widget=forms.NumberInput(
                    attrs={
                        'class': 'form-control',
                        'placeholder': '0',
                        'style': 'border-radius: .7rem .7rem .0rem .0rem;',
                    }),
                currency_widget=forms.Select(
                    attrs={
                        'class': 'form-select form-control',
                        'style': 'border-radius: .0rem .0rem .7rem .7rem; ',
                    },
                    choices=currencies)
            ),
        }


class PlaceToGetForm(forms.ModelForm):
    """A form for adding places for users to obtain their orders (available to admins only)."""

    class Meta:

        model = PlaceToGet
        fields = [
            'place', 'available',
        ]
        labels = {
            'place': "Manzil",
            'available': "Mavjud",
        }
        error_messages = {
            'place': {
                'required': "Forma to'ldirilmadi!",
            },
        }
        widgets = {
            'place': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'available': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }


class PrinterForm(forms.ModelForm):
    """A form for adding printer information."""

    class Meta:

        model = Printer
        fields = [
            'brand', 'model', 'bought_at', 'status_when_bought',
            'initial_page_count', 'current_page_count', 'current_status',
        ]
        labels = {
            'brand': "Markasi",
            'model': "Modeli",
            'bought_at': "Sotib olingan vaqti",
            'status_when_bought': "Sotib olingandagi holati",
            'initial_page_count': "Chop etgan betlari soni (boshlang'ich)",
            'current_page_count': "Chop etgan betlari soni (ayni damdagi)",
            'current_status': "Ayni damdagi holati",
        }
        error_messages = {
            'brand': {
                'required': "Forma to'ldirilmadi!",
            },
            'model': {
                'required': "Forma to'ldirilmadi!",
            },
            'bought_at': {
                'invalid': "Forma noto'g'ri to'ldirildi!",
                'required': "Forma to'ldirilmadi!",
            },
            'status_when_bought': {
                'required': "Forma to'ldirilmadi!",
            },
            'initial_page_count': {
                'invalid': "Butun son kiriting!",
                'required': "Forma to'ldirilmadi!",
            },
            'current_page_count': {
                'invalid': "Butun son kiriting!",
                'required': "Forma to'ldirilmadi!",
            },
            'current_status': {
                'required': "Forma to'ldirilmadi!",
            },
        }
        widgets = {
            'brand': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Canon',
            }),
            'model': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ImageRUNNER 2206N',
            }),
            'bought_at': DatePickerInput(attrs={
                'class': 'form-control',
                'placeholder': f'{time.strftime("%Y-%m-%d", time.localtime())}',
            }),
            'status_when_bought': forms.Select(attrs={
                'class': 'form-control',
            }),
            'initial_page_count': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0',
            }),
            'current_page_count': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0',
            }),
            'current_status': forms.Select(attrs={
                'class': 'form-control',
            }),
        }


class RefillAndPageCountForm(forms.ModelForm):
    """A form for adding counting information on the printers that are in service."""

    class Meta:

        model = RefillAndPageCount
        fields = [
            'printer', 'total_refill_count', 'last_refill', 'printed',
            'accounted',
        ]
        labels = {
            'printer': "Printer",
            'total_refill_count': "Umumiy rang to'ldirishlar soni (sotib olinganidan beri)",
            'last_refill': "So'nggi rang to'ldirish sanasi",
            'printed': "Chop etgan betlari soni",
            'accounted': "Chop etilgan betlar soni hisoblangan"
        }
        error_messages = {
            'printer': {
                'required': "Forma to'ldirilmadi!",
            },
            'total_refill_count': {
                'invalid': "Butun son kiriting!",
                'required': "Forma to'ldirilmadi!",
            },
            'last_refill': {
                'invalid': "Forma noto'g'ri to'ldirildi!",
                'required': "Forma to'ldirilmadi!",
            },
            'printed': {
                'invalid': "Butun son kiriting!",
                'required': "Forma to'ldirilmadi!",
            },
        }
        widgets = {
            'printer': forms.Select(attrs={
                'class': 'form-control',
            }),
            'total_refill_count': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0',
            }),
            'last_refill': DatePickerInput(attrs={
                'class': 'form-control',
                'placeholder': f'{time.strftime("%Y-%m-%d", time.localtime())}',
            }),
            'printed': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0',
            }),
            'accounted': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }


class ResourceForm(forms.ModelForm):
    """A form for adding resources available in the business (available to admins only)."""

    class Meta:

        currencies = [
            ('EUR', 'EUR'),
            ('RUB', 'RUB'),
            ('USD', 'USD'),
            ('UZS', 'UZS'),
        ]

        model = Resource
        fields = [
            'rtype', 'size', 'type', 'color',
            'amount', 'time_bought', 'worth', 'last_used_date',
            'amount_used', 'user', 'available',
        ]
        labels = {
            'rtype': "Resurs nomi",
            'size': "O'lchami",
            'type': "Turi",
            'color': "Ranggi",
            'amount': "Miqdori/Soni",
            'time_bought': "Sotib olingan sana",
            'worth': "Qiymati",
            'last_used_date': "So'nggi marta ishlatilgan sana",
            'amount_used': "Ishlatilgan miqdor",
            'user': "Foydalanuvchi",
            'available': "Mavjud",
        }
        error_messages = {
            'rtype': {
                'required': "Forma to'ldirilmadi!",
            },
            'amount': {
                'required': "Forma to'ldirilmadi!",
            },
            'time_bought': {
                'invalid': "Vaqt noto'g'ri formatda kiritildi!",
                'required': "Forma to'ldirilmadi!",
            },
            'worth': {
                'invalid': "Forma noto'g'ri to'ldirildi!",
                'required': "Forma to'ldirilmadi!",
            },
            'last_used_date': {
                'invalid': "Vaqt noto'g'ri formatda kiritildi!",
            },
            'user': {
                'required': "Forma to'ldirilmadi!",
            },
            'available': {
                'required': "Forma to'ldirilmadi!",
            },
        }
        widgets = {
            'rtype': forms.Select(attrs={
                'class': 'form-control',
            }),
            'size': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'A4/20mm/...',
            }),
            'type': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Classic/Plastic/Type-2/...',
            }),
            'color': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Ko'k/Qora/Yashil/...",
            }),
            'amount': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '50 gram/50ta/...',
            }),
            'time_bought': DatePickerInput(attrs={
                'class': 'form-control',
                'placeholder': f'{time.strftime("%Y-%m-%d", time.localtime())}',
            }),
            'worth': MoneyWidget(
                amount_widget=forms.NumberInput(
                    attrs={
                        'class': 'form-control',
                        'placeholder': '0',
                        'style': 'border-radius: .7rem .7rem .0rem .0rem;',
                    }),
                currency_widget=forms.Select(
                    attrs={
                        'class': 'form-select form-control',
                        'style': 'border-radius: .0rem .0rem .7rem .7rem; ',
                    },
                    choices=currencies)
            ),
            'last_used_date': DatePickerInput(attrs={
                'class': 'form-control',
                'placeholder': f'{time.strftime("%Y-%m-%d", time.localtime())}',
            }),
            'amount_used': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0',
            }),
            'user': forms.Select(attrs={
                'class': 'form-control',
            }),
            'available': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "50 gram/50ta/50sm/..."
            }),
        }


class RingPriceForm(forms.ModelForm):
    """A form for adding ring type, size and price (available to admins only)."""

    class Meta:

        currencies = [
            ('EUR', 'EUR'),
            ('RUB', 'RUB'),
            ('USD', 'USD'),
            ('UZS', 'UZS'),
        ]

        model = RingPrice
        fields = [
            'date', 'type', 'size', 'price',
        ]
        labels = {
            'date': "Sana",
            'type': "Turi",
            'size': "O'lchami",
            'price': "Narxi",
        }
        error_messages = {
            'date': {
                'required': "Forma to'ldirilmadi!",
            },
            'type': {
                'required': "Forma to'ldirilmadi!",
            },
            'size': {
                'required': "Forma to'ldirilmadi!",
            },
            'price': {
                'invalid': "Forma noto'g'ri to'ldirildi!",
                'required': "Forma to'ldirilmadi!",
            },
        }
        widgets = {
            'date': DatePickerInput(attrs={
                'class': 'form-control',
                'placeholder': f'{time.strftime("%Y-%m-%d", time.localtime())}',
            }),
            'type': forms.Select(attrs={
                'class': 'form-control',
            }),
            'size': forms.Select(attrs={
                'class': 'form-control',
            }),
            'price': MoneyWidget(
                amount_widget=forms.NumberInput(
                    attrs={
                        'class': 'form-control',
                        'placeholder': '0',
                        'style': 'border-radius: .7rem .7rem .0rem .0rem;',
                    }),
                currency_widget=forms.Select(
                    attrs={
                        'class': 'form-select form-control',
                        'style': 'border-radius: .0rem .0rem .7rem .7rem; ',
                    },
                    choices=currencies)
            ),
        }


class RTypeForm(forms.ModelForm):
    """A form for adding resource types to the model Resource (available to admins only)."""

    class Meta:
        model = RType
        fields = [
            'type', 'size', 'color',
        ]
        labels = {
            'type': "Resurs nomi",
            'size': "Turli o'lchamlari mavjud/O'lchamlari mavjud",
            'color': "Turli ranglari mavjud",
        }
        error_messages = {
            'type': {
                'required': "Forma to'ldirilmadi!",
            }
        }
        widgets = {
            'type': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Qog'oz/Rang/Prujina/...",
            }),
            'size': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
            'color': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }


class SelfOrderForm(forms.ModelForm):
    """A form for making changes to order made by users for books provided by them (available to admins only)."""

    class Meta:

        model = Order
        fields = [
            'custom_book', 'book_type', 'ring_color', 'front_cover_color',
            'back_cover_color', 'size', 'custom_page_number', 'number',
            'user_needs', 'place_to_get', 'customer', 'payment',
            'status', 'delivered',
        ]
        labels = {
            'custom_book': "Kitob",
            'book_type': "Kitob shakli",
            'ring_color': "Prujina ranggi",
            'front_cover_color': "Old muqova ranggi",
            'back_cover_color': "Orqa muqova ranggi",
            'size': "O'lchami",
            'custom_page_number': "Betlari soni",
            'number': "Soni",
            'user_needs': "Kitob kerak bo'ladigan vaqt",
            'place_to_get': "Buyurtmani olish mumkin bo'lgan joylar",
            'customer': "Xaridor",
            'payment': "To'lov usuli",
            'status': "Holati",
            'delivered': "Yetkazildi",
        }
        error_messages = {
            'custom_book': {
                'required': "Forma to'ldirilmadi!",
            },
            'book_type': {
                'required': "Forma to'ldirilmadi!",
            },
            'ring_color': {
                'required': "Forma to'ldirilmadi!",
            },
            'front_cover_color': {
                'required': "Forma to'ldirilmadi!",
            },
            'back_cover_color': {
                'required': "Forma to'ldirilmadi!",
            },
            'size': {
                'required': "Forma to'ldirilmadi!",
            },
            'custom_page_number': {
                'invalid': "Butun son kiriting!",
                'required': "Forma to'ldirilmadi!",
            },
            'number': {
                'invalid': "Butun son kiriting!",
                'required': "Forma to'ldirilmadi!",
            },
            'user_needs': {
                'invalid': "Vaqt noto'g'ri formatda kiritildi!",
                'required': "Forma to'ldirilmadi!",
            },
            'place_to_get': {
                'required': "Forma to'ldirilmadi!",
            },
            'customer': {
                'required': "Forma to'ldirilmadi!",
            },
            'payment': {
                'required': "Forma to'ldirilmadi!",
            },
            'status': {
                'required': "Forma to'ldirilmadi!",
            },
            'delivered': {
                'required': "Forma to'ldirilmadi",
            },
        }
        widgets = {
            'custom_book': forms.FileInput(attrs={
                'class': 'custom-file-input',
                'style': 'padding: 0;',
            }),
            'book_type': forms.Select(attrs={
                'class': 'form-control',
            }),
            'ring_color': forms.Select(attrs={
                'class': 'form-control',
            }),
            'front_cover_color': forms.Select(attrs={
                'class': 'form-control',
            }),
            'back_cover_color': forms.Select(attrs={
                'class': 'form-control',
            }),
            'size': forms.Select(attrs={
                'class': 'form-control',
            }),
            'custom_page_number': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0',
            }),
            'number': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0',
            }),
            'user_needs': DateTimePickerInput(attrs={
                'class': 'form-control',
                'placeholder': f'{time.strftime("%Y-%m-%d %H:%I", time.localtime())}',
            }),
            'place_to_get': forms.Select(attrs={
                'class': 'form-control',
            }),
            'customer': forms.Select(attrs={
                'class': 'form-control',
            }),
            'payment': forms.Select(attrs={
                'class': 'form-control',
            }),
            'status': forms.Select(attrs={
                'class': 'form-control',
            }),
            'delivered': forms.NullBooleanSelect(attrs={
                'class': 'form-control',
            }),
        }


class SiteOrderForm(forms.ModelForm):
    """A form for making changes to order made by users for books available in the base (available to admins only)."""

    class Meta:

        model = Order
        fields = [
            'book', 'book_type', 'ring_color', 'front_cover_color',
            'back_cover_color', 'size', 'number', 'user_needs',
            'place_to_get', 'customer',  'payment', 'status',
            'delivered',
        ]
        labels = {
            'book': "Kitob",
            'book_type': "Kitob shakli",
            'ring_color': "Prujina ranggi",
            'front_cover_color': "Old muqova ranggi",
            'back_cover_color': "Orqa muqova ranggi",
            'size': "O'lchami",
            'number': "Soni",
            'user_needs': "Kitob kerak bo'ladigan vaqt",
            'place_to_get': "Buyurtmani olish mumkin bo'lgan joylar",
            'customer': "Xaridor",
            'payment': "To'lov usuli",
            'status': "Holati",
            'delivered': "Yetkazildi",
        }
        error_messages = {
            'book': {
                'required': "Forma to'ldirilmadi!",
            },
            'book_type': {
                'required': "Forma to'ldirilmadi!",
            },
            'ring_color': {
                'required': "Forma to'ldirilmadi!",
            },
            'front_cover_color': {
                'required': "Forma to'ldirilmadi!",
            },
            'back_cover_color': {
                'required': "Forma to'ldirilmadi!",
            },
            'size': {
                'required': "Forma to'ldirilmadi!",
            },
            'number': {
                'invalid': "Butun son kiriting!",
                'required': "Forma to'ldirilmadi!",
            },
            'user_needs': {
                'invalid': "Vaqt noto'g'ri formatda kiritildi!",
                'required': "Forma to'ldirilmadi!",
            },
            'place_to_get': {
                'required': "Forma to'ldirilmadi!",
            },
            'customer': {
                'required': "Forma to'ldirilmadi!",
            },
            'payment': {
                'required': "Forma to'ldirilmadi!",
            },
            'status': {
                'required': "Forma to'ldirilmadi!",
            },
            'delivered': {
                'required': "Forma to'ldirilmadi",
            },
        }
        widgets = {
            'book': forms.Select(attrs={
                'class': 'form-control',
            }),
            'book_type': forms.Select(attrs={
                'class': 'form-control',
            }),
            'ring_color': forms.Select(attrs={
                'class': 'form-control',
            }),
            'front_cover_color': forms.Select(attrs={
                'class': 'form-control',
            }),
            'back_cover_color': forms.Select(attrs={
                'class': 'form-control',
            }),
            'size': forms.Select(attrs={
                'class': 'form-control',
            }),
            'number': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0',
            }),
            'user_needs': DateTimePickerInput(attrs={
                'class': 'form-control',
                'placeholder': f'{time.strftime("%Y-%m-%d %H:%I", time.localtime())}',
            }),
            'place_to_get': forms.Select(attrs={
                'class': 'form-control',
            }),
            'customer': forms.Select(attrs={
               'class': 'form-control',
            }),
            'payment': forms.Select(attrs={
                'class': 'form-control',
            }),
            'status': forms.Select(attrs={
                'class': 'form-control',
            }),
            'delivered': forms.NullBooleanSelect(attrs={
                'class': 'form-control',
            }),
        }


class SubCategoryExForm(forms.ModelForm):
    """A form handling expense categories (available to admins only)."""

    class Meta:
        model = SubCategoryEx
        fields = [
            'subcategory',
        ]
        labels = {
            'subcategory': "Xarajat quyi kategoriyasi",
        }
        error_messages = {
            'subcategory': {
                'required': "Forma to'lidirilmadi!",
            }
        }
        widgets = {
            'subcategory': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Taksi",
            }),
        }


class SubCategoryInForm(forms.ModelForm):
    """A form handling expense categories (available to admins only)."""

    class Meta:
        model = SubCategoryIn
        fields = [
            'subcategory',
        ]
        labels = {
            'subcategory': 'Daromad quyi kategoriyasi',
        }
        error_messages = {
            'subcategory': {
                'required': "Forma to'lidirilmadi!",
            }
        }
        widgets = {
            'subcategory': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Kitob savdosi",
            }),
        }


class TransactionForm(forms.ModelForm):
    """A form for making transactions between accounts (available to admins only)."""

    class Meta:

        currencies = [
            ('EUR', 'EUR'),
            ('RUB', 'RUB'),
            ('USD', 'USD'),
            ('UZS', 'UZS'),
        ]

        model = Transaction
        fields = [
            'acc_1', 'acc_2', 'amount',
        ]
        labels = {
            'acc_1': "Mablag' yechiladigan hisob",
            'acc_2': "Mablag' o'tkaziladigan hisob",
            'amount': "Pul o'tkazmasi miqdori",
        }
        error_messages = {
            'acc_1': {
                'required': "Forma to'ldirilmadi!",
            },
            'acc_2': {
                'required': "Forma to'ldirilmadi!",
            },
            'amount': {
                'invalid': "Forma noto'g'ri to'ldirildi!",
                'required': "Forma to'ldirilmadi!",
            }
        }
        widgets = {
            'acc_1': forms.Select(attrs={
                'class': 'form-control',
            }),
            'acc_2': forms.Select(attrs={
                'class': 'form-control',
            }),
            'amount': MoneyWidget(
                amount_widget=forms.NumberInput(
                    attrs={
                        'class': 'form-control',
                        'placeholder': '0',
                        'style': 'border-radius: .7rem .7rem .0rem .0rem;',
                    }),
                currency_widget=forms.Select(
                    attrs={
                        'class': 'form-select form-control',
                        'style': 'border-radius: .0rem .0rem .7rem .7rem; ',
                    },
                    choices=currencies)
            ),
        }


class WorkforceForm(forms.ModelForm):
    """A form for adding information on workers that are in service or out."""

    class Meta:

        currencies = [
            ('EUR', 'EUR'),
            ('RUB', 'RUB'),
            ('USD', 'USD'),
            ('UZS', 'UZS'),
        ]

        model = Workforce
        fields = [
            'name', 'surname', 'middle_name', 'age',
            'address_living', 'career_status', 'joined_service', 'position',
            'salary', 'last_salary_reception', 'last_salary_paid',
        ]
        labels = {
            'name': "Ismi",
            'surname': "Famliyasi",
            'middle_name': "Sharifi (ixtiyoriy)",
            'age': "Yoshi",
            'address_living': "Yashash manzili",
            'career_status': "Martabasi",
            'joined_service': "Xizmatga qo'shilgan vaqti",
            'position': "Lavozimi",
            'salary': "Ish haqqi",
            'last_salary_reception': "So'nggi marta ish haqqini qabul qilgan sana",
            'last_salary_paid': "So'nggi ish haqqi to'landi",
        }
        error_messages = {
            'name': {
                'required': "Forma to'ldirilmadi!"
            },
            'surname': {
                'required': "Forma to'ldirilmadi!"
            },
            'age': {
                'invalid': "Butun son kiriting!",
                'required': "Forma to'ldirilmadi!"
            },
            'address_living': {
                'required': "Forma to'ldirilmadi!"
            },
            'career_status': {
                'required': "Forma to'ldirilmadi!"
            },
            'joined_service': {
                'invalid': "Forma noto'g'ri to'ldirildi",
                'required': "Forma to'ldirilmadi!"
            },
            'position': {
                'required': "Forma to'ldirilmadi!"
            },
            'salary': {
                'required': "Forma to'ldirilmadi!"
            },
            'last_salary_reception': {
                'invalid': "Forma noto'g'ri to'ldirildi",
                'required': "Forma to'ldirilmadi!"
            },
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Rasul",
            }),
            'surname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Rasulov",
            }),
            'middle_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Rasulovich",
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': "18",
            }),
            'address_living': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Qarshi shahri, XXXXX mahallasi, XXXXX ko'chasi 00-uy",
            }),
            'career_status': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Talaba/Hech qayerda o'qimaydi/...",
            }),
            'joined_service': DatePickerInput(attrs={
                'class': 'form-control',
                'placeholder': f"{time.strftime('%Y-%m-%d', time.localtime())}",
            }),
            'position': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Ish boshqaruvchi/Kitob ulovchi/Kesuvchi/..."
            }),
            'salary': MoneyWidget(
                amount_widget=forms.NumberInput(
                    attrs={
                        'class': 'form-control',
                        'placeholder': '0',
                        'style': 'border-radius: .7rem .7rem .0rem .0rem;',
                    }),
                currency_widget=forms.Select(
                    attrs={
                        'class': 'form-select form-control',
                        'style': 'border-radius: .0rem .0rem .7rem .7rem; ',
                    },
                    choices=currencies)
            ),
            'last_salary_reception': DatePickerInput(attrs={
                'class': "form-control",
                'placeholder': f"{time.strftime('%Y-%m-%d', time.localtime())}",
            }),
            'last_salary_paid': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            })
        }


class YarnPriceForm(forms.ModelForm):
    """A form for adding prices to yarn based on type (available to admins only)."""

    class Meta:

        currencies = [
            ('EUR', 'EUR'),
            ('RUB', 'RUB'),
            ('USD', 'USD'),
            ('UZS', 'UZS'),
        ]

        model = YarnPrice
        fields = [
            'date', 'type', 'size', 'price',
        ]
        labels = {
            'date': "Sana",
            'type': "Turi",
            'size': "Kitob o'lchami",
            'price': "Narx",
        }
        error_messages = {
            'date': {
                'invalid': "Forma noto'g'ri to'ldirildi!",
                'required': "Forma to'ldirilmadi!",
            },
            'type': {
                'required': "Forma to'ldirilmadi!",
            },
            'size': {
                'required': "Forma to'ldirilmadi!",
            },
            'price': {
                'invalid': "Forma noto'g'ri to'ldirildi!",
                'required': "Forma to'ldirilmadi!",
            },
        }
        widgets = {
            'date': DatePickerInput(attrs={
                'class': 'form-control',
                'placeholder': f"{time.strftime('%Y-%m-%d', time.localtime())}",
            }),
            'type': forms.Select(attrs={
                'class': 'form-control',
            }),
            'size': forms.Select(attrs={
                'class': 'form-control',
            }),
            'price': MoneyWidget(
                amount_widget=forms.NumberInput(
                    attrs={
                        'class': 'form-control',
                        'placeholder': '0',
                        'style': 'border-radius: .7rem .7rem .0rem .0rem;',
                    }),
                currency_widget=forms.Select(
                    attrs={
                        'class': 'form-select form-control',
                        'style': 'border-radius: .0rem .0rem .7rem .7rem; ',
                    },
                    choices=currencies)
            ),
        }
