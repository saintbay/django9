from django.shortcuts import render

def home(request):
    return render(request, 'moon/home.html')

def create(request):
    return render(request, 'moon/create.html')

def update(request):
    return render(request, 'moon/update.html')

def search(request):
    return render(request, 'moon/search.html')

def delete(request):
    return render(request, 'moon/delete.html')