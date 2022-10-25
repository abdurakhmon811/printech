from django.db import models
from django.contrib.auth.models import User

# Third party application fields
from djmoney.models.fields import MoneyField
from phonenumber_field.modelfields import PhoneNumberField


class BlogPost(models.Model):
    """A model handling blog posts by admins."""

    title = models.CharField(max_length=100, default=None)
    subtitle_1 = models.CharField(max_length=100, default=None)
    subtitle_2 = models.CharField(max_length=100, null=True, blank=True, default=None)
    subtitle_3 = models.CharField(max_length=100, null=True, blank=True, default=None)
    picture_1 = models.ImageField(upload_to='user_loaded_images/', default='user_loaded_images')
    picture_2 = models.ImageField(upload_to='user_loaded_images/', null=True, blank=True, default='user_loaded_images')
    picture_3 = models.ImageField(upload_to='user_loaded_images/', null=True, blank=True, default='user_loaded_images')
    body_1 = models.TextField(default=None)
    body_2 = models.TextField(null=True, blank=True, default=None)
    body_3 = models.TextField(null=True, blank=True, default=None)
    conclusion = models.TextField(default=None)
    publisher = models.ForeignKey(User, on_delete=models.PROTECT)
    publisher_tg = models.URLField(default=None)
    publisher_li = models.URLField(default=None)
    publisher_gm = models.EmailField(default=None)
    publisher_tw = models.URLField(default=None)
    ref_links = models.TextField(null=True, blank=True, default=None)
    date_published = models.DateTimeField(auto_now_add=True, null=True)

    objects = models.Manager()

    def __str__(self):

        return self.title


class Book(models.Model):
    """A model handling books."""
    categories = [
        ('Aniq fanlar', 'Aniq fanlar'),
        ('Axborot Texnologiyalariga oid', 'Axborot Texnologiyalariga oid'),
        ('Detektiv', 'Detektiv'),
        ('Fantastika', 'Fantastika'),
        ('Ilmiy Fantastika', 'Ilmiy Fantastika'),
        ('Qisqa hikoyalar', 'Qisqa hikoyalar'),
        ('Romanlar', 'Romanlar'),
        ('Romantika', 'Romantika'),
        ('Sarguzashtlar', 'Sarguzashtlar'),
        ('Tarixiy Fantastika', 'Tarixiy Fantastika'),
        ('Tilga oid', 'Tilga oid'),
        ('Zamonaviy Fantastika', 'Zamonaviy Fantastika'),
    ]

    category = models.CharField(max_length=100, choices=categories, default=None, null=True)
    name_coded = models.CharField(max_length=50, null=True)
    picture = models.ImageField(default='user_loaded_images',
                                null=True, blank=True, upload_to='user_loaded_images/')
    pages = models.IntegerField(null=True)
    chars = models.TextField(default=None, null=True)
    telegram_link = models.URLField(default=None, null=True)

    objects = models.Manager()

    def __str__(self):

        return self.name_coded

    def image_url(self):
        """Return the image URL if it does exist, otherwise return a default image."""

        if self.picture and hasattr(self.picture, 'url'):
            return self.picture.url
        else:
            return 'service/static/images/books22.jpg'


class Complaint(models.Model):
    """A model handling complaints from users."""

    complainant = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=50, default=None, null=True)
    book = models.ForeignKey(Book, on_delete=models.PROTECT, default=None, null=True)
    time_bought = models.DateField(auto_now_add=False, default=None, null=True)
    problem = models.TextField()

    objects = models.Manager()

    def __str__(self):

        return self.problem[:50] + '...'


class Contact(models.Model):
    """A model handling inquiries from users."""

    phone_number = PhoneNumberField(region='UZ', null=True)
    telegram = models.URLField(default=None, null=True)
    title = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)
    applicant = models.ForeignKey(User, on_delete=models.PROTECT)
    date_made = models.DateTimeField(auto_now_add=True, null=True)

    objects = models.Manager()

    def __str__(self):

        return f'{self.title[:50]}...'


class CreateSite(models.Model):
    """A model handling inquires for Web Development service provided by the main admin."""

    person_choices = [
        ('Jismoniy shaxs', 'Jismoniy shaxs'),
        ('Yuridik shaxs', 'Yuridik shaxs'),
    ]

    f_name = models.CharField(max_length=200, null=True)
    l_name = models.CharField(max_length=200, null=True)
    m_name = models.CharField(max_length=200, null=True)
    age = models.IntegerField(default=18, null=True, blank=True)
    person = models.CharField(max_length=25, choices=person_choices, null=True)
    company = models.CharField(null=True, blank=True, max_length=200)
    mail = models.EmailField(default=None, null=True)
    client_number = PhoneNumberField(region='UZ', default=None, null=True)
    client = models.ForeignKey(User, on_delete=models.PROTECT)
    site_description = models.CharField(max_length=400, null=True)
    date_applied = models.DateTimeField(auto_now_add=True, null=True)

    objects = models.Manager()

    def __str__(self):

        return f'{self.f_name[:50]}...'


