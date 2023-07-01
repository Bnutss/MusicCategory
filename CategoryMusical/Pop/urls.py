from django.urls import path
from Hiphop.views import menu_view
from Pop.views import pop_menu_view

app_name = 'pop'

urlpatterns = [
    path('main-menu/', menu_view, name='main_menu'),
    path('pop-menu/', pop_menu_view, name='pop_menu')
]
