from rest_framework import serializers

from .models import Activity, Deal


class DealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal
        fields = [
            "id",
            "deal_name",
            "client_name",
            "status",
            "next_follow_up_at",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = [
            "id",
            "deal",
            "activity_type",
            "date",
            "memo",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class ActivityCreateSerializer(serializers.ModelSerializer):
    """/deals/{id}/activities の POST 用（dealはURLから決める）"""

    class Meta:
        model = Activity
        fields = ["date", "activity_type", "memo"]
