from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30, default='Not Defined')
    description = models.CharField(max_length=1000)
    first_release_date = models.DateField(null=True)

    def __str__(self):
        return "Name: " + self.name + ", " + \
               "Description: " + self.description + ", " + \
               "First release date: " + self.first_release_date


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    name = models.CharField(null=False, max_length=30, default='Not Defined')
    dealer_id = models.IntegerField(default=0)
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    SEDAN, SUV, WAGON, TRUCK = 'Sedan', 'SUV', 'Wagon', 'Truck'
    TYPE_CHOICES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
        (TRUCK, 'Truck')
    ]
    car_type = models.CharField(
        null=False,
        max_length=20,
        choices=TYPE_CHOICES,
        default=SEDAN
    )
    year = models.DateField(null=True)
    WHITE, BLACK, RED, NAVY, GRAY = 'White', 'Black', 'Red', 'Navy', 'Gray'
    COLOR_CHOICES = [
        (WHITE, 'White'),
        (BLACK, 'Black'),
        (RED, 'Red'),
        (NAVY, 'Navy'),
        (GRAY, 'Gray')
    ]
    car_color = models.CharField(
        null=False,
        max_length=20,
        choices=COLOR_CHOICES,
        default=WHITE
    )

    def __str__(self):
        return "Name: " + self.name + ", " + \
               "Dealer: " + self.dealer_id + ", " + \
               "Type: " + self.car_type + ", " +\
               "Year: " + self.year + ", " + \
               "Color: " + self.car_color

# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer(models.Model):
    name = models.CharField(max_length=200, default="name")
    address = models.CharField(max_length=200, default="address")
    description = models.CharField(max_length=1000, default="description")
    contact_info = models.CharField(max_length=500, default="contact")
    total_reviews = models.IntegerField(default=0)

# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview(models.Model):
    title = models.CharField(max_length=200, default="title")
    content = models.CharField(max_length=1000, default="content")