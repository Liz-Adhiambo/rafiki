from django.apps import AppConfig


class RafikiAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rafiki_app'

    def ready(self):
        import rafiki_app.signals