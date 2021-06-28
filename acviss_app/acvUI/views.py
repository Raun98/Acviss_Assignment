from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import NumberForm, SearchForm
from .services import populateDB, register_batch_update, load_user_table
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from datetime import datetime
import mysql.connector
import requests


class ApiView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):

        return Response(content)

def search(request):
    dbconnect = mysql.connector.connect(host='localhost', port='3306', user='raun', passwd='root', database='avcissdb')
    cursor = dbconnect.cursor()
    query = request.GET.get('search', '')
    cursor.execute('select * from codes')
    result = cursor.fetchall()
    dbconnect.commit()
    results = []
    #print(result)
    #print(query)
    if query:
        for batchname, code in result:
            #print(code)
            if query in code:
                results.append((batchname,code))
    #print(results)
    return render(request, 'search.html', {'results': results})



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
            time = datetime.now()
            f_datetime = time.strftime('%Y-%m-%d %H:%M:%S')
            populateDB(number_of_codes, batch_name)
            register_batch_update(name, batch_name, number_of_codes, f_datetime)
            result = load_user_table(name)
            form = NumberForm()
            return redirect('/')
    return render(request, 'index.html', {'form': form, 'result': result})

def HomePage(request):
    name = request.user
    result = None
    if name.is_authenticated:
        name = str(name)
        result = load_user_table(name)
    return render(request, 'index.html', {'result': result})