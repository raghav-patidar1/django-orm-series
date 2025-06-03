from django.shortcuts import render

from .models import Restaurant, Rating, Sale
# Create your views here.


def home_view(request):
      
    restaurants = Restaurant.objects.prefetch_related(
        'ratings_for_restaurant',
        'sales'
    )

    context = {
        'restaurants': restaurants,
    }
    return render(request, 'core/index.html', context)
