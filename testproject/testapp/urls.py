from django.urls import path
from .views import default, text_list

urlpatterns = [
    path('', default, name='default'),
    path('api/texts', text_list, name='text-list'),
]