"""Views for the admin panel."""
from .assisting_functions import *
from django.contrib import messages
from django.db.models import ProtectedError
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist, RequestAborted
from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404
from .forms import AccountForm, \
    BindingPriceForm, BlogPostForm, BookForm, \
    CategoryExForm, CategoryInForm, ColorPriceForm, \
    CouponForm, CoverPriceForm, \
    ExpenseForm, \
    GluePriceForm, \
    IncomeForm, \
    LossForm, LTypeForm, \
    NewsForm, \
    OrderOptionsForm, OuterPriceForm, \
    PagePriceForm, PaperPriceForm, PlaceToGetForm, PrinterForm, \
    RefillAndPageCountForm, ResourceForm, RingPriceForm, RTypeForm, \
    SelfOrderForm, SiteOrderForm, SubCategoryExForm, SubCategoryInForm, \
    TransactionForm, \
    WorkforceForm, \
    YarnPriceForm
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


def main_page(request):
    """
    First checks whether a requesting user is a super user or not, if so it allows the user, else throws 404.

    Once the user is checked, the main page of the admin panel is rendered.

    NOTE: All of the views rendering templates for the admin panel first check and should check
    if a requesting user is a super user and act based on the result. Also, for most of the pages which retrieve
    a single object from the database, the GET_OBJECT_OR_404 method is used and should be used to raise Http404
    in case a queried object is not found.
    """

    check_super_user(request)

    return render(request, 'service/admin_panel_templates/mains_and_adds/main_page.html')


def orders(request):
    """
    Renders the page for checking orders made by customers/users for books.
    """

    check_super_user(request)

    orders_made = Order.objects.all()
    orders_num = len(orders_made)

    context = {
        'orders_made': orders_made,
        'orders_num': orders_num,
    }
    return render(request, 'service/admin_panel_templates/mains_and_adds/orders.html', context)


def edit_order(request, order_number):
    """
    Renders the page for editing an order.

    If an order made for a book/books from the site, the instance is returned using Site Order Form.
    Otherwise, Self Order Form is used.
    """

    check_super_user(request)

    order = get_object_or_404(Order, pk=order_number)

    if order.book:
        if request.method != 'POST':
            form = SiteOrderForm(instance=order)
        else:
            form = SiteOrderForm(instance=order, data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('orders')
            else:
                messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

        context = {
            'form': form,
            'order': order,
        }
        return render(request, 'service/admin_panel_templates/edits/edit_ordersite.html', context)
    elif not order.book and order.custom_book:
        if request.method != 'POST':
            form = SelfOrderForm(instance=order)
        else:
            form = SelfOrderForm(instance=order, data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('orders')
            else:
                messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

        context = {
            'form': form,
            'order': order,
        }
        return render(request, 'service/admin_panel_templates/edits/edit_orderself.html', context)


def delete_order(request, order_number):
    """
    Renders the page which tells a user that an order has been deleted.
    """

    check_super_user(request)

    order = get_object_or_404(Order, pk=order_number)
    order.delete()

    return render(request, 'service/admin_panel_templates/deletes/order_deleted.html')


def order_options(request):
    """
    Renders the page for either checking or adding order options for users.

    Two forms are rendered, one of which is for adding order options.
    The latter one is for adding places from where customers can obtain their orders.

    NOTE: Beware if you ever happen to change the names (optionssubmit and placessubmit) which are checked
    whether they are in POST dictionary or not, you will also have to change them in the template rendered by this view.
    """

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
    return render(request, 'service/admin_panel_templates/mains_and_adds/order_options.html', context)


def edit_orderoptions(request, orderoptions_id):
    """
    Renders the page for editing an order option.
    """

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
    return render(request, 'service/admin_panel_templates/edits/edit_orderoptions.html', context)


def delete_orderoptions(request, orderoptions_id):
    """
    Renders the page which tells a user that an order option has been deleted.
    """

    check_super_user(request)

    options = get_object_or_404(OrderOptions, pk=orderoptions_id)
    options.delete()

    return render(request, 'service/admin_panel_templates/deletes/orderoptions_deleted.html')


def edit_placetoget(request, placetoget_id):
    """
    Renders the page for editing a place-to-get.
    """

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
    return render(request, 'service/admin_panel_templates/edits/edit_placetoget.html', context)


def delete_placetoget(request, placetoget_id):
    """
    Renders the page which tells a user that a place-to-get has been deleted.

    There can raise a ProtectedError exception because of the connection between places-to-get and orders.
    """

    check_super_user(request)

    place = get_object_or_404(PlaceToGet, pk=placetoget_id)

    try:
        place.delete()
    except ProtectedError:
        return render(request, 'service/admin_panel_templates/exception_pages/not_delete_placetoget.html')
    else:
        return render(request, 'service/admin_panel_templates/deletes/placetoget_deleted.html')


def staff_info(request):
    """
    Renders the page for either checking or adding staff information.

    The GET_NAME_DICTS method retrieves names from the database and saves them in dictionaries
    which are places in a list. In this case, first, second and middle names are passed to a dictionary.

    The MATCH_WITH_EXISTING_NAMES method is used to check whether an employee a user tries to key in exists
    in the database or not. If exists, an error using MESSAGES module is shown and a user is not let to continue.

    The same operations are implemented in the EDIT_STAFF_INFO view.
    """

    check_super_user(request)

    staff_information = Workforce.objects.all()
    list_of_dicts = get_name_dicts(staff_information)
    staff_num = len(staff_information)

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
                return redirect('staff_info')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'staff_information': staff_information,
        'staff_num': staff_num,
    }
    return render(request, 'service/admin_panel_templates/mains_and_adds/staff_info.html', context)


def edit_staff_info(request, workforce_id):
    """
    Renders the page for editing staff information.

    If a user does not change the form, they are just redirected to the staff information page.
    Also, the names of an employee are not changed but other information, the form is saved and
    a user is redirected to the staff information page.

    For more information, take a look at the STAFF_INFO view.
    """

    check_super_user(request)

    staff_information = Workforce.objects.all()
    list_of_dicts = get_name_dicts(staff_information)

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
                return redirect('staff_info')
            elif form.has_changed() and True not in array:
                edited_info.save()
                return redirect('staff_info')
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
    return render(request, 'service/admin_panel_templates/edits/edit_staff_info.html', context)


def delete_staff_info(request, workforce_id):
    """
    Renders the page which tells a user that staff information has been deleted.
    """

    check_super_user(request)

    employee_info = get_object_or_404(Workforce, pk=workforce_id)
    employee_info.delete()

    return render(request, 'service/admin_panel_templates/deletes/staff_info_deleted.html')


def books(request):
    """
    Renders the page for either checking or adding books for sales.

    Before a user adds a new book, the book code is checked whether it exists in the database,
    using the MATCH_WITH_BOOK_CODES method. If so, an error is raised.

    The same operation is implemented in the EDIT_BOOK view.
    """

    check_super_user(request)

    book_objects = Book.objects.all()
    list_of_book_codes = get_book_codes(book_objects)
    books_num = len(book_objects)

    if request.method != 'POST':
        form = BookForm()
    else:
        form = BookForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_book = form.save(commit=False)
            exists = match_with_book_codes(list_of_book_codes, new_book)
            if exists:
                form.add_error('name_coded', "")
                messages.error(request, "Kiritilgan kod bo'yicha kitob mavjud!")
            else:
                new_book.save()
                return redirect('books')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'book_objects': book_objects,
        'books_num': books_num,
        'form': form,
    }
    return render(request, 'service/admin_panel_templates/mains_and_adds/books.html', context)


