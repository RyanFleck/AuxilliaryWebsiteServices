from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from services.viewcounts.serializers import PageViewSerializer


class PageTrackingView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = PageViewSerializer

    def post(self, request, format=None):
        """Adds one to the page view tally, and returns the views."""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        return Response({"status": "POST OK", "data": data})


page_tracking_view = PageTrackingView.as_view()
