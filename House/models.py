from django.db import models

# Create your models here.

class House(models.Model):

    quarter_choices = (
        ('KIGOBE', "KIGOBE"),
        ('KININDO', "KININDO"),
        ('KINANIRA', "KINANIRA"),
        ('KIBENGA', "KIBENGA"),
        ('GASEKEBUYE', "GASEKEBUYE"),  
    )



    status_choices = (
        ('Occupe', "Occupe"),
        ('Nonoccupe', "Nonoccupe"),
    )

    type_choices = (
        ('Simple', 'Simple'),
        ('Etage', 'Etage'),
        ('Appartements', 'Appartements'),
        )

    maison_choices = (
        ('four', 'four'),
        ('three', 'three'),
        ('two', 'two'),
        ('one', 'one'),
        )

    but_choices = (
        ('location', 'location'),
        ('vente', 'vente'),
        )

    number = models.IntegerField()
    owner_name = models.CharField(max_length=200)
    quarter = models.CharField(max_length=100, choices=quarter_choices)
    status = models.CharField(max_length=50, choices=status_choices)
    but = models.CharField(max_length=30, choices=but_choices, null=True, blank=False)
    type_maison = models.CharField(max_length=30, choices=type_choices)
    room = models.CharField(max_length=30, choices=maison_choices, null=True)
    image = models.ImageField(blank=True)
    propsalon = models.BooleanField(default=False)
    propbalcon = models.BooleanField(default=False)
    propchambr = models.IntegerField(null=True)
    propsalemanger = models.BooleanField(default=False)
    propcuisine = models.BooleanField(default=False)
    propdouche = models.IntegerField(null=True)
    price = models.CharField(max_length=20)


    def __str__(self):
        return "{} ".format(self.number) + self.owner_name+ " => " +self.quarter


class HouseImage(models.Model):
    house = models.ForeignKey(House, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return "{}".format(self.house.number) + self.house.owner_name+ " => " +self.house.quarter


