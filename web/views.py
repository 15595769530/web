from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def culture(request):
    return render(request, 'culture.html')


def contact(request):
    return render(request, 'contact.html')

def addr(request):
    return render(request,'addr.html')

def product(request):
    return render(request,'product.html')

def agent(request):
    return  render(request,'agent.html')