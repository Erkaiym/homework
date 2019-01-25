from django.shortcuts import render

def main_page(request):
    products = Product.objects.all()
    return render(request, 'index.html', context={'products':products})

