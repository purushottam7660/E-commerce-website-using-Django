from products.models import Products
from django.contrib.auth.models import User

def get_cart_count(request):
    count = 0
    # user = User.objects.get(user=request.user)
    if request.user.is_authenticated:
        try:
            prods=Products.objects.filter(cards=request.user)
            # print("card->",prods)
            if prods:
                for i in prods:
                    count+=1
            else:
                count = 0         
        except:
            count = 0
    return dict(count=count) 

def get_wishlist_count(request):
    wish_count = 0
    # user = User.objects.get(user=request.user)
    if request.user.is_authenticated:
        try:
            prods=Products.objects.filter(likes=request.user)
            if prods:
                for i in prods:
                    wish_count+=1
            else:
                wish_count = 0         
        except:
            wish_count = 0
    return dict(wish_count=wish_count) 





