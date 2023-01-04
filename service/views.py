from .assisting_functions import check_user
from django.contrib import messages
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render, get_object_or_404
from .forms import ComplaintBookForm, ComplaintOtherForm, ComplaintSiteForm, ContactForm, \
    OrderSelfForm, OrderSiteForm
from .models import BlogPost, Book, \
    News, \
    Order, OrderOptions, \
    PlaceToGet
import re


def index(request):
    """
    Renders the home page.
    """

    news_objects = News.objects.all().order_by('-id', '-date_added')[:3]
    posts = BlogPost.objects.all().order_by('-id', '-date_published')[:3]

    context = {
        'news_objects': news_objects,
        'posts': posts,
    }

    return render(request, 'service/index.html', context)


def contact(request):
    """
    Renders the contact page.
    """

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
    """
    Renders the page which tells a user that an application has successfully been sent.
    """

    return render(request, 'service/success_application.html')


def view_book_categories(request):
    """
    Renders the book categories page.
    """

    return render(request, 'service/view_book_categories.html')


# Here are the views rendering so-called "online book shelves"
def adventure_books(request):

    book_objects = Book.objects.filter(category='Sarguzashtlar')

    context = {
        'book_objects': book_objects,
    }
    return render(request, 'service/books/adventure_books.html', context)


def contemporary_fiction_books(request):

    book_objects = Book.objects.filter(category='Zamonaviy Fantastika')

    context = {
        'book_objects': book_objects,
    }
    return render(request, 'service/books/contemporary_fiction_books.html', context)


def exact_science_books(request):

    book_objects = Book.objects.filter(category='Aniq fanlar')

    context = {
        'book_objects': book_objects,
    }
    return render(request, 'service/books/exact_science_books.html', context)


def fantasy_books(request):

    book_objects = Book.objects.filter(category='Fantastika')

    context = {
        'book_objects': book_objects,
    }
    return render(request, 'service/books/fantasy_books.html', context)


def historical_fiction_books(request):

    book_objects = Book.objects.filter(category='Tarixiy Fantastika')

    context = {
        'book_objects': book_objects,
    }
    return render(request, 'service/books/historical_fiction_books.html', context)


def it_books(request):

    book_objects = Book.objects.filter(category='Axborot Texnologiyalariga oid')

    context = {
        'book_objects': book_objects,
    }
    return render(request, 'service/books/it_books.html', context)


def language_books(request):

    book_objects = Book.objects.filter(category='Tilga oid')

    context = {
        'book_objects': book_objects,
    }
    return render(request, 'service/books/language_books.html', context)


def mystery_books(request):

    book_objects = Book.objects.filter(category='Detektiv')

    context = {
        'book_objects': book_objects,
    }
    return render(request, 'service/books/mystery_books.html', context)


def novel_books(request):

    book_objects = Book.objects.filter(category='Romanlar')

    context = {
        'book_objects': book_objects,
    }
    return render(request, 'service/books/novel_books.html', context)


def romance_books(request):

    book_objects = Book.objects.filter(category='Romantika')

    context = {
        'book_objects': book_objects,
    }
    return render(request, 'service/books/romance_books.html', context)


def science_fiction_books(request):

    book_objects = Book.objects.filter(category='Ilmiy Fantastika')

    context = {
        'book_objects': book_objects,
    }
    return render(request, 'service/books/science_fiction_books.html', context)


def short_story_books(request):

    book_objects = Book.objects.filter(category='Qisqa hikoyalar')

    context = {
        'book_objects': book_objects,
    }
    return render(request, 'service/books/short_story_books.html', context)


def view_blogposts(request):
    """A view rendering the page for checking blog posts."""

    blogpost_objects = BlogPost.objects.all().order_by('-date_published')

    context = {
        'posts': blogpost_objects,
    }
    return render(request, 'service/view_blogposts.html', context)


def view_blogpost(request, blogpost_id):
    """
    Renders the page for checking a blogpost in detail.
    """

    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)

    context = {
        'post': blogpost,
    }
    return render(request, 'service/view_blogpost.html', context)


def complaint_category(request):
    """
    Renders the page for choosing on which category the complaint a user is trying to make is.
    """

    return render(request, 'service/complaint_category.html')


def complain_site(request):
    """
    Renders the page for making a complaint on the website.
    """

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
    """
    Renders the page for making a complaint on books.
    """

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
    """
    Renders the page for making a complaint on other topics.
    """

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
    """
    Renders the page which tells a user that an application has successfully been sent.
    """

    return render(request, 'service/success_application.html')


def view_news(request):
    """
    Renders the page for checking news.
    """

    news_objects = News.objects.all().order_by('-date_added')

    context = {
        'news_objects': news_objects,
    }
    return render(request, 'service/view_news.html', context)


def view_detailed_news(request, news_id):
    """
    Renders the page for checking news in detail.
    """

    new = get_object_or_404(News, pk=news_id)

    context = {
        'new': new,
    }
    return render(request, 'service/view_detailed_news.html', context)


def search(request):
    """
    Renders the page of search results.
    """

    if request.method == 'GET':
        searched = request.GET.get('searched')
        book_objects = Book.objects.filter(Q(name_coded__contains=searched) |
                                           Q(chars__contains=searched) |
                                           Q(category__contains=searched))
        news_objects = News.objects.filter(Q(title__contains=searched) |
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
            return redirect('order_source')
        elif re.fullmatch(searched, 'Shikoyat', flags=re.IGNORECASE):
            return redirect('complaint_category')
        elif re.fullmatch(searched, "Bog'lanish", flags=re.IGNORECASE):
            return redirect('contact')
        elif re.fullmatch(searched, 'Kutubxona', flags=re.IGNORECASE):
            return redirect('book_categories')
        elif re.fullmatch(searched, 'Yangiliklar', flags=re.IGNORECASE):
            return redirect('view_news')
        elif re.fullmatch(searched, 'Sayt yaratish', flags=re.IGNORECASE):
            return redirect('create_site')
        elif re.fullmatch(searched, 'Mening buyurtmalarim', flags=re.IGNORECASE):
            return redirect('myorders')
        elif re.fullmatch(searched, 'Maqolalar', flags=re.IGNORECASE):
            return redirect('blogposts')
        context = {
            'book_objects': book_objects,
            'news_objects': news_objects,
            'posts': posts,
            'searched': searched,
        }
        return render(request, 'service/search.html', context)
    else:
        return render(request, 'service/search.html')


def myorders(request):
    """
    Renders the page for checking 'My orders'.
    """

    order_objects = Order.objects.filter(customer=request.user)

    for order in order_objects:
        check_user(request, order.customer)

    context = {
        'order_objects': order_objects,
    }
    return render(request, 'service/myorders.html', context)


def order_src(request):
    """
    Renders the page for choosing an order source.
    """

    return render(request, 'service/order_src.html')


def order_site(request, book_id=None):
    """
    Renders the page for ordering a book from the site's source.
    """

    try:
        res = OrderOptions.objects.latest('date')
    except ObjectDoesNotExist:
        res = None

    places = PlaceToGet.objects.all()

    if request.method != 'POST':
        form = OrderSiteForm(initial={'book': str(book_id)} if book_id is not None else None)
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
        'book_id': book_id,
        'form': form,
        'places': places,
        'res': res,
    }
    return render(request, 'service/order_site.html', context)


def order_users(request):
    """
    Renders the page for ordering a book from users themselves.
    """

    try:
        res = OrderOptions.objects.latest('date')
    except ObjectDoesNotExist:
        res = None

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
    """
    Renders the page which tells a user that an application has successfully been sent.
    """

    return render(request, 'service/success_order.html')
