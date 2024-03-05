from django.shortcuts import render , redirect
from accounts.models import CustomUser
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.decorators import login_required
from .models import CalcHistory

@login_required
def home(requests):
    if requests.method == "GET":
        data = requests.GET.get('data')
        if data:
            user = requests.user
            history = CalcHistory.objects.create(user = user,expression = data)
    historyData = CalcHistory.objects.all()
    context = {
        'calc_history': historyData
    }
    return render(requests,'index.html' , context )

def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = CustomUser.objects.filter(email=email,password=password).first()
        if user:
            login(request,user)
            print("Loggined")
            return redirect('Home')
        else :
            print("Not Logged In")
            return render(request,"login.html")

    return render(request,'login.html')

def signup(request):
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']
        confirm_pass=request.POST['cPassword']
        #Checking the password and confirm password field are same or not
        if password !=confirm_pass:
            return render(request,"signup.html",{"msg":"Passwords do not match"})
        
        #Creating a new User object with the given parameters  
        user = CustomUser(email=email,password=password)
        try:
            user.save()
            print("User Created Successfully!")
            return redirect('user_login')
        except Exception as e:
            print(e)
            return render(request,"signup.html") 
    return render(request,'signup.html')