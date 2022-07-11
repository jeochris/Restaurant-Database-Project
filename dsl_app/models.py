# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_details = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'category'

class Menu(models.Model):
    menu_name = models.CharField(max_length=50)
    price = models.IntegerField(blank=True, null=True)
    restaurant = models.ForeignKey('Restaurant', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'menu'


class Restaurant(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    restaurant_name = models.CharField(unique=True, max_length=20)
    category = models.ForeignKey(Category, models.DO_NOTHING)
    adrs = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'restaurant'


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    rating = models.IntegerField()
    comment = models.CharField(max_length=1000, blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    restaurant = models.ForeignKey(Restaurant, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'review'


class ReviewDetails(models.Model):
    tag = models.ForeignKey('Tag', models.DO_NOTHING)
    review = models.ForeignKey(Review, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'review_details'


class Tag(models.Model):
    tag_id = models.IntegerField(primary_key=True)
    tag_details = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tag'


# class User(models.Model):
#     user_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=20)
#     login_id = models.CharField(unique=True, max_length=20)
#     login_pw = models.CharField(max_length=10)
#     join_date = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'user'