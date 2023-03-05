from django.db import models

# Create your models here.
class walletDB(models.Model):
    card_holder = models.CharField(max_length=25)
    card_no = models.CharField(max_length=19)
    purse_amt = models.IntegerField()

    def __str__(self):
        return f"{self.card_no, self.purse_amt}"