def edit_book(request, book_id):
    """
    Renders the page for editing a book.

    For more information, take a look at the BOOKS view.
    """

    check_super_user(request)

    book_objects = Book.objects.all()
    list_of_book_codes = get_book_codes(book_objects)

    book = get_object_or_404(Book, pk=book_id)

    if request.method != 'POST':
        form = BookForm(instance=book)
    else:
        form = BookForm(instance=book, data=request.POST, files=request.FILES)
        if form.is_valid():
            edited_book = form.save(commit=False)
            code_changed = 'name_coded' in form.changed_data
            if not form.has_changed():
                return redirect('books')
            elif code_changed:
                exists = match_with_book_codes(list_of_book_codes, edited_book)
                if exists:
                    form.add_error('name_coded', "")
                    messages.error(request, "Kiritilgan kod bo'yicha kitob mavjud!")
            else:
                edited_book.save()
                return redirect('books')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'book': book,
    }
    return render(request, 'service/admin_panel_templates/edits/edit_book.html', context)


def delete_book(request, book_id):
    """
    Renders the page which tells a user that a book has been deleted.
    """

    check_super_user(request)

    book = get_object_or_404(Book, pk=book_id)
    book.delete()

    return render(request, 'service/admin_panel_templates/deletes/book_deleted.html')


def incomes_expenses(request):
    """
    Renders the page for either checking or adding incomes, expenses, transactions or accounts.

    NOTE: Matching operations are implemented in most parts of the incomes-expenses section as some information
    should not match each other - such as Categories, Subcategories or Account names.
    For the operations, the MATCH_WITH_NAMES and GET_NAMES methods are utilized which are located
    in the ASSISTING_FUNCTIONS module.
    """

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
    return render(request, 'service/admin_panel_templates/mains_and_adds/incomes_expenses.html', context)


def add_account(request):
    """
    Renders the page for adding monetary accounts.

    For more information, take a look at the INCOMES_EXPENSES view (main for the section).
    """

    check_super_user(request)
    accounts = Account.objects.all()
    list_of_accounts = get_names(accounts=accounts)

    if request.method != 'POST':
        form = AccountForm()
    else:
        form = AccountForm(data=request.POST)
        if form.is_valid():
            new_account = form.save(commit=False)
            if match_with_names(list_of_accounts=list_of_accounts, account=new_account):
                form.add_error('name', "")
                messages.error(request, "Mavjud hisob kiritildi!")
            else:
                new_account.save()
                return redirect('incomes_expenses')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
    }
    return render(request, 'service/admin_panel_templates/mains_and_adds/add_account.html', context)


def edit_account(request, account_id):
    """
    Renders the page for editing an account.

    For more information, take a look at the INCOMES_EXPENSES view (main for the section).
    """

    check_super_user(request)

    accounts = Account.objects.all()
    list_of_accounts = get_names(accounts=accounts)

    acc = get_object_or_404(Account, pk=account_id)

    if request.method != 'POST':
        form = AccountForm(instance=acc)
    else:
        form = AccountForm(data=request.POST, instance=acc)
        if form.is_valid():
            edited_account = form.save(commit=False)
            name_changed = 'name' in form.changed_data
            if not form.has_changed():
                return redirect('incomes_expenses')
            elif form.has_changed() and name_changed is False:
                edited_account.save()
                return redirect('incomes_expenses')
            elif match_with_names(list_of_accounts=list_of_accounts, account=edited_account):
                form.add_error('name', "")
                messages.error(request, "Mavjud hisob kiritildi!")
            else:
                edited_account.save()
                return redirect('incomes_expenses')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'acc': acc,
    }
    return render(request, 'service/admin_panel_templates/edits/edit_account.html', context)


def delete_account(request, account_id):
    """
    Renders the page which tells a user that an account has been deleted.

    There can raise a ProtectedError exception because of the connection of accounts with incomes and expenses.
    """

    check_super_user(request)

    acc = get_object_or_404(Account, pk=account_id)

    try:
        acc.delete()
    except ProtectedError:
        return render(request, 'service/admin_panel_templates/exception_pages/not_delete_account.html')
    else:
        return render(request, 'service/admin_panel_templates/deletes/account_deleted.html')


def expense_categories(request):
    """
    Renders the page for either checking or adding expense categories.

    For more information, take a look at the INCOMES_EXPENSES view (main for the section).
    """

    check_super_user(request)

    cats = CategoryEx.objects.all()
    list_of_cats = get_names(categories=cats)
    cats_num = len(cats)

    if request.method != 'POST':
        form = CategoryExForm()
    else:
        form = CategoryExForm(data=request.POST)
        if form.is_valid():
            new_cat = form.save(commit=False)
            if match_with_names(list_of_categories=list_of_cats, category=new_cat):
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
    return render(request, 'service/admin_panel_templates/mains_and_adds/expense_categories.html', context)


def edit_excategory(request, excategory_id):
    """
    Renders the page for editing an expense category.

    For more information, take a look at the INCOMES_EXPENSES view (main for the section).
    """

    check_super_user(request)

    cats = CategoryEx.objects.all()
    list_of_cats = get_names(categories=cats)

    cat = get_object_or_404(CategoryEx, pk=excategory_id)

    if request.method != 'POST':
        form = CategoryExForm(instance=cat)
    else:
        form = CategoryExForm(data=request.POST, instance=cat)
        if form.is_valid():
            edited_cat = form.save(commit=False)
            if not form.has_changed():
                return redirect('expense_categories')
            elif match_with_names(list_of_categories=list_of_cats, category=edited_cat):
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
    return render(request, 'service/admin_panel_templates/edits/edit_excategory.html', context)


def delete_excategory(request, excategory_id):
    """
    Renders the page which tells a user that an expense category has been deleted.

    There can raise a Protected error exception because of the connection between expense categories and expenses.
    """

    check_super_user(request)

    cat = get_object_or_404(CategoryEx, pk=excategory_id)

    try:
        cat.delete()
    except ProtectedError:
        return render(request, 'service/admin_panel_templates/exception_pages/not_delete_excat.html')
    else:
        return render(request, 'service/admin_panel_templates/deletes/excat_deleted.html')


def expense_subcats(request):
    """
    Renders the page for either checking or adding expense subcategories.

    For more information, take a look at the INCOMES_EXPENSES view (main for the section).
    """

    check_super_user(request)

    subcats = SubCategoryEx.objects.all()
    list_of_subcats = get_names(subcategories=subcats)
    subcats_num = len(subcats)

    if request.method != 'POST':
        form = SubCategoryExForm()
    else:
        form = SubCategoryExForm(data=request.POST)
        if form.is_valid():
            new_subcat = form.save(commit=False)
            if match_with_names(list_of_subcategories=list_of_subcats, subcategory=new_subcat):
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
    return render(request, 'service/admin_panel_templates/mains_and_adds/expense_subcats.html', context)


def edit_exsubcat(request, exsubcategory_id):
    """
    Renders the page for editing an expense subcategories.

    For more information, take a look at the INCOMES_EXPENSES view (main for the section).
    """

    check_super_user(request)

    subcats = SubCategoryEx.objects.all()
    list_of_subcats = get_names(subcategories=subcats)

    subcat = get_object_or_404(SubCategoryEx, pk=exsubcategory_id)

    if request.method != 'POST':
        form = SubCategoryExForm(instance=subcat)
    else:
        form = SubCategoryExForm(data=request.POST, instance=subcat)
        if form.is_valid():
            edited_subcat = form.save(commit=False)
            if not form.has_changed():
                return redirect('expense_subcats')
            elif match_with_names(list_of_subcategories=list_of_subcats, subcategory=edited_subcat):
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
    return render(request, 'service/admin_panel_templates/edits/edit_exsubcat.html', context)


