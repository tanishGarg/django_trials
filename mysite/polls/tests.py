import datetime
from django.utils import timezone
from django.test import TestCase
from .models import Question
from django.urls import reverse

def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionViewTests(TestCase):
    def test_index_view_with_no_question(self):
        #IF NO QUES -> appropriate message should display
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code , 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_index_view_with_a_past_question(self):
        #Question with pub_date in the past should be displayed on the index page
        create_question(question_text='Past question', days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question : Past question.>']
        )

    def test_index_view_with_a_future_question(self):
        #Question with pub_date in the future should not be displayed on the index page
        create_question(question_text='Future question', days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_index_view_with_future_question_and_past_question(self):
        #EVEN IF Both future & past question are present- only past one will be displayed
        create_question(question_text='Past question', days=-30)
        create_question(question_text='Future question', days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question : Past question.>']
        )

    def test_index_view_with_two_past_question(self):
        #multiple past question will be displayed
        create_question(question_text='Past question', days=-30)
        create_question(question_text='Past question', days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question : Past question 2.>', '<Question : Past question 1.>']
        )


class QuestionMethodTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

class QuestionIndexDetailTests(TestCase):

    def test_detail_view_with_a_future_question(self):
        #The detail view of a question with a pub_date in the future should return a 404 not found.
        future_question = create_question(question_text='Future question.', days=5)
        url=reverse('polls:detail', args=(future_question.id))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_detail_view_with_a_past_question(self):
        #The detail view of a question with a pub_date in the future should return a 404 not found.
        past_question = create_question(question_text='Past question.', days=-5)
        url=reverse('polls:detail', args=(past_question.id))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)
