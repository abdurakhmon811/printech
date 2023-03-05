"""Assisting functions for the view functions."""
from .models import BindingPrice, \
    ColorPrice, CoverPrice, \
    GluePrice, \
    OuterPrice, \
    PagePrice, PaperPrice, Printer, \
    YarnPrice
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist, RequestAborted
from django.http import Http404
from django.shortcuts import get_object_or_404
from random import choice, shuffle
import decimal
import math
import json


def change_account_means(initial_val,
                         edited_val,
                         account=None,
                         account_1=None,
                         account_2=None,
                         income_edited=False,
                         expense_edited=False,
                         transaction_edited=False):
    """
    An assisting function for view functions.

    Used in the INCOMES_EXPENSES section.

    :param initial_val: Pass this parameter to make calculations.
    :param edited_val: Pass this parameter to make calculations.
    :param account: Pass this parameter if either an income or an expense is being edited.
    :param account_1: Pass this parameter if a transaction is being edited.
    :param account_2: Pass this parameter if a transaction is being edited.
    :param income_edited: Set this parameter to True if an income is edited.
    :param expense_edited: Set this parameter to True if an expense is edited.
    :param transaction_edited: Set this parameter to True if a transaction is being edited.
    :return Will return nothing, but will change the means of an account chosen.
    """

    if income_edited and account is not None:
        if edited_val == initial_val:
            pass
        elif edited_val > initial_val:
            gap = edited_val - initial_val
            account.means.amount += gap
        elif edited_val < initial_val:
            gap = initial_val - edited_val
            account.means.amount -= gap
        account.save()
    elif expense_edited and account is not None:
        if edited_val == initial_val:
            pass
        elif edited_val > initial_val:
            gap = edited_val - initial_val
            account.means.amount -= gap
        elif edited_val < initial_val:
            gap = initial_val - edited_val
            account.means.amount += gap
        account.save()
    elif account_1 is not None and account_2 is not None and transaction_edited:
        if edited_val == initial_val:
            pass
        elif edited_val > initial_val:
            gap = edited_val - initial_val
            account_1.means.amount -= gap
            account_2.means.amount += gap
        elif edited_val < initial_val:
            gap = initial_val - edited_val
            account_1.means.amount += gap
            account_2.means.amount -= gap
        account_1.save()
        account_2.save()


def check_super_user(request):
    """
    An assisting function for view functions.

    Should be used in every view function of the admin panel.

    Checks whether a requesting user is a super user or not. If not throws an Http404.
    """

    if request.user.is_superuser:
        pass
    else:
        raise Http404


def check_user(request, user):
    """
    An assisting function for view functions.

    Is used when a requesting user should be checked whether they own an object they are requesting.
    """

    if request.user == user:
        pass
    else:
        raise Http404


def edit_bprice(**kwargs):
    """
    An assisting function in general.

    Is used to change the current price for binding when correlated prices are changed.

    :param kwargs: Takes in three arguments - edited_price_val, initial_price_val and price_to_be_changed.
    NOTE: edited_price_val and initial_price_val take in django-money's Money field.
    The last parameter takes in an instance with PRICE attribute.
    """

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
    """
    An assisting function in general.

    Is used to change the current price for a single page when correlated prices are changed.

    :param kwargs: Takes in four arguments - edited_price, edited_price_val, initial_price_val and price_to_be_changed.
    NOTE: edited_price takes in an instance with an important attribute price, and either type or color.
    edited_price_val and initial_price_val take in django-money's Money field.
    The last parameter takes in an instance with PRICE attribute.
    """

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
    An assisting function for view functions.

    accounted and new_info parameters are used when a new count is added to the count information for printers.

    edited_info and initial_info parameters are used when an existing count information is edited.

    The parameter count_to_be_changed is used in both cases as it is the target to be changed.
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
    """
    An assisting function for view functions.

    :param price: Takes in the price of binding only.
    """

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
    """
    An assisting function for view functions.

    :param price: Takes in the price of page only.
    """

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
    """
    An assisting function for view functions.

    :param kwargs: Takes in three arguments - edited_price, edited_price_val and initial_price_val.
    edited_price parameter should be an instance of the cover price.
    Next two parameters should be django-money's Money field.
    """

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
    """
    An assisting function for view functions.

    :param kwargs: Takes in three arguments - edited_price, edited_price_val and initial_price_val.
    edited_price parameter should be an instance of either glue or yarn prices.
    Next two parameters should be django-money's Money field.
    """

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
        # In "else" cases types can be the types of glue which are insignificant for now.
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
    """
    An assisting function for view functions.

    :param kwargs: Takes in three arguments - edited_price, edited_price_val and initial_price_val.
    edited_price parameter should be an instance of either color or paper prices.
    Next two parameters should be django-money's Money field.
    """

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
    """
    An assisting function for view functions.

    :param new_info: If new information on printers is being added, pass this parameter that new information's instance.
    :param edited_info: If existing information on printers is being edited, pass this parameter
    that information's edited instance.
    :param initial_count: This parameter is used together with edited_info.
    :param date_changed: This parameter is used together with edited_info.
    """

    if new_info is not None:
        words = get_list_of_words_2(str(new_info.printer))
        brand, *model_and_number = words
        model = ' '.join(model_and_number)
        try:
            printer_information = get_object_or_404(Printer,
                                                    brand=brand,
                                                    model=model)
        except MultipleObjectsReturned:
            raise RequestAborted
        else:
            edit_printercount(accounted=bool(new_info.accounted),
                              new_info=new_info,
                              count_to_be_changed=printer_information)
    elif edited_info is not None and initial_count is not None and date_changed is False:
        words = get_list_of_words_2(str(edited_info.printer))
        brand, *model_and_number = words
        model = ' '.join(model_and_number)
        try:
            printer_information = get_object_or_404(Printer,
                                                    brand=brand,
                                                    model=model)
        except MultipleObjectsReturned:
            raise RequestAborted
        else:
            edit_printercount(edited_info=edited_info,
                              initial_count=initial_count,
                              count_to_be_changed=printer_information)
    elif edited_info is not None and date_changed is True:
        words = get_list_of_words_2(str(edited_info.printer))
        brand, *model_and_number = words
        model = ' '.join(model_and_number)
        try:
            printer_information = get_object_or_404(Printer,
                                                    brand=brand,
                                                    model=model)
        except MultipleObjectsReturned:
            raise RequestAborted
        else:
            edit_printercount(edited_info=edited_info,
                              count_to_be_changed=printer_information)


