# from django.shortcuts import render
# from rest_framework import permissions
# from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet

from uslugi.models import Uslugi

from uslugi.serializers import UslugiSerializer


# Create your views here.
class UslugiViewSet(ModelViewSet):
    queryset = Uslugi.objects.all()
    serializer_class = UslugiSerializer

    def perform_create(self, serializer):
        data = self.request.data
        Uslugi.objects.create(
            owner=self.request.user,
            title=data['title']
        )




