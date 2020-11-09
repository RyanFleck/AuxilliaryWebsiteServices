from django.conf.urls import url

from services.swagger.views import swagger_view

app_name = "swagger"
urlpatterns = [
    url(
        r"^swagger/$",
        swagger_view.with_ui("swagger", cache_timeout=0),
        name="swagger-docs",
    )
]
