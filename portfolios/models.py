from django.db import models


class Portfolio(models.Model):
    name = models.CharField(max_length=200, unique=True)
    content = models.TextField()

    def __str__(self) -> str:
        return self.name


class PortfolioImage(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="portfolio_images/")
