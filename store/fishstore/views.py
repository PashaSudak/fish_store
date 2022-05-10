from django.shortcuts import render
from fishstore.models import Product
from fishstore.models import User
from fishstore.models import Order

def index(request):
    prdouct = Product.objects.all()

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0,
                 'get_cart_items': 0}

    context = {
        'pr': prdouct,
        'items': items,
        'order': order,
    }

    return render(request, 'fishstore/index.html', context)

def registration(request):
    return render(request, 'fishstore/registration.html')

def register_user(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confpassword']:
            newuser = User(fullname = request.POST['fullname'], 
                            username = request.POST['username'], 
                            password = request.POST['password'],
                            email = request.POST['email'],
                            phone = request.POST['phone'],)
            newuser.save()
            return render(request, 'fishstore/registration.html', {'result': 'Успішно'})
        else:
            return render(request, 'fishstore/registration.html', {'result': 'Паролі не збігаються'})
    return render(request, 'fishstore/registration.html', {'result': 'error'})

def login(request):
    return render(request, 'fishstore/login.html')

