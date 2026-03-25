# from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Activity, Deal
from .serializers import (
    ActivityCreateSerializer,
    ActivitySerializer,
    DealSerializer,
)


@api_view(["GET"])
def health(request):
    return Response({"ok": True})


# Deals
class DealListCreateView(generics.ListCreateAPIView):
    queryset = Deal.objects.all().order_by("-created_at")
    serializer_class = DealSerializer


class DealRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer


# Activities
class DealActivityListCreateView(generics.ListCreateAPIView):
    serializer_class = ActivitySerializer

    def get_deal(self) -> Deal:
        return get_object_or_404(Deal, pk=self.kwargs["deal_id"])

    def get_queryset(self):
        deal = self.get_deal()
        return Activity.objects.filter(deal=deal).order_by("-date", "-created_at")

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ActivityCreateSerializer
        return ActivitySerializer

    def perform_create(self, serializer):
        deal = self.get_deal()
        serializer.save(deal=deal)
