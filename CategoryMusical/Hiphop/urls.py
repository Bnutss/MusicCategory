from django.urls import path
from Hiphop.views import menu_view, hiphop_menu_view

app_name = 'hiphop'

urlpatterns = [
    path('main-menu/', menu_view, name='main_menu'),
    path('hiphop-menu/', hiphop_menu_view, name='hiphop_menu')
]
