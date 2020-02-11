from django.http import HttpResponse
from django.shortcuts import render
from .models import Product,Contactus,Order,OrderUpdate
from math import ceil
import json

def Index(request):
    products=Product.objects.all()
    allProducts=[]
    allCategories=Product.objects.values('product_category','id')
    categories={item['product_category'] for item in allCategories}
    for category in categories:
        products=Product.objects.filter(product_category=category)
        n=len(products)
        nSlides=n//4+ceil((n/4)-(n//4))
        allProducts.append([products,range(1,nSlides),nSlides])
    params={'allProducts':allProducts}
    return render(request,'shop/index.html',params)

def MatchSearch(search_item,product):
    if (search_item in product.product_description.lower() or search_item in product.product_name.lower()
            or search_item in product.product_category.lower() or search_item in product.product_subcategory.lower()):
        return True 
    else:
        return False   

def searchProducts(request):
    search_item=request.GET.get('search')
    products=Product.objects.all()
    allProducts=[]
    allCategories=Product.objects.values('product_category','id')
    categories={item['product_category'] for item in allCategories}
    for category in categories:
        products_category=Product.objects.filter(product_category=category)
        products=[product for product in products_category if MatchSearch(search_item,product)]
        n=len(products)
        nSlides=n//4+ceil((n/4)-(n//4))
        if(len(products)!=0):
            allProducts.append([products,range(1,nSlides),nSlides])
    params={'allProducts':allProducts}
    if(len(allProducts)==0 or len(search_item)<4):
        msg="Please Make Sure you are searching for the right product in our store"
        params['msg']=msg
    return render(request,'shop/search.html',params)

def AboutUs(request):
    return render(request,'shop/about.html')

def ContactUs(request):
    msg=''
    status=''
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phonenumber=request.POST.get('phoneNumber','')
        description=request.POST.get('description','')
        print(name)
        if(name!='' and name!=None and email!='' and email!=None and phonenumber!='' and phonenumber!=None and description!='' and description!=None    ):
            contact=Contactus(contact_name=name,contact_email=email,contact_phonenumber=phonenumber,contact_description=description)
            contact.save()
            msg="Thanks for Contacting Us! Our Support Person will get back to you soon."
            status="success"
        else:
            status="error"
            msg="Please make sure you have entered data in all the fields before proceeding ahead."
            
    params={'msg':msg,'status':status}
    return render(request,'shop/contact.html',params)

def TrackingStatus(request): 
    if request.method=="POST":
        order_name=request.POST.get('name','')
        order_id=request.POST.get('orderId')
        order_email=request.POST.get('email','')
        print(order_id)
        print(order_email)
        try:
            order=Order.objects.filter(order_id=order_id,order_email=order_email,order_name=order_name)
            print(len(order))
            if len(order)>0:
                order_update=OrderUpdate.objects.filter(order_id=order_id)
                print(order_update)
                order_updates=[]
                for item in order_update:
                    order_updates.append({'update_description':item.orderupdate_description,'update_timestamp':item.orderupdate_timestamp})
                    response=json.dumps({'status':'success','order_update':order_updates,'order_item_json':order[0].orderitems_json},default=str)
                    print(response)
                return HttpResponse(response)
            else:
                response=json.dumps({'status':'noitems'},default=str)
                return HttpResponse(response)  
        except Exception as e:
            response=json.dumps({'status':'itemsmissing'},default=str)
            return HttpResponse(response)  
    return render(request,'shop/tracker.html')


def ProductView(request,myid):
    product=Product.objects.filter(id=myid)

    return render(request,'shop/productView.html',{'product':product[0]})

def CheckOut(request):
    if request.method=="POST":
        order_name=request.POST.get('name','')
        order_itemsjson=request.POST.get('orderitems_json','')
        email=request.POST.get('email','')
        phonenumber=request.POST.get('phone','')
        full_address=request.POST.get('address1','')+' '+request.POST.get('address2','')
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        zipcode=request.POST.get('zip','')
        if(order_name!='' and order_itemsjson!='' and email!='' and phonenumber!='' and full_address!='' and city!='' and state!='' and zipcode!=''):
                
                order=Order(order_name=order_name,orderitems_json=order_itemsjson,order_email=email,order_phone=phonenumber,order_address=full_address,order_city=city,order_state=state,order_zip=zipcode)
                order.save()
                update=OrderUpdate(order_id=order.order_id,order_name=order_name,orderupdate_description="Your Order Has been placed and will get dispatched in a day or two!")
                update.save()
                acknowledgement=True
                order_id=order.order_id
                return render(request,'shop/checkout.html',{'acknowledgement':acknowledgement,'order_id':order_id})    
        else:
                acknowledgement=False 
                return render(request,'shop/checkout.html',{'acknowledgement':acknowledgement})
    return render(request,'shop/checkout.html')
    