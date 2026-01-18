from django.core.management.base import BaseCommand
from chai.models import Chai, ChaiType, ChaiSize
from decimal import Decimal
import random


class Command(BaseCommand):
    help = "Seed dummy chai data"

    def handle(self, *args, **kwargs):

        chai_data = [
            {
                "name": "Classic Masala Chai",
                "description": "Strong Indian masala chai with spices",
                "type": ChaiType.MASALA,
            },
            {
                "name": "Ginger Zing Chai",
                "description": "Spicy ginger infused chai",
                "type": ChaiType.GINGER,
            },
            {
                "name": "Elaichi Royal Chai",
                "description": "Premium cardamom flavored chai",
                "type": ChaiType.ELAICHI,
            },
            {
                "name": "Green Detox Tea",
                "description": "Healthy green tea for freshness",
                "type": ChaiType.GREEN,
            },
            {
                "name": "Midnight Black Tea",
                "description": "Strong black tea for late nights",
                "type": ChaiType.BLACK,
            },
        ]

        for chai in chai_data:
            Chai.objects.create(
                name=chai["name"],
                description=chai["description"],
                type=chai["type"],
                size=random.choice(ChaiSize.values),
                price=Decimal(random.choice(["15.00", "20.00", "25.00"])),
                rating=round(random.uniform(3.8, 5.0), 1),
                is_available=True,
            )

        self.stdout.write(self.style.SUCCESS("✅ Dummy chai data added successfully!"))
