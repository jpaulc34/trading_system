from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=225, blank=True)
    city = models.CharField(max_length=225, blank=True)
    avatar = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.user.username

class ProfileStatus(models.Model):
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="profile_status")
    status_content = models.CharField(max_length=510, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "profile_statuses"

    def __str__(self):
        return str(self.user_profile)+ " - "+ self.status_content

class Comment(models.Model):
    profile_status = models.ForeignKey(ProfileStatus, on_delete=models.CASCADE, related_name="comments")
    profile_commenter = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="profile_comments")
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment

class Stock(models.Model):
    name = models.CharField(max_length=70, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="profile_order")
    stock = models.DecimalField(max_digits=10, decimal_places=2)
    quantity =  models.SmallIntegerField(blank=False, null=False)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user_profile)
