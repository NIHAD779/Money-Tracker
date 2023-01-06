from django.urls import path
from . import views

urlpatterns = [
    path('getname/',views.getname),
    path('Transactions/',views.Transactions),
]