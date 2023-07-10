from django.apps import AppConfig
# from django.db.models.signals import post_migrate
# from django.dispatch import receiver
# from .models import User

class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'
    # def ready(self):
    #     post_migrate.connect(create_default_object, sender=self)

# @receiver(post_migrate)
# def create_default_object(sender, **kwargs):
#     if sender.name == 'base':
#         User.objects.get_or_create(username = "Chatgpt",name="Chatgpt",bio="I am here to help in between your discussions")
