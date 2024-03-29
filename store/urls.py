from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart', views.cart, name="cart"),
	path('product/<str:pk>', views.view_product, name="view"),

	path('checkout', views.checkout, name="checkout"),
	path('details', views.details, name="details"),
	path('search_results', views.search, name="search_results"),
	path('contact', views.contact, name="contact"),
	

	path('update_item', views.updateItem, name="update_item"),
	path('process_order', views.processOrder, name="process_order"),
	
]