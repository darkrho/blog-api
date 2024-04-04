from rest_framework.serializers import ModelSerializer
from .models import Topic, Entry

class TopicSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields = ("text",)


class EntrySerializer(ModelSerializer):
    class Meta:
        model = Entry
        fields = ("text",)