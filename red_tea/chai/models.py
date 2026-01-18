from django.db import models


class ChaiType(models.TextChoices):
    MASALA = "MASALA", "Masala Chai"
    GINGER = "GINGER", "Ginger Chai"
    ELAICHI = "ELAICHI", "Elaichi Chai"
    GREEN = "GREEN", "Green Tea"
    BLACK = "BLACK", "Black Tea"
    SPECIAL = "SPECIAL", "Special Chai"


class ChaiSize(models.TextChoices):
    SMALL = "S", "Small"
    MEDIUM = "M", "Medium"
    LARGE = "L", "Large"


class Chai(models.Model):

    name = models.CharField(
        max_length=100
    )

    description = models.TextField(
        blank=True
    )

    type = models.CharField(
        max_length=20,
        choices=ChaiType.choices,
        default=ChaiType.MASALA
    )

    size = models.CharField(
        max_length=1,                     # S / M / L
        choices=ChaiSize.choices,         # ✅ FIXED
        default=ChaiSize.MEDIUM
    )

    price = models.DecimalField(
        max_digits=6,                     # up to 9999.9
        decimal_places=1
    )

    image = models.ImageField(
        upload_to="chais/",
        blank=True,
        null=True
    )

    rating = models.FloatField(
        default=0.0
    )

    is_available = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"
