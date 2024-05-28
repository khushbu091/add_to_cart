from django.shortcuts import render
from .forms import UserForm
from .models import*
from project.settings import MEDIA_URL, MEDIA_ROOT
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def home(request):
    my_dict ={}
    my_dict['form'] = UserForm
    return render(request,'home.html',my_dict)

def register(request):
    print(request.POST)
    print(request.FILES)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            my_dict ={}
            my_dict['form']=UserForm
            my_dict['msg']="register successfull"
            return render(request, 'home.html', my_dict)
        else:
            msg = 'found some error'
            return render(request,'home.html',{'key':msg})
    return render(request,'home.html')

def showdata(request):
    data = User.objects.all()  # Retrieve the instance you want to display
    return render(request, 'show.html', {'data': data,'media_url':MEDIA_URL})

def addtocard(request,pk):
    print(pk)
    print(request)
    cart = request.session.get('cart', [])
    if pk not in cart:
        cart.append(pk)
        print(cart)
        request.session['cart'] = cart
    print(len(cart))   
    data = User.objects.all()
    print(data)
    return render(request, 'show.html',{'data': data, 'media_url':MEDIA_URL})

# def cart(request):
#     cart = request.session.get('cart',[])
#     print(cart)

def cart_item(request):
    cart = request.session.get('cart')
    detail = []
    total_price = 0

    for i in cart:
        data = User.objects.get(id=i)
        cont = {
            "name":data.Name,
            "dec":data.Descri,
            "img":data.Image,
            "price":data.Price
        }
        total_price += data.Price
        detail.append(cont)

    return render(request,'cart_item.html',{'data':detail,'total_price': total_price,'media_url':MEDIA_URL})


    
    
    


   
