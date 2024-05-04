from django.db import models
from django .contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.

class Userdetails(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    # email = models.EmailField()
    user_img=models.ImageField(upload_to='img/',blank=True,null=True)
    phone=models.BigIntegerField(null=True)
    address=models.CharField(max_length=200)
    street=models.CharField(max_length=200)
    landmark=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    STATE_CHOICES = (
        ('Andhra Pradesh', 'Andhra Pradesh'),
        ('Arunachal Pradesh', 'Arunachal Pradesh'),
        ('Assam', 'Assam'),
        ('Bihar', 'Bihar'),
        ('Chhattisgarh', 'Chhattisgarh'),
        ('Goa', 'Goa'),
        ('Gujarat', 'Gujarat'),
        ('Haryana', 'Haryana'),
        ('Himachal Pradesh', 'Himachal Pradesh'),
        ('Jharkhand', 'Jharkhand'),
        ('Karnataka', 'Karnataka'),
        ('Kerala', 'Kerala'),
        ('Madhya Pradesh', 'Madhya Pradesh'),
        ('Maharashtra', 'Maharashtra'),
        ('Manipur', 'Manipur'),
        ('Meghalaya', 'Meghalaya'),
        ('Mizoram', 'Mizoram'),
        ('Nagaland', 'Nagaland'),
        ('Odisha', 'Odisha'),
        ('Punjab', 'Punjab'),
        ('Rajasthan', 'Rajasthan'),
        ('Sikkim', 'Sikkim'),
        ('Tamil Nadu', 'Tamil Nadu'),
        ('Telangana', 'Telangana'),
        ('Tripura', 'Tripura'),
        ('Uttar Pradesh', 'Uttar Pradesh'),
        ('Uttarakhand', 'Uttarakhand'),
        ('West Bengal', 'West Bengal'),
        ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
        ('Chandigarh', 'Chandigarh'),
        ('Dadra and Nagar Haveli and Daman and Diu', 'Dadra and Nagar Haveli and Daman and Diu'),
        ('Lakshadweep', 'Lakshadweep'),
        ('Delhi', 'Delhi'),
        ('Puducherry', 'Puducherry'),
    )
    state=models.CharField(max_length=200,choices=STATE_CHOICES)
    zipcode=models.BigIntegerField(null=True)

    def __str__(self):
        return str(self.user.username)
    
    def clean(self):
        super().clean()
        if self.phone:
            phone_str = str(self.phone)
            if len(phone_str) != 10 or phone_str[0] not in ('6', '7', '8', '9'):
                raise ValidationError('Phone Number must be 10 digits and start with 6, 7, 8, or 9')
        self.clean_zipcode()    

    def clean_zipcode(self):
        if self.zipcode:
            zipcode_str = str(self.zipcode)
            if not (5 <= len(zipcode_str) <= 6):  # Corrected condition
                raise ValidationError('Please Enter a Valid zipcode!!!')