def find_duplicates(array) -> bool:
    """
    An assisting function for view functions.
    """

    items = []
    for obj in array:
        if obj not in items:
            items.append(obj)
        elif obj in items:
            return True


def generate_code(code_1=False, code_2=False) -> str:
    """
    An assisting function for view functions.

    Coupons for discount have two kinds of codes with different length.
    CODE_1 is 12 character code.
    CODE_2 is 15 character code.

    :param code_1: Set this parameter to True if CODE_1 needs to be generated, and omit code_2.
    :param code_2: Set this parameter to True if CODE_2 needs to be genereted, and omit code_1.
    """

    capital_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_letters = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'

    code = ''
    array = []

    if code_1 is True and code_2 is False:
        while len(array) < 12:
            capital_letter = choice(capital_letters)
            lower_letter = choice(lower_letters)
            digit = choice(digits)
            array.append(capital_letter)
            array.append(lower_letter)
            array.append(digit)

        shuffle(array)
        code += code.join(array)
    elif code_2 is True and code_1 is False:
        while len(array) < 15:
            capital_letter = choice(capital_letters)
            lower_letter = choice(lower_letters)
            digit = choice(digits)
            array.append(capital_letter)
            array.append(lower_letter)
            array.append(digit)

        shuffle(array)
        code += code.join(array)

    return code


def get_book_codes(queryset) -> list:
    """
    An assisting function for view functions.
    """

    list_of_codes = []
    for obj in queryset:
        list_of_codes.append(str(obj.name_coded))

    return list_of_codes


def get_code_1(codes) -> str:
    """
    An assisting function for view functions.

    :returns the requested code as long as a newly generated code does not exist in the database.
    """

    code = None

    generate = True
    while generate:
        code = generate_code(code_1=True)
        if code in codes:
            continue
        else:
            generate = False

    return code


def get_code_2(codes) -> str:
    """
    An assisting function for view functions.

    :returns the requested code as long as a newly generated code does not exist in the database.
    """

    code = None

    generate = True
    while generate:
        code = generate_code(code_2=True)
        if code in codes:
            continue
        else:
            generate = False

    return code


def get_codes(queryset) -> list:
    """
    An assisting function for view functions.
    """

    list_of_codes = []
    for obj in queryset:
        list_of_codes.append(str(obj.code_1))
        list_of_codes.append(str(obj.code_2))

    return list_of_codes


def get_color_price_dicts(prices) -> list:
    """
    An assisting function for view functions.
    """

    list_of_price_dicts = []
    for price in prices:
        price_dict = {
            'date': str(price.date),
            'color': str(price.color),
            'size': str(price.size),
        }
        list_of_price_dicts.append(price_dict)

    return list_of_price_dicts


def get_dicts(objs):
    """
    An assisting function for view functions.
    """

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


def get_list_of_words_1(string) -> list:
    """
    An assisting function for view functions.

    :returns a list the second items of which is capitalized (only if they are "rangli" or "qora")
    """

    array = []
    for word in string.split():
        array.append(str(word.strip('()')))

    array = [pattern.replace('rangli', 'rangli'.capitalize()) for pattern in array]
    array = [pattern.replace('qora', 'qora'.capitalize()) for pattern in array]

    return array


def get_list_of_words_2(string) -> list:
    """
    An assisting function for view functions.
    """

    array = []
    for word in string.split():
        array.append(str(word))

    return array


def get_types(queryset):
    """
    An assisting function for view functions.
    """

    list_of_types = []
    for obj in queryset:
        list_of_types.append(str(obj.type))

    return list_of_types


