from django.db import models


class Deal(models.Model):
    class Status(models.TextChoices):
        NEW = "new", "新規"
        CONTACTED = "contacted", "連絡済み"
        PROPOSED = "proposed", "提案中"
        WON = "won", "獲得"
        LOST = "lost", "お断り"
        ON_HOLD = "on_hold", "保留"
        NEEDS_FOLLOW_UP = "needs_follow_up", "要フォロー"

    status = models.CharField(max_length=20, choices=Status.choices, default=Status.NEW)
    deal_name = models.CharField(max_length=255)
    client_name = models.CharField(max_length=255)
    next_follow_up_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.deal_name


class Activity(models.Model):
    class ActivityType(models.TextChoices):
        CALL = "call", "電話"
        EMAIL = "email", "メール"
        MEETING = "meeting", "ミーティング"

    activity_type = models.CharField(max_length=20, choices=ActivityType.choices)
    deal = models.ForeignKey(Deal, related_name="activities", on_delete=models.CASCADE)
    date = models.DateField()
    memo = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.get_activity_type_display()} (deal_id={self.deal_id})"
