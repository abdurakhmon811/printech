from django.contrib import messages
from django.db.models import ProtectedError
from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404
from .forms import AccountForm, BlogPostForm, BookForm, CategoryExForm, CategoryInForm, ComplaintBookForm, \
    ComplaintOtherForm, ComplaintSiteForm, ContactForm, CreateSiteForm, ExpenseForm, IncomeForm, LossForm, \
    LTypeForm, NewsForm, OrderOptionsForm, OrderSelfForm, OrderSiteForm, ResourceForm, RTypeForm, \
    SelfOrderForm, SiteOrderForm, SubCategoryExForm, SubCategoryInForm, TransactionForm
from .models import Account, BlogPost, Book, CategoryEx, CategoryIn, Complaint, Contact, CreateSite, \
    Expense, Income, Loss, LType, News, Order, OrderOptions, Resource, RType, SubCategoryEx, SubCategoryIn, \
    Transaction
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


def welcome_admin(request):
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

    if request.method != 'POST':
        form = OrderOptionsForm()
    else:
        form = OrderOptionsForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_options')
        messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'res_s': res_s,
    }
    return render(request, 'service/order_options.html', context)


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
            if new_account.name in list_of_accounts:
                form.add_error('name', "Ushbu hisob mavjud!")
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
            if not form.has_changed():
                return redirect('choose_ex_in')
            elif edited_account.name in list_of_accounts:
                form.add_error('name', "Ushbu hisob mavjud!")
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
            if new_cat.category in list_of_cats:
                form.add_error('category', "Ushbu kategoriya mavjud!")
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
            if not form.has_changed():
                return redirect('expense_categories')
            elif edited_cat.category in list_of_cats:
                form.add_error('category', "Ushbu kategoriya mavjud!")
                messages.error(request, "Mavjud kategoriya kiritildi!")
            else:
                edited_cat.save()
                return redirect('expense_categories')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri kiritildi!")

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
            if new_subcat.subcategory in list_of_subcats:
                form.add_error('subcategory', "Ushbu quyi kategoriya mavjud!")
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
            if not form.has_changed():
                return redirect('expense_subcats')
            elif edited_subcat.subcategory in list_of_subcats:
                form.add_error('subcategory', "Ushbu quyi kategoriya mavjud!")
                messages.error(request, "Mavjud quyi kategoriya kiritildi!")
            else:
                edited_subcat.save()
                return redirect('expense_subcats')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri kiritildi!")

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
            if new_cat.category in list_of_cats:
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
            if not form.has_changed():
                return redirect('income_categories')
            elif edited_cat.category in list_of_cats:
                form.add_error('category', "Ushbu kategoriya mavjud!")
                messages.error(request, "Mavjud kategoriya kiritildi!")
            else:
                edited_cat.save()
                return redirect('income_categories')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri kiritildi!")

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
            if new_subcat.subcategory in list_of_subcats:
                form.add_error('subcategory', "Ushbu quyi kategoriya mavjud!")
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
            if not form.has_changed():
                return redirect('income_subcats')
            elif edited_subcat.subcategory in list_of_subcats:
                form.add_error('subcategory', "Ushbu quyi kategoriya mavjud!")
                messages.error(request, "Mavjud quyi kategoriya kiritildi!")
            else:
                edited_subcat.save()
                return redirect('income_subcats')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri kiritildi!")

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
            messages.error(request, "Ma'lumotlar noto'g'ri kiritildi!")

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
            messages.error(request, "Ma'lumotlar noto'g'ri kiritildi!")

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
            messages.error(request, "Ma'lumotlar noto'g'ri kiritildi!")

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
            messages.error(request, "Ma'lumotlar noto'g'ri kiritildi!")

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
            messages.error(request, "Ma'lumotlar noto'g'ri kiritildi!")

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


def rtypes(request):
    """A view providing the content for the page for adding resource types."""

    check_super_user(request)

    types = RType.objects.all()

    if request.method != 'POST':
        form = RTypeForm()
    else:
        form = RTypeForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('resources')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri kiritildi!")

    context = {
        'form': form,
        'types': types,
    }
    return render(request, 'service/rtypes.html', context)


def edit_rtype(request, rtype_id):
    """A view providing the content for the page for editing the chosen resource type."""

    check_super_user(request)

    rtype = get_object_or_404(RType, pk=rtype_id)

    if request.method != 'POST':
        form = RTypeForm(instance=rtype)
    else:
        form = RTypeForm(data=request.POST, instance=rtype)
        if form.is_valid():
            form.save()
            return redirect('rtypes')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri kiritildi!")

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

    res_s = Resource.objects.all().order_by('-time_bought')
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
            messages.error(request, "Ma'lumotlar noto'g'ri kiritildi!")

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
            messages.error(request, "Ma'lumotlar noto'g'ri kiritildi!")

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
            messages.error(request, "Ma'lumotlar noto'g'ri kiritildi!")

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
            messages.error(request, "Ma'lumotlar noto'g'ri kiritildi!")

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


# ========================================================================================================


def search(request):
    """A view providing the content for the search page to illustrate the results."""
    from django.db.models import Q
    import re

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

    if request.method != 'POST':
        form = OrderSiteForm()
    else:
        form = OrderSiteForm(data=request.POST)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.customer = request.user
            new_order.save()
            return redirect('success_order')
        messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'res': res,
    }
    return render(request, 'service/order_site.html', context)


def order_users(request):
    """A view providing the content for the page for making orders for the books provided by users themselves."""

    res = OrderOptions.objects.latest('date')

    if request.method != 'POST':
        form = OrderSelfForm()
    else:
        form = OrderSelfForm(data=request.POST)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.customer = request.user
            new_order.save()
            return redirect('success_order')
        messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
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


def provide_dicts(objs):
    """An assisting function returning the JavaScript object for the usage in resources section of the admin panel."""

    dicts = []
    for rtype in objs:
        types_dict = {}
        types_dict['type'] = rtype.type
        types_dict['size'] = rtype.size
        types_dict['color'] = rtype.color
        dicts.append(types_dict)
    json_dicts = json.dumps(dicts)
    return json_dicts
