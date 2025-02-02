from django.urls import path,include
from .views import (
    FAQListView, 
    FAQCreateView, 
    FAQUpdateView, 
    FAQDeleteView,
    FAQAPIView,
    FAQViewSet
)
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'faqs', FAQViewSet)
urlpatterns = [
     path('api/', include(router.urls)),
    
    path('', FAQListView.as_view(), name='faq-list'),
    path('create/', FAQCreateView.as_view(), name='faq-create'),
    path('update/<int:pk>/', FAQUpdateView.as_view(), name='faq-update'),
    path('delete/<int:pk>/', FAQDeleteView.as_view(), name='faq-delete'),
]