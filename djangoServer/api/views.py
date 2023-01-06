from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils import getTransactions, createTransactions

@api_view(['GET',])
def getname(request):
    return Response({"return":"Hi Nihad"})
# Create your views here.

@api_view(['GET','POST'])
def Transactions(request):
    if request.method == 'GET':
        return getTransactions(request)

    if request.method == 'POST':
        return createTransactions(request)
