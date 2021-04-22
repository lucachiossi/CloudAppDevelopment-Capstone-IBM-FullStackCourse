from django.db import models
from django.utils.timezone import now


# Car Make model
class CarMake(models.Model):
    Name = models.CharField(
        null=False,
        max_length=20,
        )
    Description = models.CharField(
        null=False,
        max_length=20,
        )
    Slogan = models.CharField(
        null=False,
        max_length=20,
        )

    def __str__(self):
        return "CarMake: " + self.Name  + \
                " - Descritpion: " + self.Description + \
                "\nSlogan: " + self.Slogan


# Car Model model
class CarModel(models.Model):
    NOT_SPEC = ' '
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'WAGON'
    SPORT = 'Sport'
    CAR_TYPES = [
        (NOT_SPEC,'N/A'),
        (SEDAN,'Sedan'),
        (SUV,'SUV'),
        (WAGON,'WAGON'),
        (SPORT,'Sport')
        ]
    CarMake = models.ForeignKey(
        CarMake,
        on_delete=models.CASCADE
        )
    DealerId = models.IntegerField(
        default=-1
        )
    Name = models.CharField(
        null=False,
        max_length=20,
        )
    Type = models.CharField(
        max_length=7,
        choices=CAR_TYPES,
        default=NOT_SPEC
        )
    Year = models.DateField(
        null=False
        )

    def __str__(self):
        return "Car Model: " + self.Name + \
                ", Type: " + self.Type + \
                ", Year: " +self.Year + \
                ", DealerId: " + self.DealerId + \
                ", Car Make < " + self.CarMake + " >"


# CarDealer class
class CarDealer:
    def __init__(self, address, city, full_name, id_val, lat, long_val, short_name, st, zip_val):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id_val
        # Location lat
        self.lat = lat
        # Location long
        self.long = long_val
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip_val

        def __str__(self):
            return "Dealer name: " + self.full_name


# DealerReview class
# TODO:<HINT> Create a plain Python class `DealerReview` to hold review data
