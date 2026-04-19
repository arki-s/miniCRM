# from django.shortcuts import render
from apps.api.crm import models
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
    serializer_class = DealSerializer

    def get_queryset(self):
        queryset = Deal.objects.all().order_by("-created_at")

        # status フィルタ
        status_list = self.request.query_params.get("status")
        if status_list:
            queryset = queryset.filter(status__in=status_list)

        # q フィルタ（部分一致）
        q = self.request.query_params.get("q")
        if q:
            queryset = queryset.filter(
                models.Q(deal_name__icontains=q) |
                models.Q(client_name__icontains=q)
            )

        return queryset


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
