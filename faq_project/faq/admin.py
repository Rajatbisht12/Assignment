from django.contrib import admin
from .models import FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'question_hi', 'answer_hi', 'question_bn', 'answer_bn')
    search_fields = ('question', 'answer', 'question_hi', 'answer_hi', 'question_bn', 'answer_bn')
    list_filter = ('question', 'answer')

    fieldsets = (
        ('English', {
            'fields': ('question', 'answer'),
        }),
        ('Hindi', {
            'fields': ('question_hi', 'answer_hi'),
        }),
        ('Bengali', {
            'fields': ('question_bn', 'answer_bn'),
        }),
    )