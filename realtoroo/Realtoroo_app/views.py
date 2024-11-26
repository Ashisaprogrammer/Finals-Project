from django.shortcuts import render
from django.http import HttpResponse
from .models import Users_Login
from .models import home_info
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import home_info 
from django.db import  connection as cn
from django.shortcuts import render, redirect
from .models import home_info
#from .forms import ItemForm
# Create your views here.

def home(request):
 return render(request,'home.html')

def sign_up(request): 
 return render(request,'sign_up.html')

def login(request): 
 return  (render(request,'login.html'))

def houses(request):
    all_houses = home_info.objects.all()  # Retrieve all houses from the database
    return render(request, 'houses.html', {'houses': all_houses})

def Registerprocess(request):
 flag=False
 us=request.POST.get("username")
 emailM=request.POST.get("email")
 pwds=request.POST.get("password1")
 cpwds = request.POST.get('password2')
 if Users_Login.objects.filter(user_name=us).exists():
    return render(request, "sign_up.html", {"user_exists": "Please enter different username"})
 else:
     if pwds==cpwds:
        sref=Users_Login(user_name=us,email=emailM,pwd=pwds)
        sref.save()
        flag=True
 if flag == True:
      return render(request,'sign_up.html',{"RegisConfirmMsg":"REGISTRATION SUCCESSFUL!!"})
 else:
      return render(request,'sign_up.html',{"RegisInvalid":"ENTERED PASSWORD AND CONFIRMED PASSWORD DO NOT MATCH. PLEASE TRY AGAIN."})		        	
	    

def loginprocess(request):
	users = Users_Login.objects.all()
	lflag=False
	funame=request.POST.get("email")
	fpwd=request.POST.get("password")
	print(funame,fpwd)
	print(users)
	
	if Users_Login.objects.filter(email=funame,pwd=fpwd).exists():
		return render(request,"houses.html",{"loggedinUser":funame})
	else:
		return render(request, "login.html", {"invalid": "INVALID DETAILS. PLEASE TRY AGAIN."})
    

def view_details(request): 
    return render(request, 'details.html')	


def details(request):
    #data = home_info.objects.all
    hids=request.POST.get("houseid")
    print("aafhid",hids)
    with cn.cursor() as cursor: 
        cursor.execute("SELECT * FROM realtoroo_app_home_info where hid = %s",[hids])
        data = cursor.fetchall()
        print("ssss",data)

        '''house_details =[] 
        for row in data: 
            house_info = {
                "hid":row[1],
                "cost":row[2],
                "location":row[3],
                "num_rooms":row[4]
                }
            house_details.append(house_info)'''
    print("something",data)
    return render(request,"details.html",{"house_details": data})


def register_house(request):
    if request.method == 'POST':
        hid = request.POST.get("hid")
        cost = request.POST.get("cost")
        location = request.POST.get("location")
        num_rooms = request.POST.get("num_rooms")
        type_building = request.POST.get("type_building")
        bid = request.POST.get("bid")
        num_floors = request.POST.get("num_floors")
        img = request.FILES.get('img')

        # Create a new house entry
        new_house = home_info(
            hid=hid,
            cost=cost,
            location=location,
            num_rooms=num_rooms,
            type_building=type_building,
            bid=bid,
            num_floors=num_floors,
            img=img
        )
        new_house.save()

        houses = home_info.objects.all()
        
        return redirect('houses')  # Redirect to the houses page after registration

    return render(request, 'register_house.html')



'''def register_house(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('houses.html')  # Redirect to display page
    else:
        form = ItemForm()
    return render(request, 'register_house.html', {'form': form})

# View for displaying data
def show_items(request):
    items = home_info.objects.all()
    return render(request, 'houses.html', {'items': items})'''
