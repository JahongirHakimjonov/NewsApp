from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name="home-page"),
    path('contact', views.contact_page, name="contact-page"),
    path('404', views.page_notfound, name="page-notfound"),
    path('single_page', views.single_page, name="single-page"),
]
