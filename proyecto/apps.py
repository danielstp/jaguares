from django.apps import AppConfig


class ProyectoAppConfig(AppConfig):

    name = "proyecto"
    verbose_name = "Sistema para la gestión de Proyectos Agiles"

    def ready(self):
        try:
            import users.signals  # noqa F401
        except ImportError:
            pass
