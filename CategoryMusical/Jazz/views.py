from django.shortcuts import render


def jaz_menu_view(request):
    return render(request, 'jazmusic_menu.html')