from django.contrib.auth.models import User
from django.db import models

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
        ("Aniq fanlar", "Aniq fanlar"),
        ("Axborot Texnologiyalariga oid", "Axborot Texnologiyalariga oid"),
        ("Detektiv", "Detektiv"),
        ("Fantastika", "Fantastika"),
        ("Ilmiy Fantastika", "Ilmiy Fantastika"),
        ("Qisqa hikoyalar", "Qisqa hikoyalar"),
        ("Romanlar", "Romanlar"),
        ("Romantika", "Romantika"),
        ("Sarguzashtlar", "Sarguzashtlar"),
        ("Tarixiy Fantastika", "Tarixiy Fantastika"),
        ("Tilga oid", "Tilga oid"),
        ("Zamonaviy Fantastika", "Zamonaviy Fantastika"),
    ]

    category = models.CharField(max_length=100, choices=categories, default=None, null=True)
    name_coded = models.CharField(max_length=50, null=True)
    picture = models.ImageField(default='user_loaded_images',
                                null=True, blank=True, upload_to='user_loaded_images/')
    pages = models.PositiveIntegerField(null=True)
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
        ("Jismoniy shaxs", "Jismoniy shaxs"),
        ("Yuridik shaxs", "Yuridik shaxs"),
    ]

    f_name = models.CharField(max_length=200, null=True)
    l_name = models.CharField(max_length=200, null=True)
    m_name = models.CharField(max_length=200, null=True)
    age = models.PositiveIntegerField(default=18, null=True, blank=True)
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


# ========================================== A model for using in Discount ==========================================


class Coupon(models.Model):
    """A model handling coupons for discounting."""

    statuses = [
        ("Faol", "Faol"),
        ("To'xtatilgan", "To'xtatilgan"),
        ("Muddati o'tgan", "Muddati o'tgan"),
    ]

    types = [
        ('Classic', 'Classic'),
        ('Silver', 'Silver'),
        ('Gold', 'Gold'),
        ('Premium', 'Premium'),
    ]

    date_release = models.DateField(auto_now_add=False)
    type = models.CharField(max_length=10, choices=types, null=True)
    lifetime = models.DateField(auto_now_add=False, null=True)
    code = models.CharField(max_length=15, null=True)
    status = models.CharField(max_length=20, choices=statuses, null=True)

    objects = models.Manager()

    def __str__(self):

        return f'*****{self.code[5:10]}*****'


# ===================================================================================================================


class Discount(models.Model):
    """A model handling discounts for orders from those who have got special coupons and in general."""

    date = models.DateField(auto_now_add=False, null=True)
    coupon = models.ForeignKey(Coupon, on_delete=models.PROTECT)
    for_books = models.PositiveIntegerField(null=True)
    minus = models.PositiveIntegerField(null=True)

    objects = models.Manager()

    def __str__(self):

        return str(self.date)


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

    currencies = [
        ('EUR', 'EUR'),
        ('RUB', 'RUB'),
        ('USD', 'USD'),
        ('UZS', 'UZS'),
    ]

    class Meta:

        verbose_name = 'Loss'
        verbose_name_plural = 'Losses'

    ltype = models.ForeignKey(LType, on_delete=models.PROTECT)
    # The name attribute is for books
    name = models.CharField(max_length=100, null=True, blank=True)
    size = models.CharField(max_length=10, null=True, blank=True)
    type = models.CharField(max_length=50, null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)
    amount = models.CharField(max_length=50, null=True)
    reason = models.CharField(max_length=100, null=True)
    time_loss = models.DateField(auto_now_add=False, null=True)
    loser = models.ForeignKey(User, on_delete=models.PROTECT)
    worth = MoneyField(max_digits=50, decimal_places=2, default_currency='UZS',
                       currency_choices=currencies, null=True)

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


# ================================ A model defining the PLACES_TO_GET for Order model ================================

class PlaceToGet(models.Model):
    """A model handling the places from where customers can get their orders."""

    class Meta:

        verbose_name = 'PlaceToGet'
        verbose_name_plural = 'PlacesToGet'

    place = models.CharField(max_length=200, null=True)
    available = models.BooleanField(default=True)

    objects = models.Manager()

    def __str__(self):

        return self.place

# ====================================================================================================================


