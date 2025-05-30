from datetime import date

from django.db import connection
from django.contrib.auth.models import User

from ..models import Restaurant, Rating, Sale


def run():

    # 1. Create
    #===========


    # Create a restaurant name 'Pizzeria'
    pizzeria_restaurant = Restaurant.objects.create(
        name='Pizzeria', 
        website='https://www.pizzeria.com/',
        restaurant_type = Restaurant.RestaurantTypeChoices.MEXICAN,
        date_opened = date(2020,1,1),
        latitude=19.11,
        longitude=73,
    )

    # Create rating for Pizzeria Restaurant by first user
    first_user = User.objects.first()
    rating, created = Rating.objects.get_or_create(
        user=first_user,
        restaurant=pizzeria_restaurant,
        rating=4
    )

    # Create sale for Pizzeria Restaurant
    sale = Sale()
    sale.restaurant = pizzeria_restaurant
    sale.income = 24000
    sale.on_date = date(2020, 1, 25)
    sale.save()

    # Create a restaurant name 'La Nino Pizza'
    lanino_restaurant, created = Restaurant.objects.update_or_create(
        name='La Nino Pizza',
        website="https://laninopizza.com/",
        restaurant_type=Restaurant.RestaurantTypeChoices.ITALIAN,
        date_opened=date(2023, 12, 10),
        latitude=22.119,
        longitude=72.89
    )

    # Create admin user
    admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin123',
    )

    # Create a restaurant name 'Spice Hub'
    spice_hub_restaurant, created = Restaurant.objects.get_or_create(
        name='Spice Hub',
        website="https://spicehub.com/",
        restaurant_type=Restaurant.RestaurantTypeChoices.INDIAN,
        date_opened=date(2022, 9, 10),
        latitude=17.119,
        longitude=72.89
    )

    
    # Create rating for Spice Hub restaurant by admin user
    Rating.objects.create(
        user=admin_user,
        restaurant=spice_hub_restaurant,
        rating=4
    )
    

    # 2. Retrieve
    #============

    # Get all restaurants
    restaurants = Restaurant.objects.all()
    
    # Get restaurant name "Spice Hub"
    spice_hub_restaurant = Restaurant.objects.get(name__iexact='spice hub')

    # Get all ratings given by a particular user (id=3) to each restaurant
    ratings_by_user = User.objects.get(id=3).ratings_by_user.all()

    for r in ratings_by_user:
        print(f"{r.user.username} gave {r.rating} star rating to {r.restaurant.name}.")

    # Get all the sales for first restaurant
    first_restaurant_sales = Restaurant.objects.first().sales.all()

    
    # 3. Update
    #==========

    # Update the rating of last record created in Ratings model
    rating = Rating.objects.last()
    rating.rating = 5
    rating.save(update_fields=['rating'])

    # Update website for 'Spice Hub' Restaurant
    spice_hub_restaurant.website = 'https://www.spicehub.in/'
    spice_hub_restaurant.save()


    # 4. Delete
    #==========

    # Delete last sale record
    deleted_sale = Sale.objects.last().delete()

    # Delete user (id=2) and also the ratings given by him
    deleted_user = User.objects.filter(id=3).delete()


    # Reverse Relations
    #==================


    # From a Restaurant's (name='Pizzeria') instance, get all related ratings and sales.
    restaurant = Restaurant.objects.get(name__iexact='pizzeria')
    ratings = restaurant.ratings_for_restaurant.all()
    sales = restaurant.sales.all()

    # From an admin user instance, get all ratings they have made.
    ratings_by_admin = User.objects.get(username='admin').ratings_by_user.all()