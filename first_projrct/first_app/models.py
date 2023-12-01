from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=500)
    deadline = models.DateField()

    def __str__(self) -> str:
        return self.title

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # firs_name = models.CharField(max_length=60)
    # phone_nambern = models.CharField(max_length=60)
    # email = models.CharField(max_length=60)
    # reg_data = models.DateField(auto_created=True)

    def __str__(self) -> str:
        return self.user
    


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    publication_date = models.DateField(auto_created=True)

    def __str__(self) -> str:
        return self.title






# class Task(models.Model):
#     sarlavha = models.CharField(max_length=255)
#     tavsif = models.TextField()
#     oxirgi_muddat = models.DateField()



