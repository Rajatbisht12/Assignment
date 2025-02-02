from django import forms
from .models import FAQ

class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['question', 'answer', 'question_hi', 'answer_hi', 'question_bn', 'answer_bn']