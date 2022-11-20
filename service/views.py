from django.contrib import messages
from django.db.models import ProtectedError, Q
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist, RequestAborted
from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404
from .forms import AccountForm, \
    BindingPriceForm, BlogPostForm, BookForm, \
    CategoryExForm, CategoryInForm, ComplaintBookForm, ColorPriceForm, ComplaintOtherForm, ComplaintSiteForm, \
    ContactForm, CouponForm, CoverPriceForm, CreateSiteForm, \
    DiscountForm, \
    ExpenseForm, \
    GluePriceForm, \
    IncomeForm, \
    LossForm, LTypeForm, \
    NewsForm, \
    OrderOptionsForm, OrderSelfForm, OrderSiteForm, OuterPriceForm, \
    PagePriceForm, PaperPriceForm, PlaceToGetForm, PrinterForm, \
    RefillAndPageCountForm, ResourceForm, RingPriceForm, RTypeForm, \
    SelfOrderForm, SiteOrderForm, SubCategoryExForm, SubCategoryInForm, \
    TransactionForm, \
    WorkforceForm, \
    YarnPriceForm
from .models import Account, \
    BindingPrice, BlogPost, Book, \
    CategoryEx, CategoryIn, ColorPrice, Complaint, Contact, Coupon, CoverPrice, CreateSite, \
    Discount, \
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
import decimal
import math
import re
import json


def index(request):
    """A view providing content for the home page."""

    news = News.objects.all().order_by('-id', '-date_added')[:3]
    posts = BlogPost.objects.all().order_by('-id', '-date_published')[:3]
    context = {
        'news': news,
        'posts': posts,
    }

    return render(request, 'service/index.html', context)


def contact(request):
    """A view providing content for the contact page."""

    if request.method != 'POST':
        form = ContactForm()
    else:
        form = ContactForm(data=request.POST)
        if form.is_valid():
            new_reference = form.save(commit=False)
            new_reference.applicant = request.user
            new_reference.save()
            return redirect('success_contact')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
    }
    return render(request, 'service/contact.html', context)


def success_contact(request):
    """A view rendering the page which tells that the contact application has successfully been sent."""

    return render(request, 'service/success_contact.html')


def view_book_categories(request):
    """A view rendering the page including the book categories."""

    return render(request, 'service/view_book_categories.html')


# Here goes the book categories
def adventure_books(request):

    books = Book.objects.filter(category='Sarguzashtlar')
    context = {
        'books': books
    }
    return render(request, 'service/adventure_books.html', context)


def contemporary_fiction_books(request):

    books = Book.objects.filter(category='Zamonaviy Fantastika')
    context = {
        'books': books
    }
    return render(request, 'service/contemporary_fiction_books.html', context)


def exact_science_books(request):

    books = Book.objects.filter(category='Aniq fanlar')
    context = {
        'books': books
    }
    return render(request, 'service/exact_science_books.html', context)


def fantasy_books(request):

    books = Book.objects.filter(category='Fantastika')
    context = {
        'books': books
    }
    return render(request, 'service/fantasy_books.html', context)


def historical_fiction_books(request):

    books = Book.objects.filter(category='Tarixiy Fantastika')
    context = {
        'books': books
    }
    return render(request, 'service/historical_fiction_books.html', context)


def it_books(request):

    books = Book.objects.filter(category='Axborot Texnologiyalariga oid')
    context = {
        'books': books
    }
    return render(request, 'service/it_books.html', context)


def language_books(request):

    books = Book.objects.filter(category='Tilga oid')
    context = {
        'books': books
    }
    return render(request, 'service/language_books.html', context)


def mystery_books(request):

    books = Book.objects.filter(category='Detektiv')
    context = {
        'books': books
    }
    return render(request, 'service/mystery_books.html', context)


def novel_books(request):

    books = Book.objects.filter(category='Romanlar')
    context = {
        'books': books
    }
    return render(request, 'service/novel_books.html', context)


def romance_books(request):

    books = Book.objects.filter(category='Romantika')
    context = {
        'books': books
    }
    return render(request, 'service/romance_books.html', context)


def science_fiction_books(request):

    books = Book.objects.filter(category='Ilmiy Fantastika')
    context = {
        'books': books
    }
    return render(request, 'service/science_fiction_books.html', context)


def short_story_books(request):

    books = Book.objects.filter(category='Qisqa hikoyalar')
    context = {
        'books': books
    }
    return render(request, 'service/short_story_books.html', context)


def view_blogposts(request):
    """A view rendering the page for checking blog posts."""

    blogposts = BlogPost.objects.all().order_by('-date_published')
    context = {
        'posts': blogposts,
    }
    return render(request, 'service/blogposts.html', context)


def view_post(request, blogpost_id):
    """A view rendering the page for checking a blog post in detail."""

    blogpost = BlogPost.objects.get(id=blogpost_id)
    context = {
        'post': blogpost,
    }
    return render(request, 'service/blogpost.html', context)


def create_site(request):
    """A view providing the content for Web Development services."""

    if request.method != 'POST':
        form = CreateSiteForm()
    else:
        form = CreateSiteForm(data=request.POST)
        if form.is_valid():
            new_application = form.save(commit=False)
            new_application.client = request.user
            new_application.save()
            return redirect('success_create')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
    }
    return render(request, 'service/create_site.html', context)


def success_create(request):
    """A view rendering the page which tells that the application has successfully been sent."""

    return render(request, 'service/success_create.html')


def complaint_category(request):
    """A view rendering the page which shows the category of complaints to users."""

    return render(request, 'service/complaint_category.html')


def complain_site(request):
    """A view providing the content for the page receiving complaints about the website."""

    if request.method != 'POST':
        form = ComplaintSiteForm()
    else:
        form = ComplaintSiteForm(data=request.POST)
        if form.is_valid():
            new_complaint = form.save(commit=False)
            new_complaint.complainant = request.user
            new_complaint.save()
            return redirect('success_complaint')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
    }
    return render(request, 'service/complain_site.html', context)


def complain_books(request):
    """A view providing the content for the page receiving complaints about books."""

    if request.method != 'POST':
        form = ComplaintBookForm()
    else:
        form = ComplaintBookForm(data=request.POST)
        if form.is_valid():
            new_complaint = form.save(commit=False)
            new_complaint.complainant = request.user
            new_complaint.save()
            return redirect('success_complaint')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
    }
    return render(request, 'service/complain_books.html', context)


def complain_other(request):
    """A view providing the content for the page receiving complaints about other topics."""

    if request.method != 'POST':
        form = ComplaintOtherForm()
    else:
        form = ComplaintOtherForm(data=request.POST)
        if form.is_valid():
            new_complaint = form.save(commit=False)
            new_complaint.complainant = request.user
            new_complaint.save()
            return redirect('success_complaint')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
    }
    return render(request, 'service/complain_other.html', context)


def success_complaint(request):
    """A view rendering the page which tells that the complaint application has successfully been sent."""

    return render(request, 'service/success_complaint.html')


def view_news(request):
    """A view providing the content for the page of news."""

    news = News.objects.all().order_by('-date_added')
    context = {
        'news': news,
    }
    return render(request, 'service/view_news.html', context)


def detailed_news(request, news_id):
    """A view providing the content for the page of news in detail."""

    new = News.objects.get(id=news_id)
    context = {
        'new': new,
    }
    return render(request, 'service/detailed_news.html', context)


# ==================================== A management system for admins ====================================


def main_page(request):
    """A view rendering the page which welcomes admins."""

    check_super_user(request)

    return render(request, 'service/welcome_admin.html')


def check_orders(request):
    """A view providing the content for checking orders."""

    check_super_user(request)

    orders = Order.objects.all()
    orders_num = len(orders)
    context = {
        'orders': orders,
        'orders_num': orders_num,
    }
    return render(request, 'service/view_orders.html', context)


def edit_order(request, order_number):
    """A view providing the content for editing the chosen order."""

    check_super_user(request)

    order = Order.objects.get(pk=order_number)

    if order.book:
        if request.method != 'POST':
            form = SiteOrderForm(instance=order)
        else:
            form = SiteOrderForm(instance=order, data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('check_orders')
            else:
                messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

        context = {
            'form': form,
            'order': order,
        }
        return render(request, 'service/edit_ordersite.html', context)
    elif not order.book and order.custom_book:
        if request.method != 'POST':
            form = SelfOrderForm(instance=order)
        else:
            form = SelfOrderForm(instance=order, data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('check_orders')
            else:
                messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

        context = {
            'form': form,
            'order': order,
        }
        return render(request, 'service/edit_orderself.html', context)


def delete_order(request, order_number):
    """A view providing the function which deletes the chosen order."""

    check_super_user(request)

    order = get_object_or_404(Order, pk=order_number)
    order.delete()
    return render(request, 'service/order_deleted.html')


def order_options(request):
    """A view providing the content for the page for checking available resources and adding new ones."""

    check_super_user(request)

    res_s = OrderOptions.objects.all().order_by('-date')
    places = PlaceToGet.objects.all()
    places_num = len(places)

    options_form = OrderOptionsForm()
    places_form = PlaceToGetForm()

    if request.method == 'POST' and 'optionssubmit' in request.POST:
        options_form = OrderOptionsForm(data=request.POST)
        if options_form.is_valid():
            options_form.save()
            return redirect('order_options')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")
    elif request.method == 'POST' and 'placessubmit' in request.POST:
        places_form = PlaceToGetForm(data=request.POST)
        if places_form.is_valid():
            places_form.save()
            return redirect('order_options')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'options_form': options_form,
        'places': places,
        'places_form': places_form,
        'places_num': places_num,
        'res_s': res_s,
    }
    return render(request, 'service/order_options.html', context)


def edit_orderoptions(request, orderoptions_id):
    """A view providing the content for the page for editing the chosen order options."""

    check_super_user(request)

    options = get_object_or_404(OrderOptions, pk=orderoptions_id)

    if request.method != 'POST':
        form = OrderOptionsForm(instance=options)
    else:
        form = OrderOptionsForm(data=request.POST, instance=options)
        if form.is_valid():
            form.save()
            return redirect('order_options')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'options': options,
    }
    return render(request, 'service/edit_orderoptions.html', context)


def delete_orderoptions(request, orderoptions_id):
    """A view for deleting the chosen order options object and rendering the page telling
    the delete proces has gone successfully."""

    check_super_user(request)

    options = get_object_or_404(OrderOptions, pk=orderoptions_id)
    options.delete()
    return render(request, 'service/orderoptions_deleted.html')


def edit_placetoget(request, placetoget_id):
    """A view providing the content for the page for editing the chosen place from where
    customers can get their orders."""

    check_super_user(request)

    place = get_object_or_404(PlaceToGet, pk=placetoget_id)

    if request.method != 'POST':
        form = PlaceToGetForm(instance=place)
    else:
        form = PlaceToGetForm(data=request.POST, instance=place)
        if form.is_valid():
            form.save()
            return redirect('order_options')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'place': place,
    }
    return render(request, 'service/edit_placetoget.html', context)


def delete_placetoget(request, placetoget_id):
    """A view for deleting the chosen placetoget object and rendering the page telling
    the delete process has gone successfully."""

    check_super_user(request)

    place = get_object_or_404(PlaceToGet, pk=placetoget_id)
    try:
        place.delete()
    except ProtectedError:
        return render(request, 'service/not_delete_placetoget.html')
    else:
        return render(request, 'service/placetoget_deleted.html')


def check_staff_info(request):
    """A view providing the content for the page for checking information on the staff."""

    check_super_user(request)

    staff_info = Workforce.objects.all()
    list_of_dicts = get_name_dicts(staff_info)
    staff_num = len(staff_info)

    if request.method != 'POST':
        form = WorkforceForm()
    else:
        form = WorkforceForm(data=request.POST)
        if form.is_valid():
            new_info = form.save(commit=False)
            if match_with_existing_names(list_of_dicts, new_info):
                form.add_error('name', "")
                form.add_error('surname', "")
                form.add_error('middle_name', "")
                messages.error(request, "Kiritilgan ism, familiya va sharif bo'yicha ma'lumotlar mavjud!")
            else:
                new_info.save()
                return redirect('check_staff_info')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'staff_info': staff_info,
        'staff_num': staff_num,
    }
    return render(request, 'service/check_staff_info.html', context)


def edit_staff_info(request, workforce_id):
    """A view providing the content for the page for editing the chosen information on an employee."""

    check_super_user(request)

    staff_info = Workforce.objects.all()
    list_of_dicts = get_name_dicts(staff_info)

    employee_info = get_object_or_404(Workforce, pk=workforce_id)

    if request.method != 'POST':
        form = WorkforceForm(instance=employee_info)
    else:
        form = WorkforceForm(data=request.POST, instance=employee_info)
        if form.is_valid():
            edited_info = form.save(commit=False)
            name_changed = 'name' in form.changed_data
            surname_changed = 'surname' in form.changed_data
            middle_name_changed = 'middle_name' in form.changed_data
            array = [name_changed, surname_changed, middle_name_changed]
            if not form.has_changed():
                return redirect('check_staff_info')
            elif form.has_changed() and True not in array:
                edited_info.save()
                return redirect('check_staff_info')
            elif True in array and match_with_existing_names(list_of_dicts, edited_info):
                form.add_error('name', "")
                form.add_error('surname', "")
                form.add_error('middle_name', "")
                messages.error(request, "Kiritilgan ism, familiya va sharif bo'yicha ma'lumotlar mavjud!")
            else:
                edited_info.save()
                return redirect('check_staff_info')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'employee_info': employee_info,
        'form': form,
    }
    return render(request, 'service/edit_staff_info.html', context)


def delete_staff_info(request, workforce_id):
    """A view for deleting the chosen information on an employee and rendering the page telling
    the delete process has gone successfully."""

    check_super_user(request)

    employee_info = get_object_or_404(Workforce, pk=workforce_id)
    employee_info.delete()
    return render(request, 'service/staff_info_deleted.html')


def check_books(request):
    """A view providing the content for checking the existing books in the library."""

    check_super_user(request)

    books = Book.objects.all()
    books_num = len(books)
    context = {
        'books': books,
        'books_num': books_num,
    }
    return render(request, 'service/check_books.html', context)


def add_book(request):
    """A view providing the content for the page for adding books to the library."""

    check_super_user(request)

    if request.method != 'POST':
        form = BookForm()
    else:
        form = BookForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('check_books')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
    }
    return render(request, 'service/add_book.html', context)


def edit_book(request, book_id):
    """A view providing the content for the page for editing book characters."""

    check_super_user(request)

    book = Book.objects.get(pk=book_id)

    if request.method != 'POST':
        form = BookForm(instance=book)
    else:
        form = BookForm(instance=book, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('check_books')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'book': book,
    }
    return render(request, 'service/edit_book.html', context)


def delete_book(request, book_id):
    """A view deleting the requested book and rendering the page telling user
    the delete process has gone successfully."""

    check_super_user(request)

    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return render(request, 'service/book_deleted.html')


def choose_ex_in(request):
    """A view rendering the page for choosing whether to make an expense or an income,
    and also to see other related information."""

    check_super_user(request)

    expenses = Expense.objects.all().order_by('-date_made')
    exp_num = len(expenses)
    incomes = Income.objects.all().order_by('-date_made')
    inc_num = len(incomes)
    accs = Account.objects.all()

    context = {
        'expenses': expenses,
        'exp_num': exp_num,
        'incomes': incomes,
        'inc_num': inc_num,
        'accs': accs,
    }
    return render(request, 'service/choose_ex_in.html', context)


