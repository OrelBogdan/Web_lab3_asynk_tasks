from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        print(f"Sending test email...")
        from .tasks import send_startup_email
        send_startup_email()
        # send_startup_email.delay()
