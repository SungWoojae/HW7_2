from django.urls import path, include
from .views import *

urlpatterns= [
    path('<str:id>',detail,name="detail"),
    path('new/',new,name='new'),
    path('create/',create,name="create"),
    path('delete/<str:id>',delete,name='delete'),
    path('update/<str:id>',edit,name='update'),
]
