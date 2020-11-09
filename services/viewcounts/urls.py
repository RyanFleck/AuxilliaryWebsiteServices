from django.urls import path

from services.viewcounts.views import page_tracking_view

app_name = "viewcounts"
urlpatterns = [path("page-tracker/", page_tracking_view, name="page-tracker")]
