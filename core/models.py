from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.db.models.functions import Lower


class Restaurant(models.Model):

    class RestaurantTypeChoices(models.TextChoices):
        INDIAN = "IN", "Indian"
        ITALIAN = "IT", "Italian"
        CHINESE = "CH", "Chinese"
        MEXICAN = "MX", "Mexican"
        GREEK = "GR", "Greek"
        FAST_FOOD = "FF", "Fast Food"
        OTHERS = "OT", "Others"

    name = models.CharField(max_length=64, unique=True)
    website = models.URLField(
        max_length=64,
        unique=True,
        null=True,
        blank=True
    )
    restaurant_type = models.CharField(
        max_length=2,
        choices=RestaurantTypeChoices.choices,
        default=RestaurantTypeChoices.OTHERS,
    )
    date_opened = models.DateField()
    latitude = models.FloatField(
        validators=[MinValueValidator(-90), MaxValueValidator(90)]
    )
    longitude = models.FloatField(
        validators=[MinValueValidator(-180), MaxValueValidator(180)]
    )

    class Meta:
        ordering = [Lower("name")]
        get_latest_by = ("date_opened", "id")

    def __str__(self):
        return self.name


class Rating(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="ratings_by_user"
    )
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name="ratings_for_restaurant"
    )
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "restaurant"],
                name="unique_user_restaurant_rating"
            )
        ]

    def __str__(self):
        return f"Rating for {self.restaurant.name}"


class Sale(models.Model):

    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.SET_NULL, null=True, related_name="sales"
    )
    income = models.DecimalField(max_digits=10, decimal_places=2)
    on_date = models.DateField()

    def __str__(self):
        return f"Sales [{self.restaurant.name}]"


class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Student(models.Model):
    name = models.CharField(max_length=64)
    course = models.ManyToManyField(
        Course,
        related_name='enrolled_by_students'
    )

    def __str__(self):
        return self.name
    
