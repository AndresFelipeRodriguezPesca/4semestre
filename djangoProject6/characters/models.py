from django.db import models

class City(models.Model):
    name=models.CharField(max_length=100)
    lat=models.FloatField( )
    lon=models.FloatField()

    class Meta:
        db_table="cities"

class Universe(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    foundation= models.DateTimeField()

    class Meta:
        db_table="universes"


class Power(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table="powers"

class Character(models.Model):

    universe=models.ForeignKey(Universe, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    path = models.FileField(upload_to="")
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "characters"


class PowerCharacter(models.Model):
    power=models.ForeignKey(Power, on_delete=models.CASCADE)
    character=models.ForeignKey(Character, on_delete=models.CASCADE)
    level=models.FloatField()


    class Meta:
        db_table="powers_characters"