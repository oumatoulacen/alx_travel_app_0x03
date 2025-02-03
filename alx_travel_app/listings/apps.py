from django.apps import AppConfig


class ListingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'alx_travel_app.listings'

    def ready(self):
        import alx_travel_app.listings.signals # register the signals when the app is ready