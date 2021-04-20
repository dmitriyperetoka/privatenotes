from django.views.generic import FormView, DetailView

from .forms import NoteForm
from .models import Note


class NoteCreateView(FormView):
    template_name = 'notes/note_form.html'
    form_class = NoteForm


class NoteDetailView(DetailView):
    model = Note