def add_account(request):
    """A view providing the content for the page for creating money accounts."""

    check_super_user(request)
    accounts = Account.objects.all()
    list_of_accounts = []
    for account in accounts:
        list_of_accounts.append(account.name)

    if request.method != 'POST':
        form = AccountForm()
    else:
        form = AccountForm(data=request.POST)
        if form.is_valid():
            new_account = form.save(commit=False)
            item = str(find_string_in_list(new_account.name, list_of_accounts))
            if re.fullmatch(new_account.name, item, flags=re.IGNORECASE):
                form.add_error('name', "")
                messages.error(request, "Mavjud hisob kiritildi!")
            else:
                new_account.save()
                return redirect('choose_ex_in')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
    }
    return render(request, 'service/includes/add_account.html', context)


def edit_account(request, account_id):
    """A views providing the content for the page for editing the chosen account."""

    check_super_user(request)

    acc = get_object_or_404(Account, pk=account_id)
    name_of_account = acc.name
    accounts = Account.objects.all()
    list_of_accounts = []
    for account in accounts:
        list_of_accounts.append(account.name)

    if request.method != 'POST':
        form = AccountForm(instance=acc)
    else:
        form = AccountForm(data=request.POST, instance=acc)
        if form.is_valid():
            edited_account = form.save(commit=False)
            item = str(find_string_in_list(edited_account.name, list_of_accounts))
            if not form.has_changed():
                return redirect('choose_ex_in')
            elif re.fullmatch(edited_account.name, name_of_account, flags=re.IGNORECASE):
                edited_account.save()
                return redirect('choose_ex_in')
            elif re.fullmatch(edited_account.name, item, flags=re.IGNORECASE):
                form.add_error('name', "")
                messages.error(request, "Mavjud hisob kiritildi!")
            else:
                edited_account.save()
                return redirect('choose_ex_in')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'acc': acc,
    }
    return render(request, 'service/edit_account.html', context)


def delete_account(request, account_id):
    """A view for deleting the chosen account and rendering the page telling
    the delete process has gone successfully."""

    check_super_user(request)

    acc = get_object_or_404(Account, pk=account_id)
    try:
        acc.delete()
    except ProtectedError:
        return render(request, 'service/cannot_delete.html')
    else:
        return render(request, 'service/account_deleted.html')


def expense_categories(request):
    """A view providing the content for the page for creating categories for expenses."""

    check_super_user(request)

    cats = CategoryEx.objects.all()
    cats_num = len(cats)
    list_of_cats = []
    for cat in cats:
        list_of_cats.append(cat.category)

    if request.method != 'POST':
        form = CategoryExForm()
    else:
        form = CategoryExForm(data=request.POST)
        if form.is_valid():
            new_cat = form.save(commit=False)
            item = str(find_string_in_list(new_cat.category, list_of_cats))
            if re.fullmatch(new_cat.name, item, flags=re.IGNORECASE):
                form.add_error('category', "")
                messages.error(request, "Mavjud kategoriya kiritildi!")
            else:
                new_cat.save()
                return redirect('make_expense')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'cats': cats,
        'cats_num': cats_num,
    }
    return render(request, 'service/includes/expense_categories.html', context)


def edit_excategory(request, excategory_id):
    """A view providing the content for the page for editing the expense categories."""

    check_super_user(request)

    cat = get_object_or_404(CategoryEx, pk=excategory_id)
    name_of_cat = cat.category
    cats = CategoryEx.objects.all()
    list_of_cats = []
    for a_cat in cats:
        list_of_cats.append(a_cat.category)

    if request.method != 'POST':
        form = CategoryExForm(instance=cat)
    else:
        form = CategoryExForm(data=request.POST, instance=cat)
        if form.is_valid():
            edited_cat = form.save(commit=False)
            item = str(find_string_in_list(edited_cat.category, list_of_cats))
            if not form.has_changed():
                return redirect('expense_categories')
            elif re.fullmatch(edited_cat.category, name_of_cat, flags=re.IGNORECASE):
                edited_cat.save()
                return redirect('expense_categories')
            elif re.fullmatch(edited_cat.category, item, flags=re.IGNORECASE):
                form.add_error('category', "")
                messages.error(request, "Mavjud kategoriya kiritildi!")
            else:
                edited_cat.save()
                return redirect('expense_categories')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'cat': cat,
    }
    return render(request, 'service/edit_excategory.html', context)


def delete_excategory(request, excategory_id):
    """A view for deleting the chosen expense category object and rendering the page telling
    the delete process has gone successfully."""

    check_super_user(request)

    cat = get_object_or_404(CategoryEx, pk=excategory_id)
    try:
        cat.delete()
    except ProtectedError:
        return render(request, 'service/not_delete_excat.html')
    else:
        return render(request, 'service/excat_deleted.html')


def expense_subcats(request):
    """A view providing the content for the page for creating subcategories for expenses."""

    check_super_user(request)

    subcats = SubCategoryEx.objects.all()
    subcats_num = len(subcats)
    list_of_subcats = []
    for subcat in subcats:
        list_of_subcats.append(subcat.subcategory)

    if request.method != 'POST':
        form = SubCategoryExForm()
    else:
        form = SubCategoryExForm(data=request.POST)
        if form.is_valid():
            new_subcat = form.save(commit=False)
            item = str(find_string_in_list(new_subcat.subcategory, list_of_subcats))
            if re.fullmatch(new_subcat.subcategory, item, flags=re.IGNORECASE):
                form.add_error('subcategory', "")
                messages.error(request, "Mavjud quyi kategoriya kiritildi!")
            else:
                new_subcat.save()
                return redirect('make_expense')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'subcats': subcats,
        'subcats_num': subcats_num,
    }
    return render(request, 'service/includes/expense_subcats.html', context)


def edit_exsubcat(request, exsubcategory_id):
    """A view providing the content for the page for editing the expense subcategories."""

    check_super_user(request)

    subcat = get_object_or_404(SubCategoryEx, pk=exsubcategory_id)
    name_of_subcat = subcat.subcategory
    subcats = SubCategoryEx.objects.all()
    list_of_subcats = []
    for a_subcat in subcats:
        list_of_subcats.append(a_subcat.subcategory)

    if request.method != 'POST':
        form = SubCategoryExForm(instance=subcat)
    else:
        form = SubCategoryExForm(data=request.POST, instance=subcat)
        if form.is_valid():
            edited_subcat = form.save(commit=False)
            item = str(find_string_in_list(edited_subcat.subcategory, list_of_subcats))
            if not form.has_changed():
                return redirect('expense_subcats')
            elif re.fullmatch(edited_subcat.subcategory, name_of_subcat, flags=re.IGNORECASE):
                edited_subcat.save()
                return redirect('expense_subcats')
            elif re.fullmatch(edited_subcat.subcategory, item, flags=re.IGNORECASE):
                form.add_error('subcategory', "")
                messages.error(request, "Mavjud quyi kategoriya kiritildi!")
            else:
                edited_subcat.save()
                return redirect('expense_subcats')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'subcat': subcat,
    }
    return render(request, 'service/edit_exsubcat.html', context)


def delete_exsubcat(request, exsubcategory_id):
    """A view for deleting the chosen expense subcategory object and rendering the page telling
    the delete process has gone successfully."""

    check_super_user(request)

    subcat = get_object_or_404(SubCategoryEx, pk=exsubcategory_id)
    try:
        subcat.delete()
    except ProtectedError:
        return render(request, 'service/not_delete_exsubcat.html')
    else:
        return render(request, 'service/exsubcat_deleted.html')


def income_categories(request):
    """A view providing the content for the page for creating categories for incomes."""

    check_super_user(request)

    cats = CategoryIn.objects.all()
    cats_num = len(cats)
    list_of_cats = []
    for cat in cats:
        list_of_cats.append(cat.category)

    if request.method != 'POST':
        form = CategoryInForm()
    else:
        form = CategoryInForm(data=request.POST)
        if form.is_valid():
            new_cat = form.save(commit=False)
            item = str(find_string_in_list(new_cat.category, list_of_cats))
            if re.fullmatch(new_cat.category, item, flags=re.IGNORECASE):
                form.add_error('category', "Ushbu kategoriya mavjud!")
                messages.error(request, "Mavjud kategoriya kiritildi!")
            else:
                new_cat.save()
                return redirect('make_income')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'cats': cats,
        'cats_num': cats_num,
    }
    return render(request, 'service/includes/income_categories.html', context)


def edit_incategory(request, incategory_id):
    """A view providing the content for the page for editing the income categories."""

    check_super_user(request)

    cat = get_object_or_404(CategoryIn, pk=incategory_id)
    name_of_cat = cat.category
    cats = CategoryIn.objects.all()
    list_of_cats = []
    for a_cat in cats:
        list_of_cats.append(a_cat.category)

    if request.method != 'POST':
        form = CategoryInForm(instance=cat)
    else:
        form = CategoryInForm(data=request.POST, instance=cat)
        if form.is_valid():
            edited_cat = form.save(commit=False)
            item = str(find_string_in_list(edited_cat.category, list_of_cats))
            if not form.has_changed():
                return redirect('income_categories')
            elif re.fullmatch(edited_cat.category, name_of_cat, flags=re.IGNORECASE):
                edited_cat.save()
                return redirect('income_categories')
            elif re.fullmatch(edited_cat.category, item, flags=re.IGNORECASE):
                form.add_error('category', "")
                messages.error(request, "Mavjud kategoriya kiritildi!")
            else:
                edited_cat.save()
                return redirect('income_categories')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'cat': cat,
    }
    return render(request, 'service/edit_incategory.html', context)


def delete_incategory(request, incategory_id):
    """A view for deleting the chosen income category object and rendering the page telling
    the delete process has gone successfully."""

    check_super_user(request)

    cat = get_object_or_404(CategoryIn, pk=incategory_id)
    try:
        cat.delete()
    except ProtectedError:
        return render(request, 'service/not_delete_incat.html')
    else:
        return render(request, 'service/incat_deleted.html')


def income_subcats(request):
    """A view providing the content for the page for creating subcategories for incomes."""

    check_super_user(request)

    subcats = SubCategoryIn.objects.all()
    subcats_num = len(subcats)
    list_of_subcats = []
    for subcat in subcats:
        list_of_subcats.append(subcat.subcategory)

    if request.method != 'POST':
        form = SubCategoryInForm()
    else:
        form = SubCategoryInForm(data=request.POST)
        if form.is_valid():
            new_subcat = form.save(commit=False)
            item = str(find_string_in_list(new_subcat.subcategory, list_of_subcats))
            if re.fullmatch(new_subcat.subcategory, item, flags=re.IGNORECASE):
                form.add_error('subcategory', "")
                messages.error(request, "Mavjud quyi kategoriya kiritildi!")
            else:
                new_subcat.save()
                return redirect('make_income')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'subcats': subcats,
        'subcats_num': subcats_num,
    }
    return render(request, 'service/includes/income_subcats.html', context)


def edit_insubcat(request, insubcategory_id):
    """A view providing the content for the page for editing the income subcategories."""

    check_super_user(request)

    subcat = get_object_or_404(SubCategoryIn, pk=insubcategory_id)
    name_of_subcat = subcat.subcategory
    subcats = SubCategoryIn.objects.all()
    list_of_subcats = []
    for a_subcat in subcats:
        list_of_subcats.append(a_subcat.subcategory)

    if request.method != 'POST':
        form = SubCategoryInForm(instance=subcat)
    else:
        form = SubCategoryInForm(data=request.POST, instance=subcat)
        if form.is_valid():
            edited_subcat = form.save(commit=False)
            item = str(find_string_in_list(edited_subcat.subcategory, list_of_subcats))
            if not form.has_changed():
                return redirect('income_subcats')
            elif re.fullmatch(edited_subcat.subcategory, name_of_subcat, flags=re.IGNORECASE):
                edited_subcat.save()
                return redirect('income_subcats')
            elif re.fullmatch(edited_subcat.subcategory, item, flags=re.IGNORECASE):
                form.add_error('subcategory', "")
                messages.error(request, "Mavjud quyi kategoriya kiritildi!")
            else:
                edited_subcat.save()
                return redirect('income_subcats')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'subcat': subcat,
    }
    return render(request, 'service/edit_insubcat.html', context)


def delete_insubcat(request, insubcategory_id):
    """A view for deleting the chosen income subcategory object and rendering the page telling
    the delete process has gone successfully."""

    check_super_user(request)

    subcat = get_object_or_404(SubCategoryIn, pk=insubcategory_id)
    try:
        subcat.delete()
    except ProtectedError:
        return render(request, 'service/not_delete_insubcat.html')
    else:
        return render(request, 'service/insubcat_deleted.html')


def make_expense(request):
    """A view providing the content for the page for making expenses."""

    check_super_user(request)

    if request.method != 'POST':
        form = ExpenseForm()
    else:
        form = ExpenseForm(data=request.POST)
        if form.is_valid():
            new_expense = form.save(commit=False)
            acc = Account.objects.get(pk=new_expense.account.pk)
            exp = acc.means.amount - new_expense.amount.amount
            acc.means.amount = exp
            acc.save()
            new_expense.save()
            return redirect('choose_ex_in')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
    }
    return render(request, 'service/make_expense.html', context)


def edit_expense(request, expense_id):
    """A view providing the content for the page for editing the chosen expense."""

    check_super_user(request)

    expense = get_object_or_404(Expense, pk=expense_id)
    initial_val = expense.amount.amount

    if request.method != 'POST':
        form = ExpenseForm(instance=expense)
    else:
        form = ExpenseForm(data=request.POST, instance=expense)
        if form.is_valid():
            edited_ex = form.save(commit=False)
            edited_val = edited_ex.amount.amount
            if edited_val == initial_val:
                pass
            elif edited_val > initial_val:
                gap = edited_val - initial_val
                acc = get_object_or_404(Account, pk=edited_ex.account.pk)
                new_val = acc.means.amount - gap
                acc.means.amount = new_val
                acc.save()
            elif edited_val < initial_val:
                gap = initial_val - edited_val
                acc = get_object_or_404(Account, pk=edited_ex.account.pk)
                new_val = acc.means.amount + gap
                acc.means.amount = new_val
                acc.save()
            edited_ex.save()
            return redirect('choose_ex_in')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'expense': expense,
    }
    return render(request, 'service/edit_expense.html', context)


def delete_expense(request, expense_id):
    """A view for deleting the chosen expense object and rendering the page telling
    the delete process has gone successfully."""

    check_super_user(request)

    expense = get_object_or_404(Expense, pk=expense_id)
    acc = get_object_or_404(Account, pk=expense.account.pk)
    changed_amount = acc.means.amount + expense.amount.amount
    acc.means.amount = changed_amount
    acc.save()
    expense.delete()
    return render(request, 'service/expense_deleted.html')


def make_income(request):
    """A view providing the content for the page for making incomes."""

    check_super_user(request)

    if request.method != 'POST':
        form = IncomeForm()
    else:
        form = IncomeForm(data=request.POST)
        if form.is_valid():
            new_income = form.save(commit=False)
            acc = Account.objects.get(pk=new_income.account.pk)
            inc = acc.means.amount + new_income.amount.amount
            acc.means.amount = inc
            acc.save()
            new_income.save()
            return redirect('choose_ex_in')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
    }
    return render(request, 'service/make_income.html', context)


