import uuid

from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from services.viewcounts.models import PageViewsModel
from services.viewcounts.serializers import PageViewSerializer, PageViewsModelSerializer
from services.viewcounts.utils import get_page_views


class PageViewsViewSet(ReadOnlyModelViewSet):
    """Generic CRUD endpoints for BellboyDevice."""

    serializer_class = PageViewsModelSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = PageViewsModel.objects.all()


class PageViewsAdminViewSet(ModelViewSet):
    """Generic CRUD endpoints for BellboyDevice."""

    serializer_class = PageViewsModelSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser]
    queryset = PageViewsModel.objects.all()


class PageTrackingView(GenericAPIView):
    throttle_classes = [AnonRateThrottle]
    permission_classes = [AllowAny]
    serializer_class = PageViewSerializer

    def post(self, request, format=None):
        """Adds one to the page view tally, and returns the views."""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        # Begin creating returned data object.
        returned_data = {"status": "OK, Thanks for reading! :)"}
        # If no ID, add a new one to the object:
        if not data["user_id"]:
            # Temporarily generate a random user id.
            returned_data.update({"new_id": str(uuid.uuid4())})

        views = get_page_views(data["page_url"])
        returned_data.update({"page_views": views})

        return Response(returned_data)


page_tracking_view = PageTrackingView.as_view()
