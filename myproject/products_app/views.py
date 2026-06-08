from django.shortcuts import render


def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def contacts_view(request):
    return render(request, 'contacts.html')

def how_to_find_view(request):
    return render(request, 'how_to_find.html')

def products_view(request):
    return render(request, 'products.html')

def categories_view(request):
    return render(request, 'categories.html')

def all_products_view(request):
    return render(request, 'all_products.html')

def cart_view(request):
    return render(request, 'cart.html')
