from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from django.db.models import Q

# Create your views here.


def home(request):
    if request.user.is_authenticated:
        return redirect('getmedicine')
    context = {}
    return render(request, 'work/index.html', context)

@login_required(login_url='userlogin')
def update(request):
    d = request.session.get('id')
    del d['csrfmiddlewaretoken']
    for id,qty in d.items():
        if qty=='':
            continue
        else:
            val = int(qty)
            db = Medicines.objects.get(id=id)
            if val>=db.available:
                db.available = 0
            else:
                db.available = db.available - val
            db.save()
    return redirect('getmedicine')
            

@login_required(login_url='userlogin')
def order(request):
    data = []
    d = request.session.get('id')
    items = 0
    total = 0
    del d['csrfmiddlewaretoken']
    for id,qty in d.items():
        if qty=='':
            continue
        else:
            
            val = int(qty)
            db = Medicines.objects.get(id=id)
            if val>db.available:
                val=db.available
            
            items+=val
            total+=val*db.price
            data.append({'name':db.name,'mg':db.mg,'qty':val,'price':db.price*val})
    context = {'data':data,'items':str(items),'total':str(total), 'user':request.user}
    print(context)
    return render(request, 'work/order.html', context)


@login_required(login_url='userlogin')
def getmedicine(request):
    if request.method=='POST':
        context={}
        d = request.POST.dict()
        request.session['id'] = d
        # print(d)
        return redirect('order')
    else:
        # print(request.user)
        medicines = Medicines.objects.all()
        context = {'medicines': medicines, 'user':request.user}
        return render(request, 'work/getmedicine.html', context)


def userlogin(request):
    # print(request.user)
    if request.user.is_authenticated:
        return redirect('getmedicine')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('getmedicine')
                # context = {'user':user}
                # return render(request, 'store/store.html', context)
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'work/login.html', context)


def signup(request):
    if request.user.is_authenticated:
        return redirect('getmedicine')
    else:
        if request.method == 'POST':
            print(request.POST)
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            messages.success(request, 'Account created successfully!')
            user = User.objects.create_user(username,email,password)
            user.save()

            user1,created = Customer.objects.get_or_create(username=request.POST.get("username"),firstname=request.POST.get("firstname"),lastname=request.POST.get("lastname"),password=request.POST.get("password"),phonecode=request.POST.get("pcode"),phNo=request.POST.get("phone"),email=request.POST.get("email"),houseNo=request.POST.get("house"),area=request.POST.get("area"),pincode=request.POST.get("pincode"),requirement=request.POST.get("req"))
            
            return redirect('userlogin')
        context = {}
        return render(request, 'work/signup.html', context)

def Logout(request):
    logout(request)
    return redirect('userlogin')
