from django.contrib import admin
from .models import Listing, Booking, Review
from django_celery_beat.models import PeriodicTask, IntervalSchedule

# Register your models here.
admin.site.register(Listing)
admin.site.register(Booking)
admin.site.register(Review)

# Register Celery models
# admin.site.register(PeriodicTask)
# admin.site.register(IntervalSchedule)
