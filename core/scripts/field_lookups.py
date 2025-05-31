from django.contrib.auth.models import User
from core.models import Restaurant, Rating, Sale


def run():

    # Field Lookups
    #==============

    # Get a restaurant named 'Spice Hub'
    spice_hub = Restaurant.objects.filter(name__iexact='spice hub')

    # Get all restaurants whose name begin with any of these chars ["abcd"]
    restaurants = Restaurant.objects.filter(name__lt='e')

    # Get all Indian Cuisine restaurants
    restaurants = Restaurant.objects.filter(
        restaurant_type=Restaurant.RestaurantTypeChoices.INDIAN,
    )
    
    italian = Restaurant.RestaurantTypeChoices.ITALIAN
    mexican = Restaurant.RestaurantTypeChoices.MEXICAN
    chinese = Restaurant.RestaurantTypeChoices.CHINESE
    cuisine_types = [italian, mexican, chinese]

    # Get all restaurants from cuisine types list
    restaurants = Restaurant.objects.filter(restaurant_type__in=cuisine_types)

    # Get all restaurants except italian and chinese cuisine
    restaurants = Restaurant.objects.exclude(
        restaurant_type=[italian, chinese]
    )

    # Get all chinese cuisine whose name begins with 'c'
    restaurants = Restaurant.objects.filter(
        restaurant_type=Restaurant.RestaurantTypeChoices.CHINESE,
        name__istartswith='c',
    )

    # Get all chinese cuisine whose name does not begin with 'c'
    restaurants = Restaurant.objects.filter(
        restaurant_type=Restaurant.RestaurantTypeChoices.CHINESE
    ).exclude(name__istartswith='c')

    # Get all restaurants whose name begins with 'C'
    restaurants = Restaurant.objects.filter(name__startswith='C')

    # Get all restaurants whose name ends with 'a'
    restaurants = Restaurant.objects.filter(name__endswith='a')

    # Get all restaurants which contain substring "zz"
    restaurants = Restaurant.objects.filter(name__icontains='zz')

    # Get all restaurants opened after 2020-01-01
    restaurants = Restaurant.objects.filter(date_opened__gt='2020-01-01')

    # Get all restaurants opened in the year 2025
    restaurants = Restaurant.objects.filter(date_opened__year=2025)

    # Get all restaurants which have a website
    restaurants = Restaurant.objects.filter(website__isnull=False)

    # Get all restaurants which do not have a website
    restaurants = Restaurant.objects.filter(website__isnull=True)

    # Get all ratings associated with a restaurant whose name begin with 'C'
    ratings = Rating.objects.filter(restaurant__name__startswith='C')
    
    # Get all restaurants whose ratings >= 4
    restaurants = Rating.objects.filter(rating__gte=4)

    # Get all sales income between 5000 and 10000
    sales = Sale.objects.filter(income__range=(5000,10000))

    # Check whether a user "randomname" exists or not
    user = User.objects.filter(username='randomname')
    if user.exists():
        print(user)

    # Get total number of restaurants
    total_restaurants = Restaurant.objects.count()

    # Get nth restaurant
    n = 6
    nth_restaurant = Restaurant.objects.all()[n-1]
