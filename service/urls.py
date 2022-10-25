"""Defines URL patterns for the project."""
from django.urls import path
from . import views


appname = 'service'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # A page for contacting
    path('contact/', views.contact, name='contact'),
    # A page telling users that their reference has successfully been sent
    path('contact/success-contact/', views.success_contact, name='success_contact'),
    # A page for checking book categories
    path('books/categories/', views.view_book_categories, name='book_categories'),
    # Here goes books divided by categories
    path('books/categories/adventure/', views.adventure_books, name='adventure_books'),
    path('books/categories/contemporary-fiction/', views.contemporary_fiction_books, name='contemporary_fiction_books'),
    path('books/categories/exact-sciences/', views.exact_science_books, name='exact_science_books'),
    path('books/categories/fantasy/', views.fantasy_books, name='fantasy_books'),
    path('books/categories/historical-fiction/', views.historical_fiction_books, name='historical_fiction_books'),
    path('books/categories/information-technology/', views.it_books, name='it_books'),
    path('books/categories/language/', views.language_books, name='language_books'),
    path('books/categories/mystery/', views.mystery_books, name='mystery_books'),
    path('books/categories/novels/', views.novel_books, name='novel_books'),
    path('books/categories/romance/', views.romance_books, name='romance_books'),
    path('books/categories/science-fiction/', views.science_fiction_books, name='science_fiction_books'),
    path('books/categories/short-stories/', views.short_story_books, name='short_story_books'),
    # A page for checking blog posts
    path('blogposts/', views.view_blogposts, name='blogposts'),
    # A page for checking a blog post in detail
    path('blogposts/<int:blogpost_id>/', views.view_post, name='post'),
    # A page for receiving application on creating a website
    path('website/apply-creation/', views.create_site, name='create_site'),
    # A page telling users that their application has successfully been accepted
    path('website/apply-creation/success/', views.success_create, name='success_create'),
    # A page for users to choose the category of complaint
    path('complain/category/', views.complaint_category, name='complaint_category'),
    # A page for users to make complaints about the website
    path('complain/category/site/', views.complain_site, name='complain_site'),
    # A page for users to make complaints about books
    path('complain/category/books/', views.complain_books, name='complain_books'),
    # A page for users to make different complaints
    path('complain/category/other/', views.complain_other, name='complain_other'),
    # A page telling users that their complaint applications has successfully been accepted
    path('complain/success-complaint/', views.success_complaint, name='success_complaint'),
    # A page for checking news
    path('news/check/', views.view_news, name='view_news'),
    # A page for checking news in detail
    path('news/check/details/<int:news_id>/', views.detailed_news, name='detailed_news'),

    # ==================================== A management system for administrators ====================================

    # Welcoming page for admins
    path('admin/welcome/', views.welcome_admin, name='welcome_admin'),
    # A page for checking orders
    path('admin/orders/check/', views.check_orders, name='check_orders'),
    # A page for modifying orders
    path('admin/orders/check/edit-order/<int:order_number>/', views.edit_order, name='edit_order'),
    # A path for deleting the chosen order
    path('admin/orders/check/delete-order/<int:order_number>/', views.delete_order, name='delete_order'),
    # A page for checking (and adding available) the base of options
    path('admin/order-options/', views.order_options, name='order_options'),
    # A page for checking available books in the library
    path('admin/check-books/', views.check_books, name="check_books"),
    # A page for adding books
    path('admin/check-books/add-book/', views.add_book, name='add_book'),
    # A page for editing books
    path('admin/check-books/edit-book/<int:book_id>/', views.edit_book, name='edit_book'),
    # A page for deleting the chosen book
    path('admin/check-books/delete-book/<int:book_id>/', views.delete_book, name='delete_book'),
    # A page for choosing whether to make an expense or an income
    path('admin/expenses-incomes/', views.choose_ex_in, name='choose_ex_in'),
    # A page for creating money accounts
    path('admin/expenses-incomes/accounts/add/', views.add_account, name='add_account'),
    # A page for editing the chosen account
    path('admin/expenses-incomes/accounts/edit/<int:account_id>/', views.edit_account, name='edit_account'),
    # A page for deleting the chosen account
    path('admin/expenses-incomes/accounts/delete/<int:account_id>/', views.delete_account, name='delete_account'),
    # A page for creating and checking expense categories
    path('admin/expenses-incomes/expense-categories/', views.expense_categories, name='expense_categories'),
    # A page for editing the chosen expense category
    path('admin/expenses-incomes/expense-categories/edit/<int:excategory_id>/',
         views.edit_excategory, name='edit_excategory'),
    # A page for editing the chosen expense category
    path('admin/expenses-incomes/expense-categories/delete/<int:excategory_id>/',
         views.delete_excategory, name='delete_excategory'),
    # A page for creating expense subcategories
    path('admin/expenses-incomes/expense-subcategories/', views.expense_subcats, name='expense_subcats'),
    # A page for editing the chosen expense category
    path('admin/expenses-incomes/expense-subcategories/edit/<int:exsubcategory_id>/',
         views.edit_exsubcat, name='edit_exsubcat'),
    # A page for editing the chosen expense category
    path('admin/expenses-incomes/expense-subcategories/delete/<int:exsubcategory_id>/',
         views.delete_exsubcat, name='delete_exsubcat'),
    # A page for creating and checking income categories
    path('admin/expenses-incomes/income-categories/', views.income_categories, name='income_categories'),
    # A page for editing the chosen income category
    path('admin/expenses-incomes/income-categories/edit/<int:incategory_id>/',
         views.edit_incategory, name='edit_incategory'),
    # A page for editing the chosen income category
    path('admin/expenses-incomes/income-categories/delete/<int:incategory_id>/',
         views.delete_incategory, name='delete_incategory'),
    # A page for creating expense subcategories
    path('admin/expenses-incomes/income-subcategories/', views.income_subcats, name='income_subcats'),
    # A page for editing the chosen income category
    path('admin/expenses-incomes/income-subcategories/edit/<int:insubcategory_id>/',
         views.edit_insubcat, name='edit_insubcat'),
    # A page for editing the chosen income category
    path('admin/expenses-incomes/income-subcategories/delete/<int:insubcategory_id>/',
         views.delete_insubcat, name='delete_insubcat'),
    # A page for making expenses
    path('admin/expenses-incomes/make/expense/', views.make_expense, name='make_expense'),
    # A page for editing the chosen expense
    path('admin/expenses-incomes/edit/expense/<int:expense_id>/', views.edit_expense, name='edit_expense'),
    # A page for deleting the chosen expense object
    path('admin/expenses-incomes/delete/expense/<int:expense_id>/', views.delete_expense, name='delete_expense'),
    # A page for making incomes
    path('admin/expenses-incomes/make/income/', views.make_income, name='make_income'),
    # A page for editing the chosen income
    path('admin/expenses-incomes/edit/income/<int:income_id>/', views.edit_income, name='edit_income'),
    # A page for deleting the chosen income
    path('admin/expenses-incomes/delete/<int:income_id>/', views.delete_income, name='delete_income'),
    # A page for making transactions between accounts
    path('admin/expenses-incomes/make/transaction/', views.make_transaction, name='make_transaction'),
    # A page for editing the chosen transaction between money accounts
    path('admin/expenses-incomes/edit/transaction/<int:transaction_id>/',
         views.edit_transaction, name='edit_transaction'),
    # A page for deleting the chosen transaction between money accounts
    path('admin/expenses-incomes/delete/transaction/<int:transaction_id>/',
         views.delete_transaction, name='delete_transaction'),
    # A page for checking blog posts
    path('admin/blogposts/', views.check_blogposts, name='check_blogposts'),
    # A page for adding blog posts
    path('admin/blogposts/add/', views.add_blogpost, name='add_blogpost'),
    # A page for editing a blog post
    path('admin/blogposts/edit/<int:blogpost_id>/', views.edit_blogpost, name='edit_blogpost'),
    # A page for deleting a blog post
    path('admin/blogposts/delete/<int:blogpost_id>/', views.delete_blogpost, name='delete_blogpost'),
    # A page for checking contact inquires made by users
    path('admin/contacts/check/', views.check_contacts, name='check_contacts'),
    # A page for asking the admin whether they are sure about deleting the contact or not
    path('admin/contacts/ask-to-delete/<int:contact_id>/', views.ask_del_contact, name='ask_del_contact'),
    # A page for deleting the chosen contact
    path('admin/contacts/delete/<int:contact_id>/', views.delete_contact, name='delete_contact'),
    # A page for adding/checking a resource type
    path('admin/resources/types/add-check', views.rtypes, name='rtypes'),
    # A page for editing a resource type
    path('admin/resources/types/edit/<int:rtype_id>/', views.edit_rtype, name='edit_rtype'),
    # A page for deleting a resource type
    path('admin/resources/types/delete/<int:rtype_id>/', views.delete_rtype, name='delete_rtype'),
    # A page for working with resources
    path('admin/resources/', views.resources, name='resources'),
    # A page for editing the chosen resource
    path('admin/resources/edit/<int:resource_id>/', views.edit_resource, name='edit_resource'),
    # A page for deleting the chosen resource
    path('admin/resources/delete/<int:resource_id>/', views.delete_resource, name='delete_resource'),
    # A page for checking applications on creating a website
    path('admin/website-applications/check/', views.check_web_applies, name='check_web_applies'),
    # A page for asking the admin whether they are sure about deleting the application or not
    path('admin/website-applications/ask-to-delete/<int:createsite_id>/', views.ask_del_webapp, name='ask_del_webapp'),
    # A page for deleting the chosen application on creating a website
    path('admin/website-applications/delete/<int:createsite_id>/', views.del_webapp, name='del_webapp'),
    # A page for checking complaints
    path('admin/complaints/check/', views.view_complaints, name='check_complaints'),
    # A page for asking the admin whether they are sure about deleting the complaint or not
    path('admin/complaints/ask-to-delete/<int:complaint_id>/', views.ask_del_complaint, name='ask_del_complaint'),
    # A page for deleting the chosen complaint
    path('admin/complaints/delete/<int:complaint_id>/', views.delete_complaint, name='delete_complaint'),
    # A page for checking news
    path('admin/news/check/', views.check_news, name='check_news'),
    # A page for announcing news
    path('admin/news/make/', views.make_news, name='make_news'),
    # A page for editing the news
    path('admin/news/edit/<int:news_id>/', views.edit_news, name='edit_news'),
    # A page for deleting news
    path('admin/news/delete/<int:news_id>/', views.delete_news, name='delete_news'),

    # ================================================================================================================

    # A page for showing a search results
    path('search/', views.search, name='search'),
    # A page for users to check their own orders
    path('order/myorders/', views.myorders, name='myorders'),
    # A page for users to choose the source for ordering books
    path('order/source/', views.order_src, name='order_source'),
    # A page for users to make orders for books available in the library
    path('order/from-site/', views.order_site, name='order_site'),
    # A page for users to make orders for books provided by themselves
    path('order/from-users/', views.order_users, name='order_users'),
    # A page telling users that their orders have successfully been sent
    path('order/book/success-order/', views.success_order, name='success_order'),
]