def delete_exsubcat(request, exsubcategory_id):
    """
    Renders the page which tells a user that an expense subcategory has been deleted.

    There can raise a ProtectedError exception because of the connection between expense subcategories and expenses.
    """

    check_super_user(request)

    subcat = get_object_or_404(SubCategoryEx, pk=exsubcategory_id)

    try:
        subcat.delete()
    except ProtectedError:
        return render(request, 'service/admin_panel_templates/exception_pages/not_delete_exsubcat.html')
    else:
        return render(request, 'service/admin_panel_templates/deletes/exsubcat_deleted.html')


def income_categories(request):
    """
    Renders the page for either checking or adding income categories.

    For more information, take a look at the INCOMES_EXPENSES view (main for the section).
    """

    check_super_user(request)

    cats = CategoryIn.objects.all()
    list_of_cats = get_names(categories=cats)
    cats_num = len(cats)

    if request.method != 'POST':
        form = CategoryInForm()
    else:
        form = CategoryInForm(data=request.POST)
        if form.is_valid():
            new_cat = form.save(commit=False)
            if match_with_names(list_of_categories=list_of_cats, category=new_cat):
                form.add_error('category', "")
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
    return render(request, 'service/admin_panel_templates/mains_and_adds/income_categories.html', context)


def edit_incategory(request, incategory_id):
    """
    Renders the page for editing an income category.

    For more information, take a look at the INCOMES_EXPENSES view (main for the section).
    """

    check_super_user(request)

    cats = CategoryIn.objects.all()
    list_of_cats = get_names(categories=cats)

    cat = get_object_or_404(CategoryIn, pk=incategory_id)

    if request.method != 'POST':
        form = CategoryInForm(instance=cat)
    else:
        form = CategoryInForm(data=request.POST, instance=cat)
        if form.is_valid():
            edited_cat = form.save(commit=False)
            if not form.has_changed():
                return redirect('income_categories')
            elif match_with_names(list_of_categories=list_of_cats, category=edited_cat):
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
    return render(request, 'service/admin_panel_templates/edits/edit_incategory.html', context)


def delete_incategory(request, incategory_id):
    """
    Renders the page which tells a user that an income category has been deleted.

    There can raise a ProtectedError exception because of the connection between income categories and incomes.
    """

    check_super_user(request)

    cat = get_object_or_404(CategoryIn, pk=incategory_id)

    try:
        cat.delete()
    except ProtectedError:
        return render(request, 'service/admin_panel_templates/exception_pages/not_delete_incat.html')
    else:
        return render(request, 'service/admin_panel_templates/deletes/incat_deleted.html')


def income_subcats(request):
    """
    Renders the page for either checking or adding an income subcategory.

    For more information, take a look at the INCOMES_EXPENSES view (main for the section).
    """

    check_super_user(request)

    subcats = SubCategoryIn.objects.all()
    list_of_subcats = get_names(subcategories=subcats)
    subcats_num = len(subcats)

    if request.method != 'POST':
        form = SubCategoryInForm()
    else:
        form = SubCategoryInForm(data=request.POST)
        if form.is_valid():
            new_subcat = form.save(commit=False)
            if match_with_names(list_of_subcategories=list_of_subcats, subcategory=new_subcat):
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
    return render(request, 'service/admin_panel_templates/mains_and_adds/income_subcats.html', context)


def edit_insubcat(request, insubcategory_id):
    """
    Renders the page for editing an income subcategory.

    For more information, take a look at the INCOMES_EXPENSES view (main for the section).
    """

    check_super_user(request)

    subcats = SubCategoryIn.objects.all()
    list_of_subcats = get_names(subcategories=subcats)

    subcat = get_object_or_404(SubCategoryIn, pk=insubcategory_id)

    if request.method != 'POST':
        form = SubCategoryInForm(instance=subcat)
    else:
        form = SubCategoryInForm(data=request.POST, instance=subcat)
        if form.is_valid():
            edited_subcat = form.save(commit=False)
            if not form.has_changed():
                return redirect('income_subcats')
            elif match_with_names(list_of_subcategories=list_of_subcats, subcategory=edited_subcat):
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
    return render(request, 'service/admin_panel_templates/edits/edit_insubcat.html', context)


def delete_insubcat(request, insubcategory_id):
    """
    Renders the page which tells a user that an income subcategory has been deleted.

    There can raise a ProtectedError exception because of the connection between income subcategories and incomes.
    """

    check_super_user(request)

    subcat = get_object_or_404(SubCategoryIn, pk=insubcategory_id)

    try:
        subcat.delete()
    except ProtectedError:
        return render(request, 'service/admin_panel_templates/exception_pages/not_delete_insubcat.html')
    else:
        return render(request, 'service/admin_panel_templates/deletes/insubcat_deleted.html')


def make_expense(request):
    """
    Renders the page for making an expense and decrements the inserted amount from a chosen account.
    """

    check_super_user(request)

    if request.method != 'POST':
        form = ExpenseForm()
    else:
        form = ExpenseForm(data=request.POST)
        if form.is_valid():
            new_expense = form.save(commit=False)
            acc = get_object_or_404(Account, pk=new_expense.account.pk)
            acc.means.amount -= new_expense.amount.amount
            acc.save()
            new_expense.save()
            return redirect('incomes_expenses')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
    }
    return render(request, 'service/admin_panel_templates/mains_and_adds/make_expense.html', context)


def edit_expense(request, expense_id):
    """
    Renders the page for editing an expense.
    """

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
            account = get_object_or_404(Account, pk=edited_ex.account.pk)
            change_account_means(initial_val=initial_val,
                                 edited_val=edited_val,
                                 account=account,
                                 expense_edited=True)
            edited_ex.save()
            return redirect('incomes_expenses')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'expense': expense,
    }
    return render(request, 'service/admin_panel_templates/edits/edit_expense.html', context)


def delete_expense(request, expense_id):
    """
    Renders the page which tells a user that an expense has been deleted.
    """

    check_super_user(request)

    expense = get_object_or_404(Expense, pk=expense_id)
    acc = get_object_or_404(Account, pk=expense.account.pk)

    acc.means.amount += expense.amount.amount
    acc.save()
    expense.delete()
    return render(request, 'service/admin_panel_templates/deletes/expense_deleted.html')


def make_income(request):
    """
    Renders the page for making an income.
    """

    check_super_user(request)

    if request.method != 'POST':
        form = IncomeForm()
    else:
        form = IncomeForm(data=request.POST)
        if form.is_valid():
            new_income = form.save(commit=False)
            account = Account.objects.get(pk=new_income.account.pk)
            account.means.amount += new_income.amount.amount
            account.save()
            new_income.save()
            return redirect('incomes_expenses')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
    }
    return render(request, 'service/admin_panel_templates/mains_and_adds/make_income.html', context)


def edit_income(request, income_id):
    """
    Renders the page for editing an income.
    """

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
            account = get_object_or_404(Account, pk=edited_income.account.pk)
            change_account_means(initial_val=initial_val,
                                 edited_val=edited_val,
                                 account=account,
                                 income_edited=True)
            edited_income.save()
            return redirect('incomes_expenses')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'income': income,
    }
    return render(request, 'service/admin_panel_templates/edits/edit_income.html', context)


def delete_income(request, income_id):
    """
    Renders the page which tells a user that an income has been deleted.
    """

    check_super_user(request)

    income = get_object_or_404(Income, pk=income_id)
    acc = get_object_or_404(Account, pk=income.account.pk)

    acc.means.amount -= income.amount.amount
    acc.save()
    income.delete()
    return render(request, 'service/admin_panel_templates/deletes/income_deleted.html')


