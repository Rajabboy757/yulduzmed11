from django.apps import AppConfig


class NewclientsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'newclients'

    def ready(self):
        import newclients.signals
