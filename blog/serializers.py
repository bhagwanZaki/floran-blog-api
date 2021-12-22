from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Blog

class blogSerializers(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

        