def edit_income(request, income_id):
    """A view providing the content for the page for editing the chosen income."""

    check_super_user(request)

    income = get_object_or_404(Income, pk=income_id)
    initial_val = income.amount.amount

    if request.method != 'POST':
        form = IncomeForm(instance=income)
    else:
        form = IncomeForm(data=request.POST, instance=income)
        if form.is_valid():
            edited_income = form.save(commit=False)
            edited_val = edited_income.amount.amount
            if edited_val == initial_val:
                pass
            elif edited_val > initial_val:
                gap = edited_val - initial_val
                acc = get_object_or_404(Account, pk=edited_income.account.pk)
                new_val = acc.means.amount + gap
                acc.means.amount = new_val
                acc.save()
            elif edited_val < initial_val:
                gap = initial_val - edited_val
                acc = get_object_or_404(Account, pk=edited_income.account.pk)
                new_val = acc.means.amount - gap
                acc.means.amount = new_val
                acc.save()
            edited_income.save()
            return redirect('choose_ex_in')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'income': income,
    }
    return render(request, 'service/edit_income.html', context)


def delete_income(request, income_id):
    """A view for deleting the chosen income object and rendering the page telling
    the delete process has gone successfully."""

    check_super_user(request)

    income = get_object_or_404(Income, pk=income_id)
    acc = get_object_or_404(Account, pk=income.account.pk)
    changed_amount = acc.means.amount - income.amount.amount
    acc.means.amount = changed_amount
    acc.save()
    income.delete()
    return render(request, 'service/income_deleted.html')


def make_transaction(request):
    """A view providing the content for the page for making transactions between money accounts."""

    check_super_user(request)

    transfers = Transaction.objects.all()
    transfers_num = len(transfers)

    if request.method != 'POST':
        form = TransactionForm()
    else:
        form = TransactionForm(data=request.POST)
        if form.is_valid():
            new_transaction = form.save(commit=False)
            acc1 = get_object_or_404(Account, pk=new_transaction.acc_1.pk)
            acc2 = get_object_or_404(Account, pk=new_transaction.acc_2.pk)
            if acc1.means.amount == 0:
                messages.error(request, "Hisobda mablag' mavjud emas!")
                return redirect('make_transaction')
            elif new_transaction.acc_1 == new_transaction.acc_2:
                messages.error(request, "Iltimos ikkita turli hisoblarni tanlang!")
                return redirect('make_transaction')
            elif acc1.means.amount < 0 or acc1.means.amount < new_transaction.amount.amount:
                messages.error(request, "Hisobda mablag' yetarli emas!")
                return redirect('make_transaction')
            else:
                changed_value1 = acc1.means.amount - new_transaction.amount.amount
                changed_value2 = acc2.means.amount + new_transaction.amount.amount
                acc1.means.amount = changed_value1
                acc2.means.amount = changed_value2
                acc1.save()
                acc2.save()
                form.save()
                return redirect('choose_ex_in')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'transfers': transfers,
        'transfers_num': transfers_num,
    }
    return render(request, 'service/includes/make_transaction.html', context)


def edit_transaction(request, transaction_id):
    """A view providing the content for the page for editing the chosen transaction."""

    check_super_user(request)

    transfer = get_object_or_404(Transaction, pk=transaction_id)
    initial_val = transfer.amount.amount

    if request.method != 'POST':
        form = TransactionForm(instance=transfer)
    else:
        form = TransactionForm(data=request.POST, instance=transfer)
        if form.is_valid():
            edited_transfer = form.save(commit=False)
            edited_val = edited_transfer.amount.amount
            if edited_val == initial_val:
                pass
            elif edited_val > initial_val:
                gap = edited_val - initial_val
                acc1 = get_object_or_404(Account, pk=edited_transfer.acc_1.pk)
                acc2 = get_object_or_404(Account, pk=edited_transfer.acc_2.pk)
                new_val1 = acc1.means.amount - gap
                new_val2 = acc2.means.amount + gap
                acc1.means.amount = new_val1
                acc2.means.amount = new_val2
                acc1.save()
                acc2.save()
            elif edited_val < initial_val:
                gap = initial_val - edited_val
                acc1 = get_object_or_404(Account, pk=edited_transfer.acc_1.pk)
                acc2 = get_object_or_404(Account, pk=edited_transfer.acc_2.pk)
                new_val1 = acc1.means.amount + gap
                new_val2 = acc2.means.amount - gap
                acc1.means.amount = new_val1
                acc2.means.amount = new_val2
                acc1.save()
                acc2.save()
            edited_transfer.save()
            return redirect('make_transaction')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'transfer': transfer,
    }
    return render(request, 'service/edit_transaction.html', context)


def delete_transaction(request, transaction_id):
    """A view for deleting the chosen transaction object and rendering the page telling
    the delete process has gone successfully."""

    check_super_user(request)

    transfer = get_object_or_404(Transaction, pk=transaction_id)
    acc1 = get_object_or_404(Account, pk=transfer.acc_1.pk)
    acc2 = get_object_or_404(Account, pk=transfer.acc_2.pk)
    changed_value1 = acc1.means.amount + transfer.amount.amount
    changed_value2 = acc2.means.amount - transfer.amount.amount
    acc1.means.amount = changed_value1
    acc2.means.amount = changed_value2
    acc1.save()
    acc2.save()
    transfer.delete()
    return render(request, 'service/transaction_deleted.html')


def check_blogposts(request):
    """A view providing the content for the page for checking the existing blog posts."""

    check_super_user(request)

    posts = BlogPost.objects.all().order_by('-date_published')
    posts_num = len(posts)
    context = {
        'posts': posts,
        'posts_num': posts_num,
    }
    return render(request, 'service/check_blogposts.html', context)


def add_blogpost(request):
    """A view providing the content for the page for adding blog posts."""

    check_super_user(request)

    if request.method != 'POST':
        form = BlogPostForm()
    else:
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.publisher = request.user
            new_post.save()
            return redirect('check_blogposts')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
    }
    return render(request, 'service/add_blogpost.html', context)


def edit_blogpost(request, blogpost_id):
    """A view providing the content for the page for editing the chosen blog post."""

    check_super_user(request)

    blogpost = BlogPost.objects.get(pk=blogpost_id)

    if request.method != 'POST':
        form = BlogPostForm(instance=blogpost)
    else:
        form = BlogPostForm(instance=blogpost, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('check_blogposts')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'blogpost': blogpost,
    }
    return render(request, 'service/edit_blogpost.html', context)


def delete_blogpost(request, blogpost_id):
    """A view for deleting the chosen blog post object and rendering the page telling
    the delete process has gone successfully."""

    check_super_user(request)

    post = get_object_or_404(BlogPost, pk=blogpost_id)
    post.delete()
    return render(request, 'service/blogpost_deleted.html')


def check_contacts(request):
    """A view providing the content for the page for checking contact inquires made by users."""

    check_super_user(request)

    contacts = Contact.objects.all().order_by('-date_made')
    contacts_num = len(contacts)
    context = {
        'contacts': contacts,
        'contacts_num': contacts_num,
    }
    return render(request, 'service/check_contacts.html', context)


def ask_del_contact(request, contact_id):
    """A view rendering the page asking the admin whether they are sure about deleting the contact."""

    check_super_user(request)

    cont = get_object_or_404(Contact, pk=contact_id)
    context = {
        'contact': cont,
    }
    return render(request, 'service/ask_del_contact.html', context)


def delete_contact(request, contact_id):
    """A view for deleting the chosen contact object and rendering the page telling
    the delete process has gone successfully."""

    check_super_user(request)

    cont = get_object_or_404(Contact, pk=contact_id)
    cont.delete()
    return render(request, 'service/contact_deleted.html')


def pricing(request):
    """A view providing the content for the page for either adding or checking out_prices."""

    check_super_user(request)

    # Dictionary versions of the below objects are got to check whether there exist duplicates of objects
    # If so the admin is warned as it may raise unwanted exceptions

    binding_prices = BindingPrice.objects.all().order_by('date')
    binding_prices_array = get_price_dicts(binding_prices)

    if find_duplicates(binding_prices_array):
        messages.warning(request,
                         "DIQQAT! Ulash narxlari bo'limida farqsiz o'zaro mos tushadigan ma'lumotlar topildi! "
                         "Bu xatoliklarga sabab bo'lishi mumkin.")

    color_prices = ColorPrice.objects.all().order_by('date')
    color_prices_array = get_color_price_dicts(color_prices)

    if find_duplicates(color_prices_array):
        messages.warning(request,
                         "DIQQAT! Rang narxlari bo'limida farqsiz o'zaro mos tushadigan ma'lumotlar topildi! "
                         "Bu xatoliklarga sabab bo'lishi mumkin.")

    cover_prices = CoverPrice.objects.all().order_by('date')
    cover_prices_array = get_price_dicts(cover_prices)

    if find_duplicates(cover_prices_array):
        messages.warning(request,
                         "DIQQAT! Muqova narxlari bo'limida farqsiz o'zaro mos tushadigan ma'lumotlar topildi! "
                         "Bu xatoliklarga sabab bo'lishi mumkin.")

    glue_prices = GluePrice.objects.all().order_by('date')
    glue_prices_array = get_price_dicts(glue_prices)

    if find_duplicates(glue_prices_array):
        messages.warning(request,
                         "DIQQAT! Yelim narxlari bo'limida farqsiz o'zaro mos tushadigan ma'lumotlar topildi! "
                         "Bu xatoliklarga sabab bo'lishi mumkin.")

    out_prices = OuterPrice.objects.all().order_by('date')
    out_price_dates = get_price_dates(out_prices)

    if find_duplicates(out_price_dates):
        messages.warning(request,
                         "DIQQAT! Tashqi xarajatlar va foyda bo'limida farqsiz o'zaro mos tushadigan ma'lumotlar "
                         "topildi! Bu xatoliklarga sabab bo'lishi mumkin.")

    page_prices = PagePrice.objects.all().order_by('date')
    page_prices_array = get_price_dicts(page_prices)

    if find_duplicates(page_prices_array):
        messages.warning(request,
                         "DIQQAT! Bir bet uchun narxlar bo'limida farqsiz o'zaro mos tushadigan ma'lumotlar topildi! "
                         "Bu xatoliklarga sabab bo'lishi mumkin.")

    paper_prices = PaperPrice.objects.all().order_by('date')
    paper_prices_array = get_price_dicts(paper_prices)

    if find_duplicates(paper_prices_array):
        messages.warning(request,
                         "DIQQAT! Qog'oz narxlari bo'limida farqsiz o'zaro mos tushadigan ma'lumotlar topildi! "
                         "Bu xatoliklarga sabab bo'lishi mumkin.")
    ring_prices = RingPrice.objects.all().order_by('date')
    ring_prices_array = get_price_dicts(ring_prices)

    if find_duplicates(ring_prices_array):
        messages.warning(request,
                         "DIQQAT! Prujina narxlari bo'limida farqsiz o'zaro mos tushadigan ma'lumotlar topildi! "
                         "Bu xatoliklarga sabab bo'lishi mumkin.")

    yarn_prices = YarnPrice.objects.all().order_by('date')
    yarn_prices_array = get_price_dicts(yarn_prices)

    if find_duplicates(yarn_prices_array):
        messages.warning(request,
                         "DIQQAT! Ip narxlari bo'limida farqsiz o'zaro mos tushadigan ma'lumotlar topildi! "
                         "Bu xatoliklarga sabab bo'lishi mumkin.")

    context = {
        'binding_prices': binding_prices,
        'color_prices': color_prices,
        'cover_prices': cover_prices,
        'glue_prices': glue_prices,
        'out_prices': out_prices,
        'page_prices': page_prices,
        'paper_prices': paper_prices,
        'ring_prices': ring_prices,
        'yarn_prices': yarn_prices,
    }
    return render(request, 'service/pricing.html', context)


def page_price(request):
    """A view providing the content for the page for adding page prices."""

    check_super_user(request)

    page_prices = PagePrice.objects.all()
    list_of_dicts = get_price_dicts(page_prices)

    if request.method != 'POST':
        form = PagePriceForm()
    else:
        form = PagePriceForm(data=request.POST)
        if form.is_valid():
            new_price = form.save(commit=False)
            if match_with_existing(list_of_dicts, new_price):
                form.add_error('date', "")
                form.add_error('type', "")
                form.add_error('size', "")
                messages.error(request, "Kiritilgan sana, tur va o'lcham bo'yicha narx mavjud!")
            else:
                try:
                    def_or_redef_page_price(new_price)
                except Http404:
                    return render(request, 'service/external_prices_insufficient.html')
                except RequestAborted:
                    return render(request, 'service/multiple_objects_3.html')
                new_price.save()
                return redirect('pricing')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
    }
    return render(request, 'service/page_price.html', context)


def edit_page_price(request, pageprice_id):
    """A view providing the content for the page for editing the chosen page price."""

    check_super_user(request)

    page_prices = PagePrice.objects.all()
    list_of_dicts = get_price_dicts(page_prices)

    p_price = get_object_or_404(PagePrice, pk=pageprice_id)

    if request.method != 'POST':
        form = PagePriceForm(instance=p_price)
    else:
        form = PagePriceForm(data=request.POST, instance=p_price)
        if form.is_valid():
            edited_price = form.save(commit=False)
            if not form.has_changed():
                return redirect('pricing')
            elif match_with_existing(list_of_dicts, edited_price):
                form.add_error('date', "")
                form.add_error('type', "")
                form.add_error('size', "")
                messages.error(request, "Kiritilgan sana, tur va o'lcham bo'yicha narx mavjud!")
            else:
                try:
                    def_or_redef_page_price(edited_price)
                except Http404:
                    return render(request, 'service/external_prices_insufficient.html')
                except RequestAborted:
                    return render(request, 'service/multiple_objects_3.html')
                edited_price.save()
                return redirect('pricing')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'p_price': p_price,
    }
    return render(request, 'service/edit_page_price.html', context)


def delete_page_price(request, pageprice_id):
    """A view for deleting the chosen page price object and rendering the page telling
    the delete process has gone successfully."""

    check_super_user(request)

    p_price = get_object_or_404(PagePrice, pk=pageprice_id)
    p_price.delete()
    return render(request, 'service/page_price_deleted.html')


def binding(request):
    """A view providing the content for the page for either adding or checking binding prices."""

    check_super_user(request)

    binding_prices = BindingPrice.objects.all()
    list_of_price_dicts = get_price_dicts(binding_prices)

    if request.method != 'POST':
        form = BindingPriceForm()
    else:
        form = BindingPriceForm(data=request.POST)
        if form.is_valid():
            new_price = form.save(commit=False)
            if match_with_existing(list_of_price_dicts, new_price):
                form.add_error('date', "")
                form.add_error('type', "")
                form.add_error('size', "")
                messages.error(request, "Kiritilgan sana, tur va o'lcham bo'yicha narx mavjud!")
            else:
                try:
                    def_or_redef_binding_price(new_price)
                except Http404:
                    return render(request, 'service/external_prices_donotexist.html')
                except RequestAborted:
                    return render(request, 'service/multiple_objects_1.html')
                else:
                    new_price.save()
                    return redirect('pricing')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri kiritildi!")

    context = {
        'form': form,
    }
    return render(request, 'service/binding.html', context)


