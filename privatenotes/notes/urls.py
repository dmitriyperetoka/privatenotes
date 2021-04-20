from django.urls import path

from . import views

app_name = 'notes'

urlpatterns = [
    path('form/', views.NoteCreateView.as_view(), name='note_form'),
    path('<str:pk>/', views.NoteDetailView.as_view(), name='note_detail'),
]
