import csv
import io, csv, pandas as pd
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings
from rest_framework_csv import renderers as r
from rest_framework.decorators import action
from rest_framework_csv.parsers import CSVParser
from rest_framework_csv.renderers import CSVRenderer
from rest_framework import generics

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.db import connection
from django.shortcuts import render

from .serializers import (
    ClientsSerializers, UserSerializers, CustomTokenObtainPairSerializer, CustomUserSerializer, FileUploadSerializer
    )

from .models import Clients

class ClientsViewSet(viewsets.ModelViewSet):
    serializer_class = ClientsSerializers
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, pk=None):
        if pk is None:
            #query = Clients.objects.raw()
            return self.get_serializer().Meta.model.objects.all()
        return self.get_serializer().Meta.model.objects.filter(id=pk).first()

    def list(self, request):
        clients_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(clients_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        # send information to serializer
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Cliente creado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            # send information to serializer referencing the instance
            clients_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if clients_serializer.is_valid():
                clients_serializer.save()
                return Response(clients_serializer.data, status=status.HTTP_200_OK)
            return Response(clients_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request,pk=None):
        clients = self.get_queryset().filter(id=pk)
        print(clients)# get instance
        if clients:
            clients.delete()
            return Response({'message':'Cliente eliminado correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error':'No existe un Cliente con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializers

    def get_queryset(self, pk=None):
        if pk is None:
            #query = Clients.objects.raw()
            return self.get_serializer().Meta.model.objects.all()
        return self.get_serializer().Meta.model.objects.filter(id=pk).first()

    def create(self, request):
        # send information to serializer
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Usuario creado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email', '')
        password = request.data.get('password', '')
        user = authenticate(
            email=email,
            password=password
        )

        if user:
            login_serializer = self.serializer_class(data = request.data)
            if login_serializer.is_valid():
                user_serializer = CustomUserSerializer(user)
                return Response({
                    'token': login_serializer.validated_data.get('access'),
                    'refresh-token': login_serializer.validated_data.get('refresh'),
                    'user': user_serializer.data,
                    'message': 'inicio de sesion exitoso'
                }, status=status.HTTP_200_OK)
            return Response({
                'error':'Contraseña o nomobre de usuario incorrectos'
                }, status=status.HTTP_400_BAD_REQUEST)
        return Response({
                'error':'Contraseña o nomobre de usuario incorrectos'
                }, status=status.HTTP_400_BAD_REQUEST)


class Logout(GenericAPIView):
    def post(self, request, *args, **kwargs):
        user = Clients.objects.filter(id=request.data.get('user', ''))
        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({'message': 'Sesión cerrada correctamente'}, status=status.HTTP_200_OK)
        return Response({
                'error':'no existe este usuario'
                }, status=status.HTTP_400_BAD_REQUEST)


def export_csv(request):

    with connection.cursor() as cursor:
        cursor.execute("select documento, (first_name ||' '|| last_name), count(client_id) from clients_clients, bills where  clients_clients.id = bills.client_id group by documento")
        rawData = cursor.fetchall()
        query_set = []
        for i in rawData:
            query_set.append(i)
        print(query_set)

    response = HttpResponse(content_type = 'text/csv')
    response ['Content-Disposition'] = 'atachment; filename="clients_and_bills.csv"'

    writer = csv.writer(response)
    writer.writerow(query_set)

    return response

class UploadFileView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            file = serializer.validated_data['file']
            reader = pd.read_csv(file)
            for _, row in reader.iterrows():
                new_file = Clients(
                                password= row.password,
                                email= row.email,
                                first_name= row.first_name,
                                last_name= row.last_name,
                                documento= row.documento
                                )
                var = new_file.password
                new_file.set_password(var)
                new_file.save()
            return Response({'message':'Clientes insertados correctamente!'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)