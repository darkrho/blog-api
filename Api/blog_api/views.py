from django.shortcuts import render
from .models import Topic, Entry
from .serializers import TopicSerializer, EntrySerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class TopicViewSet(ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class= TopicSerializer


class EntryViewSet(ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class= EntrySerializer