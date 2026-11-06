from datetime import date
from decimal import Decimal
from django.core.management.base import BaseCommand
from shop.models import Brand, Category, Product

CATALOG = [
    ("Smartphones", "Apple", "iPhone 15", "A powerful smartphone with a vibrant display and advanced camera system.", "699.00", 12, "https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=900"),
    ("Smartphones", "Samsung", "Galaxy S24", "A modern Android smartphone for everyday work, photos and entertainment.", "749.00", 10, "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=900"),
    ("Laptops", "Apple", "MacBook Air 13", "A slim laptop designed for study, productivity and everyday creativity.", "2499.00", 6, "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=900"),
    ("Laptops", "Lenovo", "IdeaPad Slim 5", "A versatile laptop for university, office tasks and browsing.", "1599.00", 8, "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=900"),
    ("Headphones", "Sony", "Wireless Noise-Cancelling Headphones", "Comfortable over-ear headphones for music, calls and travel.", "499.00", 15, "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=900"),
    ("Headphones", "Apple", "Wireless Earbuds", "Compact wireless earbuds for listening on the go.", "329.00", 20, "https://images.unsplash.com/photo-1606220945770-b5b6c2c55bf1?w=900"),
    ("Cameras", "Canon", "EOS Mirrorless Camera", "A mirrorless camera for photography and video projects.", "1899.00", 4, "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=900"),
    ("Smartwatches", "Samsung", "Galaxy Watch", "A smartwatch for notifications, activity and everyday convenience.", "599.00", 9, "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=900"),
    ("Accessories", "Logitech", "Wireless Keyboard", "A clean, comfortable keyboard for a home or office setup.", "149.00", 18, "https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=900"),
    ("Accessories", "Logitech", "Wireless Mouse", "An ergonomic wireless mouse for daily computer use.", "89.00", 25, "https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=900"),
    ("Monitors", "ASUS", "27-inch Monitor", "A large monitor for productivity, learning and entertainment.", "899.00", 7, "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=900"),
    ("Accessories", "Samsung", "Portable SSD 1TB", "Portable storage for backing up files and carrying projects.", "279.00", 11, "https://images.unsplash.com/photo-1597872200969-2b65d56bd16b?w=900"),
]

class Command(BaseCommand):
    help = "Create demo electronics categories, brands and products."

    def handle(self, *args, **options):
        created_products = 0
        for category_name, brand_name, name, description, price, stock, image_url in CATALOG:
            category, _ = Category.objects.get_or_create(name=category_name)
            brand, _ = Brand.objects.get_or_create(name=brand_name)
            product, created = Product.objects.get_or_create(
                name=name,
                defaults={
                    "description": description,
                    "price": Decimal(price),
                    "image_url": image_url,
                    "category": category,
                    "brand": brand,
                    "release_date": date(2025, 1, 1),
                    "stock": stock,
                },
            )
            if created:
                created_products += 1
        self.stdout.write(self.style.SUCCESS(
            f"Electronics demo catalog ready. Added {created_products} new products."
        ))
