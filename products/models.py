from django.db import models
from django .contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    Category_name=models.CharField(max_length=100)
    C_description=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Category_name

class Products(models.Model):

    categorys_m=models.ForeignKey(Category,on_delete=models.CASCADE)
    
    # likes=models.ManyToManyField(User,related_name='liked',blank=True,null=True)
    # cards=models.ManyToManyField(User,related_name='card',blank=True,null=True)
    likes = models.ManyToManyField(User, related_name='liked_products', blank=True)
    cards = models.ManyToManyField(User, related_name='card_products', blank=True)
    # Add_card=models.OneToOneField(User,related_name='cards',on_delete=models.CASCADE,blank=True,null=True)

    Products_name=models.CharField(max_length=100)
    prod_img=models.ImageField(upload_to='img/',blank=True,null=True)
    price=models.IntegerField()
    P_description=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Products_name