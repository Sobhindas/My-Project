from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, validators
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from webapp.models import Product,Cart,Contact
from array import *
import json


def index(request):
    if request.user.is_authenticated:
        context = {"variable":  request.user }
        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html', {})


def contact(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        mymessage = Contact.objects.create()
        mymessage.Name = name
        mymessage.Email = email
        mymessage.Message = message
        mymessage.save()
        messages.success(request, "Recieved your feedback")

    return render(request, 'contact.html', {})


def about(request):
    return render(request, 'about.html', {})


def products(request):
    return render(request, 'products.html', {})


def analogmen(request):


    t = []
    t = [0 for i in range(0, 16)]
    u = [0 for i in range(0, 16)]
    v = [0 for i in range(0, 16)]
    w = [0 for i in range(0, 16)]
    i = 0
    for a in Product.objects.all():
        for b in range(0,1):
                t[i] = a.product_name
                u[i] = a.product_image
                v[i] = a.product_description
                w[i] = a.product_price
                print(u[2])
                print(t[i])
                i = i + 1





    context = {"proname0" : t[0],"proname1" : t[1],"proname2" : t[2],"proname3" : t[4],"proname4" : t[4],"proname5" : t[5],"proname6" : t[6],"proname7" : t[7],
               "prodesc0": v[0],"prodesc1": v[1],"prodesc2": v[2],"prodesc3": v[3],"prodesc4": v[4],"prodesc5": v[5],"prodesc6": v[6],"prodesc7": v[7],
               "price0": w[0], "price1": w[1], "price2": w[2],"price3": w[3],"price4": w[4],"price5": w[5],"price6": w[6],"price7": w[7],
               "img0":u[0],"img1":u[1],"img2":u[2],"img3":u[3],"img4":u[4],"img5":u[5],"img6":u[6],"img7":u[7] }
    return render(request, 'analogmen.html', context)





def analogwomen(request):
    t = []
    t = [0 for i in range(0, 20)]
    u = [0 for i in range(0, 20)]
    v = [0 for i in range(0, 20)]
    w = [0 for i in range(0, 20)]
    i = 0
    for a in Product.objects.all():
        for b in range(0, 1):
            t[i] = a.product_name
            u[i] = a.product_image
            v[i] = a.product_description
            w[i] = a.product_price
            print(u[2])
            print(t[i])
            i = i + 1

    context = {"proname8": t[8], "proname9": t[9], "proname10": t[10], "proname11": t[11], "proname12": t[12],
               "proname13": t[13], "proname14": t[14], "proname15": t[15],
               "prodesc8": v[8], "prodesc9": v[9], "prodesc10": v[10], "prodesc11": v[11], "prodesc12": v[12],
               "prodesc13": v[13], "prodesc14": v[14], "prodesc15": v[15],
               "price8": w[8], "price9": w[9], "price10": w[10], "price11": w[11], "price12": w[12], "price13": w[13],
               "price14": w[14], "price15": w[15],
               "img8": u[8], "img9": u[9], "img10": u[10], "img11": u[11], "img12": u[12], "img13": u[13], "img14": u[14],
               "img15": u[15]}
    return render(request, 'analogwomen.html', context)


def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        # Check for error inputs
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Account was created Successfully")
        return redirect('registration')
    else:
        messages.success(request, "")
    return render(request, 'registration.html',{})


def loginh(request):
    if request.user.is_authenticated:
        return redirect('products')
    else:
        if request.method == "POST":
            loginusername = request.POST['loginusername']
            loginpassword = request.POST['loginpassword']
            user = authenticate(username=loginusername, password=loginpassword)
            if user is not None:
                login(request, user)
                messages.success(request, "success")
                return render(request, 'products.html')
            else:
             messages.success(request, "Invalid username or Password")
        else:
            messages.success(request, "")

    context = {}
    return render(request, 'loginh.html', context)


@login_required(login_url='loginh')
def buy1(request):
    t = []
    t = [0 for i in range(0, 16)]
    u = [0 for i in range(0, 16)]
    v = [0 for i in range(0, 16)]
    w = [0 for i in range(0, 16)]
    z = [0 for i in range(0,16)]
    i = 0
    for a in Product.objects.all():
        for b in range(0, 1):
            t[i] = a.product_name
            u[i] = a.product_image
            v[i] = a.product_description
            w[i] = a.product_price
            z[i] = a.product_buyer
            i = i + 1

    if request.method == 'POST':
        buyer_name = request.POST['Buyer_Name']
        item_name = request.POST['Item_Name']
        item_quantity = request.POST['Item_Quantity']
        price = request.POST['Price']
        mycart = Cart.objects.create()
        mycart.Buyer_Name = buyer_name
        mycart.Item_Name = item_name
        mycart.Item_Quantity = item_quantity
        mycart.Price = price
        mycart.save()
        messages.success(request, " Product added to Cart")

    print("hello")
    context = {"variable": request.user,"proname": t[0],"prodesc": v[0],"price": w[0],"img": u[0] }
    return render(request, 'buypage.html', context)

@login_required(login_url='loginh')
def buy2(request):
    t = []
    t = [0 for i in range(0, 16)]
    u = [0 for i in range(0, 16)]
    v = [0 for i in range(0, 16)]
    w = [0 for i in range(0, 16)]
    i = 0
    for a in Product.objects.all():
        for b in range(0, 1):
            t[i] = a.product_name
            u[i] = a.product_image
            v[i] = a.product_description
            w[i] = a.product_price
            print(u[2])
            print(t[i])
            i = i + 1
    if request.method == 'POST':
        buyer_name = request.POST['Buyer_Name']
        item_name = request.POST['Item_Name']
        item_quantity = request.POST['Item_Quantity']
        price = request.POST['Price']
        mycart = Cart.objects.create()
        mycart.Buyer_Name = buyer_name
        mycart.Item_Name = item_name
        mycart.Item_Quantity = item_quantity
        mycart.Price = price
        mycart.save()
        messages.success(request,"Product added to Cart")
    print("hello")
    context = {"variable": request.user,"proname": t[1],"prodesc": v[1],"price": w[1],"img": u[1] }
    return render(request, 'buypage.html', context)

@login_required(login_url='loginh')
def buy3(request):
    t = []
    t = [0 for i in range(0, 16)]
    u = [0 for i in range(0, 16)]
    v = [0 for i in range(0, 16)]
    w = [0 for i in range(0, 16)]
    i = 0
    for a in Product.objects.all():
        for b in range(0, 1):
            t[i] = a.product_name
            u[i] = a.product_image
            v[i] = a.product_description
            w[i] = a.product_price
            print(u[2])
            print(t[i])
            i = i + 1
    if request.method == 'POST':
        buyer_name = request.POST['Buyer_Name']
        item_name = request.POST['Item_Name']
        item_quantity = request.POST['Item_Quantity']
        price = request.POST['Price']
        mycart = Cart.objects.create()
        mycart.Buyer_Name = buyer_name
        mycart.Item_Name = item_name
        mycart.Item_Quantity = item_quantity
        mycart.Price = price
        mycart.save()
        messages.success(request,"Product added to Cart")
    print("hello")
    context = {"variable": request.user,"proname": t[2],"prodesc": v[2],"price": w[2],"img": u[2] }
    return render(request, 'buypage.html', context)

@login_required(login_url='loginh')
def buy4(request):
    t = []
    t = [0 for i in range(0, 16)]
    u = [0 for i in range(0, 16)]
    v = [0 for i in range(0, 16)]
    w = [0 for i in range(0, 16)]
    i = 0
    for a in Product.objects.all():
        for b in range(0, 1):
            t[i] = a.product_name
            u[i] = a.product_image
            v[i] = a.product_description
            w[i] = a.product_price
            print(u[2])
            print(t[i])
            i = i + 1
    if request.method == 'POST':
        buyer_name = request.POST['Buyer_Name']
        item_name = request.POST['Item_Name']
        item_quantity = request.POST['Item_Quantity']
        price = request.POST['Price']
        mycart = Cart.objects.create()
        mycart.Buyer_Name = buyer_name
        mycart.Item_Name = item_name
        mycart.Item_Quantity = item_quantity
        mycart.Price = price
        mycart.save()
        messages.success(request,"Product added to Cart")
    print("hello")
    context = {"variable": request.user,"proname": t[3],"prodesc": v[3],"price": w[3],"img": u[3] }
    return render(request, 'buypage.html', context)

@login_required(login_url='loginh')
def buy5(request):
    t = []
    t = [0 for i in range(0, 16)]
    u = [0 for i in range(0, 16)]
    v = [0 for i in range(0, 16)]
    w = [0 for i in range(0, 16)]
    i = 0
    for a in Product.objects.all():
        for b in range(0, 1):
            t[i] = a.product_name
            u[i] = a.product_image
            v[i] = a.product_description
            w[i] = a.product_price
            print(u[2])
            print(t[i])
            i = i + 1
    if request.method == 'POST':
        buyer_name = request.POST['Buyer_Name']
        item_name = request.POST['Item_Name']
        item_quantity = request.POST['Item_Quantity']
        price = request.POST['Price']
        mycart = Cart.objects.create()
        mycart.Buyer_Name = buyer_name
        mycart.Item_Name = item_name
        mycart.Item_Quantity = item_quantity
        mycart.Price = price
        mycart.save()
        messages.success(request,"Product added to Cart")
    print("hello")
    context = {"variable": request.user,"proname": t[4],"prodesc": v[4],"price": w[4],"img": u[4] }
    return render(request, 'buypage.html', context)

@login_required(login_url='loginh')
def buy6(request):
    t = []
    t = [0 for i in range(0, 16)]
    u = [0 for i in range(0, 16)]
    v = [0 for i in range(0, 16)]
    w = [0 for i in range(0, 16)]
    i = 0
    for a in Product.objects.all():
        for b in range(0, 1):
            t[i] = a.product_name
            u[i] = a.product_image
            v[i] = a.product_description
            w[i] = a.product_price
            print(u[2])
            print(t[i])
            i = i + 1
    if request.method == 'POST':
        buyer_name = request.POST['Buyer_Name']
        item_name = request.POST['Item_Name']
        item_quantity = request.POST['Item_Quantity']
        price = request.POST['Price']
        mycart = Cart.objects.create()
        mycart.Buyer_Name = buyer_name
        mycart.Item_Name = item_name
        mycart.Item_Quantity = item_quantity
        mycart.Price = price
        mycart.save()
        messages.success(request,"Product added to Cart")
    print("hello")
    context = {"variable": request.user,"proname": t[5],"prodesc": v[5],"price": w[5],"img": u[5] }
    return render(request, 'buypage.html', context)

@login_required(login_url='loginh')
def buy7(request):
    t = []
    t = [0 for i in range(0, 16)]
    u = [0 for i in range(0, 16)]
    v = [0 for i in range(0, 16)]
    w = [0 for i in range(0, 16)]
    i = 0
    for a in Product.objects.all():
        for b in range(0, 1):
            t[i] = a.product_name
            u[i] = a.product_image
            v[i] = a.product_description
            w[i] = a.product_price
            print(u[2])
            print(t[i])
            i = i + 1
    if request.method == 'POST':
        buyer_name = request.POST['Buyer_Name']
        item_name = request.POST['Item_Name']
        item_quantity = request.POST['Item_Quantity']
        price = request.POST['Price']
        mycart = Cart.objects.create()
        mycart.Buyer_Name = buyer_name
        mycart.Item_Name = item_name
        mycart.Item_Quantity = item_quantity
        mycart.Price = price
        mycart.save()
        messages.success(request,"Product added to Cart")
    print("hello")
    context = {"variable": request.user,"proname": t[6],"prodesc": v[6],"price": w[6],"img": u[6] }
    return render(request, 'buypage.html', context)

@login_required(login_url='loginh')
def buy8(request):
    t = []
    t = [0 for i in range(0, 16)]
    u = [0 for i in range(0, 16)]
    v = [0 for i in range(0, 16)]
    w = [0 for i in range(0, 16)]
    i = 0
    for a in Product.objects.all():
        for b in range(0, 1):
            t[i] = a.product_name
            u[i] = a.product_image
            v[i] = a.product_description
            w[i] = a.product_price
            print(u[2])
            print(t[i])
            i = i + 1
    if request.method == 'POST':
        buyer_name = request.POST['Buyer_Name']
        item_name = request.POST['Item_Name']
        item_quantity = request.POST['Item_Quantity']
        price = request.POST['Price']
        mycart = Cart.objects.create()
        mycart.Buyer_Name = buyer_name
        mycart.Item_Name = item_name
        mycart.Item_Quantity = item_quantity
        mycart.Price = price
        mycart.save()
        messages.success(request,"Product added to Cart")
    print("hello")
    context = {"variable": request.user,"proname": t[7],"prodesc": v[7],"price": w[7],"img": u[7] }
    return render(request, 'buypage.html', context)

@login_required(login_url='loginh')
def buy9(request):
    t = []
    t = [0 for i in range(0, 16)]
    u = [0 for i in range(0, 16)]
    v = [0 for i in range(0, 16)]
    w = [0 for i in range(0, 16)]
    i = 0
    for a in Product.objects.all():
        for b in range(0, 1):
            t[i] = a.product_name
            u[i] = a.product_image
            v[i] = a.product_description
            w[i] = a.product_price
            print(u[2])
            print(t[i])
            i = i + 1
    if request.method == 'POST':
        buyer_name = request.POST['Buyer_Name']
        item_name = request.POST['Item_Name']
        item_quantity = request.POST['Item_Quantity']
        price = request.POST['Price']
        mycart = Cart.objects.create()
        mycart.Buyer_Name = buyer_name
        mycart.Item_Name = item_name
        mycart.Item_Quantity = item_quantity
        mycart.Price = price
        mycart.save()
        messages.success(request,"Product added to Cart")
    print("hello")
    context = {"variable": request.user,"proname": t[8],"prodesc": v[8],"price": w[8],"img": u[8] }
    return render(request, 'buypage.html', context)

@login_required(login_url='loginh')
def buy10(request):
    t = []
    t = [0 for i in range(0, 16)]
    u = [0 for i in range(0, 16)]
    v = [0 for i in range(0, 16)]
    w = [0 for i in range(0, 16)]
    i = 0
    for a in Product.objects.all():
        for b in range(0, 1):
            t[i] = a.product_name
            u[i] = a.product_image
            v[i] = a.product_description
            w[i] = a.product_price
            print(u[2])
            print(t[i])
            i = i + 1
    if request.method == 'POST':
        buyer_name = request.POST['Buyer_Name']
        item_name = request.POST['Item_Name']
        item_quantity = request.POST['Item_Quantity']
        price = request.POST['Price']
        mycart = Cart.objects.create()
        mycart.Buyer_Name = buyer_name
        mycart.Item_Name = item_name
        mycart.Item_Quantity = item_quantity
        mycart.Price = price
        mycart.save()
        messages.success(request,"Product added to Cart")
    print("hello")
    context = {"variable": request.user,"proname": t[9],"prodesc": v[9],"price": w[9],"img": u[9] }
    return render(request, 'buypage.html', context)

@login_required(login_url='loginh')
def buy11(request):
    t = []
    t = [0 for i in range(0, 16)]
    u = [0 for i in range(0, 16)]
    v = [0 for i in range(0, 16)]
    w = [0 for i in range(0, 16)]
    i = 0
    for a in Product.objects.all():
        for b in range(0, 1):
            t[i] = a.product_name
            u[i] = a.product_image
            v[i] = a.product_description
            w[i] = a.product_price
            print(u[2])
            print(t[i])
            i = i + 1
    if request.method == 'POST':
        buyer_name = request.POST['Buyer_Name']
        item_name = request.POST['Item_Name']
        item_quantity = request.POST['Item_Quantity']
        price = request.POST['Price']
        mycart = Cart.objects.create()
        mycart.Buyer_Name = buyer_name
        mycart.Item_Name = item_name
        mycart.Item_Quantity = item_quantity
        mycart.Price = price
        mycart.save()
        messages.success(request,"Product added to Cart")
    print("hello")
    context = {"variable": request.user,"proname": t[10],"prodesc": v[10],"price": w[10],"img": u[10] }
    return render(request, 'buypage.html', context)

@login_required(login_url='loginh')
def buy12(request):
    t = []
    t = [0 for i in range(0, 16)]
    u = [0 for i in range(0, 16)]
    v = [0 for i in range(0, 16)]
    w = [0 for i in range(0, 16)]
    i = 0
    for a in Product.objects.all():
        for b in range(0, 1):
            t[i] = a.product_name
            u[i] = a.product_image
            v[i] = a.product_description
            w[i] = a.product_price
            print(u[2])
            print(t[i])
            i = i + 1
    if request.method == 'POST':
        buyer_name = request.POST['Buyer_Name']
        item_name = request.POST['Item_Name']
        item_quantity = request.POST['Item_Quantity']
        price = request.POST['Price']
        mycart = Cart.objects.create()
        mycart.Buyer_Name = buyer_name
        mycart.Item_Name = item_name
        mycart.Item_Quantity = item_quantity
        mycart.Price = price
        mycart.save()
        messages.success(request,"Product added to Cart")
    print("hello")
    context = {"variable": request.user,"proname": t[11],"prodesc": v[11],"price": w[11],"img": u[11] }
    return render(request, 'buypage.html', context)

@login_required(login_url='loginh')
def buy13(request):
    t = []
    t = [0 for i in range(0, 16)]
    u = [0 for i in range(0, 16)]
    v = [0 for i in range(0, 16)]
    w = [0 for i in range(0, 16)]
    i = 0
    for a in Product.objects.all():
        for b in range(0, 1):
            t[i] = a.product_name
            u[i] = a.product_image
            v[i] = a.product_description
            w[i] = a.product_price
            print(u[2])
            print(t[i])
            i = i + 1
    if request.method == 'POST':
        buyer_name = request.POST['Buyer_Name']
        item_name = request.POST['Item_Name']
        item_quantity = request.POST['Item_Quantity']
        price = request.POST['Price']
        mycart = Cart.objects.create()
        mycart.Buyer_Name = buyer_name
        mycart.Item_Name = item_name
        mycart.Item_Quantity = item_quantity
        mycart.Price = price
        mycart.save()
        messages.success(request,"Product added to Cart")
    print("hello")
    context = {"variable": request.user,"proname": t[12],"prodesc": v[12],"price": w[12],"img": u[12] }
    return render(request, 'buypage.html', context)

@login_required(login_url='loginh')
def buy14(request):
    t = []
    t = [0 for i in range(0, 16)]
    u = [0 for i in range(0, 16)]
    v = [0 for i in range(0, 16)]
    w = [0 for i in range(0, 16)]
    i = 0
    for a in Product.objects.all():
        for b in range(0, 1):
            t[i] = a.product_name
            u[i] = a.product_image
            v[i] = a.product_description
            w[i] = a.product_price
            print(u[2])
            print(t[i])
            i = i + 1
    if request.method == 'POST':
        buyer_name = request.POST['Buyer_Name']
        item_name = request.POST['Item_Name']
        item_quantity = request.POST['Item_Quantity']
        price = request.POST['Price']
        mycart = Cart.objects.create()
        mycart.Buyer_Name = buyer_name
        mycart.Item_Name = item_name
        mycart.Item_Quantity = item_quantity
        mycart.Price = price
        mycart.save()
        messages.success(request,"Product added to Cart")
    print("hello")
    context = {"variable": request.user,"proname": t[13],"prodesc": v[13],"price": w[13],"img": u[13] }
    return render(request, 'buypage.html', context)

@login_required(login_url='loginh')
def buy15(request):
    t = []
    t = [0 for i in range(0, 16)]
    u = [0 for i in range(0, 16)]
    v = [0 for i in range(0, 16)]
    w = [0 for i in range(0, 16)]
    i = 0
    for a in Product.objects.all():
        for b in range(0, 1):
            t[i] = a.product_name
            u[i] = a.product_image
            v[i] = a.product_description
            w[i] = a.product_price
            print(u[2])
            print(t[i])
            i = i + 1
    if request.method == 'POST':
        buyer_name = request.POST['Buyer_Name']
        item_name = request.POST['Item_Name']
        item_quantity = request.POST['Item_Quantity']
        price = request.POST['Price']
        mycart = Cart.objects.create()
        mycart.Buyer_Name = buyer_name
        mycart.Item_Name = item_name
        mycart.Item_Quantity = item_quantity
        mycart.Price = price
        mycart.save()
        messages.success(request,"Product added to Cart")
    print("hello")
    context = {"variable": request.user,"proname": t[14],"prodesc": v[14],"price": w[14],"img": u[14] }
    return render(request, 'buypage.html', context)

@login_required(login_url='loginh')
def buy16(request):
    t = []
    t = [0 for i in range(0, 16)]
    u = [0 for i in range(0, 16)]
    v = [0 for i in range(0, 16)]
    w = [0 for i in range(0, 16)]
    i = 0
    for a in Product.objects.all():
        for b in range(0, 1):
            t[i] = a.product_name
            u[i] = a.product_image
            v[i] = a.product_description
            w[i] = a.product_price
            print(u[2])
            print(t[i])
            i = i + 1
    if request.method == 'POST':
        buyer_name = request.POST['Buyer_Name']
        item_name = request.POST['Item_Name']
        item_quantity = request.POST['Item_Quantity']
        price = request.POST['Price']
        mycart = Cart.objects.create()
        mycart.Buyer_Name = buyer_name
        mycart.Item_Name = item_name
        mycart.Item_Quantity = item_quantity
        mycart.Price = price
        mycart.save()
        messages.success(request,"Product added to Cart")
    print("hello")
    context = {"variable": request.user,"proname": t[15],"prodesc": v[15],"price": w[15],"img": u[15] }
    return render(request, 'buypage.html', context)




def logouth(request):
    logout(request)
    messages.success(request, "successfully loggedout")
    return redirect('loginh')
# Create your views here.