def make_transaction(request):
    """
    Renders the page for making transactions.
    """

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
            elif new_transaction.acc_1 == new_transaction.acc_2:
                messages.error(request, "Iltimos ikkita turli hisoblarni tanlang!")
            elif acc1.means.amount < 0 or acc1.means.amount < new_transaction.amount.amount:
                messages.error(request, "Hisobda mablag' yetarli emas!")
            else:
                acc1.means.amount -= new_transaction.amount.amount
                acc2.means.amount += new_transaction.amount.amount
                acc1.save()
                acc2.save()
                new_transaction.save()
                return redirect('incomes_expenses')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'transfers': transfers,
        'transfers_num': transfers_num,
    }
    return render(request, 'service/admin_panel_templates/mains_and_adds/make_transaction.html', context)


def edit_transaction(request, transaction_id):
    """
    Renders the page for editing a transaction.
    """

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
            account_1 = get_object_or_404(Account, pk=edited_transfer.acc_1.pk)
            account_2 = get_object_or_404(Account, pk=edited_transfer.acc_2.pk)
            change_account_means(initial_val=initial_val,
                                 edited_val=edited_val,
                                 account_1=account_1,
                                 account_2=account_2,
                                 transaction_edited=True)
            edited_transfer.save()
            return redirect('make_transaction')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'transfer': transfer,
    }
    return render(request, 'service/admin_panel_templates/edits/edit_transaction.html', context)


def delete_transaction(request, transaction_id):
    """
    Renders the page which tells a user that a transaction has been deleted.
    """

    check_super_user(request)

    transfer = get_object_or_404(Transaction, pk=transaction_id)
    account_1 = get_object_or_404(Account, pk=transfer.acc_1.pk)
    account_2 = get_object_or_404(Account, pk=transfer.acc_2.pk)

    account_1.means.amount += transfer.amount.amount
    account_2.means.amount -= transfer.amount.amount
    account_1.save()
    account_2.save()
    transfer.delete()
    return render(request, 'service/admin_panel_templates/deletes/transaction_deleted.html')


def blogposts(request):
    """
    Renders the page for either checking or adding blogposts.
    """

    check_super_user(request)

    posts = BlogPost.objects.all().order_by('-date_published')
    posts_num = len(posts)

    if request.method != 'POST':
        form = BlogPostForm()
    else:
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.publisher = request.user
            new_post.save()
            return redirect('blogposts')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'posts': posts,
        'posts_num': posts_num,
    }
    return render(request, 'service/admin_panel_templates/mains_and_adds/blogposts.html', context)


def edit_blogpost(request, blogpost_id):
    """
    Renders the page for editing a blogpost.
    """

    check_super_user(request)

    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)

    if request.method != 'POST':
        form = BlogPostForm(instance=blogpost)
    else:
        form = BlogPostForm(instance=blogpost, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blogposts')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'blogpost': blogpost,
    }
    return render(request, 'service/admin_panel_templates/edits/edit_blogpost.html', context)


def delete_blogpost(request, blogpost_id):
    """
    Renders the page which tells a user that a blogpost has been deleted.
    """

    check_super_user(request)

    post = get_object_or_404(BlogPost, pk=blogpost_id)

    post.delete()
    return render(request, 'service/admin_panel_templates/deletes/blogpost_deleted.html')


def contacts(request):
    """
    Renders the page for checking contact inquires.
    """

    check_super_user(request)

    contact_objects = Contact.objects.all().order_by('-date_made')
    contacts_num = len(contact_objects)

    context = {
        'contact_objects': contact_objects,
        'contacts_num': contacts_num,
    }
    return render(request, 'service/admin_panel_templates/mains_and_adds/contacts.html', context)


def ask_del_contact(request, contact_id):
    """
    Renders the page which asks a user whether they are sure about deleting a contact inquiry.
    """

    check_super_user(request)

    cont = get_object_or_404(Contact, pk=contact_id)

    context = {
        'contact': cont,
    }
    return render(request, 'service/admin_panel_templates/mains_and_adds/ask_del_contact.html', context)


def delete_contact(request, contact_id):
    """
    Renders the page which tells a user that a contact inquiry has been deleted.
    """

    check_super_user(request)

    cont = get_object_or_404(Contact, pk=contact_id)

    cont.delete()
    return render(request, 'service/admin_panel_templates/deletes/contact_deleted.html')


def pricing(request):
    """
    Renders the page for checking prices for certain objects.
    """

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
    return render(request, 'service/admin_panel_templates/mains_and_adds/pricing.html', context)


def page_price(request):
    """
    Renders the page for adding page prices for a book.
    """

    check_super_user(request)

    page_prices = PagePrice.objects.all()
    list_of_dicts = get_price_dicts(page_prices)

    if request.method != 'POST':
        form = PagePriceForm()
    else:
        form = PagePriceForm(data=request.POST)
        if form.is_valid():
            new_price = form.save(commit=False)
            if match_with_existing_prices(list_of_dicts, new_price):
                form.add_error('date', "")
                form.add_error('type', "")
                form.add_error('size', "")
                messages.error(request, "Kiritilgan sana, tur va o'lcham bo'yicha narx mavjud!")
            else:
                try:
                    def_or_redef_page_price(new_price)
                except Http404:
                    return render(request,
                                  'service/admin_panel_templates/exception_pages/external_prices_insufficient.html')
                except RequestAborted:
                    return render(request, 'service/admin_panel_templates/exception_pages/multiple_objects_3.html')
                new_price.save()
                return redirect('pricing')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
    }
    return render(request, 'service/admin_panel_templates/mains_and_adds/page_price.html', context)


def edit_page_price(request, pageprice_id):
    """
    Renders the page for editing a page price.
    """

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
            elif match_with_existing_prices(list_of_dicts, edited_price):
                form.add_error('date', "")
                form.add_error('type', "")
                form.add_error('size', "")
                messages.error(request, "Kiritilgan sana, tur va o'lcham bo'yicha narx mavjud!")
            else:
                try:
                    def_or_redef_page_price(edited_price)
                except Http404:
                    return render(request,
                                  'service/admin_panel_templates/exception_pages/external_prices_insufficient.html')
                except RequestAborted:
                    return render(request, 'service/admin_panel_templates/exception_pages/multiple_objects_3.html')
                edited_price.save()
                return redirect('pricing')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'p_price': p_price,
    }
    return render(request, 'service/admin_panel_templates/edits/edit_page_price.html', context)


def delete_page_price(request, pageprice_id):
    """
    Renders the page which tells a user that a page price has been deleted.
    """

    check_super_user(request)

    p_price = get_object_or_404(PagePrice, pk=pageprice_id)

    p_price.delete()
    return render(request, 'service/admin_panel_templates/deletes/page_price_deleted.html')


def binding_price(request):
    """
    Renders the page for adding a binding price for books.
    """

    check_super_user(request)

    binding_prices = BindingPrice.objects.all()
    list_of_price_dicts = get_price_dicts(binding_prices)

    if request.method != 'POST':
        form = BindingPriceForm()
    else:
        form = BindingPriceForm(data=request.POST)
        if form.is_valid():
            new_price = form.save(commit=False)
            if match_with_existing_prices(list_of_price_dicts, new_price):
                form.add_error('date', "")
                form.add_error('type', "")
                form.add_error('size', "")
                messages.error(request, "Kiritilgan sana, tur va o'lcham bo'yicha narx mavjud!")
            else:
                try:
                    def_or_redef_binding_price(new_price)
                except Http404:
                    return render(request,
                                  'service/admin_panel_templates/exception_pages/external_prices_donotexist.html')
                except RequestAborted:
                    return render(request, 'service/admin_panel_templates/exception_pages/multiple_objects_1.html')
                else:
                    new_price.save()
                    return redirect('pricing')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri kiritildi!")

    context = {
        'form': form,
    }
    return render(request, 'service/admin_panel_templates/mains_and_adds/binding_price.html', context)


