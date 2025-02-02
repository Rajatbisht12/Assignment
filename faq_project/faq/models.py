from django.db import models
from django.core.cache import cache
from django.utils.translation import gettext_lazy as _
from googletrans import Translator


def translate_text(text, dest_lang):
    """Translate text to the specified language using googletrans."""
    translator = Translator()
    try:
        translation = translator.translate(text, dest=dest_lang)
        return translation.text
    except Exception as e:
        print(f"Translation failed: {e}")
        return text

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    question_hi = models.CharField(max_length=255, blank=True, null=True)
    answer_hi = models.TextField(blank=True, null=True) 
    question_bn = models.CharField(max_length=255, blank=True, null=True)  
    answer_bn = models.TextField(blank=True, null=True)  

    def get_translated_question(self, lang):
        cache_key = f"faq_{self.id}_question_{lang}"
        cached_question = cache.get(cache_key)
        if cached_question:
            return cached_question
        translated_question = getattr(self, f"question_{lang}", self.question)
        cache.set(cache_key, translated_question, timeout=60 * 60)  
        return translated_question

    def get_translated_answer(self, lang):
        cache_key = f"faq_{self.id}_answer_{lang}"
        cached_answer = cache.get(cache_key)
        if cached_answer:
            return cached_answer
        translated_answer = getattr(self, f"answer_{lang}", self.answer)
        cache.set(cache_key, translated_answer, timeout=60 * 60)  
        return translated_answer

    def save(self, *args, **kwargs):
        if not self.question_hi and self.question:
            self.question_hi = translate_text(self.question, 'hi')
        if not self.answer_hi and self.answer:
            self.answer_hi = translate_text(self.answer, 'hi')
        if not self.question_bn and self.question:
            self.question_bn = translate_text(self.question, 'bn')
        if not self.answer_bn and self.answer:
            self.answer_bn = translate_text(self.answer, 'bn')
        super().save(*args, **kwargs)
