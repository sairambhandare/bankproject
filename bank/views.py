from django.shortcuts import render
from rest_framework import generics

from bank.models import Bank, Branch
from bank.serializers import BankSerializer, BranchSerializer


class BankListView(generics.ListAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class BranchDetailView(generics.RetrieveAPIView):
    queryset = Branch.objects.select_related('bank')
    serializer_class = BranchSerializer
    lookup_field = 'ifsc'