def edit_binding_price(request, bindingprice_id):
    """
    Renders the page for editing a binding price.
    """

    check_super_user(request)

    binding_prices = BindingPrice.objects.all()
    list_of_price_dicts = get_price_dicts(binding_prices)

    bprice = get_object_or_404(BindingPrice, pk=bindingprice_id)

    if request.method != 'POST':
        form = BindingPriceForm(instance=bprice)
    else:
        form = BindingPriceForm(data=request.POST, instance=bprice)
        if form.is_valid():
            edited_price = form.save(commit=False)
            if not form.has_changed():
                return redirect('pricing')
            elif match_with_existing_prices(list_of_price_dicts, edited_price):
                form.add_error('date', "")
                form.add_error('type', "")
                form.add_error('size', "")
                messages.error(request, "Kiritilgan sana, tur va o'lcham bo'yicha narx mavjud!")
            else:
                try:
                    def_or_redef_binding_price(edited_price)
                except Http404:
                    return render(request,
                                  'service/admin_panel_templates/exception_pages/external_prices_donotexist.html')
                except RequestAborted:
                    return render(request, 'service/admin_panel_templates/exception_pages/multiple_objects_1.html')
                else:
                    edited_price.save()
                    return redirect('pricing')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'bprice': bprice,
    }
    return render(request, 'service/admin_panel_templates/edits/edit_binding_price.html', context)


def delete_binding_price(request, bindingprice_id):
    """
    Renders the page which tells a user that a binding price has been deleted.
    """

    check_super_user(request)

    bprice = get_object_or_404(BindingPrice, pk=bindingprice_id)

    bprice.delete()
    return render(request, 'service/admin_panel_templates/deletes/binding_deleted.html')


def ring_price(request):
    """
    Renders the page for adding a ring price.
    """

    check_super_user(request)

    ring_prices = RingPrice.objects.all()
    list_of_dicts = get_price_dicts(ring_prices)

    if request.method != 'POST':
        form = RingPriceForm()
    else:
        form = RingPriceForm(data=request.POST)
        if form.is_valid():
            new_price = form.save(commit=False)
            if match_with_existing_prices(list_of_dicts, new_price):
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
    return render(request, 'service/admin_panel_templates/mains_and_adds/ring_price.html', context)


def edit_ring_price(request, ringprice_id):
    """
    Renders the page for editing a ring price.
    """

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
            elif match_with_existing_prices(list_of_dicts, edited_price):
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
    return render(request, 'service/admin_panel_templates/edits/edit_ring_price.html', context)


def delete_ring_price(request, ringprice_id):
    """
    Renders the page which tells a user that a ring price has been deleted.
    """

    check_super_user(request)

    r_price = get_object_or_404(RingPrice, pk=ringprice_id)

    r_price.delete()
    return render(request, 'service/admin_panel_templates/deletes/ring_price_deleted.html')


def color_price(request):
    """
    Renders the page for adding a color price.
    """

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
    return render(request, 'service/admin_panel_templates/mains_and_adds/color_price.html', context)


def edit_color_price(request, colorprice_id):
    """
    Renders the page for editing a color price.
    """

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
                    return render(request, 'service/admin_panel_templates/exception_pages/multiple_objects_4.html')
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
                    return render(request, 'service/admin_panel_templates/exception_pages/multiple_objects_4.html')
                else:
                    edited_price.save()
                    return redirect('pricing')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'c_price': c_price,
        'form': form,
    }
    return render(request, 'service/admin_panel_templates/edits/edit_color_price.html', context)


def delete_color_price(request, colorprice_id):
    """
    Renders the page which tells a user that a color price has been deleted.
    """

    check_super_user(request)

    c_price = get_object_or_404(ColorPrice, pk=colorprice_id)

    page_prices = PagePrice.objects.filter(date=c_price.date,
                                           type__icontains=c_price.color,
                                           size=c_price.size)

    # Get the list of page price dictionaries to check whether there are no duplicates
    list_of_dicts = get_price_dicts(page_prices)

    if not page_prices:
        c_price.delete()
        return render(request, 'service/admin_panel_templates/deletes/color_price_deleted.html')
    elif find_duplicates(list_of_dicts):
        return render(request, 'service/admin_panel_templates/exception_pages/multiple_objects_4.html')
    else:
        context = {
            'page_prices': page_prices,
        }
        return render(request, 'service/admin_panel_templates/exception_pages/not_delete_color_price.html', context)


def cover_price(request):
    """
    Renders the page for adding a cover price.
    ."""

    check_super_user(request)

    cover_prices = CoverPrice.objects.all()
    list_of_dicts = get_price_dicts(cover_prices)

    if request.method != 'POST':
        form = CoverPriceForm()
    else:
        form = CoverPriceForm(data=request.POST)
        if form.is_valid():
            new_price = form.save(commit=False)
            if match_with_existing_prices(list_of_dicts, new_price):
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
    return render(request, 'service/admin_panel_templates/mains_and_adds/cover_price.html', context)


def edit_cover_price(request, coverprice_id):
    """
    Renders the page for editing a cover price.
    """

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
                    return render(request, 'service/admin_panel_templates/exception_pages/multiple_objects_2.html')
                else:
                    edited_price.save()
                    return redirect('pricing')
            elif match_with_existing_prices(list_of_dicts, edited_price):
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
                    return render(request, 'service/admin_panel_templates/exception_pages/multiple_objects_2.html')
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
    return render(request, 'service/admin_panel_templates/edits/edit_cover_price.html', context)


def delete_cover_price(request, coverprice_id):
    """
    Renders the page which tells a user that a cover price has been deleted.
    """

    check_super_user(request)

    c_price = get_object_or_404(CoverPrice, pk=coverprice_id)

    try:
        bprice = None
        if c_price.type == "Plastik prujinali ulash uchun":
            try:
                bprice = BindingPrice.objects.get(date=c_price.date,
                                                  type="Plastik prujinalash",
                                                  size=c_price.size)
            except ObjectDoesNotExist:
                raise Http404
            except MultipleObjectsReturned:
                raise RequestAborted
        elif c_price.type == "Metal prujinali ulash uchun":
            try:
                bprice = BindingPrice.objects.get(date=c_price.date,
                                                  type="Metal prujinalash",
                                                  size=c_price.size)
            except ObjectDoesNotExist:
                raise Http404
            except MultipleObjectsReturned:
                raise RequestAborted
        elif c_price.type == "Yelimli ulash uchun (Yumshoq)":
            try:
                bprice = BindingPrice.objects.get(date=c_price.date,
                                                  type="Yumshoq muqovali yelimlash",
                                                  size=c_price.size)
            except ObjectDoesNotExist:
                raise Http404
            except MultipleObjectsReturned:
                raise RequestAborted
        elif c_price.type == "Yelimli ulash uchun (Qattiq)":
            try:
                bprice = BindingPrice.objects.get(date=c_price.date,
                                                  type="Qattiq muqovali yelimlash",
                                                  size=c_price.size)
            except ObjectDoesNotExist:
                raise Http404
            except MultipleObjectsReturned:
                raise RequestAborted
    except Http404:
        c_price.delete()
        return render(request, 'service/admin_panel_templates/deletes/cover_price_deleted.html')
    except RequestAborted:
        return render(request, 'service/admin_panel_templates/exception_pages/multiple_objects_2.html')
    else:
        context = {
            'bprice': bprice,
        }
        return render(request, 'service/admin_panel_templates/exception_pages/not_delete_cover_price.html', context)


