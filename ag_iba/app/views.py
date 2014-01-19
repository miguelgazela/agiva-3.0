from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.http import HttpResponse
from app.forms import UserCreationForm
from app.forms import ClientForm
from app.models import Client


@login_required
def index(request):
    return redirect('taxes')

# Auth Views -->

def login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(data=request.POST)
        if request.POST and login_form.is_valid():
            auth_login(request, login_form.get_user())
            return redirect('taxes')
        else:
            return render(request, 'app/auth/login.html',
                {'form': login_form})
    elif request.method == 'GET':
        return render(request, 'app/auth/login.html')


@login_required
def logout(request):
    """
    Log users out and re-direct them to the main page.
    """
    auth_logout(request)
    return redirect('/')


def signup(request):
    if request.method == 'GET':
        return render(request, 'app/auth/signup.html')
    elif request.method == 'POST':
        user_form = UserCreationForm(data=request.POST)
        if user_form.is_valid():
            username = user_form.clean_username()
            password = user_form.clean_password2()
            user = user_form.save(commit=False)
            user.is_active = False
            user.save()
            return render(request, 'app/auth/signup.html',
                {'username': username, 'status': 'success'})
        else:
            return render(request, 'app/auth/signup.html',
                {'form': user_form})


# <-- /. Auth Views


# Taxes Views -->

@login_required
def taxes(request, sort='all'):
    return render(request, 'app/taxes/list.html')

@login_required
def add_tax(request):
    return HttpResponse('Add Tax')

# <-- /. Taxes Views


# Clients Views -->

@login_required
def clients(request, sort='all'):
    clients = Client.objects.all()
    return render(request, 'app/clients/list.html',
        {'list_clients': clients})

@login_required
def client(request, client_id):
    return HttpResponse("Detail Client of client with id {0}".format(client_id))

@login_required
def add_client(request):
    if request.method == 'GET':
        return render(request, 'app/clients/add.html')
    elif request.method == 'POST':
        client_form = ClientForm(request.POST)
        if client_form.is_valid():
            client = client_form.save(commit=False)
            client.from_home = request.POST.get('client_type') == 'home'
            client.save()
            return redirect('client', client_id=client.id)
        else:
            return render(request, 'app/clients/add.html',
                {'form': client_form})


