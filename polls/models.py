"""
    Module name :- models
"""


import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin


# Create your models here.
class Question(models.Model):
    """
    Data model for Question.
    """

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("Date Published")

    def __str__(self):
        """
        String representation for Question.
        """
        return self.question_text

    @admin.display(boolean=True, ordering="pub_date", description="Published recently?")
    def was_published_recently(self):
        """
        Method to check whether thw question is recent.
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    """
    Data model for Choice
    """

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """
        String representation for Choice.
        """
        return self.choice_text