def glue_price(request):
    """
    Renders the page for adding a glue price.
    """

    check_super_user(request)

    glue_prices = GluePrice.objects.all()
    list_of_dicts = list(get_price_dicts(glue_prices))

    if request.method != 'POST':
        form = GluePriceForm()
    else:
        form = GluePriceForm(data=request.POST)
        if form.is_valid():
            new_price = form.save(commit=False)
            if match_with_existing_prices(list_of_dicts, new_price):
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
    return render(request, 'service/admin_panel_templates/mains_and_adds/glue_price.html', context)


def edit_glue_price(request, glueprice_id):
    """
    Renders the page for editing a glue price.
    """

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
                    return render(request, 'service/admin_panel_templates/exception_pages/multiple_objects_2.html')
                else:
                    edited_price.save()
                    return redirect('pricing')
            elif match_with_existing_prices(list_of_dicts, edited_price):
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
                    return render(request, 'service/admin_panel_templates/exception_pages/multiple_objects_2.html')
                else:
                    edited_price.save()
                    return redirect('pricing')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'g_price': g_price,
    }
    return render(request, 'service/admin_panel_templates/edits/edit_glue_price.html', context)


def delete_glue_price(request, glueprice_id):
    """
    Renders the page which tells a user that a glue price has been deleted.
    """

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
        return render(request, 'service/admin_panel_templates/deletes/glue_price_deleted.html')
    except RequestAborted:
        return render(request, 'service/admin_panel_templates/exception_pages/multiple_objects_2.html')
    else:
        context = {
            'sg_binding_price': sg_binding_price,
            'hg_binding_price': hg_binding_price,
        }
        return render(request, 'service/admin_panel_templates/exception_pages/not_delete_glue_price.html', context)


def paper_price(request):
    """
    Renders the page for adding a paper price.
    """

    check_super_user(request)

    paper_prices = PaperPrice.objects.all()
    list_of_dicts = get_price_dicts(paper_prices)

    if request.method != 'POST':
        form = PaperPriceForm()
    else:
        form = PaperPriceForm(data=request.POST)
        if form.is_valid():
            new_price = form.save(commit=False)
            if match_with_existing_prices(list_of_dicts, new_price):
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
    return render(request, 'service/admin_panel_templates/mains_and_adds/paper_price.html', context)


def edit_paper_price(request, paperprice_id):
    """
    Renders the page for editing a paper price.
    """

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
                    return render(request, 'service/admin_panel_templates/exception_pages/multiple_objects_4.html')
                else:
                    edited_price.save()
                    return redirect('pricing')
            elif match_with_existing_prices(list_of_dicts, edited_price):
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
                    return render(request, 'service/admin_panel_templates/exception_pages/multiple_objects_4.html')
                else:
                    edited_price.save()
                    return redirect('pricing')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'p_price': p_price,
    }
    return render(request, 'service/admin_panel_templates/edits/edit_paper_price.html', context)


def delete_paper_price(request, paperprice_id):
    """
    Renders the page which tells a user that a paper price has been deleted.
    """

    check_super_user(request)

    p_price = get_object_or_404(PaperPrice, pk=paperprice_id)

    page_prices = PagePrice.objects.filter(date=p_price.date,
                                           type__icontains=p_price.type,
                                           size=p_price.size)

    # Get the list of page prices to check whether there are no duplicates
    list_of_dicts = get_price_dicts(page_prices)

    if not page_prices:
        p_price.delete()
        return render(request, 'service/admin_panel_templates/deletes/paper_price_deleted.html')
    elif find_duplicates(list_of_dicts):
        return render(request, 'service/admin_panel_templates/exception_pages/multiple_objects_4.html')
    else:
        context = {
            'page_prices': page_prices,
        }
        return render(request, 'service/admin_panel_templates/exception_pages/not_delete_paper_price.html', context)


def yarn_price(request):
    """
    Renders the page for adding a yarn price.
    """

    check_super_user(request)

    yarn_prices = YarnPrice.objects.all()
    list_of_dicts = get_price_dicts(yarn_prices)

    if request.method != 'POST':
        form = YarnPriceForm()
    else:
        form = YarnPriceForm(data=request.POST)
        if form.is_valid():
            new_price = form.save(commit=False)
            if match_with_existing_prices(list_of_dicts, new_price):
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
    return render(request, 'service/admin_panel_templates/mains_and_adds/yarn_price.html', context)


def edit_yarn_price(request, yarnprice_id):
    """
    Renders the page for editing a yarn price.
    """

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
                    return render(request, 'service/admin_panel_templates/exception_pages/multiple_objects_2.html')
                else:
                    edited_price.save()
                    return redirect('pricing')
            elif match_with_existing_prices(list_of_dicts, edited_price):
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
                    return render(request, 'service/admin_panel_templates/exception_pages/multiple_objects_2.html')
                else:
                    edited_price.save()
                    return redirect('pricing')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'y_price': y_price,
    }
    return render(request, 'service/admin_panel_templates/edits/edit_yarn_price.html', context)


def delete_yarn_price(request, yarnprice_id):
    """
    Renders the page which tells a user that a yarn price has been deleted.
    """

    check_super_user(request)

    y_price = get_object_or_404(YarnPrice, pk=yarnprice_id)

    if y_price.type == "Yupqa":
        try:
            bprice = get_object_or_404(BindingPrice,
                                       date=y_price.date,
                                       type="Yumshoq muqovali yelimlash",
                                       size=y_price.size)
        except Http404:
            y_price.delete()
            return render(request, 'service/admin_panel_templates/deletes/yarn_price_deleted.html')
        except MultipleObjectsReturned:
            return render(request, 'service/admin_panel_templates/exception_pages/multiple_objects_2.html')
        else:
            context = {
                'bprice': bprice,
            }
            return render(request, 'service/admin_panel_templates/exception_pages/not_delete_yarn_price.html', context)
    elif y_price.type == "O'rtacha":
        try:
            bprice = get_object_or_404(BindingPrice,
                                       date=y_price.date,
                                       type="Qattiq muqovali yelimlash",
                                       size=y_price.size)
        except Http404:
            y_price.delete()
            return render(request, 'service/admin_panel_templates/deletes/yarn_price_deleted.html')
        except MultipleObjectsReturned:
            return render(request, 'service/admin_panel_templates/exception_pages/multiple_objects_2.html')
        else:
            context = {
                'bprice': bprice,
            }
            return render(request, 'service/admin_panel_templates/exception_pages/not_delete_yarn_price.html', context)
    # For now, we can delete prices of any other types of yarn as no other binding types are provided by the service
    else:
        y_price.delete()
        return render(request, 'service/admin_panel_templates/deletes/yarn_price_deleted.html')


def outer_prices(request):
    """
    Renders the page for adding outer expenses and a profit.
    """

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
    return render(request, 'service/admin_panel_templates/mains_and_adds/outer_prices.html', context)


def edit_outer_prices(request, outerprice_id):
    """
    Renders the page for editing an outer expenses and a profit.
    """

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
                    return render(request, 'service/admin_panel_templates/exception_pages/multiple_objects_2.html')
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
                    return render(request, 'service/admin_panel_templates/exception_pages/multiple_objects_2.html')
                else:
                    edited_prices.save()
                    return redirect('pricing')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'out_prices': out_prices,
    }
    return render(request, 'service/admin_panel_templates/edits/edit_outer_prices.html', context)


def delete_outer_prices(request, outerprice_id):
    """
    Renders the page which tells a user that an outer expenses and a profit has been deleted.
    """

    check_super_user(request)

    out_prices = get_object_or_404(OuterPrice, pk=outerprice_id)

    binding_prices = BindingPrice.objects.filter(date=out_prices.date)
    page_prices = PagePrice.objects.filter(date=out_prices.date)

    # Get the list of binding and page price dictionaries to check whether there are no duplicates
    list_of_binding_price_dicts = get_price_dicts(binding_prices)
    list_of_page_price_dicts = get_price_dicts(page_prices)

    if not binding_prices and not page_prices:
        out_prices.delete()
        return render(request, 'service/admin_panel_templates/deletes/outer_prices_deleted.html')
    elif find_duplicates(list_of_binding_price_dicts) or find_duplicates(list_of_page_price_dicts):
        return render(request, 'service/admin_panel_templates/exception_pages/multiple_objects_2.html')
    else:
        context = {
            'binding_prices': binding_prices,
            'page_prices': page_prices,
        }
        return render(request, 'service/admin_panel_templates/exception_pages/not_delete_out_exps.html', context)