class Order(models.Model):
    """A model handling orders for books from users."""
    payment_methods = [
        ("Click", "Click"),
        ("Naqd", "Naqd"),
    ]
    statuses = [
        ("To'lovni kutmoqda", "To'lovni kutmoqda"),
        ("Bekor qilindi", "Bekor qilindi"),
        ("Qabul qilindi", "Qabul qilindi"),
        ("Chop etilmoqda", "Chop etilmoqda"),
        ("Tayyor", "Tayyor"),
    ]
    book_types = [
        ("Plastik prujinalangan (rangsiz)", "Plastik prujinalangan (rangsiz)"),
        ("Plastik prujinalangan (rangli)", "Plastik prujinalangan (rangli)"),
        ("Metal prujinalangan (rangsiz)", "Metal prujinalangan (rangsiz)"),
        ("Metal prujinalangan (rangli)", "Metal prujinalangan (rangli)"),
        ("Yelimlangan yumshoq muqovali (rangsiz)", "Yelimlangan yumshoq muqovali (rangsiz)"),
        ("Yelimlangan yumshoq muqovali (rangli)", "Yelimlangan yumshoq muqovali (rangli)"),
        ("Yelimlangan qattiq muqovali (rangsiz)", "Yelimlangan qattiq muqovali (rangsiz)"),
        ("Yelimlangan qattiq muqovali (rangli)", "Yelimlangan qattiq muqovali (rangli)"),
        ("Steplerlangan (rangsiz)", "Steplerlangan (rangsiz)"),
        ("Steplerlangan (rangli)", "Steplerlangan (rangli)"),
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
        ("Saytdan", "Saytdan"),
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
    custom_page_number = models.PositiveIntegerField(default=0, null=True)
    number = models.PositiveIntegerField(default=1, null=True)
    user_needs = models.DateTimeField(auto_now_add=False, default=None, null=True)
    place_to_get = models.ForeignKey(PlaceToGet, on_delete=models.PROTECT, null=True)
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
    stapled_colorless = models.BooleanField(default=True)
    stapled_color = models.BooleanField(default=False)

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


class Printer(models.Model):
    """A model handling information on the printers that exist in the service."""

    statuses = [
        ("Soz", "Soz"),
        ("Mayda buzilishlari mavjud", "Mayda buzilishlari mavjud"),
        ("Ta'mir talab", "Ta'mir talab"),
    ]

    statuses_when_bought = [
        ("Yangi", "Yangi"),
        ("Ishlatilgan", "Ishlatilgan"),
    ]

    brand = models.CharField(max_length=150, null=True)
    model = models.CharField(max_length=150, null=True)
    bought_at = models.DateField(auto_now_add=False, null=True)
    status_when_bought = models.CharField(max_length=20, choices=statuses_when_bought, null=True)
    initial_page_count = models.PositiveIntegerField(null=True)
    current_page_count = models.PositiveIntegerField(null=True)
    current_status = models.CharField(max_length=50, choices=statuses, null=True)

    objects = models.Manager()

    def __str__(self):

        return f'{self.brand} {self.model}'


# ========================================= A submodel for the model Printer =========================================


class RefillAndPageCount(models.Model):
    """A model handling some dynamic counting information from the model Printer."""

    printer = models.ForeignKey(Printer, on_delete=models.PROTECT)
    total_refill_count = models.PositiveIntegerField(null=True)
    last_refill = models.DateTimeField(auto_now_add=False, null=True)
    printed = models.PositiveIntegerField(null=True)
    accounted = models.BooleanField(default=False, null=True)

    objects = models.Manager()

    def __str__(self):

        return str(self.printer.__str__())


# ====================================================================================================================


# ======================================== Models for using in Prices section ========================================


class BindingPrice(models.Model):
    """A model handling binding prices based on type and size."""

    types = [
        ("Plastik prujinalash", "Plastik prujinalash"),
        ("Metal prujinalash", "Metal prujinalash"),
        ("Yumshoq muqovali yelimlash", "Yumshoq muqovali yelimlash"),
        ("Qattiq muqovali yelimlash", "Qattiq muqovali yelimlash"),
        ("Steplerlash", "Steplerlash"),
    ]

    sizes = [
        ('A4', 'A4'),
        ('A5', 'A5'),
    ]

    date = models.DateField(auto_now_add=False, null=True)
    type = models.CharField(max_length=150, choices=types, null=True)
    size = models.CharField(max_length=150, choices=sizes, null=True)
    price = MoneyField(max_digits=50, decimal_places=2, default_currency='UZS', null=True)

    objects = models.Manager()

    def __repr__(self):

        return self.type


class ColorPrice(models.Model):
    """A model handling color prices based on color."""

    colors = [
        ("Qora", "Qora"),
        ("Rangli", "Rangli"),
    ]
    sizes = [
        ('A4', 'A4'),
        ('A5', 'A5'),
    ]

    date = models.DateField(auto_now_add=False, null=True)
    color = models.CharField(max_length=100, choices=colors, null=True)
    size = models.CharField(max_length=100, choices=sizes, null=True)
    price = MoneyField(max_digits=50, decimal_places=2, default_currency='UZS', null=True)

    objects = models.Manager()

    def __repr__(self):

        return self.color


class CoverPrice(models.Model):
    """A model handling cover prices based on size and type."""

    types = [
        ("Plastik prujinali ulash uchun", "Plastik prujinali ulash uchun"),
        ("Metal prujinali ulash uchun", "Metal prujinali ulash uchun"),
        ("Yelimli ulash uchun (Yumshoq)", "Yelimli ulash uchun (Yumshoq)"),
        ("Yelimli ulash uchun (Qattiq)", "Yelimli ulash uchun (Qattiq)"),
    ]
    sizes = [
        ('A4', 'A4'),
        ('A5', 'A5'),
    ]

    date = models.DateField(auto_now_add=False, null=True)
    type = models.CharField(max_length=100, choices=types,  null=True)
    size = models.CharField(max_length=100, choices=sizes, null=True)
    price = MoneyField(max_digits=50, decimal_places=2, default_currency='UZS', null=True)

    objects = models.Manager()

    def __repr__(self):

        return self.type


class GluePrice(models.Model):
    """A model handling glue prices based on type and size."""

    sizes = [
        ('A4', 'A4'),
        ('A5', 'A5'),
    ]

    date = models.DateField(auto_now_add=False, null=True)
    type = models.CharField(max_length=100, null=True)
    size = models.CharField(max_length=100, choices=sizes, null=True)
    price = MoneyField(max_digits=50, decimal_places=2, default_currency='UZS', null=True)

    objects = models.Manager()

    def __repr__(self):
        return self.type


class OuterPrice(models.Model):
    """A model handling the prices for orders and resources."""

    date = models.DateField(auto_now_add=False, null=True)
    staple_price = MoneyField(max_digits=50, decimal_places=2, default_currency='UZS', null=True)
    packaging_expenses = MoneyField(max_digits=50, decimal_places=2, default_currency='UZS', null=True)
    delivery_expenses = MoneyField(max_digits=50, decimal_places=2, default_currency='UZS', null=True)
    workforce_expenses = MoneyField(max_digits=50, decimal_places=2, default_currency='UZS', null=True)
    electricity_expenses = MoneyField(max_digits=50, decimal_places=2, default_currency='UZS', null=True)
    printer_expenses = MoneyField(max_digits=50, decimal_places=2, default_currency='UZS', null=True)
    profit = models.PositiveIntegerField(null=True)

    objects = models.Manager()

    def __repr__(self):

        return str(self.date)


class PagePrice(models.Model):
    """A model handling page prices based on sizes."""

    types = [
        ('Classic (qora)', 'Classic (qora)'),
        ('Classic (rangli)', 'Classic (rangli)'),
        ('ECO (qora)', 'ECO (qora)'),
        ('ECO (rangli)', 'ECO (rangli)'),
        ('Premium (qora)', 'Premium (qora)'),
        ('Premium (rangli)', 'Premium (rangli)'),
    ]
    sizes = [
        ('A4', 'A4'),
        ('A5', 'A5'),
    ]

    date = models.DateField(auto_now_add=False, null=True)
    type = models.CharField(max_length=100, choices=types, null=True)
    size = models.CharField(max_length=100, choices=sizes, null=True)
    price = MoneyField(max_digits=50, decimal_places=2, default_currency='UZS', null=True)

    objects = models.Manager()

    def __repr__(self):

        return self.size


class PaperPrice(models.Model):
    """A model handling paper prices based on sizes."""

    types = [
        ('Classic', 'Classic'),
        ('ECO', 'ECO'),
        ('Premium', 'Premium'),
    ]
    sizes = [
        ('A4', 'A4'),
        ('A5', 'A5'),
    ]

    date = models.DateField(auto_now_add=False, null=True)
    type = models.CharField(max_length=100, choices=types, null=True)
    size = models.CharField(max_length=100, choices=sizes, null=True)
    price = MoneyField(max_digits=50, decimal_places=2, default_currency='UZS', null=True)

    objects = models.Manager()

    def __repr__(self):

        return self.size


class RingPrice(models.Model):
    """A model handling ring pricing based size and type."""

    types = [
        ('Plastik', 'Plastik'),
        ('Metal', 'Metal'),
    ]
    sizes = [
        ('4.5mm (<15)', '4.5mm (<15)'),
        ('6mm (15-30)', '6mm (15-30)'),
        ('8mm (30-50)', '8mm (30-50)'),
        ('10mm (50-70)', '10mm (50-70)'),
        ('12mm (70-90)', '12mm (70-90)'),
        ('14mm (90-110)', '14mm (90-110)'),
        ('16mm (110-130)', '16mm (110-130)'),
        ('18mm (130-150)', '18mm (130-150)'),
        ('20mm (150-170)', '20mm (150-170)'),
        ('22mm (170-190)', '22mm (170-190)'),
        ('25mm (190-220)', '25mm (190-220)'),
        ('28mm (220-250)', '28mm (220-250)'),
        ('32mm (250-280)', '32mm (250-280)'),
        ('38mm (280-340)', '38mm (280-340)'),
        ('45mm (340-410)', '45mm (340-410)'),
        ('51mm (410-480)', '51mm (410-480)'),
        ('5.5mm (<20)', '5.5mm (<20)'),
        ('6.9mm (20-30)', '6.9mm (20-30)'),
        ('8.1mm (30-50)', '8.1mm (30-50)'),
        ('9.5mm (50-60)', '9.5mm (50-60)'),
        ('11mm (60-80)', '11mm (60-80)'),
        ('12.7mm (80-100)', '12.7mm (80-100)'),
        ('14.3mm (100-120)', '14.3mm (100-120)'),
    ]

    date = models.DateField(auto_now_add=False, null=True)
    type = models.CharField(max_length=100, choices=types, null=True)
    size = models.CharField(max_length=50, choices=sizes, null=True)
    price = MoneyField(max_digits=50, decimal_places=2, default_currency='UZS', null=True)

    objects = models.Manager()

    def __repr__(self):

        return self.type


class YarnPrice(models.Model):
    """A model handling yarn prices based on type and size."""

    types = [
        ("Yupqa", "Yupqa"),
        ("O'rtacha", "O'rtacha"),
        ("Qalin", "Qalin"),
    ]
    sizes = [
        ('A4', 'A4'),
        ('A5', 'A5'),
    ]

    date = models.DateField(auto_now_add=False, null=True)
    type = models.CharField(max_length=100, choices=types, null=True)
    size = models.CharField(max_length=100, choices=sizes, null=True)
    price = MoneyField(max_digits=50, decimal_places=2, default_currency='UZS', null=True)

    objects = models.Manager()

    def __repr__(self):

        return self.type


# ====================================================================================================================


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
    amount_used = models.PositiveIntegerField(null=True, blank=True)
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


class Workforce(models.Model):
    """A model handling workforce information from those working for the service."""

    class Meta:

        verbose_name = 'Workforce'
        verbose_name_plural = 'Workforce'

    currencies = [
        ('EUR', 'EUR'),
        ('RUB', 'RUB'),
        ('USD', 'USD'),
        ('UZS', 'UZS'),
    ]

    name = models.CharField(max_length=200, null=True)
    surname = models.CharField(max_length=200, null=True)
    middle_name = models.CharField(max_length=200, null=True, blank=True)
    age = models.PositiveIntegerField(null=True)
    address_living = models.CharField(max_length=200, null=True)
    career_status = models.CharField(max_length=200, null=True)
    joined_service = models.DateField(auto_now_add=False, null=True)
    position = models.CharField(max_length=200, null=True)
    salary = MoneyField(max_digits=50, decimal_places=2,
                        default_currency='UZS', currency_choices=currencies, null=True)
    last_salary_reception = models.DateField(auto_now_add=False, null=True)
    last_salary_paid = models.BooleanField(null=True)

    objects = models.Manager()

    def __str__(self):

        return f'{self.name} {self.surname}'
