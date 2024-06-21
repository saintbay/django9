from django.shortcuts import render

def home(request):
    return render(request, 'app/home.html')

def create(request):
    return render(request, 'app/create.html')

def update(request):
    return render(request, 'app/update.html')

def search(request):
    return render(request, 'app/search.html')

def delete(request):
    return render(request, 'app/delete.html')