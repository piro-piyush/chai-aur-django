import random

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils import timezone

from chai.models import (
    Chai,
    ChaiStore,
    ChaiReview,
    ChaiType,
    ChaiSize
)

User = get_user_model()


class Command(BaseCommand):
    help = "Seed initial Chai, Stores, Users and Reviews data"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("🌱 Seeding chai data..."))

        users = self.create_users()
        chais = self.create_chais()
        stores = self.create_stores(chais)
        self.create_reviews(chais, users)

        self.stdout.write(self.style.SUCCESS("✅ Seeding completed successfully!"))

    # ---------------- USERS ----------------
    def create_users(self):
        usernames = ["rahul", "neha", "amit", "pooja", "rohan"]
        users = []

        for username in usernames:
            user, created = User.objects.get_or_create(
                username=username,
                defaults={
                    "email": f"{username}@example.com"
                }
            )

            if created:
                user.set_password("test1234")
                user.save()

            users.append(user)

        self.stdout.write("👤 Users seeded")
        return users

    # ---------------- CHAIS ----------------
    def create_chais(self):
        chai_data = [
            ("Masala Chai", ChaiType.MASALA, ChaiSize.MEDIUM, 20.0),
            ("Ginger Chai", ChaiType.GINGER, ChaiSize.SMALL, 15.0),
            ("Elaichi Chai", ChaiType.ELAICHI, ChaiSize.MEDIUM, 18.0),
            ("Green Tea", ChaiType.GREEN, ChaiSize.LARGE, 25.0),
            ("Black Tea", ChaiType.BLACK, ChaiSize.SMALL, 12.0),
            ("Special Chai", ChaiType.SPECIAL, ChaiSize.LARGE, 30.0),
        ]

        chais = []

        for name, chai_type, size, price in chai_data:
            chai, _ = Chai.objects.get_or_create(
                name=name,
                size=size,
                defaults={
                    "type": chai_type,
                    "price": price,
                    "description": f"Delicious {name.lower()} made with love ☕",
                    "rating": round(random.uniform(3.5, 5.0), 1),
                }
            )
            chais.append(chai)

        self.stdout.write("☕ Chais seeded")
        return chais

    # ---------------- STORES ----------------
    def create_stores(self, chais):
        store_data = [
            ("Chai Pe Charcha", "Delhi"),
            ("Tapri Chai", "Mumbai"),
            ("IIT Chaiwala", "Kanpur"),
            ("Evening Adda", "Pune"),
        ]

        stores = []

        for name, location in store_data:
            store, _ = ChaiStore.objects.get_or_create(
                name=name,
                defaults={"location": location}
            )

            store.chai_varieties.set(
                random.sample(chais, k=random.randint(2, len(chais)))
            )

            stores.append(store)

        self.stdout.write("🏪 Stores seeded")
        return stores

    # ---------------- REVIEWS ----------------
    def create_reviews(self, chais, users):
        for chai in chais:
            for _ in range(random.randint(2, 5)):
                ChaiReview.objects.create(
                    chai=chai,
                    user=random.choice(users),
                    rating=random.randint(3, 5),
                    comment=random.choice([
                        "Amazing taste!",
                        "Perfect evening chai ☕",
                        "Too good!",
                        "Worth the price",
                        "Will order again!"
                    ]),
                    posted_at=timezone.now()
                )

        self.stdout.write("⭐ Reviews seeded")
