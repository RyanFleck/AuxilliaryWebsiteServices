from django.urls import include, path
from rest_framework.routers import DefaultRouter

from services.viewcounts.views import (
    PageViewsAdminViewSet,
    PageViewsViewSet,
    page_tracking_view,
)

app_name = "viewcounts"

router = DefaultRouter()
router.register(r"pages", PageViewsViewSet, basename="page-views")
router.register(r"pages-admin", PageViewsAdminViewSet, basename="page-views-admin")

urlpatterns = [
    path("page-tracker/", page_tracking_view, name="page-tracker"),
    path("", include(router.urls)),
]
