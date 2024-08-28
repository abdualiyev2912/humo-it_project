from django.db import models


class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class PortfolioImage(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="portfolio_images/")


class Developer(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    skills = models.CharField(max_length=255)
    experience = models.IntegerField(help_text="Years of experience")

    def __str__(self):
        return self.name


class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name}: {self.content[:50]}..."
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
    