# ================================== Models for using for Expense and Income models ==================================


class Account(models.Model):
    """A model handling accounts for incomes and expenses."""

    currencies = [
        ('EUR', 'EUR'),
        ('RUB', 'RUB'),
        ('USD', 'USD'),
        ('UZS', 'UZS'),
    ]

    name = models.CharField(max_length=100, null=True, default=None)
    means = MoneyField(max_digits=50, decimal_places=2,
                       default_currency='UZS', currency_choices=currencies, null=True)

    objects = models.Manager()

    def __str__(self):

        return self.name


class CategoryEx(models.Model):
    """A model handling categories for expenses."""

    class Meta:
        verbose_name = 'ExCategory'
        verbose_name_plural = 'ExCategories'

    category = models.CharField(max_length=150, null=True, default=None)

    objects = models.Manager()

    def __str__(self):

        return self.category


class CategoryIn(models.Model):
    """A model handling categories for incomes."""

    class Meta:
        verbose_name = 'InCategory'
        verbose_name_plural = 'InCategories'

    category = models.CharField(max_length=150, null=True, default=None)

    objects = models.Manager()

    def __str__(self):

        return self.category


class SubCategoryEx(models.Model):
    """A model handling subcategories for incomes."""

    class Meta:
        verbose_name = 'ExSubcategory'
        verbose_name_plural = 'ExSubcategories'

    subcategory = models.CharField(max_length=150, null=True, default=None)

    objects = models.Manager()

    def __str__(self):

        return self.subcategory


class SubCategoryIn(models.Model):
    """A model handling subcategories for incomes."""

    class Meta:
        verbose_name = 'InSubcategory'
        verbose_name_plural = 'InSubcategories'

    subcategory = models.CharField(max_length=150, null=True, default=None)

    objects = models.Manager()

    def __str__(self):

        return self.subcategory


# ====================================================================================================================


