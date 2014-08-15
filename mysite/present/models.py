from django.contrib.auth.models import User
from django.db import models

class Address(models.Model):
    address = models.TextField('address', max_length=255, unique=True)

    class Meta:
        verbose_name = 'address'
        verbose_name_plural = 'addresses'
        ordering = ['address']

class Place(models.Model):
    description = models.TextField('description', max_length=255)
    address = models.ForeignKey(Address, verbose_name='address',
        related_name='place address')

    class Meta:
        verbose_name = 'place'
        verbose_name_plural = 'places'
        ordering = ['address', 'description']

class Lesson(models.Model):
    time = models.DateTimeField('time')
    place = models.ForeignKey(Place, verbose_name='place',
            related_name='lessons')

    class Meta:
        verbose_name = 'lesson'
        verbose_name_plural = 'lessons'
        ordering = ['time', 'place']

class LessonAttendance(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name='lesson',
            related_name='attendances')
    
    user = models.ForeignKey(User, verbose_name='user',
            related_name='attendances')

    class Meta:
        verbose_name = 'attendance'
        verbose_name_plural = 'attendances'
        ordering = ['lesson', 'user']

class UserDetails(models.Model):
    user = models.ForeignKey(User, verbose_name='user',
            unique=True)
    first_name = models.CharField('first name', max_length=40)
    last_name = models.CharField('last name', max_length=40)
    address = models.ForeignKey(Address, verbose_name='address',
        related_name='user address')

    class Meta:
        verbose_name = 'user details'
        verbose_name_plural = 'users details'
        ordering = ['last_name', 'first_name', 'address', 'user']

# TODO meta
# TODO methods
# TODO manager


# TODO later: documents, subscriptions, criteria, more user details

