from django.db import models
class Product(models.Model):
    Product_id=models.AutoField
    name=models.CharField(max_length=30)
    category=models.CharField(max_length=50 , default="")
    sub_category=models.CharField(max_length=50 , default="")
    price=models.IntegerField(default=0)

    description=models.CharField(max_length=100  ,default="")
    date=models.DateField()
    image=models.ImageField(upload_to ='ecomerce/images' ,default="")
    def __str__(self):
        return self.name
# class order(models.Model):
#     order_id=models.AutoField
#     name=models.CharField(max_length=30)
#     email=models.CharField(max_length=50 , default="")
#     address=models.CharField(max_length=50 , default="")
  

#     city=models.CharField(max_length=100  ,default="")
#     state=models.CharField(max_length=100  ,default="")
#     phone=models.CharField(max_length=100  ,default="")
#     Zipcode=models.CharField(max_length=100  ,default="")
    
class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")    

# Create your models here.