def edit_binding_price(request, bindingprice_id):
    """A view providing the content for the page for editing the chosen binding price object."""

    check_super_user(request)

    binding_prices = BindingPrice.objects.all()
    list_of_price_dicts = get_price_dicts(binding_prices)

    binding_price = get_object_or_404(BindingPrice, pk=bindingprice_id)

    if request.method != 'POST':
        form = BindingPriceForm(instance=binding_price)
    else:
        form = BindingPriceForm(data=request.POST, instance=binding_price)
        if form.is_valid():
            edited_price = form.save(commit=False)
            if not form.has_changed():
                return redirect('pricing')
            elif match_with_existing(list_of_price_dicts, edited_price):
                form.add_error('date', "")
                form.add_error('type', "")
                form.add_error('size', "")
                messages.error(request, "Kiritilgan sana, tur va o'lcham bo'yicha narx mavjud!")
            else:
                try:
                    def_or_redef_binding_price(edited_price)
                except Http404:
                    return render(request, 'service/external_prices_donotexist.html')
                except RequestAborted:
                    return render(request, 'service/multiple_objects_1.html')
                else:
                    edited_price.save()
                    return redirect('pricing')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'binding_price': binding_price,
    }
    return render(request, 'service/edit_binding_price.html', context)


def delete_binding_price(request, bindingprice_id):
    """A view for deleting the chosen binding price object and rendering the page telling
    the delete process has gone successfully."""

    check_super_user(request)

    binding_price = get_object_or_404(BindingPrice, pk=bindingprice_id)
    binding_price.delete()
    return render(request, 'service/binding_deleted.html')


def ring_price(request):
    """A view providing the content for the page for adding ring prices."""

    check_super_user(request)

    ring_prices = RingPrice.objects.all()
    list_of_dicts = get_price_dicts(ring_prices)

    if request.method != 'POST':
        form = RingPriceForm()
    else:
        form = RingPriceForm(data=request.POST)
        if form.is_valid():
            new_price = form.save(commit=False)
            if match_with_existing(list_of_dicts, new_price):
                form.add_error('date', "")
                form.add_error('type', "")
                form.add_error('size', "")
                messages.error(request, "Kiritilgan sana, tur va o'lcham bo'yicha narx mavjud!")
            else:
                new_price.save()
                return redirect('pricing')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
    }
    return render(request, 'service/ring_price.html', context)


def edit_ring_price(request, ringprice_id):
    """A view providing the content for the page for editing the chosen ring price."""

    check_super_user(request)

    ring_prices = RingPrice.objects.all()
    list_of_dicts = get_price_dicts(ring_prices)

    r_price = get_object_or_404(RingPrice, pk=ringprice_id)

    if request.method != 'POST':
        form = RingPriceForm(instance=r_price)
    else:
        form = RingPriceForm(data=request.POST, instance=r_price)
        if form.is_valid():
            edited_price = form.save(commit=False)
            date_changed = 'date' in form.changed_data
            type_changed = 'type' in form.changed_data
            size_changed = 'size' in form.changed_data
            price_changed = 'price' in form.changed_data
            array = [date_changed, type_changed, size_changed]
            if not form.has_changed():
                return redirect('pricing')
            elif form.has_changed() and True not in array and price_changed:
                edited_price.save()
                return redirect('pricing')
            elif match_with_existing(list_of_dicts, edited_price):
                form.add_error('date', "")
                form.add_error('type', "")
                form.add_error('size', "")
                messages.error(request, "Kiritilgan sana, tur va o'lcham bo'yicha narx mavjud!")
            else:
                edited_price.save()
                return redirect('pricing')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'r_price': r_price,
    }
    return render(request, 'service/edit_ring_price.html', context)


def delete_ring_price(request, ringprice_id):
    """A view for deleting the chosen RingPrice price object and rendering the page telling
    the delete process has gone successfully."""

    check_super_user(request)

    r_price = get_object_or_404(RingPrice, pk=ringprice_id)
    r_price.delete()
    return render(request, 'service/ring_price_deleted.html')


def color_price(request):
    """A view providing the content for the page for adding color prices."""

    check_super_user(request)

    color_prices = ColorPrice.objects.all()
    list_of_dicts = get_color_price_dicts(color_prices)

    if request.method != 'POST':
        form = ColorPriceForm()
    else:
        form = ColorPriceForm(data=request.POST)
        if form.is_valid():
            new_price = form.save(commit=False)
            if match_color_price_with_existing(list_of_dicts, new_price):
                form.add_error('date', "")
                form.add_error('color', "")
                form.add_error('size', "")
                messages.error(request, "Kiritilgan sana, rang va kitob o'lchami bo'yicha narx mavjud!")
            else:
                new_price.save()
                return redirect('pricing')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
    }
    return render(request, 'service/color_price.html', context)


def edit_color_price(request, colorprice_id):
    """A view providing the content for the page for editing the chosen color price."""

    check_super_user(request)

    color_prices = ColorPrice.objects.all()
    list_of_dicts = get_color_price_dicts(color_prices)

    c_price = get_object_or_404(ColorPrice, pk=colorprice_id)
    initial_price_val = c_price.price

    if request.method != 'POST':
        form = ColorPriceForm(instance=c_price)
    else:
        form = ColorPriceForm(data=request.POST, instance=c_price)
        if form.is_valid():
            edited_price = form.save(commit=False)
            edited_price_val = edited_price.price
            date_changed = 'date' in form.changed_data
            color_changed = 'color' in form.changed_data
            size_changed = 'size' in form.changed_data
            price_changed = 'price' in form.changed_data
            array = [date_changed, color_changed, size_changed]
            if not form.has_changed():
                return redirect('pricing')
            elif form.has_changed() and True not in array and price_changed:
                try:
                    # Find the correlating page price and change its value according to the changes made in color price
                    # Also abort the request in case duplicate objects found
                    find_and_change_3(edited_price=edited_price,
                                      edited_price_val=edited_price_val,
                                      initial_price_val=initial_price_val)
                except RequestAborted:
                    return render(request, 'service/multiple_objects_4.html')
                else:
                    edited_price.save()
                    return redirect('pricing')
            elif match_color_price_with_existing(list_of_dicts, edited_price):
                form.add_error('date', "")
                form.add_error('color', "")
                form.add_error('size', "")
                messages.error(request, "Kiritilgan sana, rang va o'lcham bo'yicha narx mavjud!")
            else:
                try:
                    # Find the correlating page price and change its value according to the changes made in color price
                    # Also abort the request in case duplicate objects found
                    find_and_change_3(edited_price=edited_price,
                                      edited_price_val=edited_price_val,
                                      initial_price_val=initial_price_val)
                except RequestAborted:
                    return render(request, 'service/multiple_objects_4.html')
                else:
                    edited_price.save()
                    return redirect('pricing')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'c_price': c_price,
        'form': form,
    }
    return render(request, 'service/edit_color_price.html', context)


def delete_color_price(request, colorprice_id):
    """A view for deleting the chosen color price object and rendering the page telling
    the delete process has gone successfully."""

    check_super_user(request)

    c_price = get_object_or_404(ColorPrice, pk=colorprice_id)

    page_prices = PagePrice.objects.filter(date=c_price.date,
                                           type__icontains=c_price.color,
                                           size=c_price.size)

    # Get the list of page price dictionaries to check whether there are no duplicates
    list_of_dicts = get_price_dicts(page_prices)

    if not page_prices:
        c_price.delete()
        return render(request, 'service/color_price_deleted.html')
    elif find_duplicates(list_of_dicts):
        return render(request, 'service/multiple_objects_4.html')
    else:
        context = {
            'page_prices': page_prices,
        }
        return render(request, 'service/not_delete_color_price.html', context)


def cover_price(request):
    """A view providing the content for the page for adding cover prices."""

    check_super_user(request)

    cover_prices = CoverPrice.objects.all()
    list_of_dicts = get_price_dicts(cover_prices)

    if request.method != 'POST':
        form = CoverPriceForm()
    else:
        form = CoverPriceForm(data=request.POST)
        if form.is_valid():
            new_price = form.save(commit=False)
            if match_with_existing(list_of_dicts, new_price):
                form.add_error('date', "")
                form.add_error('type', "")
                form.add_error('size', "")
                messages.error(request, "Kiritilgan sana, tur va o'lcham bo'yicha narx mavjud!")
            else:
                new_price.save()
                return redirect('pricing')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
    }
    return render(request, 'service/cover_price.html', context)


def edit_cover_price(request, coverprice_id):
    """A view providing the content for the page for editing the chosen cover price."""

    check_super_user(request)

    cover_prices = CoverPrice.objects.all()
    list_of_dicts = get_price_dicts(cover_prices)

    c_price = get_object_or_404(CoverPrice, pk=coverprice_id)
    initial_price_val = c_price.price

    if request.method != 'POST':
        form = CoverPriceForm(instance=c_price)
    else:
        form = CoverPriceForm(data=request.POST, instance=c_price)
        if form.is_valid():
            edited_price = form.save(commit=False)
            edited_price_val = edited_price.price
            date_changed = 'date' in form.changed_data
            type_changed = 'type' in form.changed_data
            size_changed = 'size' in form.changed_data
            price_changed = 'price' in form.changed_data
            array = [date_changed, type_changed, size_changed]
            if not form.has_changed():
                return redirect('pricing')
            elif form.has_changed() and True not in array and price_changed:
                try:
                    # Find the correlating binding price and change its price according to the changes made
                    # in cover price
                    # Also abort the request in case duplicate objects found
                    find_and_change_1(edited_price=edited_price,
                                      edited_price_val=edited_price_val,
                                      initial_price_val=initial_price_val)
                except RequestAborted:
                    return render(request, 'service/multiple_objects_2.html')
                else:
                    edited_price.save()
                    return redirect('pricing')
            elif match_with_existing(list_of_dicts, edited_price):
                form.add_error('date', "")
                form.add_error('type', "")
                form.add_error('size', "")
                messages.error(request, "Kiritilgan sana, tur va o'lcham bo'yicha narx mavjud!")
            else:
                try:
                    # Find the correlating binding price and change its price according to the changes made
                    # in cover price
                    # Also abort the request in case duplicate objects found
                    find_and_change_1(edited_price=edited_price,
                                      edited_price_val=edited_price_val,
                                      initial_price_val=initial_price_val)
                except RequestAborted:
                    return render(request, 'service/multiple_objects_2.html')
                else:
                    edited_price.save()
                    return redirect('pricing')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'c_price': c_price,
        'form': form,
        'lst': list_of_dicts
    }
    return render(request, 'service/edit_cover_price.html', context)


def delete_cover_price(request, coverprice_id):
    """A view for deleting the chosen cover price object and rendering the page telling
    the delete process has gone successfully."""

    check_super_user(request)

    c_price = get_object_or_404(CoverPrice, pk=coverprice_id)

    try:
        binding_price = None
        if c_price.type == "Plastik prujinali ulash uchun":
            try:
                binding_price = BindingPrice.objects.get(date=c_price.date,
                                                         type="Plastik prujinalash",
                                                         size=c_price.size)
            except ObjectDoesNotExist:
                raise Http404
            except MultipleObjectsReturned:
                raise RequestAborted
        elif c_price.type == "Metal prujinali ulash uchun":
            try:
                binding_price = BindingPrice.objects.get(date=c_price.date,
                                                         type="Metal prujinalash",
                                                         size=c_price.size)
            except ObjectDoesNotExist:
                raise Http404
            except MultipleObjectsReturned:
                raise RequestAborted
        elif c_price.type == "Yelimli ulash uchun (Yumshoq)":
            try:
                binding_price = BindingPrice.objects.get(date=c_price.date,
                                                         type="Yumshoq muqovali yelimlash",
                                                         size=c_price.size)
            except ObjectDoesNotExist:
                raise Http404
            except MultipleObjectsReturned:
                raise RequestAborted
        elif c_price.type == "Yelimli ulash uchun (Qattiq)":
            try:
                binding_price = BindingPrice.objects.get(date=c_price.date,
                                                         type="Qattiq muqovali yelimlash",
                                                         size=c_price.size)
            except ObjectDoesNotExist:
                raise Http404
            except MultipleObjectsReturned:
                raise RequestAborted
    except Http404:
        c_price.delete()
        return render(request, 'service/cover_price_deleted.html')
    except RequestAborted:
        return render(request, 'service/multiple_objects_2.html')
    else:
        context = {
            'binding_price': binding_price,
        }
        return render(request, 'service/not_delete_cover_price.html', context)


def glue_price(request):
    """A view providing the content for the page for adding glue prices."""

    check_super_user(request)

    glue_prices = GluePrice.objects.all()
    list_of_dicts = list(get_price_dicts(glue_prices))

    if request.method != 'POST':
        form = GluePriceForm()
    else:
        form = GluePriceForm(data=request.POST)
        if form.is_valid():
            new_price = form.save(commit=False)
            if match_with_existing(list_of_dicts, new_price):
                form.add_error('date', "")
                form.add_error('type', "")
                form.add_error('size', "")
                messages.error(request, "Kiritilgan sana, tur va o'lcham bo'yicha narx mavjud!")
            else:
                new_price.save()
                return redirect('pricing')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
    }
    return render(request, 'service/glue_price.html', context)


def edit_glue_price(request, glueprice_id):
    """A view providing the content for the page for editing the chosen glue price."""

    check_super_user(request)

    glue_prices = GluePrice.objects.all()
    list_of_dicts = list(get_price_dicts(glue_prices))

    g_price = get_object_or_404(GluePrice, pk=glueprice_id)
    initial_price_val = g_price.price

    if request.method != 'POST':
        form = GluePriceForm(instance=g_price)
    else:
        form = GluePriceForm(data=request.POST, instance=g_price)
        if form.is_valid():
            edited_price = form.save(commit=False)
            edited_price_val = edited_price.price
            date_changed = 'date' in form.changed_data
            type_changed = 'type' in form.changed_data
            size_changed = 'size' in form.changed_data
            price_changed = 'price' in form.changed_data
            array = [date_changed, type_changed, size_changed]
            if not form.has_changed():
                return redirect('pricing')
            elif form.has_changed() and True not in array and price_changed:
                try:
                    # Find the correlating binding price and change its price according to the changes made
                    # in glue price
                    # Also abort the request in case duplicate objects found
                    find_and_change_2(edited_price=edited_price,
                                      edited_price_val=edited_price_val,
                                      initial_price_val=initial_price_val)
                except RequestAborted:
                    return render(request, 'service/multiple_objects_2.html')
                else:
                    edited_price.save()
                    return redirect('pricing')
            elif match_with_existing(list_of_dicts, edited_price):
                form.add_error('date', "")
                form.add_error('type', "")
                form.add_error('size', "")
                messages.error(request, "Kiritilgan sana, tur va kitob o'lchami bo'yicha narxlar mavjud!")
            else:
                try:
                    # Find the correlating binding price and change its price according to the changes made
                    # in glue price
                    # Also abort the request in case duplicate objects found
                    find_and_change_2(edited_price=edited_price,
                                      edited_price_val=edited_price_val,
                                      initial_price_val=initial_price_val)
                except RequestAborted:
                    return render(request, 'service/multiple_objects_2.html')
                else:
                    edited_price.save()
                    return redirect('pricing')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'g_price': g_price,
    }
    return render(request, 'service/edit_glue_price.html', context)


