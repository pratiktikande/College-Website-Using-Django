from django.shortcuts import render
from django.http import HttpResponse

from math import ceil
from .models import Product,Orders

def index(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params={'allProds':allProds }
    return render(request,"index.html", params)
    
def about(response):
    return render(response,'about.html')
def contact(response):
    return render(response,'contact.html')
    
def tracker(response):
    return render(response,'tracker.html')
    
def search(response):
    return render(response,'search.html')
    
def productview(response,myid):
    product =Product.objects.filter(id=myid)
    print(product)
    return render(response,'productview.html' ,{'product':product[0]})
    
# def checkout(request):
#     if request.method=='Post':
#         name=request.Post.get('name','')
#         email=request.Post.get('email','')
#         address=request.Post.get('address1','')+" "+request.Post.get('address2','')
#         Zipcode=request.Post.get('Zipcode','')
#         phone=request.Post.get('Phone','')

#         city=request.Post.get('City','')
#         state=request.Post.get('State','')
#         order=Orders(name=name,email=email,address=address,Zip=Zip,phone=phone,city=city,state=state)
#         order.save()
#         return render(request,'checkout.html')
    
#     return render(request,'checkout.html')
def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone)
        order.save()
        thank = True
        id = order.order_id
        return render(request, 'checkout.html', {'thank':thank, 'id': id})
    return render(request, 'checkout.html')
    
 

# Create your views here.
