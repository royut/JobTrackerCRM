from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserRegisterForm


User = get_user_model()

# Create your views here.
def register_view(request):
    # POST
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.errors)
    # GET
    form = UserRegisterForm()
    return render(request, 'User/register.html', {'form': form})


def login_view(request):
    # POST
    if request.method == 'POST':
        email = request.POST['email']
        preAuthUser = User.objects.get(email=email)
        username = preAuthUser.get_username()
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            print('Invalid Credentials')
            return render(request, 'User/login.html', {'error': 'Invalid Credentials'})
    # GET
    return render(request, 'User/login.html')


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def index_view(request):
    user = request.user
    print(user)
    return render(request, 'User/index.html', {'user': user})


# for test purposes
def test_view(request):
    return render(request, 'base.html')