def get_names(accounts=None, categories=None, subcategories=None) -> list:
    """
    An assisting function for view functions.

    :param accounts: If a list of account names are needed, pass this parameter a queryset with accounts
    with an important attribute of NAME.
    :param categories: If a list of category names are needed, pass this parameter a queryset with categories
    with an important attribute of CATEGORY.
    :param subcategories: If a list of subcategory names are needed, pass this parameter a queryset with subcategories
    with an important attribute of SUBCATEGORY.
    """

    array = []

    if accounts is not None:
        for account in accounts:
            array.append(str(account.name))
    elif categories is not None:
        for category in categories:
            array.append(str(category.category))
    elif subcategories is not None:
        for subcategory in subcategories:
            array.append(str(subcategory.subcategory))

    return array


def get_name_dicts(queryset) -> list:
    """
    An assisting function for view functions.
    """

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
    """
    An assisting function for view functions.
    """

    list_price_dates = []
    for price in prices:
        list_price_dates.append(str(price.date))

    return list_price_dates


def get_price_dicts(prices) -> list:
    """
    An assisting function for view functions.
    """

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
    """
    An assisting function for view functions.
    """

    list_of_dicts = []
    for obj in queryset:
        printer_information = {
            'brand': str(obj.brand),
            'model': str(obj.model),
        }
        list_of_dicts.append(printer_information)

    return list_of_dicts


def get_printer_names(queryset) -> list:
    """
    An assisting function for view functions.
    """

    list_of_printers = []
    for obj in queryset:
        list_of_printers.append(str(obj.printer))

    return list_of_printers


def match_color_price_with_existing(list_of_dicts, price) -> bool:
    """
    An assisting function for view functions.
    """

    price_dict = {
        'date': str(price.date),
        'color': str(price.color),
        'size': str(price.size),
    }
    if price_dict in list_of_dicts:
        return True
    else:
        return False


def match_with_names(list_of_accounts=None,
                     account=None,
                     list_of_categories=None,
                     category=None,
                     list_of_subcategories=None,
                     subcategory=None) -> bool:
    """
    An assisting functions for view functions.

    Finds out whether a passed name (in general) exists in the correlating list passed here.

    Used in the incomes-expenses section.

    :param list_of_accounts: Takes in the existing names of accounts.
    :param account: Can take in either a new account name or the one being edited.
    :param list_of_categories: Takes in the existing categories of either income or expense.
    :param category: Can take in either a new category or the one being edited.
    :param list_of_subcategories: Takes in the existing subcategories of either income or expense.
    :param subcategory: Can take in either a new subcategory or the one being edited.
    :return: True or False based on the search result.
    """

    if list_of_accounts is not None and account is not None:
        if str(account.name) in list_of_accounts:
            return True
        else:
            return False
    elif list_of_categories is not None and category is not None:
        if str(category.category) in list_of_categories:
            return True
        else:
            return False
    elif list_of_subcategories is not None and subcategory is not None:
        if str(subcategory.subcategory) in list_of_subcategories:
            return True
        else:
            return False


def match_with_book_codes(list_of_dicts, book) -> bool:
    """
    An assisting function for view functions.
    """

    if book.name_coded in list_of_dicts:
        return True
    else:
        return False


def match_with_existing_prices(list_of_dicts, price) -> bool:
    """
    An assisting function for view functions.
    """

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
    """
    An assisting function for view functions.
    """

    if str(price.date) in list_of_dates:
        return True
    else:
        return False


def match_with_existing_names(list_of_dicts, info) -> bool:
    """
    An assisting function for view functions.
    """

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
    """
    An assisting function for view functions.
    """

    printer_information = {
        'brand': str(info.brand),
        'model': str(info.model),
    }
    if printer_information in list_of_dicts:
        return True
    else:
        return False


def outex_edited_edit_bprice(**kwargs):
    """
    An assisting function for view functions.

    :param kwargs: Takes in five arguments - initial_packaging, initial_workforce, edited_packaging, edited_prices,
    and edited_workforce.
    All of the parameters, except for edited_prices, take in Money field's amount attribute from django-money.
    edited_price should be an instance of outer expenses.
    """

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
            for bprice in binding_prices:
                if sum_edited_exps > sum_initial_exps:
                    gap = int(sum_edited_exps) - int(sum_initial_exps)
                    bprice.price = bprice.price.amount + gap
                    bprice.save()
                elif sum_edited_exps < sum_initial_exps:
                    gap = int(sum_initial_exps) - int(sum_edited_exps)
                    bprice.price = bprice.price.amount - gap
                    bprice.save()


def outex_edited_edit_pprice(**kwargs):
    """
    An assisting function for view functions.

    :param kwargs: Takes in three arguments - initial_printer_exp, edited_printer_exp and edited_prices.
    All of the parameters, except for edited_prices, take in Money field's amount attribute from django-money.
    edited_price should be an instance of outer expenses.
    """

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
