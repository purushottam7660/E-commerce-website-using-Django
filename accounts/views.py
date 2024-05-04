from django.shortcuts import render,redirect,get_object_or_404
from accounts.forms import userForm,userprofileForm,Product_Form,Category_Form
from django.contrib.auth import authenticate, login, logout
from accounts.models import Userdetails
from django.contrib import messages

from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from products.models import Products,Category
from project.settings import  RZP_KEY_ID,RZP_KEY_SECRET

def register(request):
    registered=False
    if request.method == 'POST':
        form = userForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            
            user.save()
            registered=True
            login(request, user)

    else:
        form = userForm()
    return render(request, "registeration.html", {'form': form,'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        user = authenticate(username=username, password=password, email=email)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('index')
            else:
                return HttpResponse('Your account is disabled.')
        else:
            return HttpResponse('Invalid login')
    return render(request, 'user_login.html')


@login_required(login_url='user_login')   
def index(request):
    product=Products.objects.all()

    return render(request,'index.html',{'product':product})

@login_required(login_url='user_login')   
def user_logout(request):
    logout(request)
    return redirect('user_login')

@login_required(login_url='user_login')   
def pro_details(request,pk):
    detail=Products.objects.get(id=pk)
    details=Products.objects.get(id=pk)

    is_liked=False
    if detail.likes.filter(id=request.user.id).exists():
        is_liked=True
    prod_like=is_liked  

    is_card=False
    if details.cards.filter(id=request.user.id).exists():
        is_card=True
    prod_card=is_card  
    return render(request,'details.html',{'detail':detail,'prod_like':prod_like,'prod_card':prod_card,'details':details})

@login_required(login_url='user_login')   
def profile(request):
    if request.user.is_superuser:
        supers=request.user
        p=None
        user_details=None
    else:
        supers=None    
        try:
            user_details = Userdetails.objects.get(user=request.user)
        except Userdetails.DoesNotExist:
            # If user details don't exist, set user_details to None
            user_details = None

        # Check if user_details is not None and set the appropriate variable
        if user_details:
            user_details = Userdetails.objects.get(user=request.user)
            p=request.user
        else:
            p = request.user
    return render(request,"profile.html",{'p':p,'data':user_details,'supers':supers})


@login_required(login_url='user_login')
def update_user(request):
    if request.method == 'POST':
        form1 = userprofileForm(request.POST, request.FILES, instance=request.user)
        if form1.is_valid():
            img = form1.cleaned_data['user_img']
            # eml = form1.cleaned_data['email']
            ph = form1.cleaned_data['phone']
            ad = form1.cleaned_data['address']
            srt = form1.cleaned_data['street']
            ln = form1.cleaned_data['landmark']
            ct = form1.cleaned_data['city']
            st = form1.cleaned_data['state']
            zp = form1.cleaned_data['zipcode']
            
            # Check if a Userdetails instance already exists for the user
            user_details, created = Userdetails.objects.get_or_create(user=request.user)
            
            # Update the existing Userdetails instance
            # user_details.user.email = eml
            user_details.user_img = img
            user_details.phone = ph
            user_details.address = ad
            user_details.street = srt
            user_details.landmark = ln
            user_details.city = ct
            user_details.state = st
            user_details.zipcode = zp
            
            # Save the updated Userdetails instance
            user_details.save()
            
            return redirect('profile')
    else:
        # Pre-populate the form with request.user
        form1 = userprofileForm(instance=request.user)
        
    return render(request, 'add_profile.html', {'form1': form1})


@login_required(login_url='user_login')   
def product_like(request,pk):
    # prod_id=request.POST.get('product_id')
    # print(request.POST)
    # print("id ->",prod_id)
    product=get_object_or_404(Products,id=request.POST.get('product_id'))
    # print(product)
    if product.likes.filter(id=request.user.id).exists():
        product.likes.remove(request.user)
    else:
        product.likes.add(request.user)
    return redirect('details',pk=pk)

@login_required(login_url='user_login')   
def Wishlist(request):
    prod=Products.objects.filter(likes=request.user)
    return render(request,'wishlisted.html',{'prod':prod})

@login_required(login_url='user_login')   
def search(request):
    # search_item=request.POST.get('item')
    # print(search_item)
    search_item=''
    if request.POST.get('item'):
        search_item=request.POST.get('item')
    products = Products.objects.filter(Products_name__icontains=search_item)
       
    context={
        
        'search_item':search_item,
        'products':products
    }
    return render(request,"search.html",context)

import razorpay

@login_required(login_url='user_login')   
def payment(request):
    # client = razorpay.Client(auth=(RZP_KEY_ID, RZP_KEY_SECRET))
    prods=Products.objects.filter(cards=request.user)
    T_price=0
    counts=0
    delivery=0
    for i in prods:
        T_price +=i.price
        counts +=1
    gst=(T_price*4)/100
    if T_price<1:
        T_price=0
        counts=0
        delivery=0
    elif T_price>500 and T_price<1000 :
        delivery+=30
    elif T_price<500:
        delivery+=50
    else:    
        delivery=0

    total=T_price + (gst*2) + delivery
    amount=round((total * 100), 3)
    
    RZP_KEY=RZP_KEY_ID
    client = razorpay.Client(auth=(RZP_KEY_ID, RZP_KEY_SECRET))
    if amount <=0:
        amount=0
    else:    
        payment = client.order.create({'amount':amount, 'currency': 'INR','payment_capture': '1'})
    
    return render(request,'add_to_card.html',{'prods':prods,'T_price':T_price,'counts':counts,'gst':gst,'total':total,'delivery':delivery,'amount':amount,'RZP_KEY':RZP_KEY})


@login_required(login_url='user_login')   
def Add_to_cart(request,pk):
    # prods_id=request.POST.get('prod_id')
    # print(request.POST)
    # print("card id ->",prods_id)
    product = get_object_or_404(Products, id=request.POST.get('prod_id'))

    # print(product)
    if product.cards.filter(id=request.user.id).exists():
        product.cards.remove(request.user)
    else:
        product.cards.add(request.user)
    return redirect('details',pk=pk)


@login_required(login_url='user_login')   
def delete_product(request):
    product = get_object_or_404(Products, id=request.POST.get('pro_id'))
    if product.cards.filter(id=request.user.id).exists():
        product.cards.remove(request.user)
    return redirect('card')


@login_required(login_url='user_login')   
def remove_wishlist(request):
    product = get_object_or_404(Products, id=request.POST.get('product_id'))
    if product.likes.filter(id=request.user.id).exists():
        product.likes.remove(request.user)
    return redirect('wishlisted')

@login_required(login_url='user_login')   
def success(request):
    return render(request,'success.html')



@login_required(login_url='user_login')
def Product_view(request):
    if request.method == 'POST':
        p_form = Product_Form(request.POST, request.FILES)
        if p_form.is_valid():
            p_form.save()            
    else:
        p_form = Product_Form(instance=request.user)
        
    return render(request, 'Product.html', {'p_form': p_form})

@login_required(login_url='user_login')
def Category_view(request):
    message = None
    if request.method == 'POST':
        C_form = Category_Form(request.POST)
        if C_form.is_valid():
            # Check if the category already exists
            category_name = C_form.cleaned_data['Category_name']
            if Category.objects.filter(Category_name=category_name).exists():
                # Add a pop-up message
                message= "already exists."
            else:
                # message=None
                C_form.save()
                return redirect('category')
    else:
        C_form = Category_Form(instance=request.user)
    return render(request, 'Category.html', {'C_form': C_form,'message':message})