def delete_glue_price(request, glueprice_id):
    """A view for deleting the chosen glue price object and rendering the page telling
    the delete process has gone successfully."""

    check_super_user(request)

    g_price = get_object_or_404(GluePrice, pk=glueprice_id)

    try:
        sg_binding_price = None
        hg_binding_price = None
        raise_404_1 = None
        raise_404_2 = None
        deny_request_1 = None
        deny_request_2 = None
        try:
            sg_binding_price = BindingPrice.objects.get(date=g_price.date,
                                                        type="Yumshoq muqovali yelimlash",
                                                        size=g_price.size)
        except ObjectDoesNotExist:
            raise_404_1 = True
        except MultipleObjectsReturned:
            deny_request_1 = True
        else:
            raise_404_1 = False
            deny_request_1 = False
        try:
            hg_binding_price = BindingPrice.objects.get(date=g_price.date,
                                                        type="Qattiq muqovali yelimlash",
                                                        size=g_price.size)
        except ObjectDoesNotExist:
            raise_404_2 = True
        except MultipleObjectsReturned:
            deny_request_2 = True
        else:
            raise_404_2 = False
            deny_request_2 = False
        if raise_404_1 and raise_404_2:
            raise Http404
        if deny_request_1 or deny_request_2:
            raise RequestAborted
        elif deny_request_1 and deny_request_2:
            raise RequestAborted
    except Http404:
        g_price.delete()
        return render(request, 'service/glue_price_deleted.html')
    except RequestAborted:
        return render(request, 'service/multiple_objects_2.html')
    else:
        context = {
            'sg_binding_price': sg_binding_price,
            'hg_binding_price': hg_binding_price,
        }
        return render(request, 'service/not_delete_glue_price.html', context)


def paper_price(request):
    """A view providing the content for the page for adding paper prices."""

    check_super_user(request)

    paper_prices = PaperPrice.objects.all()
    list_of_dicts = get_price_dicts(paper_prices)

    if request.method != 'POST':
        form = PaperPriceForm()
    else:
        form = PaperPriceForm(data=request.POST)
        if form.is_valid():
            new_price = form.save(commit=False)
            if match_with_existing(list_of_dicts, new_price):
                form.add_error('date', "")
                form.add_error('type', "")
                form.add_error('size', "")
                messages.error(request, "Kiritilgan sana, tur va o'lcham bo'yicha narx mavjud!")
            else:
                new_price.save()
                return redirect('pricing')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
    }
    return render(request, 'service/paper_price.html', context)


def edit_paper_price(request, paperprice_id):
    """A view providing the content for the page for editing the chosen paper price."""

    check_super_user(request)

    paper_prices = PaperPrice.objects.all()
    list_of_dicts = get_price_dicts(paper_prices)

    p_price = get_object_or_404(PaperPrice, pk=paperprice_id)
    initial_price_val = p_price.price

    if request.method != 'POST':
        form = PaperPriceForm(instance=p_price)
    else:
        form = PaperPriceForm(data=request.POST, instance=p_price)
        if form.is_valid():
            edited_price = form.save(commit=False)
            edited_price_val = edited_price.price
            date_changed = 'date' in form.changed_data
            type_changed = 'type' in form.changed_data
            size_changed = 'size' in form.changed_data
            price_changed = 'price' in form.changed_data
            array = [date_changed, type_changed, size_changed]
            if not form.has_changed():
                return redirect('pricing')
            elif form.has_changed() and True not in array and price_changed:
                try:
                    # Find the correlating page price and change its value according to the changes made in paper price
                    # Also abort the request in case duplicate objects found
                    find_and_change_3(edited_price=edited_price,
                                      edited_price_val=edited_price_val,
                                      initial_price_val=initial_price_val)
                except RequestAborted:
                    return render(request, 'service/multiple_objects_4.html')
                else:
                    edited_price.save()
                    return redirect('pricing')
            elif match_with_existing(list_of_dicts, edited_price):
                form.add_error('date', "")
                form.add_error('type', "")
                form.add_error('size', "")
                messages.error(request, "Kiritilgan sana, tur ba o'lcham bo'yicha narx mavjud!")
            else:
                try:
                    # Find the correlating page price and change its value according to the changes made in paper price
                    # Also Abort the request in case duplicate objects found
                    find_and_change_3(edited_price=edited_price,
                                      edited_price_val=edited_price_val,
                                      initial_price_val=initial_price_val)
                except RequestAborted:
                    return render(request, 'service/multiple_objects_4.html')
                else:
                    edited_price.save()
                    return redirect('pricing')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'p_price': p_price,
    }
    return render(request, 'service/edit_paper_price.html', context)


def delete_paper_price(request, paperprice_id):
    """A view for deleting the chosen paper price object and rendering the page telling
    the delete process has gone successfully."""

    check_super_user(request)

    p_price = get_object_or_404(PaperPrice, pk=paperprice_id)

    page_prices = PagePrice.objects.filter(date=p_price.date,
                                           type__icontains=p_price.type,
                                           size=p_price.size)

    # Get the list of page prices to check whether there are no duplicates
    list_of_dicts = get_price_dicts(page_prices)

    if not page_prices:
        p_price.delete()
        return render(request, 'service/paper_price_deleted.html')
    elif find_duplicates(list_of_dicts):
        return render(request, 'service/multiple_objects_4.html')
    else:
        context = {
            'page_prices': page_prices,
        }
        return render(request, 'service/not_delete_paper_price.html', context)


def yarn_price(request):
    """A view providing the content for the page for adding yarn prices."""

    check_super_user(request)

    yarn_prices = YarnPrice.objects.all()
    list_of_dicts = get_price_dicts(yarn_prices)

    if request.method != 'POST':
        form = YarnPriceForm()
    else:
        form = YarnPriceForm(data=request.POST)
        if form.is_valid():
            new_price = form.save(commit=False)
            if match_with_existing(list_of_dicts, new_price):
                form.add_error('date', "")
                form.add_error('type', "")
                form.add_error('size', "")
                messages.error(request, "Kiritilgan sana, tur va kitob o'lchami bo'yicha narx mavjud!")
            else:
                new_price.save()
                return redirect('pricing')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
    }
    return render(request, 'service/yarn_price.html', context)


def edit_yarn_price(request, yarnprice_id):
    """A view providing the content for the page for editing the chosen yarn price."""

    check_super_user(request)

    yarn_prices = YarnPrice.objects.all()
    list_of_dicts = get_price_dicts(yarn_prices)

    y_price = get_object_or_404(YarnPrice, pk=yarnprice_id)
    initial_price_val = y_price.price

    if request.method != 'POST':
        form = YarnPriceForm(instance=y_price)
    else:
        form = YarnPriceForm(data=request.POST, instance=y_price)
        if form.is_valid():
            edited_price = form.save(commit=False)
            edited_price_val = edited_price.price
            date_changed = 'date' in form.changed_data
            type_changed = 'type' in form.changed_data
            size_changed = 'size' in form.changed_data
            price_changed = 'price' in form.changed_data
            array = [date_changed, type_changed, size_changed]
            if not form.has_changed():
                return redirect('pricing')
            elif form.has_changed() and True not in array and price_changed:
                try:
                    # Find the correlating binding price and change its price according to the changes made
                    # in yarn price
                    # Also abort the request in case duplicate objects found
                    find_and_change_2(edited_price=edited_price,
                                      edited_price_val=edited_price_val,
                                      initial_price_val=initial_price_val)
                except RequestAborted:
                    return render(request, 'service/multiple_objects_2.html')
                else:
                    edited_price.save()
                    return redirect('pricing')
            elif match_with_existing(list_of_dicts, edited_price):
                form.add_error('date', "")
                form.add_error('type', "")
                form.add_error('size', "")
                messages.error(request, "Kiritilgan sana, tur va o'lcham bo'yicha narx mavjud!")
            else:
                try:
                    # Find the correlating binding price and change its price according to the changes made
                    # in yarn price
                    # Also abort the request in case duplicate objects found
                    find_and_change_2(edited_price=edited_price,
                                      edited_price_val=edited_price_val,
                                      initial_price_val=initial_price_val)
                except RequestAborted:
                    return render(request, 'service/multiple_objects_2.html')
                else:
                    edited_price.save()
                    return redirect('pricing')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'y_price': y_price,
    }
    return render(request, 'service/edit_yarn_price.html', context)


def delete_yarn_price(request, yarnprice_id):
    """A view for deleting the chosen yarn price object and rendering the page telling
    the delete process has gone successfully."""

    check_super_user(request)

    y_price = get_object_or_404(YarnPrice, pk=yarnprice_id)

    if y_price.type == "Yupqa":
        try:
            binding_price = get_object_or_404(BindingPrice,
                                              date=y_price.date,
                                              type="Yumshoq muqovali yelimlash",
                                              size=y_price.size)
        except Http404:
            y_price.delete()
            return render(request, 'service/yarn_price_deleted.html')
        except MultipleObjectsReturned:
            return render(request, 'service/multiple_objects_2.html')
        else:
            context = {
                'binding_price': binding_price,
            }
            return render(request, 'service/not_delete_yarn_price.html', context)
    elif y_price.type == "O'rtacha":
        try:
            binding_price = get_object_or_404(BindingPrice,
                                              date=y_price.date,
                                              type="Qattiq muqovali yelimlash",
                                              size=y_price.size)
        except Http404:
            y_price.delete()
            return render(request, 'service/yarn_price_deleted.html')
        except MultipleObjectsReturned:
            return render(request, 'service/multiple_objects_2.html')
        else:
            context = {
                'binding_price': binding_price,
            }
            return render(request, 'service/not_delete_yarn_price.html', context)
    # For now, we can delete prices of any other types of yarn as no other binding types are provided by the service
    else:
        y_price.delete()
        return render(request, 'service/yarn_price_deleted.html')


def outer_prices(request):
    """A view providing the content for the page for adding outer prices."""

    check_super_user(request)

    outer_expenses = OuterPrice.objects.all()
    list_of_dates = get_price_dates(outer_expenses)

    if request.method != 'POST':
        form = OuterPriceForm()
    else:
        form = OuterPriceForm(data=request.POST)
        if form.is_valid():
            new_price = form.save(commit=False)
            if match_with_existing_dates(list_of_dates, new_price):
                form.add_error('date', "")
                messages.error(request, "Kiritilgan sana bo'yicha narxlar mavjud!")
            else:
                new_price.save()
                return redirect('pricing')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
    }
    return render(request, 'service/outer_prices.html', context)


def edit_outer_prices(request, outerprice_id):
    """A view providing the content for the page for editing the chosen outer prices."""

    check_super_user(request)

    outer_expenses = OuterPrice.objects.all()
    list_of_dates = get_price_dates(outer_expenses)

    out_prices = get_object_or_404(OuterPrice, pk=outerprice_id)
    initial_workforce = out_prices.workforce_expenses.amount
    initial_packaging = out_prices.packaging_expenses.amount
    initial_printer = out_prices.printer_expenses.amount

    if request.method != 'POST':
        form = OuterPriceForm(instance=out_prices)
    else:
        form = OuterPriceForm(data=request.POST, instance=out_prices)
        if form.is_valid():
            edited_prices = form.save(commit=False)
            edited_workforce = edited_prices.workforce_expenses.amount
            edited_packaging = edited_prices.packaging_expenses.amount
            edited_printer = edited_prices.printer_expenses.amount
            date_changed = 'date' in form.changed_data
            staple_changed = 'staple_price' in form.changed_data
            packaging_changed = 'packaging_expenses' in form.changed_data
            workforce_changed = 'workforce_expenses' in form.changed_data
            printer_changed = 'printer_expenses' in form.changed_data
            bprice_to_be_changed = [staple_changed, packaging_changed, workforce_changed]
            if not form.has_changed():
                return redirect('pricing')
            elif form.has_changed() and date_changed is False:
                try:
                    if True in bprice_to_be_changed and printer_changed is False:
                        outex_edited_edit_bprice(initial_packaging=initial_packaging,
                                                 initial_workforce=initial_workforce,
                                                 edited_packaging=edited_packaging,
                                                 edited_prices=edited_prices,
                                                 edited_workforce=edited_workforce)
                    elif printer_changed is True and True not in bprice_to_be_changed:
                        outex_edited_edit_pprice(initial_printer_exp=initial_printer,
                                                 edited_prices=edited_prices,
                                                 edited_printer_exp=edited_printer)
                    else:
                        outex_edited_edit_bprice(initial_packaging=initial_packaging,
                                                 initial_workforce=initial_workforce,
                                                 edited_packaging=edited_packaging,
                                                 edited_prices=edited_prices,
                                                 edited_workforce=edited_workforce)
                        outex_edited_edit_pprice(initial_printer_exp=initial_printer,
                                                 edited_prices=edited_prices,
                                                 edited_printer_exp=edited_printer)
                except RequestAborted:
                    return render(request, 'service/multiple_objects_2.html')
                else:
                    edited_prices.save()
                    return redirect('pricing')
            elif str(edited_prices.date) in list_of_dates:
                form.add_error('date', "")
                messages.error(request, "Kiritilgan sana bo'yicha narxlar mavjud!")
            else:
                try:
                    if True in bprice_to_be_changed and printer_changed is False:
                        outex_edited_edit_bprice(initial_packaging=initial_packaging,
                                                 initial_workforce=initial_workforce,
                                                 edited_packaging=edited_packaging,
                                                 edited_prices=edited_prices,
                                                 edited_workforce=edited_workforce)
                    elif printer_changed is True and True not in bprice_to_be_changed:
                        outex_edited_edit_pprice(initial_printer_exp=initial_printer,
                                                 edited_prices=edited_prices,
                                                 edited_printer_exp=edited_printer)
                    else:
                        outex_edited_edit_bprice(initial_packaging=initial_packaging,
                                                 initial_workforce=initial_workforce,
                                                 edited_packaging=edited_packaging,
                                                 edited_prices=edited_prices,
                                                 edited_workforce=edited_workforce)
                        outex_edited_edit_pprice(initial_printer_exp=initial_printer,
                                                 edited_prices=edited_prices,
                                                 edited_printer_exp=edited_printer)
                except RequestAborted:
                    return render(request, 'service/multiple_objects_2.html')
                else:
                    edited_prices.save()
                    return redirect('pricing')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'out_prices': out_prices,
    }
    return render(request, 'service/edit_outer_prices.html', context)


def delete_outer_prices(request, outerprice_id):
    """A view for deleting the chosen outer prices object and rendering the page telling
    the delete process has gone successfully."""

    check_super_user(request)

    out_prices = get_object_or_404(OuterPrice, pk=outerprice_id)

    binding_prices = BindingPrice.objects.filter(date=out_prices.date)
    page_prices = PagePrice.objects.filter(date=out_prices.date)

    # Get the list of binding and page price dictionaries to check whether there are no duplicates
    list_of_binding_price_dicts = get_price_dicts(binding_prices)
    list_of_page_price_dicts = get_price_dicts(page_prices)

    if not binding_prices and not page_prices:
        out_prices.delete()
        return render(request, 'service/outer_prices_deleted.html')
    elif find_duplicates(list_of_binding_price_dicts) or find_duplicates(list_of_page_price_dicts):
        return render(request, 'service/multiple_objects_2.html')
    else:
        context = {
            'binding_prices': binding_prices,
            'page_prices': page_prices,
        }
        return render(request, 'service/not_delete_out_exps.html', context)


