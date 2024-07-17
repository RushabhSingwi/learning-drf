from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Author(User):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.get_full_name()


class Blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.ManyToManyField(Author)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        authors = ", ".join(author.name for author in self.author.all())
        return f"{self.title[:100]} - {authors}"
