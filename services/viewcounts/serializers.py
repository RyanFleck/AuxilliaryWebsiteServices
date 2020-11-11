from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer, Serializer

from services.viewcounts.models import PageViewsModel


class PageViewSerializer(Serializer):
    page_url = CharField(required=True, allow_blank=False, max_length=200)
    user_id = CharField(required=True, allow_blank=True, max_length=40)


class PageViewsModelSerializer(ModelSerializer):
    class Meta:
        model = PageViewsModel
        fields = "__all__"
        read_only_fields = ["id"]
