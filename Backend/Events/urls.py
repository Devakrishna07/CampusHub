from django.urls import path
from .views import PublicEventsView, EventCreateView, EventEditView

urlpatterns = [
    path("public/", PublicEventsView.as_view(), name="Public_events_view"),
    path("create/", EventCreateView.as_view(), name="EventCreateView"),
    path("edit/", EventEditView.as_view(), name="EventEditView"),
]