def coupons(request):
    """
    Renders the page for either checking or adding coupons.
    """

    check_super_user(request)

    coupon_objects = Coupon.objects.all().order_by('date_release')
    codes = get_codes(coupon_objects)

    if request.method != 'POST':
        form = CouponForm()
    else:
        form = CouponForm(data=request.POST)
        if form.is_valid():
            new_coupon = form.save(commit=False)
            # The below functions call the code generator and return the codes as long as they do not exist
            # in the database
            code_1 = get_code_1(codes)
            code_2 = get_code_2(codes)
            if new_coupon.for_retail is False:
                new_coupon.code_1 = code_1
            elif new_coupon.for_retail is True:
                new_coupon.code_2 = code_2
            new_coupon.save()
            return redirect('coupons')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'coupon_objects': coupon_objects,
        'form': form,
    }
    return render(request, 'service/admin_panel_templates/mains_and_adds/coupons.html', context)


def edit_coupon(request, coupon_id):
    """
    Renders the page for editing a coupon.
    """

    check_super_user(request)

    coupon_objects = Coupon.objects.all()
    codes = get_codes(coupon_objects)

    coupon = get_object_or_404(Coupon, pk=coupon_id)

    if request.method != 'POST':
        form = CouponForm(instance=coupon)
    else:
        form = CouponForm(data=request.POST, instance=coupon)
        if form.is_valid():
            edited_coupon = form.save(commit=False)
            # The below functions call the code generator and return the codes as long as they do not exist
            # in the database
            code_1 = get_code_1(codes)
            code_2 = get_code_2(codes)
            if not form.has_changed() and 'change_code' in request.POST:
                if edited_coupon.code_1:
                    edited_coupon.code_1 = code_1
                elif edited_coupon.code_2:
                    edited_coupon.code_2 = code_2
            elif 'change_code' in request.POST and edited_coupon.code_1:
                edited_coupon.code_1 = code_1
            elif 'change_code' in request.POST and edited_coupon.code_2:
                edited_coupon.code_2 = code_2
            edited_coupon.save()
            return redirect('coupons')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'coupon': coupon,
        'form': form,
    }
    return render(request, 'service/admin_panel_templates/edits/edit_coupon.html', context)


def delete_coupon(request, coupon_id):
    """
    Renders the page which tells a user that a coupon has been deleted.
    """

    check_super_user(request)

    coupon = get_object_or_404(Coupon, pk=coupon_id)

    coupon.delete()
    return render(request, 'service/admin_panel_templates/deletes/coupon_deleted.html')


def printer_info(request):
    """
    Renders the page for either checking or adding printer information.
    """

    check_super_user(request)

    printer_information = Printer.objects.all()
    list_of_printers = get_printer_brand_dicts(printer_information)
    printers_num = len(printer_information)

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
                return redirect('printer_info')
            elif match_with_existing_printers(list_of_printers, new_info):
                new_info.model += f' ({int(printers_num) + 1})'
                new_info.save()
                return redirect('printer_info')
            else:
                new_info.save()
                return redirect('printer_info')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'printer_information': printer_information,
        'printers_num': printers_num,
        'printer_refill_page_counts': printer_refill_page_counts,
    }
    return render(request, 'service/admin_panel_templates/mains_and_adds/printer_info.html', context)


def edit_printer_info(request, printer_id):
    """Renders the page for editing printer information."""

    check_super_user(request)

    printer_info_queryset = Printer.objects.all()
    list_of_dicts = get_printer_brand_dicts(printer_info_queryset)

    printer_information = get_object_or_404(Printer, pk=printer_id)

    if request.method != 'POST':
        form = PrinterForm(instance=printer_information)
    else:
        form = PrinterForm(data=request.POST, instance=printer_information)
        if form.is_valid():
            edited_info = form.save(commit=False)
            brand_changed = 'brand' in form.changed_data
            model_changed = 'model' in form.changed_data
            if not form.has_changed():
                return redirect('printer_info')
            elif form.has_changed() and True not in [brand_changed, model_changed]:
                edited_info.save()
                return redirect('printer_info')
            elif match_with_existing_printers(list_of_dicts, edited_info):
                form.add_error('brand', "")
                form.add_error('model', "")
                messages.error(request, "Kiritilgan marka, model va uning raqami bo'yicha ma'lumotlar mavjud!")
            else:
                edited_info.save()
                return redirect('printer_info')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'printer_information': printer_information,
    }
    return render(request, 'service/admin_panel_templates/edits/edit_printer_info.html', context)


def delete_printer_info(request, printer_id):
    """
    Renders the page which tells a user that printer information has been deleted.

    There can raise a ProtectedError exception because of the connection between printer information and
    refill-and-page-count information.
    """

    check_super_user(request)

    printer_information = get_object_or_404(Printer, pk=printer_id)

    try:
        printer_information.delete()
    except ProtectedError:
        return render(request, 'service/admin_panel_templates/exception_pages/not_delete_printer_info.html')
    else:
        return render(request, 'service/admin_panel_templates/deletes/printer_info_deleted.html')


def add_refill_page_count(request):
    """
    Renders the page for adding refill and page count information.
    """

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
                    return render(request, 'service/admin_panel_templates/exception_pages/printer_info_not_found.html')
                except RequestAborted:
                    return render(request, 'service/admin_panel_templates/exception_pages/multiple_objects_5.html')
                else:
                    new_info.save()
                    return redirect('printer_info')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
    }
    return render(request, 'service/admin_panel_templates/mains_and_adds/add_refill_page_count.html', context)


def edit_refill_page_count(request, refillandpagecount_id):
    """
    Renders the page for editing refill and page count information.
    """

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
                return redirect('printer_info')
            elif form.has_changed() and printer_changed is False:
                try:
                    # Find the correlating printer info and change its CURRENT_PAGE_COUNT based on the changes made
                    # in refill and page count
                    find_and_change_4(edited_info=edited_info,
                                      initial_count=info_printed,
                                      date_changed=date_changed)
                except Http404:
                    return render(request, 'service/admin_panel_templates/exception_pages/printer_info_not_found.html')
                except RequestAborted:
                    return render(request, 'service/admin_panel_templates/exception_pages/multiple_objects_5.html')
                else:
                    edited_info.save()
                    return redirect('printer_info')
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
                    return render(request, 'service/admin_panel_templates/exception_pages/printer_info_not_found.html')
                except RequestAborted:
                    return render(request, 'service/admin_panel_templates/exception_pages/multiple_objects_5.html')
                else:
                    edited_info.save()
                    return redirect('printer_info')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'info': info,
    }
    return render(request, 'service/admin_panel_templates/edits/edit_refill_page_count.html', context)


def delete_refill_page_count(request, refillandpagecount_id):
    """
    Renders the page which tells a user that refill and page count information has been deleted.
    """

    check_super_user(request)

    info = get_object_or_404(RefillAndPageCount, pk=refillandpagecount_id)

    info.delete()
    return render(request, 'service/admin_panel_templates/deletes/refill_page_count_deleted.html')


