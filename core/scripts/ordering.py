from django.db.models.functions import Lower

from core.models import Restaurant


def run():

    # Get all restaurants according to default ordering (order by id)
    restaurants = Restaurant.objects.all()

    # Get all restaurants order by name in ascending order
    restaurants = Restaurant.objects.order_by("name")

    # Get all restaurants order by name in descending order
    restaurants = Restaurant.objects.order_by("-name")

    # Get all restaurants order by name (case-insensitive) in ascending order
    restaurants = Restaurant.objects.order_by(Lower("name"))

    # Get all restaurants order by name (case-insensitive) in descending order
    restaurants = Restaurant.objects.order_by(Lower("name")).reverse()

    # Get one random restaurant
    random_restaurant = Restaurant.objects.order_by("?")[1]
    # random_restaurant = Restaurant.objects.order_by('?').first()

    # Get 5 random restaurants
    random_restaurants = Restaurant.objects.order_by("?")[:5]

    # Get all restaurants from newest to oldest, if two or more
    # restaurants having the same date, then order by name
    restaurants = Restaurant.objects.order_by("-date_opened", "name")

    # Get the latest restaurant
    latest_restaurant = Restaurant.objects.latest("date_opened")
    # latest_restaurant = Restaurant.objects.order_by('-date_opened')[0]

    # Get the earliest restaurant
    earliest_restaurant = Restaurant.objects.earliest("date_opened")
    # earliest_restaurant = Restaurant.objects.order_by('date_opened')[0]

    # Get the oldest restaurant order by multiple fields
    oldest_restaurant = Restaurant.objects.earliest("date_opened", "id")
    # oldest_restaurant = Restaurant.objects.order_by('date_opened', 'id')[0]

    # Change the default ordering (i.e., ORDER BY 'id')
    # by adding 'ordering' in Restaurant's meta
    restaurants = Restaurant.objects.all()

    # Set the default positional argument for latest() and
    # earliest() by using get_latest_by in Restaurant's meta
    latest_restaurant = Restaurant.objects.latest()
    earliest_restaurant = Restaurant.objects.earliest()