def check_printer_info(request):
    """A view providing the content for the page for checking and adding information on printers."""

    check_super_user(request)

    printer_info = Printer.objects.all()
    printers_num = len(printer_info)
    list_of_printers = get_printer_brand_dicts(printer_info)

    printer_refill_page_counts = RefillAndPageCount.objects.all()
    list_of_printer_names = get_printer_names(printer_refill_page_counts)

    if find_duplicates(list_of_printers):
        messages.warning(request,
                         "DIQQAT! Printerlar haqidagi ma'lumotlar "
                         "bo'limida markasi va modeli bir xil bo'lgan "
                         "ma'lumotlar topildi! Bu xatoliklarga sabab bo'lishi mumkin.")

    if find_duplicates(list_of_printer_names):
        messages.warning(request,
                         "DIQQAT! Printer ranggini to'lidirish va chop etilgan betlar soni haqidagi ma'lumotlar "
                         "bo'limida bir printerga ikki marta ma'lumot berilgani aniqlandi! "
                         "Bu xatoliklarga sabab bo'lishi mumkin.")

    if request.method != 'POST':
        form = PrinterForm()
    else:
        form = PrinterForm(data=request.POST)
        if form.is_valid():
            new_info = form.save(commit=False)
            if not form.has_changed():
                return redirect('check_printer_info')
            elif match_with_existing_printers(list_of_printers, new_info):
                new_info.model += f' ({int(printers_num) + 1})'
                new_info.save()
                return redirect('check_printer_info')
            else:
                new_info.save()
                return redirect('check_printer_info')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'printer_info': printer_info,
        'printers_num': printers_num,
        'printer_refill_page_counts': printer_refill_page_counts,
    }
    return render(request, 'service/check_printer_info.html', context)


def edit_printer_info(request, printer_id):
    """A view providing the content for the page for editing the chosen printer information."""

    check_super_user(request)

    printer_info_queryset = Printer.objects.all()
    list_of_dicts = get_printer_brand_dicts(printer_info_queryset)

    printer_info = get_object_or_404(Printer, pk=printer_id)

    if request.method != 'POST':
        form = PrinterForm(instance=printer_info)
    else:
        form = PrinterForm(data=request.POST, instance=printer_info)
        if form.is_valid():
            edited_info = form.save(commit=False)
            brand_changed = 'brand' in form.changed_data
            model_changed = 'model' in form.changed_data
            if not form.has_changed():
                return redirect('check_printer_info')
            elif form.has_changed() and True not in [brand_changed, model_changed]:
                edited_info.save()
                return redirect('check_printer_info')
            elif match_with_existing_printers(list_of_dicts, edited_info):
                form.add_error('brand', "")
                form.add_error('model', "")
                messages.error(request, "Kiritilgan marka, model va uning raqami bo'yicha ma'lumotlar mavjud!")
            else:
                edited_info.save()
                return redirect('check_printer_info')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'printer_info': printer_info,
    }
    return render(request, 'service/edit_printer_info.html', context)


def delete_printer_info(request, printer_id):
    """A view for deleting the chosen printer information and rendering the page telling
    the delete process has gone successfully."""

    check_super_user(request)

    printer_info = get_object_or_404(Printer, pk=printer_id)

    try:
        printer_info.delete()
    except ProtectedError:
        return render(request, 'service/not_delete_printer_info.html')
    else:
        return render(request, 'service/printer_info_deleted.html')


def add_refill_page_count(request):
    """A view providing the content for the page for adding refill and page count information of printers."""

    check_super_user(request)

    counts = RefillAndPageCount.objects.all()
    list_of_printers = get_printer_names(counts)

    if request.method != 'POST':
        form = RefillAndPageCountForm()
    else:
        form = RefillAndPageCountForm(data=request.POST)
        if form.is_valid():
            new_info = form.save(commit=False)
            if str(new_info.printer) in list_of_printers:
                form.add_error('printer', "")
                messages.error(request,
                               "Ushbu bo'limda bir printer uchun bir marta ma'lumot kiritiladi!")
            else:
                try:
                    # Find the correlating printer information and change its CURRENT_PAGE_COUNT based on the newly
                    # added information to refill and page count
                    find_and_change_4(new_info=new_info)
                except Http404:
                    return render(request, 'service/printer_info_not_found.html')
                except RequestAborted:
                    return render(request, 'service/multiple_objects_5.html')
                else:
                    new_info.save()
                    return redirect('check_printer_info')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
    }
    return render(request, 'service/add_refill_page_count.html', context)


def edit_refill_page_count(request, refillandpagecount_id):
    """A view providing the content for the page for editing the chosen refill and page count information."""

    check_super_user(request)

    counts = RefillAndPageCount.objects.all()
    list_of_printers = get_printer_names(counts)

    info = get_object_or_404(RefillAndPageCount, pk=refillandpagecount_id)
    info_printed = info.printed

    if request.method != 'POST':
        form = RefillAndPageCountForm(instance=info)
    else:
        form = RefillAndPageCountForm(data=request.POST, instance=info)
        if form.is_valid():
            edited_info = form.save(commit=False)
            printer_changed = 'printer' in form.changed_data
            date_changed = 'last_refill' in form.changed_data
            if not form.has_changed():
                return redirect('check_printer_info')
            elif form.has_changed() and printer_changed is False:
                try:
                    # Find the correlating printer info and change its CURRENT_PAGE_COUNT based on the changes made
                    # in refill and page count
                    find_and_change_4(edited_info=edited_info,
                                      initial_count=info_printed,
                                      date_changed=date_changed)
                except Http404:
                    return render(request, 'service/printer_info_not_found.html')
                except RequestAborted:
                    return render(request, 'service/multiple_objects_5.html')
                else:
                    edited_info.save()
                    return redirect('check_printer_info')
            elif str(edited_info.printer) in list_of_printers:
                form.add_error('printer', "")
                messages.error(request, "Kiritilgan printer haqida ma'lumotlar mavjud!")
            else:
                try:
                    # Find the correlating printer info and change its CURRENT_PAGE_COUNT based on the changes made
                    # in refill and page count
                    find_and_change_4(edited_info=edited_info,
                                      initial_count=info_printed,
                                      date_changed=date_changed)
                except Http404:
                    return render(request, 'service/printer_info_not_found.html')
                except RequestAborted:
                    return render(request, 'service/multiple_objects_5.html')
                else:
                    edited_info.save()
                    return redirect('check_printer_info')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'info': info,
    }
    return render(request, 'service/edit_refill_page_count.html', context)


def delete_refill_page_count(request, refillandpagecount_id):
    """A view for deleting the chosen refill and page count information and rendering the page telling
    the delete process has gone successfully."""

    check_super_user(request)

    info = get_object_or_404(RefillAndPageCount, pk=refillandpagecount_id)
    info.delete()
    return render(request, 'service/refill_page_count_deleted.html')


def rtypes(request):
    """A view providing the content for the page for adding resource types."""

    check_super_user(request)

    types = RType.objects.all()
    types_num = len(types)
    list_of_types = []
    for a_type in types:
        list_of_types.append(a_type.type)

    if request.method != 'POST':
        form = RTypeForm()
    else:
        form = RTypeForm(data=request.POST)
        if form.is_valid():
            new_type = form.save(commit=False)
            item = str(find_string_in_list(new_type.type, list_of_types))
            if re.fullmatch(new_type.type, item, flags=re.IGNORECASE):
                form.add_error('type', "Ushbu resurs mavjud!")
                messages.error(request, "Mavjud resurs kiritildi!")
            else:
                new_type.save()
                return redirect('resources')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'types': types,
        'types_num': types_num,
    }
    return render(request, 'service/rtypes.html', context)


def edit_rtype(request, rtype_id):
    """A view providing the content for the page for editing the chosen resource type."""

    check_super_user(request)

    rtype = get_object_or_404(RType, pk=rtype_id)
    name_of_type = rtype.type
    types = RType.objects.all()
    list_of_types = []
    for a_type in types:
        list_of_types.append(a_type.type)

    if request.method != 'POST':
        form = RTypeForm(instance=rtype)
    else:
        form = RTypeForm(data=request.POST, instance=rtype)
        if form.is_valid():
            edited_type = form.save(commit=False)
            item = str(find_string_in_list(edited_type.type, list_of_types))
            if not form.has_changed():
                return redirect('rtypes')
            elif re.fullmatch(edited_type.type, name_of_type, flags=re.IGNORECASE):
                edited_type.save()
                return redirect('rtypes')
            elif re.fullmatch(edited_type.type, item, flags=re.IGNORECASE):
                form.add_error('type', "Ushbu resurs mavjud!")
                messages.error(request, "Mavjud resurs kiritildi!")
            else:
                edited_type.save()
                return redirect('rtypes')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'rtype': rtype,
    }
    return render(request, 'service/edit_rtype.html', context)


def delete_rtype(request, rtype_id):
    """A view providing the content for the page for deleting the chosen resource type."""

    check_super_user(request)

    rtype = get_object_or_404(RType, pk=rtype_id)
    try:
        rtype.delete()
    except ProtectedError:
        return render(request, 'service/not_delete_rtype.html')
    else:
        return render(request, 'service/rtype_deleted.html')


def resources(request):
    """A view providing the content for the page for checking/adding resources."""

    check_super_user(request)

    res_s = Resource.objects.all()
    rtype_objs = RType.objects.all()
    dicts = provide_dicts(rtype_objs)

    if request.method != 'POST':
        form = ResourceForm()
    else:
        form = ResourceForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('resources')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'dicts': dicts,
        'form': form,
        'res_s': res_s,
    }
    return render(request, 'service/resources.html', context)


def edit_resource(request, resource_id):
    """A view providing the content for the page for editing the chosen resource."""

    check_super_user(request)

    resource = get_object_or_404(Resource, pk=resource_id)
    rtype_objs = RType.objects.all()
    dicts = provide_dicts(rtype_objs)

    if request.method != 'POST':
        form = ResourceForm(instance=resource)
    else:
        form = ResourceForm(data=request.POST, instance=resource)
        if form.is_valid():
            form.save()
            return redirect('resources')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'dicts': dicts,
        'form': form,
        'resource': resource,
    }
    return render(request, 'service/edit_resource.html', context)


def delete_resource(request, resource_id):
    """A view for deleting the chosen resource object on creating a website and rendering the page telling
    the delete process has gone successfully."""

    check_super_user(request)

    resource = get_object_or_404(Resource, pk=resource_id)
    resource.delete()
    return render(request, 'service/resource_deleted.html')


def check_web_applies(request):
    """A view providing the content for the page for checking applications on creating a website."""

    check_super_user(request)

    applications = CreateSite.objects.all().order_by('-date_applied')
    app_num = len(applications)
    context = {
        'applications': applications,
        'app_num': app_num,
    }
    return render(request, 'service/check_web_applies.html', context)


def ask_del_webapp(request, createsite_id):
    """A view rendering the page asking the admin whether they are sure about deleting the application."""

    check_super_user(request)

    apply = get_object_or_404(CreateSite, pk=createsite_id)
    context = {
        'apply': apply,
    }
    return render(request, 'service/ask_del_webapp.html', context)


def del_webapp(request, createsite_id):
    """A view for deleting the chosen application object on creating a website and rendering the page telling
    the delete process has gone successfully."""

    check_super_user(request)

    apply = get_object_or_404(CreateSite, pk=createsite_id)
    apply.delete()
    return render(request, 'service/webapp_deleted.html')


def view_complaints(request):
    """A view providing the content for the page for checking the complaints."""

    check_super_user(request)

    complaints = Complaint.objects.all()
    complaints_num = len(complaints)
    context = {
        'complaints': complaints,
        'complaints_num': complaints_num,
    }
    return render(request, 'service/view_complaints.html', context)


def ask_del_complaint(request, complaint_id):
    """A view rendering the page asking the admin whether they are sure about deleting the complaint."""

    check_super_user(request)

    complaint = get_object_or_404(Complaint, pk=complaint_id)
    context = {
        'complaint': complaint,
    }
    return render(request, 'service/ask_del_complaint.html', context)


def delete_complaint(request, complaint_id):
    """A view for deleting the chosen complaint object and rendering the page telling
    the delete process has gone successfully."""

    check_super_user(request)

    complaint = get_object_or_404(Complaint, pk=complaint_id)
    complaint.delete()
    return render(request, 'service/complaint_deleted.html')


def check_news(request):
    """A view providing the content for the page for checking existing news."""

    check_super_user(request)

    news = News.objects.all().order_by('-date_added')
    news_num = len(news)
    context = {
        'news': news,
        'news_num': news_num,
    }
    return render(request, 'service/check_news.html', context)


def make_news(request):
    """A view providing the content for the page for announcing news."""

    check_super_user(request)

    if request.method != 'POST':
        form = NewsForm()
    else:
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            news.publisher = request.user
            news.save()
            return redirect('check_news')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
    }
    return render(request, 'service/make_news.html', context)


def edit_news(request, news_id):
    """A view providing the content for the page for editing the existing news."""

    check_super_user(request)

    news = News.objects.get(pk=news_id)

    if request.method != 'POST':
        form = NewsForm(instance=news)
    else:
        form = NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.publisher = request.user
            new_form.save()
            return redirect('check_news')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'news': news,
    }
    return render(request, 'service/edit_news.html', context)


def delete_news(request, news_id):
    """A view for deleting the chosen news object and rendering the page telling
    the delete process has gone successfully."""

    check_super_user(request)

    new = get_object_or_404(News, pk=news_id)
    new.delete()
    return render(request, 'service/news_deleted.html')


def ltypes(request):
    """A view providing the content for the page for checking and adding loss types."""

    check_super_user(request)

    types = LType.objects.all()
    types_num = len(types)
    list_of_types = []
    for a_type in types:
        list_of_types.append(a_type.type)

    if request.method != 'POST':
        form = LTypeForm()
    else:
        form = LTypeForm(data=request.POST)
        if form.is_valid():
            new_type = form.save(commit=False)
            item = str(find_string_in_list(new_type.type, list_of_types))
            if re.fullmatch(new_type.type, item, flags=re.IGNORECASE):
                form.add_error('type', "Ushbu zarar nomi mavjud!")
                messages.error(request, "Mavjud zarar nomi kiritildi!")
            else:
                new_type.save()
                return redirect('losses')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'types': types,
        'types_num': types_num,
    }
    return render(request, 'service/ltypes.html', context)


def edit_ltype(request, ltype_id):
    """A view providing the content for the page for editing the chosen loss type."""

    check_super_user(request)

    ltype = get_object_or_404(LType, pk=ltype_id)
    name_of_type = ltype.type
    types = LType.objects.all()
    list_of_types = []
    for a_type in types:
        list_of_types.append(a_type.type)

    if request.method != 'POST':
        form = LTypeForm(instance=ltype)
    else:
        form = LTypeForm(data=request.POST, instance=ltype)
        if form.is_valid():
            edited_type = form.save(commit=False)
            item = str(find_string_in_list(edited_type.type, list_of_types))
            if not form.has_changed():
                return redirect('ltypes')
            elif re.fullmatch(edited_type.type, name_of_type, flags=re.IGNORECASE):
                edited_type.save()
                return redirect('ltypes')
            elif re.fullmatch(edited_type.type, item, flags=re.IGNORECASE):
                form.add_error('type', "Ushbu zarar nomi mavjud!")
                messages.error(request, "Mavjud zarar nomi kiritildi!")
            else:
                edited_type.save()
                return redirect('ltypes')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'ltype': ltype,
    }
    return render(request, 'service/edit_ltype.html', context)


