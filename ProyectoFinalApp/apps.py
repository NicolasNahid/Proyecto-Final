from django.apps import AppConfig


class ProyectofinalappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ProyectoFinalApp'
    
    def ready(self):
        import ProyectoFinalApp.signals
    
    


