from django.contrib import admin
from .models import Chai, ChaiStore, ChaiReview


# Inline reviews in Chai admin
class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extra = 1  # Optional: default 1 is enough
    readonly_fields = ("posted_at",)  # review time should not be editable


@admin.register(Chai)
class ChaiAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "size", "price", "is_available", "created_at")
    list_filter = ("type", "size", "is_available")  # filter sidebar
    search_fields = ("name", "description")  # search bar
    inlines = [ChaiReviewInline]


@admin.register(ChaiStore)
class ChaiStoreAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "created_at")
    search_fields = ("name", "location")
    filter_horizontal = ("chai_varieties",)  # better UI for ManyToMany


@admin.register(ChaiReview)
class ChaiReviewAdmin(admin.ModelAdmin):
    list_display = ("chai", "user", "rating", "posted_at")
    list_filter = ("rating", "posted_at", "chai__type")  # filter by chai type
    search_fields = ("user__username", "chai__name", "comment")
    readonly_fields = ("posted_at",)
