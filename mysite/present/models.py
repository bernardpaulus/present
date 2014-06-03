from django.contrib.auth.models import User
from django.db import models

class Address(models.Model):
    address = models.TextField('address', max_length=255, unique=True)

class Place(models.Model):
    description = models.TextField('description', max_length=255)
    address = models.ForeignKey(Address, verbose_name='address',
        related_name='place address')

class Lesson(models.Model):
    time = models.DateTimeField('time')
    place = models.ForeignKey(Place, verbose_name='place',
            related_name='lessons')

class LessonAttendance(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name='lesson',
            related_name='attendances')
    
    user = models.ForeignKey(User, verbose_name='user',
            related_name='attendances')


class UserDetails(models.Model):
    user = models.ForeignKey(User, verbose_name='user',
            unique=True)
    firstName = models.CharField('first name', max_length=40)
    lastName = models.CharField('last name', max_length=40)
    address = models.ForeignKey(Address, verbose_name='address',
        related_name='user address')

# TODO meta
# TODO methods
# TODO manager


# TODO later: documents, subscriptions, criteria, more user details

