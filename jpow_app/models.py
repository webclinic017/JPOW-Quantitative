from django.db import models

class SPY(models.Model):
    Date = models.DateField(null = True)
    closePrice = models.DecimalField(decimal_places = 2, max_digits = 10)

    def __str__(self):
        return str(self.Date)

class Ratio(models.Model):
    Date = models.DateField(null = True)
    PositiveSentiment = models.IntegerField()

    def __str__(self):
        return str(self.Date)

class Insider(models.Model):
    Date = models.DateField(null=True)
    Ticker = models.CharField(max_length = 5)
    Senator = models.TextField()
    PurchaseType = models.TextField()
    Amount = models.TextField()

class Compensation(models.Model):
    Ticker = models.CharField(primary_key = True, max_length = 5)
    CeoSalary = models.IntegerField()
    YTDReturn = models.DecimalField(decimal_places = 2, max_digits = 10)

    def __str__(self):
        return str(self.Ticker)

class UnusualOption(models.Model):
    Ticker = models.CharField(max_length = 5)
    Type = models.CharField(max_length = 4)
    Strike = models.TextField()
    OpenInterest = models.IntegerField()
    Volume = models.IntegerField()
    ExpirationDate = models.DateField(null=True)