def delete_ltype(request, ltype_id):
    """A view for deleting the chosen loss type object and rendering the page telling
    the delete process has gone successfully."""

    check_super_user(request)

    ltype = get_object_or_404(LType, pk=ltype_id)
    try:
        ltype.delete()
    except ProtectedError:
        return render(request, 'service/not_delete_ltype.html')
    else:
        return render(request, 'service/ltype_deleted.html')


def losses(request):
    """A view providing the content for the page for checking and adding losses happened in the business."""

    check_super_user(request)

    the_losses = Loss.objects.all()
    losses_num = len(the_losses)
    types = LType.objects.all()
    dicts = provide_dicts(types)

    if request.method != 'POST':
        form = LossForm()
    else:
        form = LossForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('losses')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'dicts': dicts,
        'form': form,
        'losses': the_losses,
        'losses_num': losses_num,
    }
    return render(request, 'service/losses.html', context)


def edit_loss(request, loss_id):
    """A view providing the content for the page for editing the chosen loss."""

    check_super_user(request)

    loss = get_object_or_404(Loss, pk=loss_id)
    the_ltypes = LType.objects.all()
    dicts = provide_dicts(the_ltypes)

    if request.method != 'POST':
        form = LossForm(instance=loss)
    else:
        form = LossForm(data=request.POST, instance=loss)
        if form.is_valid():
            form.save()
            return redirect('losses')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'dicts': dicts,
        'form': form,
        'loss': loss,
    }
    return render(request, 'service/edit_loss.html', context)


def delete_loss(request, loss_id):
    """A view for deleting the chosen loss object and rendering the page telling
    the delete process has gone successfully."""

    check_super_user(request)

    loss = get_object_or_404(Loss, pk=loss_id)
    loss.delete()
    return render(request, 'service/loss_deleted.html')


# ========================================================================================================


def search(request):
    """A view providing the content for the search page to illustrate the results."""

    if request.method == 'GET':
        searched = request.GET.get('searched')
        books = Book.objects.filter(Q(name_coded__contains=searched) |
                                    Q(chars__contains=searched) |
                                    Q(category__contains=searched))
        news = News.objects.filter(Q(title__contains=searched) |
                                   Q(subtitle_1__contains=searched) |
                                   Q(subtitle_2__contains=searched) |
                                   Q(subtitle_3__contains=searched) |
                                   Q(short_body__contains=searched) |
                                   Q(body_1__contains=searched) |
                                   Q(body_2__contains=searched) |
                                   Q(body_3__contains=searched))
        posts = BlogPost.objects.filter(Q(title__contains=searched) |
                                        Q(subtitle_1__contains=searched) |
                                        Q(subtitle_2__contains=searched) |
                                        Q(subtitle_3__contains=searched) |
                                        Q(body_1__contains=searched) |
                                        Q(body_2__contains=searched) |
                                        Q(body_3__contains=searched))
        if re.fullmatch(searched, 'Buyurtma berish', flags=re.IGNORECASE):
            return redirect('order')
        elif re.fullmatch(searched, 'Shikoyat', flags=re.IGNORECASE):
            return redirect('complaint_category')
        elif re.fullmatch(searched, "Bog'lanish", flags=re.IGNORECASE):
            return redirect('contact')
        elif re.fullmatch(searched, 'Kutubxona', flags=re.IGNORECASE):
            return redirect('book_categories')
        elif re.fullmatch(searched, 'Yangiliklar', flags=re.IGNORECASE):
            return redirect('check_news')
        elif re.fullmatch(searched, 'Sayt yaratish', flags=re.IGNORECASE):
            return redirect('create_site')
        elif re.fullmatch(searched, 'Mening buyurtmalarim', flags=re.IGNORECASE):
            return redirect('myorders')
        elif re.fullmatch(searched, 'Maqolalar', flags=re.IGNORECASE):
            return redirect('blogposts')
        context = {
            'books': books,
            'news': news,
            'posts': posts,
            'searched': searched,
        }
        return render(request, 'service/search.html', context)
    else:
        return render(request, 'service/search.html')


def myorders(request):
    """A view providing the content of myorders page for users to see their own orders."""

    orders = Order.objects.filter(customer=request.user)

    for order in orders:
        check_user(request, order.customer)

    context = {
        'orders': orders,
    }
    return render(request, 'service/myorders.html', context)


def order_src(request):
    """A view rendering the page for choosing the source for ordering books."""

    return render(request, 'service/order_src.html')


def order_site(request):
    """A view providing the content for the page for making orders for the books in the library."""

    res = OrderOptions.objects.latest('date')
    places = PlaceToGet.objects.all()

    if request.method != 'POST':
        form = OrderSiteForm()
    else:
        form = OrderSiteForm(data=request.POST)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.customer = request.user
            new_order.save()
            return redirect('success_order')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'places': places,
        'res': res,
    }
    return render(request, 'service/order_site.html', context)


def order_users(request):
    """A view providing the content for the page for making orders for the books provided by users themselves."""

    res = OrderOptions.objects.latest('date')
    places = PlaceToGet.objects.all()

    if request.method != 'POST':
        form = OrderSelfForm()
    else:
        form = OrderSelfForm(data=request.POST)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.customer = request.user
            new_order.save()
            return redirect('success_order')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'places': places,
        'res': res,
    }
    return render(request, 'service/order_users.html', context)


def success_order(request):
    """A view rendering the content for the page which tells that the application has successfully been sent."""

    return render(request, 'service/success_order.html')


# ================================== assisting functions ==================================


def check_super_user(request):
    """An assisting function checking whether the user requesting the admin page is super user or not."""

    if request.user.is_superuser:
        pass
    else:
        raise Http404


def check_user(request, user):
    """An assisting function checking whether the user
    requesting particular objects is the owner of those objects or not."""

    if request.user == user:
        pass
    else:
        raise Http404


def edit_bprice(**kwargs):
    """An assisting function editing the binding price based on edited correlated price."""

    edited_price_val = kwargs['edited_price_val']
    initial_price_val = kwargs['initial_price_val']
    price_to_be_changed = kwargs['price_to_be_changed']

    if edited_price_val and initial_price_val and price_to_be_changed:
        if edited_price_val > initial_price_val:
            gap = edited_price_val.amount - initial_price_val.amount
            new_value = price_to_be_changed.price.amount + gap
            price_to_be_changed.price = new_value
            price_to_be_changed.save()
        elif edited_price_val.amount < initial_price_val.amount:
            gap = initial_price_val.amount - edited_price_val.amount
            new_value = price_to_be_changed.price.amount - gap
            price_to_be_changed.price = new_value
            price_to_be_changed.save()
        elif edited_price_val.amount == initial_price_val.amount:
            pass


def edit_pprice(**kwargs):
    """An assisting function editing the page price based on edited correlated price."""

    edited_price = kwargs['edited_price']
    edited_price_val = kwargs['edited_price_val']
    initial_price_val = kwargs['initial_price_val']
    price_to_be_changed = kwargs['price_to_be_changed']

    if edited_price and edited_price_val and initial_price_val and price_to_be_changed:
        if hasattr(edited_price, 'color') and str(edited_price.size) == 'A4':
            if edited_price_val > initial_price_val:
                gap = edited_price_val.amount - initial_price_val.amount
                price_to_be_changed.price = price_to_be_changed.price.amount + gap
                price_to_be_changed.save()
            elif edited_price_val.amount < initial_price_val.amount:
                gap = initial_price_val.amount - edited_price_val.amount
                price_to_be_changed.price = price_to_be_changed.price.amount - gap
                price_to_be_changed.save()
            elif edited_price_val.amount == initial_price_val.amount:
                pass
        elif hasattr(edited_price, 'type') and str(edited_price.size) == 'A3':
            if edited_price_val > initial_price_val:
                gap = edited_price_val.amount - initial_price_val.amount
                price_to_be_changed.price = price_to_be_changed.price.amount + gap
                price_to_be_changed.save()
            elif edited_price_val.amount < initial_price_val.amount:
                gap = initial_price_val.amount - edited_price_val.amount
                price_to_be_changed.price = price_to_be_changed.price.amount - gap
                price_to_be_changed.save()
            elif edited_price_val.amount == initial_price_val.amount:
                pass
        elif hasattr(edited_price, 'color') and str(edited_price.size) == 'A5':
            if edited_price_val > initial_price_val:
                gap = edited_price_val.amount - initial_price_val.amount
                new_value = price_to_be_changed.price.amount + gap
                price_to_be_changed.price = new_value
                price_to_be_changed.save()
            elif edited_price_val.amount < initial_price_val.amount:
                gap = initial_price_val.amount - edited_price_val.amount
                new_value = price_to_be_changed.price.amount - gap
                price_to_be_changed.price = new_value
                price_to_be_changed.save()
            elif edited_price_val.amount == initial_price_val.amount:
                pass
        elif hasattr(edited_price, 'type') and str(edited_price.size) == 'A4':
            if edited_price_val > initial_price_val:
                gap = edited_price_val.amount - initial_price_val.amount
                new_value = price_to_be_changed.price.amount + gap
                price_to_be_changed.price = new_value
                price_to_be_changed.save()
            elif edited_price_val.amount < initial_price_val.amount:
                gap = initial_price_val.amount - edited_price_val.amount
                new_value = price_to_be_changed.price.amount - gap
                price_to_be_changed.price = new_value
                price_to_be_changed.save()
            elif edited_price_val.amount == initial_price_val.amount:
                pass


def edit_printercount(accounted=None,
                      new_info=None,
                      edited_info=None,
                      initial_count=None,
                      count_to_be_changed=None):
    """

    An assisting function editing the printer count based on the correlated count.

    Accounted and new info attributes are used when a new count is added to the count information for printers.

    Edited info and initial info attributes are used when an existing count information is edited.

    An attribute count to be changed is used in both cases as it is the target to be changed.

    """

    if new_info is not None and accounted is False:
        count_to_be_changed.current_page_count += int(new_info.printed)
        count_to_be_changed.save()
    elif edited_info is not None and initial_count is not None:
        if int(edited_info.printed) > int(initial_count):
            gap = int(edited_info.printed) - int(initial_count)
            count_to_be_changed.current_page_count += int(gap)
            count_to_be_changed.save()
        elif int(edited_info.printed) < int(initial_count):
            gap = int(initial_count) - int(edited_info.printed)
            count_to_be_changed.current_page_count -= int(gap)
            count_to_be_changed.save()
    elif edited_info is not None and initial_count is None:
        count_to_be_changed.current_page_count += int(edited_info.printed)
        count_to_be_changed.save()


def def_or_redef_binding_price(price):
    """An assisting function defining or redefining the chosen binding price based on the prices of other resources,
    and outer expenses."""

    if price.type == "Plastik prujinalash":
        try:
            cov_price = CoverPrice.objects.get(date=price.date,
                                               type="Plastik prujinali ulash uchun",
                                               size=price.size)
            outer_expenses = OuterPrice.objects.get(date=price.date)
        except ObjectDoesNotExist:
            raise Http404
        except MultipleObjectsReturned:
            raise RequestAborted
        else:
            price.price = math.fsum([cov_price.price.amount,
                                     outer_expenses.workforce_expenses.amount,
                                     outer_expenses.packaging_expenses.amount])
    elif price.type == "Metal prujinalash":
        try:
            cov_price = CoverPrice.objects.get(date=price.date,
                                               type="Metal prujinali ulash uchun",
                                               size=price.size)
            outer_expenses = OuterPrice.objects.get(date=price.date)
        except ObjectDoesNotExist:
            raise Http404
        except MultipleObjectsReturned:
            raise RequestAborted
        else:
            price.price = math.fsum([cov_price.price.amount,
                                     outer_expenses.workforce_expenses.amount,
                                     outer_expenses.packaging_expenses.amount])
    elif price.type == "Yumshoq muqovali yelimlash":
        try:
            cov_price = CoverPrice.objects.get(date=price.date,
                                               type="Yelimli ulash uchun (Yumshoq)",
                                               size=price.size)
            g_price = GluePrice.objects.get(date=price.date,
                                            size=price.size)
            y_price = YarnPrice.objects.get(date=price.date,
                                            type="Yupqa",
                                            size=price.size)
            outer_expenses = OuterPrice.objects.get(date=price.date)
        except ObjectDoesNotExist:
            raise Http404
        except MultipleObjectsReturned:
            raise RequestAborted
        else:
            price.price = math.fsum([cov_price.price.amount,
                                     g_price.price.amount,
                                     y_price.price.amount,
                                     outer_expenses.workforce_expenses.amount,
                                     outer_expenses.packaging_expenses.amount])
    elif price.type == "Qattiq muqovali yelimlash":
        try:
            cov_price = CoverPrice.objects.get(date=price.date,
                                               type="Yelimli ulash uchun (Qattiq)",
                                               size=price.size)
            g_price = GluePrice.objects.get(date=price.date,
                                            size=price.size)
            y_price = YarnPrice.objects.get(date=price.date,
                                            type="O'rtacha",
                                            size=price.size)
            outer_expenses = OuterPrice.objects.get(date=price.date)
        except ObjectDoesNotExist:
            raise Http404
        except MultipleObjectsReturned:
            raise RequestAborted
        else:
            price.price = math.fsum([cov_price.price.amount,
                                     g_price.price.amount,
                                     y_price.price.amount,
                                     outer_expenses.workforce_expenses.amount,
                                     outer_expenses.packaging_expenses.amount])
    elif price.type == "Steplerlash":
        try:
            outer_expenses = OuterPrice.objects.get(date=price.date)
        except ObjectDoesNotExist:
            raise Http404
        except MultipleObjectsReturned:
            raise RequestAborted
        else:
            price.price = math.fsum([outer_expenses.staple_price.amount,
                                     outer_expenses.packaging_expenses.amount,
                                     outer_expenses.workforce_expenses.amount])

    return price


def def_or_redef_page_price(price):
    """An assisting function defining or redefining a price for a single page."""

    # PRICE parameter can take in either new price or edited price
    try:
        col_price = ColorPrice.objects.get(date=price.date,
                                           color__in=list(get_list_of_words_1(str(price.type))),
                                           size=price.size)
        pap_price = PaperPrice.objects.get(date=price.date,
                                           type__in=list(get_list_of_words_1(str(price.type))),
                                           size=price.size)
        outer_expenses = OuterPrice.objects.get(date=price.date)
        # Delivery and electricity expenses should be accounted while an order is being made
        printer_exp = outer_expenses.printer_expenses
    except ObjectDoesNotExist:
        raise Http404
    except MultipleObjectsReturned:
        raise RequestAborted
    else:
        if str(price.size) == 'A4':
            price.price = math.fsum([
                col_price.price.amount,
                pap_price.price.amount,
                printer_exp.amount,
            ])
        elif str(price.size) == 'A5':
            price.price = math.fsum([
                col_price.price.amount,
                pap_price.price.amount,
                printer_exp.amount / 2,
            ])

        return price


