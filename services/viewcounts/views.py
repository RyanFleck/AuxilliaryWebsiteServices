import uuid

from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from services.viewcounts.serializers import PageViewSerializer
from services.viewcounts.utils import get_page_views


class PageTrackingView(GenericAPIView):
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
