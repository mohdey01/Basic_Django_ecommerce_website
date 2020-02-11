from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name=models.CharField(max_length=50)
    product_category=models.CharField(max_length=50,default="")
    product_subcategory=models.CharField(max_length=50,default="")
    product_price=models.IntegerField(default=0)
    product_description=models.CharField(max_length=300)
    product_image=models.ImageField(upload_to="shop/images",default="")
    product_publishDate=models.DateField()

    def __str__(self):
        return self.product_name
class Contactus(models.Model):
    contact_id = models.AutoField(primary_key=True)
    contact_name=models.CharField(max_length=50)
    contact_email=models.CharField(max_length=50,default="")
    contact_phonenumber=models.CharField(max_length=50,default="")
    contact_description=models.CharField(max_length=50,default="")
    

    def __str__(self):
        return self.contact_name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    orderitems_json=models.CharField(max_length=4000)
    order_name=models.CharField(max_length=50)
    order_email=models.CharField(max_length=50,default="")
    order_phone=models.CharField(max_length=50,default="")
    order_address=models.CharField(max_length=50,default="")
    order_city=models.CharField(max_length=50,default="")
    order_state=models.CharField(max_length=50,default="")
    order_zip=models.CharField(max_length=50,default="")
    

    def __str__(self):
        return self.order_name

class OrderUpdate(models.Model):
    orderupdate_id = models.AutoField(primary_key=True)
    order_id=models.IntegerField(default=0)
    order_name=models.CharField(max_length=50,default="")
    orderupdate_description=models.CharField(max_length=4000,default="")
    orderupdate_timestamp=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.order_name