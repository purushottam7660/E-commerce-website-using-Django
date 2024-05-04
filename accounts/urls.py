from django.urls import path
from accounts import views
urlpatterns = [
    path('',views.user_login,name='user_login'),
    path('register',views.register,name='register'),
    path('index',views.index,name='index'),
    path('details/<int:pk>/',views.pro_details,name='details'),
    path('user_logout/',views.user_logout,name='user_logout'),
    path("profile",views.profile,name='profile'),
    path("add_profile",views.update_user,name="add_profile"),

    path('product_like/<int:pk>/',views.product_like,name='product_like'),
    path("wishlisted",views.Wishlist,name="wishlisted"),
    path("search",views.search,name="search"),
    path('add_to_card/<int:pk>/',views.Add_to_cart,name='add_to_card'),
    path("card",views.payment,name="card"),
    path('delete',views.delete_product,name="delete"),
    
    path('remove_wish',views.remove_wishlist,name="remove_wish"),

    # path("add_to_card",views.add_to_card,name="add_to_card"),
    # path("Wishlist_b/<int:pk>/",views.Wishlist_b,name="Wishlist_b"),
    path("success",views.success,name="success"),
    # path('user_list',views.user_list,name="user_list"),
    path("product",views.Product_view,name="product"),
    path("category",views.Category_view,name="category"),


]