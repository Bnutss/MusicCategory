from django.urls import path
from Hiphop.views import menu_view
from Jazz.views import jaz_menu_view

app_name = 'jaz'

urlpatterns = [
    path('main-menu/', menu_view, name='main_menu'),
    path('jaz-menu/', jaz_menu_view, name='jaz_menu')
]
