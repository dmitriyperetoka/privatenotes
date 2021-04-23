import xmlrpc.client

from django.http import Http404
from django.views.generic import FormView, TemplateView

from .forms import NoteForm
from privatenotes import settings


class NoteCreateView(FormView):
    template_name = 'notes/note_form.html'
    form_class = NoteForm


class NoteDetailView(TemplateView):
    template_name = 'notes/note_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        with xmlrpc.client.ServerProxy(settings.XML_RPC_SERVER_PATH) as proxy:
            content = proxy.read_and_delete_note(self.kwargs['pk'])
            if not content:
                raise Http404
            context['content'] = content
        return context
