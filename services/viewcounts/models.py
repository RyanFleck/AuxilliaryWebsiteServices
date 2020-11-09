import uuid

from django.db.models import CharField, IntegerField, UUIDField
from django.db.models.base import Model


class PageViewsModel(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    path = CharField(unique=True, blank=False, max_length=200)
    views = IntegerField(default=1)
