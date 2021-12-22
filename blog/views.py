import rest_framework
from .models import Blog
from rest_framework import viewsets, permissions
from .serializers import *


class blogAPI(viewsets.ModelViewSet):
    serializer_class = blogSerializers
    permissions_classes = [permissions.AllowAny]
    queryset= Blog.objects.all()