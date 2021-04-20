from django.conf.urls import handler404  # noqa
from django.contrib import admin
from django.urls import include, path, reverse_lazy
from django.views.generic import RedirectView

handler404 = 'privatenotes.views.page_not_found'  # noqa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls', namespace='api')),
    path('notes/', include('notes.urls', namespace='notes')),
    path('', RedirectView.as_view(url=reverse_lazy('notes:note_form')),
         name='index'),
]
