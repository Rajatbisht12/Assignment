from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import FAQ
from .forms import FAQForm
from .serializers import FAQSerializer
from rest_framework import viewsets

from django.views.generic import ListView

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def get_queryset(self):
        lang = self.request.query_params.get('lang', 'en')
        queryset = super().get_queryset()
        for faq in queryset:
            faq.question = faq.get_translated_question(lang)
            faq.answer = faq.get_translated_answer(lang)
        return queryset
    
class FAQAPIView(ListView):
    model = FAQ
    template_name = 'faq/faq_list.html'
    context_object_name = 'faqs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get language from URL parameter
        context['current_lang'] = self.request.GET.get('lang', 'en')
        
        # Get all FAQs with translations
        faqs = FAQ.objects.all()
        
        # Create a list of FAQs with translations based on selected language
        translated_faqs = []
        for faq in faqs:
            if context['current_lang'] == 'hi':
                translated_faqs.append({
                    'id': faq.id,
                    'question': faq.question_hi or faq.question,
                    'answer': faq.answer_hi or faq.answer
                })
            elif context['current_lang'] == 'bn':
                translated_faqs.append({
                    'id': faq.id,
                    'question': faq.question_bn or faq.question,
                    'answer': faq.answer_bn or faq.answer
                })
            else:
                translated_faqs.append({
                    'id': faq.id,
                    'question': faq.question,
                    'answer': faq.answer
                })
        
        context['faqs'] = translated_faqs
        return context

# The rest of your views are correct
class FAQListView(ListView):
    model = FAQ
    template_name = 'faq/faq_list.html'
    context_object_name = 'faqs'

class FAQCreateView(CreateView):
    model = FAQ
    form_class = FAQForm
    template_name = 'faq/faq_form.html'
    success_url = reverse_lazy('faq-list')

class FAQUpdateView(UpdateView):
    model = FAQ
    form_class = FAQForm
    template_name = 'faq/faq_form.html'
    success_url = reverse_lazy('faq-list')

class FAQDeleteView(DeleteView):
    model = FAQ
    template_name = 'faq/faq_confirm_delete.html'
    success_url = reverse_lazy('faq-list')