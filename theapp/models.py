from django.db import models

# Create your models here.

class Shior(models.Model):
    title1 = models.CharField(max_length=25)
    title2 = models.CharField(max_length=25)
    description = models.CharField(max_length=80)
    
    def __str__(self):
        return f"{self.title1} - {self.title2}"
    

class Category_Name(models.Model):
    category_name_select = models.CharField(max_length=55)

    def __str__(self):
        return self.category_name_select

class Category(models.Model):
    img = models.ImageField(upload_to='images/category')
    category_name = models.ForeignKey(Category_Name, on_delete=models.CASCADE)

    def __str__(self):
        return self.category_name

    
class Category_home(models.Model):
    home_type = models.CharField(max_length=35)

    def __str__(self):
        return self.home_type


class Home(models.Model):
    img = models.ImageField(upload_to='images/home')
    home_type = models.ForeignKey(Category_home, on_delete=models.CASCADE)
    category_name = models.ForeignKey(Category_Name, on_delete=models.CASCADE)
    price = models.FloatField()
    company_name = models.CharField(max_length=40)
    address = models.CharField(max_length=35)
    maydoni = models.FloatField()
    uy_count = models.PositiveIntegerField()
    bathroom_count = models.PositiveIntegerField()

    def __str__(self):
        return self.company_name

class Team(models.Model):
    img = models.ImageField(upload_to='images/team')
    facebook_link = models.URLField(max_length=255)   
    instagram_link = models.URLField(max_length=255)
    telegram_link = models.URLField(max_length=255)
    full_name = models.CharField(max_length=40)
    profession = models.CharField(max_length=30)

    def __str__(self):
        return self.full_name


class Contact(models.Model):
    name1 = models.CharField(max_length=25)
    email = models.EmailField(max_length=45)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name1