def find_and_change_1(**kwargs):
    """An assisting function retrieving the queried object and changing its value using EDIT_PRICE."""

    edited_price = kwargs['edited_price']
    edited_price_val = kwargs['edited_price_val']
    initial_price_val = kwargs['initial_price_val']

    if edited_price.type == "Plastik prujinali ulash uchun":
        try:
            pring_binding_price = BindingPrice.objects.get(date=edited_price.date,
                                                           type='Plastik prujinalash',
                                                           size=edited_price.size)
        except ObjectDoesNotExist:
            pass
        except MultipleObjectsReturned:
            raise RequestAborted
        else:
            edit_bprice(edited_price_val=edited_price_val,
                        initial_price_val=initial_price_val,
                        price_to_be_changed=pring_binding_price)
    elif edited_price.type == "Metal prujinali ulash uchun":
        try:
            mring_binding_price = BindingPrice.objects.get(date=edited_price.date,
                                                           type='Metal prujinalash',
                                                           size=edited_price.size)
        except ObjectDoesNotExist:
            pass
        except MultipleObjectsReturned:
            raise RequestAborted
        else:
            edit_bprice(edited_price_val=edited_price_val,
                        initial_price_val=initial_price_val,
                        price_to_be_changed=mring_binding_price)
    elif edited_price.type == "Yelimli ulash uchun (Yumshoq)":
        try:
            sg_binding_price = BindingPrice.objects.get(date=edited_price.date,
                                                        type='Yumshoq muqovali yelimlash',
                                                        size=edited_price.size)
        except ObjectDoesNotExist:
            pass
        except MultipleObjectsReturned:
            raise RequestAborted
        else:
            edit_bprice(edited_price_val=edited_price_val,
                        initial_price_val=initial_price_val,
                        price_to_be_changed=sg_binding_price)
    elif edited_price.type == "Yelimli ulash uchun (Qattiq)":
        try:
            hg_binding_price = BindingPrice.objects.get(date=edited_price.date,
                                                        type='Qattiq muqovali yelimlash',
                                                        size=edited_price.size)
        except ObjectDoesNotExist:
            pass
        except MultipleObjectsReturned:
            raise RequestAborted
        else:
            edit_bprice(edited_price_val=edited_price_val,
                        initial_price_val=initial_price_val,
                        price_to_be_changed=hg_binding_price)


def find_and_change_2(**kwargs):
    """An assisting function retrieving the queried object and changing its value using EDIT_PRICE."""

    edited_price = kwargs['edited_price']
    edited_price_val = kwargs['edited_price_val']
    initial_price_val = kwargs['initial_price_val']

    if edited_price.type == "Yupqa":
        try:
            sg_binding_price = BindingPrice.objects.get(date=edited_price.date,
                                                        type='Yumshoq muqovali yelimlash',
                                                        size=edited_price.size)
        except ObjectDoesNotExist:
            pass
        except MultipleObjectsReturned:
            raise RequestAborted
        else:
            edit_bprice(edited_price_val=edited_price_val,
                        initial_price_val=initial_price_val,
                        price_to_be_changed=sg_binding_price)
    elif edited_price.type == "O'rtacha":
        try:
            hg_binding_price = BindingPrice.objects.get(date=edited_price.date,
                                                        type='Qattiq muqovali yelimlash',
                                                        size=edited_price.size)
        except ObjectDoesNotExist:
            pass
        except MultipleObjectsReturned:
            raise RequestAborted
        else:
            edit_bprice(edited_price_val=edited_price_val,
                        initial_price_val=initial_price_val,
                        price_to_be_changed=hg_binding_price)
    elif edited_price.type == "Qalin":
        pass
    else:
        try:
            sg_binding_price = BindingPrice.objects.get(date=edited_price.date,
                                                        type='Yumshoq muqovali yelimlash',
                                                        size=edited_price.size)
        except ObjectDoesNotExist:
            pass
        except MultipleObjectsReturned:
            raise RequestAborted
        else:
            edit_bprice(edited_price_val=edited_price_val,
                        initial_price_val=initial_price_val,
                        price_to_be_changed=sg_binding_price)
        try:
            hg_binding_price = BindingPrice.objects.get(date=edited_price.date,
                                                        type='Qattiq muqovali yelimlash',
                                                        size=edited_price.size)
        except ObjectDoesNotExist:
            pass
        except MultipleObjectsReturned:
            raise RequestAborted
        else:
            edit_bprice(edited_price_val=edited_price_val,
                        initial_price_val=initial_price_val,
                        price_to_be_changed=hg_binding_price)


def find_and_change_3(**kwargs):
    """An assisting function retrieving the queried object and changing its value using EDIT_PRICE."""

    edited_price = kwargs['edited_price']
    edited_price_val = kwargs['edited_price_val']
    initial_price_val = kwargs['initial_price_val']

    if hasattr(edited_price, 'color'):
        page_prices = PagePrice.objects.filter(date=edited_price.date,
                                               type__icontains=edited_price.color,
                                               size=edited_price.size)

        # Get the list of page prices to check whether there are no duplicates
        list_of_dicts = get_price_dicts(page_prices)

        if not page_prices:
            pass
        elif find_duplicates(list_of_dicts):
            raise RequestAborted
        else:
            for pag_price in page_prices:
                edit_pprice(edited_price=edited_price,
                            edited_price_val=edited_price_val,
                            initial_price_val=initial_price_val,
                            price_to_be_changed=pag_price)
    else:
        page_prices = PagePrice.objects.filter(date=edited_price.date,
                                               type__icontains=edited_price.type,
                                               size=edited_price.size)

        # Get the list of page prices to check whether there are no duplicates
        list_of_dicts = get_price_dicts(page_prices)

        if not page_prices:
            pass
        elif find_duplicates(list_of_dicts):
            raise RequestAborted
        else:
            for pag_price in page_prices:
                edit_pprice(edited_price=edited_price,
                            edited_price_val=edited_price_val,
                            initial_price_val=initial_price_val,
                            price_to_be_changed=pag_price)


def find_and_change_4(new_info=None, edited_info=None, initial_count=None, date_changed=False):
    """An assisting function the queried object and changing its value using EDIT_PRINTERCOUNT."""

    if new_info is not None:
        words = get_list_of_words_2(str(new_info.printer))
        brand, *model_and_number = words
        model = ' '.join(model_and_number)
        try:
            printer_info = get_object_or_404(Printer,
                                             brand=brand,
                                             model=model)
        except MultipleObjectsReturned:
            raise RequestAborted
        else:
            edit_printercount(accounted=bool(new_info.accounted),
                              new_info=new_info,
                              count_to_be_changed=printer_info)
    elif edited_info is not None and initial_count is not None and date_changed is False:
        words = get_list_of_words_2(str(edited_info.printer))
        brand, *model_and_number = words
        model = ' '.join(model_and_number)
        try:
            printer_info = get_object_or_404(Printer,
                                             brand=brand,
                                             model=model)
        except MultipleObjectsReturned:
            raise RequestAborted
        else:
            edit_printercount(edited_info=edited_info,
                              initial_count=initial_count,
                              count_to_be_changed=printer_info)
    elif edited_info is not None and date_changed is True:
        words = get_list_of_words_2(str(edited_info.printer))
        brand, *model_and_number = words
        model = ' '.join(model_and_number)
        try:
            printer_info = get_object_or_404(Printer,
                                             brand=brand,
                                             model=model)
        except MultipleObjectsReturned:
            raise RequestAborted
        else:
            edit_printercount(edited_info=edited_info,
                              count_to_be_changed=printer_info)


def find_duplicates(array) -> bool:
    """An assisting function finding the duplicate dictionaries and returning True or False based on the result."""

    items = []
    for obj in array:
        if obj not in items:
            items.append(obj)
        elif obj in items:
            return True


def find_string_in_list(string, array):
    """An assisting function returning the string found in the provided list, ignoring the case."""

    for item in array:
        if re.fullmatch(string, item, flags=re.IGNORECASE):
            return string


def get_color_price_dicts(prices) -> list:
    """An assisting function retrieving the data from the provided queryset and
    placing it to the list as dictionaries."""

    list_of_price_dicts = []
    for price in prices:
        price_dict = {
            'date': str(price.date),
            'color': str(price.color),
            'size': str(price.size),
        }
        list_of_price_dicts.append(price_dict)

    return list_of_price_dicts


def get_list_of_words_1(string) -> list:
    """An assisting function taking in a string and returning a list, the items of which are words contained
    in the provided string."""

    array = []
    for word in string.split():
        array.append(str(word.strip('()')))

    array = [pattern.replace('rangli', 'rangli'.capitalize()) for pattern in array]
    array = [pattern.replace('qora', 'qora'.capitalize()) for pattern in array]

    return array


def get_list_of_words_2(string) -> list:
    """An assisting function taking in a string and returning a list, the items of which are words contained
    in the provided string."""

    array = []
    for word in string.split():
        array.append(str(word))

    return array


def get_name_dicts(queryset) -> list:
    """An assisting function getting people's names, surnames and middle names, and returning them as strings."""

    list_of_dicts = []
    for obj in queryset:
        dictionary = {
            'name': str(obj.name),
            'surname': str(obj.surname),
            'middle_name': str(obj.middle_name),
        }
        list_of_dicts.append(dictionary)

    return list_of_dicts


def get_price_dates(prices) -> list:
    """An assisting function retrieving dates from the provided queryset and
    placing them to the list."""

    list_price_dates = []
    for price in prices:
        list_price_dates.append(str(price.date))

    return list_price_dates


def get_price_dicts(prices) -> list:
    """An assisting function retrieving the data from the provided queryset and
    placing it to the list as dictionaries."""

    list_of_price_dicts = []
    for price in prices:
        price_dict = {
            'date': str(price.date),
            'type': str(price.type),
            'size': str(price.size),
        }
        list_of_price_dicts.append(price_dict)

    return list_of_price_dicts


def get_printer_brand_dicts(queryset) -> list:
    """An assisting function retrieving the data from the provided queryset and
    placing it to the list as dictionaries."""

    list_of_dicts = []
    for obj in queryset:
        printer_info = {
            'brand': str(obj.brand),
            'model': str(obj.model),
        }
        list_of_dicts.append(printer_info)

    return list_of_dicts


def get_printer_names(queryset) -> list:
    """An assisting function retrieving the data from the provided queryset and
    placing them in the list as strings."""

    list_of_printers = []
    for obj in queryset:
        list_of_printers.append(str(obj.printer))

    return list_of_printers


def match_color_price_with_existing(list_of_dicts, price) -> bool:
    """An assisting function determining if the information trying to be posted exists in the database."""

    price_dict = {
        'date': str(price.date),
        'color': str(price.color),
        'size': str(price.size),
    }
    if price_dict in list_of_dicts:
        return True
    else:
        return False


def match_with_existing(list_of_dicts, price) -> bool:
    """An assisting function determining if the information trying to be posted exists in the database."""

    price_dict = {
        'date': str(price.date),
        'type': str(price.type),
        'size': str(price.size),
    }
    if price_dict in list_of_dicts:
        return True
    else:
        return False


def match_with_existing_dates(list_of_dates, price) -> bool:
    """An assisting function determining if the information trying to be posted exists in the database
    based on the date."""

    if str(price.date) in list_of_dates:
        return True
    else:
        return False


def match_with_existing_names(list_of_dicts, info) -> bool:
    """An assisting function determining if the information trying to be posted exists in the database
    based on the names provided."""

    info_dict = {
        'name': str(info.name),
        'surname': str(info.surname),
        'middle_name': str(info.middle_name),
    }
    if info_dict in list_of_dicts:
        return True
    else:
        return False


def match_with_existing_printers(list_of_dicts, info) -> bool:
    """An assisting function determining if the information trying to be posted exists in the database
    based on the brands and models provided."""

    printer_info = {
        'brand': str(info.brand),
        'model': str(info.model),
    }
    if printer_info in list_of_dicts:
        return True
    else:
        return False


def outex_edited_edit_bprice(**kwargs):
    """An assisting function editing all binding prices based on the edited price of outer expenses."""

    initial_packaging = kwargs['initial_packaging']
    initial_workforce = kwargs['initial_workforce']
    edited_packaging = kwargs['edited_packaging']
    edited_prices = kwargs['edited_prices']
    edited_workforce = kwargs['edited_workforce']

    sum_initial_exps = math.fsum([initial_workforce, initial_packaging])
    sum_edited_exps = math.fsum([edited_workforce, edited_packaging])

    binding_prices = BindingPrice.objects.filter(date=edited_prices.date)

    # Get the list of binding price dictionaries to check whether there are no duplicates
    list_of_dicts = get_price_dicts(binding_prices)

    if find_duplicates(list_of_dicts):
        raise RequestAborted
    else:
        if binding_prices:
            for binding_price in binding_prices:
                if sum_edited_exps > sum_initial_exps:
                    gap = int(sum_edited_exps) - int(sum_initial_exps)
                    binding_price.price = binding_price.price.amount + gap
                    binding_price.save()
                elif sum_edited_exps < sum_initial_exps:
                    gap = int(sum_initial_exps) - int(sum_edited_exps)
                    binding_price.price = binding_price.price.amount - gap
                    binding_price.save()


def outex_edited_edit_pprice(**kwargs):
    """An assisting function editing all page prices based on the edited price of outer expenses."""

    initial_printer_exp = kwargs['initial_printer_exp']
    edited_printer_exp = kwargs['edited_printer_exp']
    edited_prices = kwargs['edited_prices']

    page_prices = PagePrice.objects.filter(date=edited_prices.date)

    # Get the list of page price dictionaries to check whether there are no duplicates
    list_of_dicts = get_price_dicts(page_prices)

    if find_duplicates(list_of_dicts):
        raise RequestAborted
    else:
        if page_prices:
            for pag_price in page_prices:
                if str(pag_price.size) == 'A4':
                    if edited_printer_exp > initial_printer_exp:
                        gap = int(edited_printer_exp) - int(initial_printer_exp)
                        pag_price.price = pag_price.price.amount + gap
                        pag_price.save()
                    elif edited_printer_exp < initial_printer_exp:
                        gap = int(initial_printer_exp) - int(edited_printer_exp)
                        pag_price.price = pag_price.price.amount - gap
                        pag_price.save()
                elif str(pag_price.size) == 'A5':
                    if edited_printer_exp > initial_printer_exp:
                        gap = int(edited_printer_exp) - int(initial_printer_exp)
                        pag_price.price = pag_price.price.amount + decimal.Decimal(gap / 2)
                        pag_price.save()
                    elif edited_printer_exp < initial_printer_exp:
                        gap = int(initial_printer_exp) - int(edited_printer_exp)
                        pag_price.price = pag_price.price.amount - decimal.Decimal(gap / 2)
                        pag_price.save()


def provide_dicts(objs):
    """An assisting function returning the JavaScript object for the usage in resources
    and losses section of the admin panel."""

    dicts = []
    for a_type in objs:
        types_dict = {
            'type': a_type.type,
            'size': a_type.size,
            'color': a_type.color,
        }
        dicts.append(types_dict)
    json_dicts = json.dumps(dicts)
    return json_dicts
