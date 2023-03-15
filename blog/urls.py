from django.urls import path
from .views import (
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    Learning_disabilities_PostListView,
    Hearing_loss_PostListView,
    Cerebral_palsy_PostListView,
    Physical_disability_PostListView,
    Vision_impairment_PostListView,
    Dyslexia_PostListView,
    Stroke_PostListView,
    Diabetes_PostListView,
    Spinal_cord_injury_PostListView,
    Parkinsons_disease_PostListView,
    Neurological_disorder_PostListView
)
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('about/', views.about, name='blog-about'),
    
    path('Learning_disabilities/', Learning_disabilities_PostListView.as_view(), name='Learning_disabilities'),
    path('Hearing_loss/', Hearing_loss_PostListView.as_view(), name='Hearing_loss'),
    path('Cerebral_palsy/', Cerebral_palsy_PostListView.as_view(), name='Cerebral_palsy'),
    path('Physical_disability/', Physical_disability_PostListView.as_view(), name='Physical_disability'),
    path('Vision_impairment/', Vision_impairment_PostListView.as_view(), name='Vision_impairment'),
    path('Dyslexia/', Dyslexia_PostListView.as_view(), name='Dyslexia'),
    path('Stroke/', Stroke_PostListView.as_view(), name='Stroke'),
    path('Diabetes/', Diabetes_PostListView.as_view(), name='Diabetes'),
    path('Spinal_cord_injury/', Spinal_cord_injury_PostListView.as_view(), name='Spinal_cord_injury'),
    path('Parkinsons_disease/', Parkinsons_disease_PostListView.as_view(), name='Parkinsons_disease'),
    path('Neurological_disorder/', Neurological_disorder_PostListView.as_view(), name='Neurological_disorder'),

    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
