from __future__ import unicode_literals

from django.db import models

class Question(models.Model):

    question = models.CharField(max_length=1000)
    choice_options = models.CharField(max_length=1000,help_text=("Coma separated string of all possible variants"))
    correct_answers = models.CharField(max_length=1000,help_text=("Coma separated string of all correct answers"))
    score = models.IntegerField()

    def __str__(self):
        return "Question with score " + str(self.score)



