from django.urls import path, re_path
from .views import home, create, update, search, delete

app_name = 'app'

urlpatterns = [
    re_path(r'^$', home, name='home'), 
    re_path(r'^create/$', create, name='create'),
    path('update/', update, name='update'),
    path('search/', search, name='search'),
    path('delete/', delete, name='delete')
]