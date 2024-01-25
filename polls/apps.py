"""
    Module name :- apps
"""


from django.apps import AppConfig


class PollsConfig(AppConfig):
    """
    App Configuration for polls.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "polls"
