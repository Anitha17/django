from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Userdata,Product,Cart,Bill

# Create your views here.

def index(request):
    return render(request,'index.html')

def signup(request,method=['GET','POST']):
    if request.method == "POST":
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')

        user=Userdata.objects.filter(email=email)

        if user.exists():
            messages.info(request,"user is already exists")
        elif password1 != password2:
            messages.info(request,"passwords are does not match")
        else:
            Userdata.objects.create(email=email,password=password1)
            return render(request,'login.html')
    return render(request,'signup.html')      
def login(request,method=['GET','POST']):
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')

        user=Userdata.objects.filter(email=email,password=password)
        if user.exists():
            request.session['email']=email
            return redirect('/home/')
        else:
            messages.info(request,"email and password are incorrect")
            return render(request,'login.html')
    return render(request,'login.html')   

def home(request):
    email=request.session['email']
    products=Product.objects.all()
    return render(request,'home.html',{'products':products,'email':email})

def cart_page(request,id):
    email=request.session['email']
    user=Userdata.objects.get(email=email)
    item=Product.objects.get(id=id)

    cart_item,created=Cart.objects.get_or_create(user=user,item=item)

    if not created:
        cart_item.quantity+=1
        cart_item.save()
    return redirect('/view_cart/')

def view_cart(request):
    email=request.session['email']
    user=Userdata.objects.get(email=email)
    cart_items=Cart.objects.filter(user=user)
    total_amt=sum(i.item.dcost*i.quantity for i in cart_items)
    return render(request,'cart_page.html',{'cart_items':cart_items,'total_amt':total_amt})

def checkout(request):
    total_amt=request.GET['total_amt']
    return render(request,'checkout.html',{'total_amt':total_amt})

def billing(request,method=['GET','POST']):
    if request.method=='POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        username=request.POST.get('username')
        address=request.POST.get('address')
        country=request.POST.get('country')
        state=request.POST.get('state')
        zip=request.POST.get('zip')
        paymentMethod=request.POST.get('paymentMethod')
        Bill.objects.create(firstname=firstname,lastname=lastname,username=username,address=address,country=country,state=state,zip=zip,paymentMethod=paymentMethod)
    return render(request,'success.html')
