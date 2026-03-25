from django.urls import path

from .views import (
    DealActivityListCreateView,
    DealListCreateView,
    DealRetrieveUpdateView,
)

urlpatterns = [
    path("deals/", DealListCreateView.as_view(), name="deal-list-create"),
    path("deals/<int:pk>/", DealRetrieveUpdateView.as_view(), name="deal-detail"),
    path(
        "deals/<int:deal_id>/activities/",
        DealActivityListCreateView.as_view(),
        name="deal-activities",
    ),
]
