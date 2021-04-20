from django.shortcuts import get_object_or_404
from rest_framework import mixins, viewsets

from .serializers import NoteSerializer
from notes.models import Note


class NoteViewSet(
        mixins.CreateModelMixin,
        mixins.DestroyModelMixin,
        viewsets.GenericViewSet
):
    serializer_class = NoteSerializer

    def get_object(self):
        return get_object_or_404(Note, id=self.kwargs.get('pk'))
