from rest_framework.fields import CharField
from rest_framework.serializers import Serializer


class PageViewSerializer(Serializer):
    page_url = CharField(required=True, allow_blank=False, max_length=200)
    user_id = CharField(required=True, allow_blank=False, max_length=40)
