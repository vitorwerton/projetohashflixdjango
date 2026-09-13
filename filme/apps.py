from django.apps import AppConfig
from django.db.models.signals import post_migrate


class FilmeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'filme'

    def ready(self):
        post_migrate.connect(
            criar_usuario_admin,
            sender=self
        )


def criar_usuario_admin(sender, **kwargs):
    from .models import Usuario
    import os

    email = os.getenv('EMAIL_ADMIN')
    senha = os.getenv('SENHA_ADMIN')

    if not email or not senha:
        return

    if not Usuario.objects.filter(email=email).exists():
        Usuario.objects.create_superuser(
            username="admin",
            email=email,
            password=senha,
            is_active=True,
            is_staff=True
        )