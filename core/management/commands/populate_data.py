import random
from datetime import date, timedelta

from django.utils import timezone
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from core.models import Restaurant, Rating, Sale


def create_users(n=5):
    for i in range(n):
        User.objects.get_or_create(
            username=f"user{i+1}", defaults={"email": f"user{i+1}@gmail.com"}
        )


def create_restaurants():

    restaurants = [
        {
            "name": "Pizzeria 1",
            "date_opened": timezone.now() - timezone.timedelta(days=20),
            "restaurant_type": Restaurant.RestaurantTypeChoices.ITALIAN,
            "latitude": 55.869829854,
            "longitude": -4.28583219,
        },
        {
            "name": "Pizzeria 2",
            "date_opened": timezone.now() - timezone.timedelta(days=27),
            "restaurant_type": Restaurant.RestaurantTypeChoices.ITALIAN,
            "latitude": 55.862,
            "longitude": -4.247,
        },
        {
            "name": "Golden Dragon",
            "date_opened": timezone.now() - timezone.timedelta(days=15),
            "restaurant_type": Restaurant.RestaurantTypeChoices.CHINESE,
            "latitude": 55.953251,
            "longitude": -3.188267,
            "website": "https://www.goldendragon.com",
        },
        {
            "name": "Bombay Bustle",
            "date_opened": timezone.now() - timezone.timedelta(days=44),
            "restaurant_type": Restaurant.RestaurantTypeChoices.INDIAN,
            "latitude": 51.509865,
            "longitude": -0.118092,
            "website": "https://www.bombaybustle.com",
        },
        {
            "name": "McDonalds",
            "date_opened": timezone.now() - timezone.timedelta(days=51),
            "restaurant_type": Restaurant.RestaurantTypeChoices.FAST_FOOD,
            "latitude": 53.483959,
            "longitude": -2.244644,
            "website": "https://www.mcdonalds.com",
        },
        {
            "name": "Taco Bell",
            "date_opened": timezone.now() - timezone.timedelta(days=12),
            "restaurant_type": Restaurant.RestaurantTypeChoices.FAST_FOOD,
            "latitude": 53.413959,
            "longitude": -2.254644,
            "website": "https://www.tacobell.com",
        },
        {
            "name": "Chinese 2",
            "date_opened": timezone.now() - timezone.timedelta(days=31),
            "restaurant_type": Restaurant.RestaurantTypeChoices.CHINESE,
            "latitude": 53.400002,
            "longitude": -2.983333,
        },
        {
            "name": "Chinese 3",
            "date_opened": timezone.now() - timezone.timedelta(days=71),
            "restaurant_type": Restaurant.RestaurantTypeChoices.CHINESE,
            "latitude": 55.070859,
            "longitude": -3.60512,
        },
        {
            "name": "Indian 2",
            "date_opened": timezone.now() - timezone.timedelta(days=46),
            "restaurant_type": Restaurant.RestaurantTypeChoices.INDIAN,
            "latitude": 53.350140,
            "longitude": -6.266155,
        },
        {
            "name": "Mexican 1",
            "date_opened": timezone.now() - timezone.timedelta(days=52),
            "restaurant_type": Restaurant.RestaurantTypeChoices.MEXICAN,
            "latitude": 51.481583,
            "longitude": -3.179090,
        },
        {
            "name": "Mexican 2",
            "date_opened": timezone.now() - timezone.timedelta(days=50),
            "restaurant_type": Restaurant.RestaurantTypeChoices.MEXICAN,
            "latitude": 55.847258,
            "longitude": -4.440114,
        },
        {
            "name": "Pizzeria 3",
            "date_opened": timezone.now() - timezone.timedelta(days=4),
            "restaurant_type": Restaurant.RestaurantTypeChoices.ITALIAN,
            "latitude": 54.966667,
            "longitude": -1.600000,
        },
        {
            "name": "Pizzeria 4",
            "date_opened": timezone.now() - timezone.timedelta(days=61),
            "restaurant_type": Restaurant.RestaurantTypeChoices.ITALIAN,
            "latitude": 48.856614,
            "longitude": 2.3522219,
        },
        {
            "name": "Italian 1",
            "date_opened": timezone.now() - timezone.timedelta(days=37),
            "restaurant_type": Restaurant.RestaurantTypeChoices.ITALIAN,
            "latitude": 41.902782,
            "longitude": 12.496366,
        },
    ]

    for r in restaurants:
        Restaurant.objects.create(**r)


def create_ratings(n=10):
    users = list(User.objects.all())
    restaurants = list(Restaurant.objects.all())
    existing_pairs = set(Rating.objects.values_list("user_id", "restaurant_id"))

    attempts = 0
    created = 0
    while created < n and attempts < n * 5:
        user = random.choice(users)
        restaurant = random.choice(restaurants)
        if (user.id, restaurant.id) not in existing_pairs:
            Rating.objects.create(
                user=user, restaurant=restaurant, rating=random.randint(1, 5)
            )
            existing_pairs.add((user.id, restaurant.id))
            created += 1
        attempts += 1


def create_sales(n=15):
    restaurants = list(Restaurant.objects.all())
    for _ in range(n):
        Sale.objects.create(
            restaurant=random.choice(restaurants),
            income=round(random.uniform(1000, 10000), 2),
            on_date=date.today() - timedelta(days=random.randint(0, 365)),
        )


class Command(BaseCommand):
    help = "Populate data for User, Restaurant, Rating and Sale models in the database."

    def handle(self, *args, **kwargs):

        create_users()
        create_restaurants()
        create_ratings()
        create_sales()