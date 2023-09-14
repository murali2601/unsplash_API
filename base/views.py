from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
import requests

# Create your views here.
key = '-BteYnHKk8vtKb5JxYcuceO3OH95HnX4SMKdtxPJtv4'

def home(request):
    query = request.GET.get('query')
    
    if query:
        print(query)
        url = f'https://api.unsplash.com/search/photos/?query={query}&client_id={key}&per_page=30'
        response = requests.get(url)
        data = response.json()
        result = data['results']

        context = {
            'results' : result,
            'query' : query.capitalize()
           
        }
    else:
        url = f'https://api.unsplash.com/photos/?client_id={key}&per_page=30'
        response = requests.get(url)
        data = response.json()
        context = {
            'data' : data
        }
       

    return render(request,'base/home.html',context)

def view(request,id):
    url = f'https://api.unsplash.com/photos/{id}?client_id={key}'
    response = requests.get(url)
    data = response.json()

    url_static = f'https://api.unsplash.com/photos/{id}/statistics?client_id={key}'
    respond = requests.get(url_static)
    statics = respond.json()
  
    context = {
        'data' : data,
        'statics' : statics
    }
    return render(request,'base/view.html',context)


def search(request,category):
    
    url = f'https://api.unsplash.com/search/photos?query={category}&client_id={key}&per_page=40'
    response = requests.get(url)
    data = response.json()
    result = data['results']
    
    context = {
        'category' : category.capitalize(),
        'results' : result
    }
    return render(request,'base/search.html',context)
