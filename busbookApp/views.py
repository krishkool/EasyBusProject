from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, SearchBusForm
from .models import CustomerProfile, User, Bus
import decimal

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

@login_required
def custDash(request):
    return render(request, 'customerpage.html')

def login_view(request):
    try:
        if (request.method == 'POST'):
            username = request.POST['username']
            password = request.POST['password']
            
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('customerpage')
            else:
                return render(request, 'registration/login.html', {'error': 'Username or password error'})
    except Exception as e:     
        return render(request, 'registration/login.html', {'error': 'Form Error'})

def logout_view(request):
    logout(request)
    return redirect('login')

def signup_view(request):
    form = SignUpForm(request.POST)
    if (request.method == 'POST'):
        if form.is_valid():
            form.save()
            uname = form.cleaned_data.get('username')
            pwd   = form.cleaned_data.get('password1')

            user = authenticate(request, username = uname, password=pwd)
            login(request,user)

            return redirect('login')

    else:
        form = SignUpForm()
        return render(request, 'registration/sign_up.html', {'form': form})

def custProfile(request):
    try:
        current_user = request.user
        data = CustomerProfile.objects.get(username = current_user.username)
        return render(request, 'customerprofile.html', {"user_data": data})
    except Exception as e:
        return render(request, 'customerprofile.html')

def customerCreateProfile(request):
    try:
        if request.method == 'POST':
            current_user = request.user 
            username = current_user.username
            firstname = current_user.first_name    
            lastname = current_user.last_name 
            email = current_user.email       
            address = request.POST['addr']
            phone   = request.POST['contact']
            pic     = request.FILES['profile']
            
            user_exist = CustomerProfile.objects.filter(username = current_user.username)
            
            if user_exist is not None:
                
                user_exist.user    = current_user.id
                user_exist.address = address
                user_exist.number  = phone
                user_exist.profile_pic = pic
                
                user_exist = CustomerProfile(user_id = current_user.id, username = username, first_name = firstname, last_name = lastname, email = email, number = phone, address = address, profile_pic =  pic )
                user_exist.save()
                
                return render(request, 'customerprofile.html', {"success": "Profile Updated!"})

   
    except Exception as e:
        
                 
        return render(request, 'customerprofile.html', {"error": "Error Happened!"})

def bookingPage(request):
    try:
        datas = Bus.objects.all()
        return render(request, 'bookingpage.html', {'datas': datas})
    except Exception as e:
        return render(request, 'bookingpage.html')

def searchBus(request):
    try:
        if (request.method == 'POST'):
            source      = request.POST['source-data']
            destination = request.POST['dest-data']
            date = request.POST['date-val']
            bookData = Bus.objects.filter(date = date)
            if bookData is None:
                return render(request, 'bookingpage.html', {'error': 'No Tickets Available on this Date'} )
            if bookData is not None:
                return render(request, 'listofbus.html', {'busdata': bookData})
            
    except Exception as e:
        return render(request, 'bookingpage.html')


def bookTicket(request):
    try:
        if (request.method == 'POST'):
            bus_id = request.POST['bus-id']
            sel_seat = request.POST['bus-seat']
            dataCheck = Bus.objects.get(id = bus_id)
            
            sel_seat_val = int(sel_seat)
            rem_seat = int(dataCheck.remaining_seats) 
            unit_price = decimal.Decimal(dataCheck.price)
            
            if dataCheck is not None:
                try:
                    if sel_seat_val < dataCheck.remaining_seats:
                        
                        new_avail = rem_seat - sel_seat_val
                        dataCheck.remaining_seats = new_avail
                        tot_amt = unit_price * sel_seat_val
                        dataCheck.save()
                        return render(request, 'ticketinvoice.html', {'dataCheck': dataCheck, 'payable': tot_amt, 'seats': sel_seat_val })
                except Exception as e:
                    return render(request, 'bookingpage.html', {'errorbook': 'Remaining Seats are not Enough to Book...'})

    except Exception as e:
        print(e)
        


