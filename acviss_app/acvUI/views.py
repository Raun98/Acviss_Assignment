from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import NumberForm
from .services import populateDB, register_batch_update, load_user_table
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated



class ApiView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

class SearchView(APIView):
    #permission_classes = (IsAuthenticated,)

    def get(self, request):
        print("search started")
        resp = []
        search = request.query_params.get('name')
        name = request.user
        if name.is_authenticated:
            name = str(name)
            content = load_user_table(name)
            print(content)
            for i,j in content:
                if name == i:
                    resp.append((i,j))
        return Response(resp)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def FormPage(request):
    name = request.user
    if name.is_authenticated:
        name = str(name)
    else:
        name = 'Guest'

    #number = NumberForm.number_of_codes
    print(request.user)
    print('test triggered')
    print(type(str(request.user)))
    result = None
    if request.method == 'POST':
        form = NumberForm(request.POST)
        if form.is_valid():
            batch_name = form.cleaned_data['batch_name']
            number_of_codes = form.cleaned_data['number_of_codes']
            #print(batch_name," ", number_of_codes)
            populateDB(number_of_codes, batch_name)
            register_batch_update(name, batch_name)
            result = load_user_table(name)
            form=NumberForm()
    return render(request, 'index.html', {'form': form,'result':result})

def HomePage(request):
    name = request.user
    result = None
    if name.is_authenticated:
        name = str(name)
        result = load_user_table(name)
    #print(name," ", result)
    return render(request, 'index.html', {'result' : result})