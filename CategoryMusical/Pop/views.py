from django.shortcuts import render


def pop_menu_view(request):
    return render(request, 'popmusic_menu.html')