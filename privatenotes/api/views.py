import xmlrpc.client

from django.http import JsonResponse
from rest_framework import viewsets

from privatenotes import settings


class NoteViewSet(viewsets.ViewSet):
    @staticmethod
    def create(request):
        with xmlrpc.client.ServerProxy(settings.XML_RPC_SERVER_PATH) as proxy:
            id_ = proxy.create_note(request.data['content'])
            return JsonResponse({'id': id_})
