from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserInfoSerializer, EmailChangeSerializer, RegisterSerializer
from .services import edit_object, get_user


class RegisterAPIView(APIView):
    """"API View to register new user"""
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class UserInfoAPIView(APIView):
    """"API View to get user info"""
    def get(self, request):
        user = get_user(request)

        serializer = UserInfoSerializer(user)
        return Response(serializer.data)


class EditUserEmailAPIView(APIView):
    """"API View to change email"""
    def put(self, request):
        serializer = EmailChangeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = get_user(request)

        if user.email != serializer.validated_data['email']:
            edit_object(user, email=serializer.validated_data['email'])
            return Response({'email': serializer.validated_data['email']})

        return Response({'error': 'email is already used/bad request'}, status=status.HTTP_400_BAD_REQUEST)


class EditUserDataAPIView(generics.UpdateAPIView):
    """"API View to change user data"""
    queryset = User.objects.all()
    serializer_class = UserInfoSerializer

    def get_object(self) -> object:
        return get_user(self.request)