class Expense(models.Model):
    """A model handling the expenses made within the business area."""

    currencies = [
        ('EUR', 'EUR'),
        ('RUB', 'RUB'),
        ('USD', 'USD'),
        ('UZS', 'UZS'),
    ]

    category = models.ForeignKey(CategoryEx, on_delete=models.PROTECT, null=True)
    subcategory = models.ForeignKey(SubCategoryEx, on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    account = models.ForeignKey(Account, on_delete=models.PROTECT, null=True)
    date_made = models.DateTimeField(auto_now_add=False, default=None, null=True)
    comment = models.TextField(null=True)
    amount = MoneyField(max_digits=50, decimal_places=2,
                        default_currency='UZS', currency_choices=currencies, null=True)

    objects = models.Manager()

    def __repr__(self):

        return self.category


class Income(models.Model):
    """A model handling the incomes made within the business area."""

    currencies = [
        ('EUR', 'EUR'),
        ('RUB', 'RUB'),
        ('USD', 'USD'),
        ('UZS', 'UZS'),
    ]

    category = models.ForeignKey(CategoryIn, on_delete=models.PROTECT, null=True)
    subcategory = models.ForeignKey(SubCategoryIn, on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    account = models.ForeignKey(Account, on_delete=models.PROTECT, null=True)
    date_made = models.DateTimeField(auto_now_add=False, default=None, null=True)
    comment = models.TextField(null=True)
    amount = MoneyField(max_digits=50, decimal_places=2,
                        default_currency='UZS', currency_choices=currencies, null=True)

    objects = models.Manager()

    def __repr__(self):

        return f'{self.category}'


# =============================== Models for using within the Resource and Loss model ===============================


class LType(models.Model):
    """A model handling the loss types for the Loss model."""

    type = models.CharField(max_length=100, null=True)
    # The following attributes define what kind of attributes the resource being input does have
    size = models.BooleanField(default=False, null=True, blank=True)
    color = models.BooleanField(default=False, null=True, blank=True)

    objects = models.Manager()

    def __str__(self):

        return self.type


# ===================================================================================================================


class Loss(models.Model):
    """A model handling the losses in business."""

    class Meta:

        verbose_name = 'Loss'
        verbose_name_plural = 'Losses'

    ltype = models.ForeignKey(LType, on_delete=models.PROTECT)
    # The name attribute is for books
    name = models.CharField(max_length=100, null=True, blank=True)
    size = models.CharField(max_length=10, null=True, blank=True)
    type = models.CharField(max_length=15, null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)
    amount = models.CharField(max_length=50, null=True)
    reason = models.CharField(max_length=100, null=True)
    time_loss = models.DateField(auto_now_add=False, null=True)
    loser = models.ForeignKey(User, on_delete=models.PROTECT)

    objects = models.Manager()

    def __str__(self):

        return str(self.ltype)


class News(models.Model):
    """A model handling news about the service."""

    class Meta:

        verbose_name = 'News'
        verbose_name_plural = 'News'

    title = models.CharField(max_length=100, default=None, null=True)
    subtitle_1 = models.CharField(max_length=100, default=None, null=True)
    subtitle_2 = models.CharField(max_length=100, null=True, blank=True, default=None)
    subtitle_3 = models.CharField(max_length=100, null=True, blank=True, default=None)
    picture_1 = models.ImageField(upload_to='user_loaded_images/', default='user_loaded_images', null=True)
    picture_2 = models.ImageField(null=True, blank=True, upload_to='user_loaded_images/', default='user_loaded_images')
    picture_3 = models.ImageField(null=True, blank=True, upload_to='user_loaded_images/', default='user_loaded_images')
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    short_body = models.CharField(max_length=200, default=None, null=True)
    body_1 = models.TextField(default=None, null=True)
    body_2 = models.TextField(null=True, blank=True, default=None)
    body_3 = models.TextField(null=True, blank=True, default=None)
    publisher = models.ForeignKey(User, on_delete=models.PROTECT)
    publisher_tg = models.URLField(default=None, null=True)
    publisher_li = models.URLField(default=None, null=True)
    publisher_gm = models.EmailField(default=None, null=True)
    publisher_tw = models.URLField(default=None, null=True)

    objects = models.Manager()

    def __str__(self):

        return self.title


class Order(models.Model):
    """A model handling orders for books from users."""
    # TODO: places_to_get, book types and colors should be dynamic rather than static
    places_to_get = [
        ('Qarshi Muhandislik-Iqtisodiyot Instituti', 'Qarshi Muhandislik-Iqtisodiyot Instituti'),
        ('Kamandi MFY', 'Kamandi MFY'),
    ]
    payment_methods = [
        ('Click', 'Click'),
        ('Naqd', 'Naqd'),
        ('VISA', 'VISA'),
    ]
    statuses = [
        ("To'lovni kutmoqda", "To'lovni kutmoqda"),
        ('Bekor qilindi', 'Bekor qilindi'),
        ('Qabul qilindi', 'Qabul qilindi'),
        ('Chop etilmoqda', 'Chop etilmoqda'),
        ('Tayyor', 'Tayyor'),
    ]
    book_types = [
        ('Plastik prujinalangan (rangsiz)', 'Plastik prujinalangan (rangsiz)'),
        ('Plastik prujinalangan (rangli)', 'Plastik prujinalangan (rangli)'),
        ('Metal prujinalangan (rangsiz)', 'Metal prujinalangan (rangsiz)'),
        ('Metal prujinalangan (rangli)', 'Metal prujinalangan (rangli)'),
        ('Yelimlangan yumshoq muqovali (rangsiz)', 'Yelimlangan yumshoq muqovali (rangsiz)'),
        ('Yelimlangan yumshoq muqovali (rangli)', 'Yelimlangan yumshoq muqovali (rangli)'),
        ('Yelimlangan qattiq muqovali (rangsiz)', 'Yelimlangan qattiq muqovali (rangsiz)'),
        ('Yelimlangan qattiq muqovali (rangli)', 'Yelimlangan qattiq muqovali (rangli)'),
    ]
    colors = [
        ("Ko`k", "Ko`k"),
        ("Qizil", "Qizil"),
        ("Qora", "Qora"),
        ("Sariq", "Sariq"),
        ("Yashil", "Yashil"),
    ]
    colors_2 = [
        ("Ko`k", "Ko`k"),
        ("Qizil", "Qizil"),
        ("Qora", "Qora"),
        ('Rangsiz', 'Rangsiz'),
        ("Sariq", "Sariq"),
        ("Yashil", "Yashil"),
    ]
    sources = [
        ('Saytdan', 'Saytdan'),
        ("O'zimdan", "O'zimdan"),
    ]
    sizes = [
        ('A4', 'A4'),
        ('A5', 'A5'),
    ]

    order_number = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.PROTECT, null=True)
    custom_book = models.CharField(max_length=200, default=None, null=True)
    book_type = models.CharField(choices=book_types, max_length=100, null=True)
    ring_color = models.CharField(choices=colors_2, max_length=100, null=True, blank=True)
    back_cover_color = models.CharField(choices=colors, max_length=100, null=True, blank=True)
    front_cover_color = models.CharField(choices=colors_2, max_length=100, null=True, blank=True)
    size = models.CharField(choices=sizes, max_length=5, null=True)
    user_needs = models.DateTimeField(auto_now_add=False, default=None, null=True)
    number = models.PositiveIntegerField(default=1, null=True)
    place_to_get = models.CharField(choices=places_to_get, max_length=50, null=True)
    customer = models.ForeignKey(User, on_delete=models.PROTECT)
    customer_number = PhoneNumberField(region='UZ', default=None)
    customer_email = models.EmailField(default=None, max_length=255, null=True, blank=True)
    payment = models.CharField(choices=payment_methods, max_length=50, default=None)
    date_ordered = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=50, choices=statuses, default="To'lovni kutmoqda", null=True)
    delivered = models.BooleanField(default=False, null=True)

    objects = models.Manager()

    def __str__(self):

        return f'{self.order_number}'


