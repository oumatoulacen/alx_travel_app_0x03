import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alx_travel_app.settings")

app = Celery("alx_travel_app") # Create a Celery instance

# - namespace='CELERY' means all celery-related config keys should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY") # Load configuration from Django settings

# Load task modules from all registered Django app configs.
app.autodiscover_tasks() # Auto-discover tasks from all applications listed in INSTALLED_APPS
