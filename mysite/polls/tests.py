#stdlib imports
import time
import datetime

# 3rd party lib imports
import pytz

# django and local imports
from django.test import TestCase
from polls.models import Question, Choice

# Create your tests here.
class QCModelTest(TestCase):

    def test_saving_and_retrieving_questions(self):
        tz = pytz.timezone('America/Chicago')
        question = Question()
        question.question_text = 'Who is the most famous actress?'
        question.pub_date = datetime.datetime(2012, 3, 31, 11, 30, 5, 182371, tzinfo=tz)
        question.save()

        saved_questions = Question.objects.all()
        self.assertEqual(saved_questions.count(), 1)
        saved_question = saved_questions[0]
        self.assertEqual(saved_question.question_text, 'Who is the most famous actress?')
        self.assertEqual(saved_question.pub_date,
            datetime.datetime(2012, 3, 31, 11, 30, 5, 182371, tzinfo=tz))

        choice = Choice()
        choice.text = "1. Demi Moore 2. Julia Roberts"
        choice.votes = 1000
        choice.save()

        saved_choices = Choice.objects.all()
        self.assertEqual(saved_choices.count(), 1)
        saved_choice = saved_choices[0]
        self.assertEqual(saved_choice.text, "1. Demi Moore 2. Julia Roberts")
        self.assertEqual(saved_choice.votes, 1000)