class OrderOptions(models.Model):
    """A model handling available resources used for ordering."""

    class Meta:
        verbose_name = 'Order Options'
        verbose_name_plural = 'Order Options'

    # As of
    date = models.DateField(auto_now_add=False)

    # Book types
    ringed_colorless = models.BooleanField(default=True)
    ringed_color = models.BooleanField(default=False)
    metal_ringed_colorless = models.BooleanField(default=False)
    metal_ringed_color = models.BooleanField(default=False)
    g_soft_colorless = models.BooleanField(default=False)
    g_soft_color = models.BooleanField(default=False)
    g_hard_colorless = models.BooleanField(default=False)
    g_hard_color = models.BooleanField(default=False)

    # Colors
    black = models.BooleanField(default=False)
    blue = models.BooleanField(default=True)
    green = models.BooleanField(default=False)
    red = models.BooleanField(default=False)
    transparent = models.BooleanField(default=False)
    yellow = models.BooleanField(default=False)

    objects = models.Manager()

    def __str__(self):

        return str(self.date)


# ==================================== Models for using within the Resource model ====================================


class RType(models.Model):
    """A model handling the resource types for the Resource model."""

    type = models.CharField(max_length=100, null=True)
    # The following attributes define what kind of attributes the resource being input does have
    size = models.BooleanField(default=False, null=True, blank=True)
    color = models.BooleanField(default=False, null=True, blank=True)

    objects = models.Manager()

    def __str__(self):

        return str(self.type)


# ====================================================================================================================

class Resource(models.Model):
    """A model handling the available resources in the base."""

    currencies = [
        ('EUR', 'EUR'),
        ('RUB', 'RUB'),
        ('USD', 'USD'),
        ('UZS', 'UZS'),
    ]

    rtype = models.ForeignKey(RType, on_delete=models.PROTECT)
    size = models.CharField(max_length=10, null=True, blank=True)
    type = models.CharField(max_length=15, null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)
    amount = models.CharField(max_length=50, null=True)
    time_bought = models.DateField(auto_now_add=False, null=True)
    worth = MoneyField(max_digits=50, decimal_places=2, default_currency='UZS',
                       currency_choices=currencies, null=True)
    last_used_date = models.DateField(auto_now_add=False, null=True, blank=True)
    amount_used = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    available = models.CharField(max_length=100, null=True)

    objects = models.Manager()

    def __repr__(self):

        return str(self.rtype)


class Transaction(models.Model):
    """A model handling transactions between money accounts."""

    currencies = [
        ('EUR', 'EUR'),
        ('RUB', 'RUB'),
        ('USD', 'USD'),
        ('UZS', 'UZS'),
    ]

    acc_1 = models.ForeignKey(Account, on_delete=models.PROTECT, related_name='transactions_1', null=True)
    acc_2 = models.ForeignKey(Account, on_delete=models.PROTECT, related_name='transactions_2', null=True)
    date_made = models.DateTimeField(auto_now_add=True, editable=True, null=True)
    amount = MoneyField(max_digits=50, decimal_places=2,
                        default_currency='UZS', currency_choices=currencies, null=True)

    objects = models.Manager()

    def __repr__(self):

        return self.amount
