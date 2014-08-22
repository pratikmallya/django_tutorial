#stdlib imports
import time
import datetime

# django and local imports
from django.test import TestCase
from django.utils import timezone
from polls.models import Question, Choice

# Create your tests here.
class QCModelTest(TestCase):

    def test_saving_and_retrieving_questions(self):
        tz = timezone.get_default_timezone()
        question = Question()
        question.question_text = 'Who is the most famous actress?'
        question.pub_date = datetime.datetime(
            2012, 3, 31, 11, 30, 5, 182371, tzinfo=tz
        )
        question.save()

        saved_questions = Question.objects.all()
        self.assertEqual(saved_questions.count(), 1)
        saved_question = saved_questions[0]
        self.assertIn('Who is the most famous actress?',
            repr(saved_question),
        )
        self.assertEqual(saved_question.question_text,
            'Who is the most famous actress?')
        self.assertEqual(saved_question.pub_date,
            datetime.datetime(2012, 3, 31, 11, 30, 5, 182371, tzinfo=tz))

        self.assertFalse(saved_question.was_published_recently())

    def test_saving_and_retrieving_choices(self):

        choice = Choice()
        choice.choice_text = '1. Demi Moore 2. Julia Roberts'
        choice.votes = 1000
        choice.save()

        saved_choices = Choice.objects.all()
        self.assertEqual(saved_choices.count(), 1)
        saved_choice = saved_choices[0]
        self.assertIn('1. Demi Moore 2. Julia Roberts',
            repr(saved_choice),
        )
        self.assertEqual(saved_choice.choice_text, '1. Demi Moore 2. Julia Roberts')
        self.assertEqual(saved_choice.votes, 1000)


