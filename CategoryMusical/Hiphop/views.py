from django.shortcuts import render


def menu_view(request):
    return render(request, 'main_menu.html')


def hiphop_menu_view(request):
    return render(request, 'hiphopmusic_menu.html')