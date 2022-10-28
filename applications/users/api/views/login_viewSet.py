from datetime import  datetime
from django.contrib.auth import authenticate
from  django.contrib.sessions.models import Session

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from ...models import User
from ....users.api.serializers import CustomTokenObtainPairSerializer, UserSerializers

from rest_framework_simplejwt.views import TokenObtainPairView

class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self,request,*args,**kwargs):

        email = request.data.get('email','')
        password = request.data.get('password','')
        user = authenticate(
            email = email,
            password = password
        )
        if user:

            login_serializer =self.serializer_class(data = request.data)
            if login_serializer.is_valid():

                user_serializer = UserSerializers(user)
                return Response({
                    'token': login_serializer.validated_data.get('access'),
                    'refresh-token': login_serializer.validated_data.get('refresh'),
                    'user': user_serializer.data,
                    'message':'Inicio de Sesion Exitoso'
                },status=status.HTTP_200_OK)
            return Response({'Error':'Contraseña o nombre de usuario incorrectos'},
                             status=status.HTTP_400_BAD_REQUEST)
        return Response({'Error': 'Contraseña o nombre de usuario incorrectos'},
                        status=status.HTTP_400_BAD_REQUEST)


class Logout(GenericAPIView):

    def post(self,request,*args,**kwargs):
        user = User.objects.filter(id=request.data.get('user', 0 ))
        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({'message':'Sesion cerrada correctamente.'},status=status.HTTP_200_OK)
        return Response({'Error': 'No existe este usuario'},
                        status=status.HTTP_400_BAD_REQUEST)








