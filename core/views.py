from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import viewsets

from core.models import Tovar, CustomUser
from core.serializer import TovarSerializer

import requests


# Tovarlar olish, yoki yangi Tovar qo'shish
# List    - GET        /tovarlar      <- Tovar[]
# Create  - POST       /tovarlar      <- Tovar

# Tovarni olish, o'zgartirish, va o'chirish
# Retrive - GET        /tovarlar/:id  <- Tovar
# Update  - PUT/PATCH  /tovarlar/:id
# Destroy - DELETE     /tovarlar/:id

# class TovarlarAPI(generics.ListCreateAPIView):
#     serializer_class = TovarSerializer
#     def get_queryset(self):
#         return Tovar.objects.filter(is_active=True, user_id=self.user.id)


# class TovarAPI(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = TovarSerializer
#     queryset = Tovar.objects.all()

from rest_framework import permissions, serializers

from rest_framework.exceptions import ErrorDetail, ValidationError
# from rest_framework.authtoken.models import Token

# from django.contrib.auth.models import User

# class TokenForUser(APIView):
#     http_method_names = ["post"]

#     def post(self, request, *args, **kwargs):
#         user = CustomUser.objects.get(id=1)
#         print("salom", user)
#         (token, created) = Token.objects.get_or_create(user=user)
#         print(token.key)
#         return Response({"token": token.key, "is_created": created})


# class TokenUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ["id"]

# class TokenSerializer(serializers.ModelSerializer):
#     user = TokenUserSerializer(read_only=True)
#     user_id = serializers.IntegerField(write_only=True)

#     def create(self, validated_data):
#         user = CustomUser.objects.get(pk=validated_data.get("user_id"))
#         validated_data['user'] = user
#         instance, _ = Token.objects.get_or_create(**validated_data)
#         return instance

#     class Meta:
#         model = Token
#         fields = ["key", "user", "user_id"]
#         read_only_fields = ["key"]


# class TokenForUser(generics.CreateAPIView):
#     serializer_class = TokenSerializer
#     queryset = Token.objects.all()


class TovarViewSet(viewsets.ModelViewSet):
    serializer_class = TovarSerializer
    queryset = Tovar.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    # parser_classes = []

    def perform_create(self, serializer: TovarSerializer):
        print("here", self.request.user.has_perm("core.with_discount"))
        if not self.request.user.has_perm("core.with_discount") and serializer.validated_data["discount"] > 0:
            raise ValidationError("you don't have a permission")
        serializer.save()

    def perform_update(self, serializer):
        print("here", self.request.user)
        serializer.save()
    

from rest_framework.permissions import IsAuthenticated

class WeatherAPI(APIView):
    http_method_names = ["get"]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        res = requests.get("https://jsonplaceholder.typicode.com/todos/1")
        print(res.json())
        return Response(["ok"])