def rtypes(request):
    """
    Renders the page for either checking or adding resource types.
    """

    check_super_user(request)

    types = RType.objects.all()
    list_of_types = get_types(types)
    types_num = len(types)

    if request.method != 'POST':
        form = RTypeForm()
    else:
        form = RTypeForm(data=request.POST)
        if form.is_valid():
            new_type = form.save(commit=False)
            if str(new_type.type) in list_of_types:
                form.add_error('type', "")
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
    return render(request, 'service/admin_panel_templates/mains_and_adds/rtypes.html', context)


def edit_rtype(request, rtype_id):
    """
    Renders the page for editing a resource type.
    """

    check_super_user(request)

    types = RType.objects.all()
    list_of_types = get_types(types)

    rtype = get_object_or_404(RType, pk=rtype_id)

    if request.method != 'POST':
        form = RTypeForm(instance=rtype)
    else:
        form = RTypeForm(data=request.POST, instance=rtype)
        if form.is_valid():
            edited_type = form.save(commit=False)
            if not form.has_changed():
                return redirect('rtypes')
            elif str(edited_type.type) in list_of_types:
                form.add_error('type', "")
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
    return render(request, 'service/admin_panel_templates/edits/edit_rtype.html', context)


def delete_rtype(request, rtype_id):
    """
    Renders the page which tells a user that a resource type has been deleted.

    There can raise a ProtectedError exception because of the connection between resource information
    and resource types.
    """

    check_super_user(request)

    rtype = get_object_or_404(RType, pk=rtype_id)

    try:
        rtype.delete()
    except ProtectedError:
        return render(request, 'service/admin_panel_templates/exception_pages/not_delete_rtype.html')
    else:
        return render(request, 'service/admin_panel_templates/deletes/rtype_deleted.html')


def resources(request):
    """
    Renders the page for either checking or adding resource information.
    """

    check_super_user(request)

    res_s = Resource.objects.all()
    rtype_objs = RType.objects.all()
    dicts = get_dicts(rtype_objs)

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
    return render(request, 'service/admin_panel_templates/mains_and_adds/resources.html', context)


def edit_resource(request, resource_id):
    """
    Renders the page for editing resource information.
    """

    check_super_user(request)

    resource = get_object_or_404(Resource, pk=resource_id)
    rtype_objs = RType.objects.all()
    dicts = get_dicts(rtype_objs)

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
    return render(request, 'service/admin_panel_templates/edits/edit_resource.html', context)


def delete_resource(request, resource_id):
    """
    Renders the page which tells a user that resource information has been deleted.
    """

    check_super_user(request)

    resource = get_object_or_404(Resource, pk=resource_id)
    resource.delete()
    return render(request, 'service/admin_panel_templates/deletes/resource_deleted.html')


def complaints(request):
    """
    Renders the page for checking complaints.
    """

    check_super_user(request)

    complaint_objects = Complaint.objects.all()
    complaints_num = len(complaint_objects)

    context = {
        'complaint_objects': complaint_objects,
        'complaints_num': complaints_num,
    }
    return render(request, 'service/admin_panel_templates/mains_and_adds/complaints.html', context)


def ask_del_complaint(request, complaint_id):
    """
    Renders the page which asks a user whether they are sure about deleting a complaint.
    """

    check_super_user(request)

    complaint = get_object_or_404(Complaint, pk=complaint_id)
    context = {
        'complaint': complaint,
    }
    return render(request, 'service/admin_panel_templates/mains_and_adds/ask_del_complaint.html', context)


def delete_complaint(request, complaint_id):
    """
    Renders the page which tells a user that a complaint has been deleted.
    """

    check_super_user(request)

    complaint = get_object_or_404(Complaint, pk=complaint_id)
    complaint.delete()
    return render(request, 'service/admin_panel_templates/deletes/complaint_deleted.html')


def news(request):
    """
    Renders the page for either checking or adding news.
    """

    check_super_user(request)

    news_objects = News.objects.all().order_by('-date_added')
    news_num = len(news_objects)

    if request.method != 'POST':
        form = NewsForm()
    else:
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            new = form.save(commit=False)
            new.publisher = request.user
            new.save()
            return redirect('news')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'news_objects': news_objects,
        'news_num': news_num,
    }
    return render(request, 'service/admin_panel_templates/mains_and_adds/news.html', context)


def edit_news(request, news_id):
    """
    Renders the page for editing news.
    """

    check_super_user(request)

    news_object = News.objects.get(pk=news_id)

    if request.method != 'POST':
        form = NewsForm(instance=news_object)
    else:
        form = NewsForm(request.POST, request.FILES, instance=news_object)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.publisher = request.user
            new_form.save()
            return redirect('news')
        else:
            messages.error(request, "Ma'lumotlar noto'g'ri to'ldirildi!")

    context = {
        'form': form,
        'news_object': news_object,
    }
    return render(request, 'service/admin_panel_templates/edits/edit_news.html', context)


def delete_news(request, news_id):
    """
    Renders the page which tells a user that news has been deleted.
    """

    check_super_user(request)

    new = get_object_or_404(News, pk=news_id)

    new.delete()
    return render(request, 'service/admin_panel_templates/deletes/news_deleted.html')


def ltypes(request):
    """
    Renders the page for either checking or adding loss types.
    """

    check_super_user(request)

    types = LType.objects.all()
    list_of_types = get_types(types)
    types_num = len(types)

    if request.method != 'POST':
        form = LTypeForm()
    else:
        form = LTypeForm(data=request.POST)
        if form.is_valid():
            new_type = form.save(commit=False)
            if str(new_type.type) in list_of_types:
                form.add_error('type', "")
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
    return render(request, 'service/admin_panel_templates/mains_and_adds/ltypes.html', context)


def edit_ltype(request, ltype_id):
    """
    Renders the page for editing a loss type.
    """

    check_super_user(request)

    types = LType.objects.all()
    list_of_types = get_types(types)

    ltype = get_object_or_404(LType, pk=ltype_id)

    if request.method != 'POST':
        form = LTypeForm(instance=ltype)
    else:
        form = LTypeForm(data=request.POST, instance=ltype)
        if form.is_valid():
            edited_type = form.save(commit=False)
            if not form.has_changed():
                return redirect('ltypes')
            elif str(edited_type.type) in list_of_types:
                form.add_error('type', "")
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
    return render(request, 'service/admin_panel_templates/edits/edit_ltype.html', context)


def delete_ltype(request, ltype_id):
    """
    Renders the page which tells a user that a loss type has been deleted.

    There can raise a ProtectedError exception because of the connection between losses and loss types.
    """

    check_super_user(request)

    ltype = get_object_or_404(LType, pk=ltype_id)

    try:
        ltype.delete()
    except ProtectedError:
        return render(request, 'service/admin_panel_templates/exception_pages/not_delete_ltype.html')
    else:
        return render(request, 'service/admin_panel_templates/deletes/ltype_deleted.html')


def losses(request):
    """
    Renders the page for either checking or adding losses.
    """

    check_super_user(request)

    the_losses = Loss.objects.all()
    losses_num = len(the_losses)
    types = LType.objects.all()
    dicts = get_dicts(types)

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
    return render(request, 'service/admin_panel_templates/mains_and_adds/losses.html', context)


def edit_loss(request, loss_id):
    """
    Renders the page for editing a loss.
    """

    check_super_user(request)

    loss = get_object_or_404(Loss, pk=loss_id)
    the_ltypes = LType.objects.all()
    dicts = get_dicts(the_ltypes)

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
    return render(request, 'service/admin_panel_templates/edits/edit_loss.html', context)


def delete_loss(request, loss_id):
    """
    Renders the page which tells a user that a loss has been deleted.
    """

    check_super_user(request)

    loss = get_object_or_404(Loss, pk=loss_id)

    loss.delete()
    return render(request, 'service/admin_panel_templates/deletes/loss_deleted.html')
