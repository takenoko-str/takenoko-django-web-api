from django.shortcuts import render

# Create your views here.
from rest_framework import serializers, viewsets

from film import models


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Language
        fields = '__all__'


class FilmSerializer(serializers.ModelSerializer):
    language = LanguageSerializer()

    class Meta:
        model = models.Film
        fields = '__all__'


class FilmViewSet(viewsets.ModelViewSet):
    queryset = models.Film.objects.all()
    serializer_class = FilmSerializer
    filter_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = ('title', )

