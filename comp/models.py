from django.db import models

class ComputerModel(models.Model):
    class Meta:
        db_table = 'computers'
        verbose_name = 'computer'
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    ram = models.IntegerField()
    processor = models.FloatField()
    monitor = models.FloatField()

    def __str__(self):
        return self.brand

