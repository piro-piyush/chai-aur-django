from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


# ----------------------------
# Chai Model
# ----------------------------
class Chai(models.Model):

    # ----------------------------
    # Chai Types
    # ----------------------------
    class ChaiType(models.TextChoices):
        MASALA = "MASALA", "Masala Chai"
        GINGER = "GINGER", "Ginger Chai"
        ELAICHI = "ELAICHI", "Elaichi Chai"
        GREEN = "GREEN", "Green Tea"
        BLACK = "BLACK", "Black Tea"
        SPECIAL = "SPECIAL", "Special Chai"

    # ----------------------------
    # Chai Sizes
    # ----------------------------
    class ChaiSize(models.TextChoices):
        SMALL = "S", "Small"
        MEDIUM = "M", "Medium"
        LARGE = "L", "Large"

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    type = models.CharField(
        max_length=20,
        choices=ChaiType.choices,
        default=ChaiType.MASALA
    )
    size = models.CharField(
        max_length=1,
        choices=ChaiSize.choices,
        default=ChaiSize.MEDIUM
    )
    price = models.DecimalField(max_digits=6, decimal_places=1)
    image = models.ImageField(upload_to="chais/", blank=True, null=True)
    rating = models.FloatField(default=0.0)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.get_type_display()} - {self.get_size_display()})"


# ----------------------------
# Chai Store Model
# ----------------------------
class ChaiStore(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varieties = models.ManyToManyField(
        Chai,
        related_name="stores"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Chai Store"
        verbose_name_plural = "Chai Stores"
        ordering = ['name']

    def __str__(self):
        return self.name


# ----------------------------
# Chai Review Model
# ----------------------------
class ChaiReview(models.Model):
    chai = models.ForeignKey(
        Chai,
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField()
    posted_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-posted_at']
        unique_together = ('chai', 'user')  # optional: one review per user per chai

    def __str__(self):
        return f"{self.user.username} review for {self.chai.name}"
