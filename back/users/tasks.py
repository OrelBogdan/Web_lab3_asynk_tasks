import logging
import os
from channels.layers import get_channel_layer

from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from celery import shared_task, Task

channel_layer = get_channel_layer()

class CallbackTask(Task):
    def on_success(self, retval, task_id, args, kwargs):
        print(f"Task {task_id} is {retval}")

logging.basicConfig(level=logging.INFO)

@shared_task(name="send_welcome_email", base=CallbackTask)
def send_welcome_email(user_id):
    print("send_welcome_email")
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=user_id)
        email: str = f"{user.email!s}"
        print(email)

        send_mail(
            'Registration',
            'Account created',
            os.environ["EMAIL_HOST_USER"],
            [user.email],
            fail_silently=False,
        )
    except UserModel.DoesNotExist:
        logging.warning("Tried to send welcome email to non-existing user '%s'" % user_id)
    except Exception as e:
        logging.warning("Failed to send welcome email due to: %s" % e)


@shared_task
def send_startup_email():
    print("send_startup_email")
    logging.warning("send_startup_email")
    try:
        send_mail(
            'Registration',
            'Account created, thanks for registration!',
            os.environ["EMAIL_HOST_USER"],
            [os.environ["EMAIL_HOST_USER"]],
            fail_silently=False,
        )
    except Exception as e:
        logging.warning("Failed to send welcome email due to: %s" % e)
