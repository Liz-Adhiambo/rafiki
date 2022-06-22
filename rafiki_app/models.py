from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    
    is_employer = models.BooleanField('Is customer', default=False)
    is_employee = models.BooleanField('Is employee', default=False)


class Category(models.Model):
    name = models.CharField(max_length =50)


    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def update_category(self, update):
        self.name = update
        self.save()

    @classmethod
    def get_category_id(cls, id):
        category = Category.objects.get(pk = id)
        return category

    def __str__(self):
        return self.name


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    profile_picture = models.ImageField(upload_to = 'uploads/' ,default='default.jpg')
    bio = models.TextField()
    date_joined=models.DateTimeField(default=datetime.now)
    address = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=50, blank=True)
    availability = models.BooleanField(null=True)
    profile_category = models.ForeignKey('Category',null=True, blank=True, on_delete=models.CASCADE)

    def save_profile(self):
        self.save()

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_profile(cls, id ,user, bio , profile_category):
        update = cls.objects.filter(id = id).update(user = user, bio = bio, profile_category =profile_category)
        # return update

    @classmethod
    def get_all_profiles(cls):
        profiles = cls.objects.all()
        return profiles

    @classmethod
    def get_profile_by_id(cls,id):
        profile = cls.objects.filter(id= id).all()
        return profile

    

    @classmethod
    def filter_by_category(cls, profile_category):
        profile_category = cls.objects.filter(profile_category__id=profile_category)
        return profile_category

    def __str__(self):
        return self.user.username

    
