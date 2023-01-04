"""Defines URL patterns for the project."""
from . import admin_panel_views
from . import views
from django.urls import path, re_path


appname = 'service'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # A page for contacting
    path('contact/', views.contact, name='contact'),
    # A page telling users that their reference has successfully been sent
    path('contact/success-contact/', views.success_contact, name='success_contact'),
    # A page for checking book categories
    path('books/categories/', views.view_book_categories, name='view_book_categories'),
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
    path('blogposts/', views.view_blogposts, name='view_blogposts'),
    # A page for checking a blog post in detail
    path('blogposts/<int:blogpost_id>/', views.view_blogpost, name='view_blogpost'),
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
    path('news/view/', views.view_news, name='view_news'),
    # A page for checking news in detail
    path('news/view/details/<int:news_id>/', views.view_detailed_news, name='view_detailed_news'),

    # ==================================== A management system for administrators ====================================

    path('admin/main-page/', admin_panel_views.main_page, name='main_page'),

    path('admin/orders/check/', admin_panel_views.orders, name='orders'),
    path('admin/orders/edit/<int:order_number>/', admin_panel_views.edit_order, name='edit_order'),
    path('admin/orders/delete/<int:order_number>/', admin_panel_views.delete_order, name='delete_order'),

    path('admin/order-options/add-check/', admin_panel_views.order_options, name='order_options'),
    path('admin/order-options/edit/<int:orderoptions_id>/',
         admin_panel_views.edit_orderoptions, name='edit_orderoptions'),
    path('admin/order-options/delete/<int:orderoptions_id>/',
         admin_panel_views.delete_orderoptions, name='delete_orderoptions'),
    path('admin/order-options/edit/placetoget/<int:placetoget_id>/',
         admin_panel_views.edit_placetoget, name='edit_placetoget'),
    path('admin/order-options/delete/placetoget/<int:placetoget_id>/',
         admin_panel_views.delete_placetoget, name='delete_placetoget'),

    path('admin/staff/add-check/', admin_panel_views.staff_info, name='staff_info'),
    path('admin/staff/edit-data/<int:workforce_id>/', admin_panel_views.edit_staff_info, name='edit_staff_info'),
    path('admin/staff/delete-data/<int:workforce_id>/', admin_panel_views.delete_staff_info, name='delete_staff_info'),

    path('admin/books/add-check/', admin_panel_views.books, name='books'),
    path('admin/books/edit/<int:book_id>/', admin_panel_views.edit_book, name='edit_book'),
    path('admin/books/delete/<int:book_id>/', admin_panel_views.delete_book, name='delete_book'),


    path('admin/expenses-incomes/', admin_panel_views.incomes_expenses, name='incomes_expenses'),
    path('admin/expenses-incomes/accounts/add/', admin_panel_views.add_account, name='add_account'),
    path('admin/expenses-incomes/accounts/edit/<int:account_id>/',
         admin_panel_views.edit_account, name='edit_account'),
    path('admin/expenses-incomes/accounts/delete/<int:account_id>/',
         admin_panel_views.delete_account, name='delete_account'),
    path('admin/expenses-incomes/expense-categories/add-check/',
         admin_panel_views.expense_categories, name='expense_categories'),
    path('admin/expenses-incomes/expense-categories/edit/<int:excategory_id>/',
         admin_panel_views.edit_excategory, name='edit_excategory'),
    path('admin/expenses-incomes/expense-categories/delete/<int:excategory_id>/',
         admin_panel_views.delete_excategory, name='delete_excategory'),
    path('admin/expenses-incomes/expense-subcategories/add-check/',
         admin_panel_views.expense_subcats, name='expense_subcats'),
    path('admin/expenses-incomes/expense-subcategories/edit/<int:exsubcategory_id>/',
         admin_panel_views.edit_exsubcat, name='edit_exsubcat'),
    path('admin/expenses-incomes/expense-subcategories/delete/<int:exsubcategory_id>/',
         admin_panel_views.delete_exsubcat, name='delete_exsubcat'),
    path('admin/expenses-incomes/income-categories/add-check/',
         admin_panel_views.income_categories, name='income_categories'),
    path('admin/expenses-incomes/income-categories/edit/<int:incategory_id>/',
         admin_panel_views.edit_incategory, name='edit_incategory'),
    path('admin/expenses-incomes/income-categories/delete/<int:incategory_id>/',
         admin_panel_views.delete_incategory, name='delete_incategory'),
    path('admin/expenses-incomes/income-subcategories/add-check/',
         admin_panel_views.income_subcats, name='income_subcats'),
    path('admin/expenses-incomes/income-subcategories/edit/<int:insubcategory_id>/',
         admin_panel_views.edit_insubcat, name='edit_insubcat'),
    path('admin/expenses-incomes/income-subcategories/delete/<int:insubcategory_id>/',
         admin_panel_views.delete_insubcat, name='delete_insubcat'),
    path('admin/expenses-incomes/expenses/make/',
         admin_panel_views.make_expense, name='make_expense'),
    path('admin/expenses-incomes/expenses/edit/<int:expense_id>/',
         admin_panel_views.edit_expense, name='edit_expense'),
    path('admin/expenses-incomes/expenses/delete/<int:expense_id>/',
         admin_panel_views.delete_expense, name='delete_expense'),
    path('admin/expenses-incomes/incomes/make/',
         admin_panel_views.make_income, name='make_income'),
    path('admin/expenses-incomes/incomes/edit/<int:income_id>/',
         admin_panel_views.edit_income, name='edit_income'),
    path('admin/expenses-incomes/incomes/delete/<int:income_id>/',
         admin_panel_views.delete_income, name='delete_income'),
    path('admin/expenses-incomes/transactions/make/',
         admin_panel_views.make_transaction, name='make_transaction'),
    path('admin/expenses-incomes/transactions/edit/<int:transaction_id>/',
         admin_panel_views.edit_transaction, name='edit_transaction'),
    path('admin/expenses-incomes/transactions/delete/<int:transaction_id>/',
         admin_panel_views.delete_transaction, name='delete_transaction'),


    path('admin/blogposts/add-check/',
         admin_panel_views.blogposts, name='blogposts'),
    path('admin/blogposts/edit/<int:blogpost_id>/',
         admin_panel_views.edit_blogpost, name='edit_blogpost'),
    path('admin/blogposts/delete/<int:blogpost_id>/',
         admin_panel_views.delete_blogpost, name='delete_blogpost'),

    path('admin/contacts/check/', admin_panel_views.contacts, name='contacts'),
    path('admin/contacts/ask-to-delete/<int:contact_id>/', admin_panel_views.ask_del_contact, name='ask_del_contact'),
    path('admin/contacts/delete/<int:contact_id>/', admin_panel_views.delete_contact, name='delete_contact'),


    path('admin/pricing/add-check/', admin_panel_views.pricing, name='pricing'),
    path('admin/pricing/page-prices/add/', admin_panel_views.page_price, name='page_price'),
    path('admin/pricing/page-prices/edit/<int:pageprice_id>/',
         admin_panel_views.edit_page_price, name='edit_page_price'),
    path('admin/pricing/page-prices/delete/<int:pageprice_id>/',
         admin_panel_views.delete_page_price, name='delete_page_price'),
    path('admin/pricing/binding-prices/add/', admin_panel_views.binding_price, name='binding_price'),
    path('admin/pricing/binding-prices/edit/<int:bindingprice_id>/',
         admin_panel_views.edit_binding_price, name='edit_binding_price'),
    path('admin/pricing/binding-prices/delete/<int:bindingprice_id>/',
         admin_panel_views.delete_binding_price, name='delete_binding_price'),
    path('admin/pricing/ring-prices/add/', admin_panel_views.ring_price, name='ring_price'),
    path('admin/pricing/ring-prices/edit/<int:ringprice_id>/',
         admin_panel_views.edit_ring_price, name='edit_ring_price'),
    path('admin/pricing/ring-prices/delete/<int:ringprice_id>/',
         admin_panel_views.delete_ring_price, name='delete_ring_price'),
    path('admin/pricing/color-prices/add/',
         admin_panel_views.color_price, name='color_price'),
    path('admin/pricing/color-prices/edit/<int:colorprice_id>/',
         admin_panel_views.edit_color_price, name='edit_color_price'),
    path('admin/pricing/color-prices/delete/<int:colorprice_id>/',
         admin_panel_views.delete_color_price, name='delete_color_price'),
    path('admin/pricing/cover-prices/add/', admin_panel_views.cover_price, name='cover_price'),
    path('admin/pricing/cover-prices/edit/<int:coverprice_id>/',
         admin_panel_views.edit_cover_price, name='edit_cover_price'),
    path('admin/pricing/cover-prices/delete/<int:coverprice_id>/',
         admin_panel_views.delete_cover_price, name='delete_cover_price'),
    path('admin/pricing/glue-prices/add/', admin_panel_views.glue_price, name='glue_price'),
    path('admin/pricing/glue-prices/edit/<int:glueprice_id>/',
         admin_panel_views.edit_glue_price, name='edit_glue_price'),
    path('admin/pricing/glue-prices/delete/<int:glueprice_id>/',
         admin_panel_views.delete_glue_price, name='delete_glue_price'),
    path('admin/pricing/paper-prices/add/', admin_panel_views.paper_price, name='paper_price'),
    path('admin/pricing/paper-prices/edit/<int:paperprice_id>/',
         admin_panel_views.edit_paper_price, name='edit_paper_price'),
    path('admin/pricing/paper-prices/delete/<int:paperprice_id>/',
         admin_panel_views.delete_paper_price, name='delete_paper_price'),
    path('admin/pricing/yarn-prices/add/', admin_panel_views.yarn_price, name='yarn_price'),
    path('admin/pricing/yarn-prices/edit/<int:yarnprice_id>/',
         admin_panel_views.edit_yarn_price, name='edit_yarn_price'),
    path('admin/pricing/yarn-prices/delete/<int:yarnprice_id>/',
         admin_panel_views.delete_yarn_price, name='delete_yarn_price'),
    path('admin/pricing/outer-prices/add/', admin_panel_views.outer_prices, name='outer_prices'),
    path('admin/pricing/outer-prices/edit/<int:outerprice_id>/',
         admin_panel_views.edit_outer_prices, name='edit_outer_prices'),
    path('admin/pricing/outer-prices/delete/<int:outerprice_id>/',
         admin_panel_views.delete_outer_prices, name='delete_outer_prices'),
    path('admin/pricing/coupons/add-check/', admin_panel_views.coupons, name='coupons'),
    path('admin/pricing/coupons/edit/<int:coupon_id>/', admin_panel_views.edit_coupon, name='edit_coupon'),
    path('admin/pricing/coupons/delete/<int:coupon_id>/', admin_panel_views.delete_coupon, name='delete_coupon'),


    path('admin/printers/add-check/', admin_panel_views.printer_info, name='printer_info'),
    path('admin/printers/edit/<int:printer_id>/', admin_panel_views.edit_printer_info, name='edit_printer_info'),
    path('admin/printers/delete/<int:printer_id>/', admin_panel_views.delete_printer_info, name='delete_printer_info'),
    path('admin/printers/refill-and-page-count/add/',
         admin_panel_views.add_refill_page_count, name='add_refill_page_count'),
    path('admin/printers/refill-and-page-count/edit/<int:refillandpagecount_id>/',
         admin_panel_views.edit_refill_page_count, name='edit_refill_page_count'),
    path('admin/printers/refill-and-page-count/delete/<int:refillandpagecount_id>/',
         admin_panel_views.delete_refill_page_count, name='delete_refill_page_count'),

    path('admin/resources/types/add-check', admin_panel_views.rtypes, name='rtypes'),
    path('admin/resources/types/edit/<int:rtype_id>/', admin_panel_views.edit_rtype, name='edit_rtype'),
    path('admin/resources/types/delete/<int:rtype_id>/', admin_panel_views.delete_rtype, name='delete_rtype'),
    path('admin/resources/add-check/', admin_panel_views.resources, name='resources'),
    path('admin/resources/edit/<int:resource_id>/', admin_panel_views.edit_resource, name='edit_resource'),
    path('admin/resources/delete/<int:resource_id>/', admin_panel_views.delete_resource, name='delete_resource'),

    path('admin/complaints/check/', admin_panel_views.complaints, name='complaints'),
    path('admin/complaints/ask-to-delete/<int:complaint_id>/',
         admin_panel_views.ask_del_complaint, name='ask_del_complaint'),
    path('admin/complaints/delete/<int:complaint_id>/',
         admin_panel_views.delete_complaint, name='delete_complaint'),

    path('admin/news/add-check/', admin_panel_views.news, name='news'),
    path('admin/news/edit/<int:news_id>/', admin_panel_views.edit_news, name='edit_news'),
    path('admin/news/delete/<int:news_id>/', admin_panel_views.delete_news, name='delete_news'),

    path('admin/losses/types/add-check/', admin_panel_views.ltypes, name='ltypes'),
    path('admin/losses/types/edit/<int:ltype_id>/', admin_panel_views.edit_ltype, name='edit_ltype'),
    path('admin/losses/types/delete/<int:ltype_id>/', admin_panel_views.delete_ltype, name='delete_ltype'),
    path('admin/losses/add-check/', admin_panel_views.losses, name='losses'),
    path('admin/losses/edit/<int:loss_id>/', admin_panel_views.edit_loss, name='edit_loss'),
    path('admin/losses/delete/<int:loss_id>/', admin_panel_views.delete_loss, name='delete_loss'),

    # ================================================================================================================

    # A page for showing a search results
    path('search/', views.search, name='search'),
    # A page for users to check their own orders
    path('order/myorders/', views.myorders, name='myorders'),
    # A page for users to choose the source for ordering books
    path('order/source/', views.order_src, name='order_source'),
    # A page for users to make orders for books available in the library
    re_path(r'order/from-site/(?:/(?P<book_id>[0-9]+)/)?/', views.order_site, name='order_site'),
    # A page for users to make orders for books provided by themselves
    path('order/from-users/', views.order_users, name='order_users'),
    # A page telling users that their orders have successfully been sent
    path('order/book/success-order/', views.success_order, name='success_order'),
]
