from rest_framework.response import Response
from .models import Transaction
from rest_framework.parsers import JSONParser 
from .serializers import TransactionSerializer
def getTransactions(request):
    transactions = Transaction.objects.all()
    transactionSerializer = TransactionSerializer(transactions,many = True) 
    return Response(transactionSerializer.data)


def createTransactions(request):
    Trans_data = JSONParser().parse(request)
    transactionSerializer = TransactionSerializer(data = Trans_data)
    if transactionSerializer.is_valid():
        transactionSerializer.save()
        return Response(transactionSerializer.data)