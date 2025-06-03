from pprint import pprint

from django.db import connection

from core.models import Restaurant, Rating, Sale


def run():

    # Without N+1 optimization
    # ========================

    # Get all the ratings associated with each restaurant
    restaurants = Restaurant.objects.all() 
    for restaurant in restaurants:
        for rating in restaurant.ratings_for_restaurant.all(): 
            print(restaurant.name, rating.rating)
    pprint(connection.queries)  # N + 1 queries


    # With N+1 optimization
    # =====================

    # Get all ratings associated with each restaurant
    restaurants = Restaurant.objects.prefetch_related('ratings_for_restaurant')
    for restaurant in restaurants:
        for rating in restaurant.ratings_for_restaurant.all(): 
            print(restaurant.name, rating.rating)
    pprint(connection.queries)  # No N + 1 queries, just 2 queries

    # # Get all ratings and sales associated with each restaurant
    restaurants = Restaurant.objects.prefetch_related(
        'ratings_for_restaurant',
        'sales'
    )
    for restaurant in restaurants:
        print(restaurant.name)
        for rating in restaurant.ratings_for_restaurant.all():
            print(rating.rating)
        for sale in restaurant.sales.all():
            print(sale.income)
    pprint(connection.queries)  # only 3 queries

    # Get all the ratings
    ratings = Rating.objects.select_related('restaurant')
    for rating in ratings:
        print(rating.restaurant.name, rating.rating)
    pprint(connection.queries)  # just a single join query

    # Get all the sales
    sales = Sale.objects.select_related('restaurant')
    for sale in sales:
        print(sale.restaurant.name, sale.income)
    pprint(connection.queries) 