from django.shortcuts import render
from .models import User
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated , AllowAny
from .serializers import UserSerializer , LoginSerializer , CreateSerializer
from rest_framework.decorators import action


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,]

    serializer_class = UserSerializer
    queryset = User.objects.all()
    http_method_names = ['get','post']


    action_serializers = {
        'create': CreateSerializer,
        'login': LoginSerializer,
    }


    def get_serializer_class(self):
        return self.action_serializers.get(self.action, self.serializer_class)


    @action(methods=['post'], detail=False, permission_classes=(AllowAny,))
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data)