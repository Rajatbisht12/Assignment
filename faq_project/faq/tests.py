from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import FAQ

class FAQModelTest(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a Python-based web framework.",
            question_hi="डिजैंगो क्या है?",
            answer_hi="डिजैंगो एक पायथन-आधारित वेब फ्रेमवर्क है।"
        )
    
    def test_faq_creation(self):
        self.assertEqual(self.faq.question, "What is Django?")
        self.assertEqual(self.faq.answer_hi, "डिजैंगो एक पायथन-आधारित वेब फ्रेमवर्क है।")

class FAQViewTests(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a Python-based web framework.",
            question_hi="डिजैंगो क्या है?",
            answer_hi="डिजैंगो एक पायथन-आधारित वेब फ्रेमवर्क है।"
        )
    
    def test_faq_list_view(self):
        response = self.client.get(reverse('faq-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'faq/faq_list.html')

    def test_faq_translation_hi(self):
        response = self.client.get(reverse('faq-list') + '?lang=hi')
        self.assertContains(response, "डिजैंगो क्या है?")
        self.assertContains(response, "डिजैंगो एक पायथन-आधारित वेब फ्रेमवर्क है।")

class FAQAPITestCase(APITestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a Python-based web framework.",
            question_hi="डिजैंगो क्या है?",
            answer_hi="डिजैंगो एक पायथन-आधारित वेब फ्रेमवर्क है।"
        )
        self.url = reverse('faq-list')
    
    def test_get_faqs(self):
        response = self.client.get('/api/faqs/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_create_faq(self):
        data = {
            "question": "What is REST API?",
            "answer": "REST API is a web service architecture.",
            "question_hi": "REST API क्या है?",
            "answer_hi": "REST API एक वेब सेवा आर्किटेक्चर है।"
        }
        response = self.client.post('/api/faqs/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(FAQ.objects.count(), 2)
    
    def test_update_faq(self):
        url = f'/api/faqs/{self.faq.id}/'
        data = {"question": "Updated Question", "answer": "Updated Answer"}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.faq.refresh_from_db()
        self.assertEqual(self.faq.question, "Updated Question")
    
    def test_delete_faq(self):
        url = f'/api/faqs/{self.faq.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(FAQ.objects.count(), 0)
