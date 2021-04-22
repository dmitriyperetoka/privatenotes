import requests
from django.shortcuts import reverse
from django.views.generic import FormView, DetailView

from .forms import NoteForm
from .models import Note


class NoteCreateView(FormView):
    template_name = 'notes/note_form.html'
    form_class = NoteForm


class NoteDetailView(DetailView):
    model = Note

    def render_to_response(self, context, **response_kwargs):
        protocol = self.request.META['wsgi.url_scheme']
        host = self.request.get_host()
        path = reverse('api:note-detail', kwargs={'pk': self.object.id})
        url = f'{protocol}://{host}{path}'
        requests.delete(url)
        return super().render_to_response(context, **response_kwargs)
