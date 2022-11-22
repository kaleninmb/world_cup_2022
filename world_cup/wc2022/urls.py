from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('countrylist', views.country_list, name='CountryList'),
    path('countrygroup/<int:country_id>', views.country_group, name='CountryGroup'),
]