import uuid

from django.db import models
from ckeditor.fields import RichTextField


class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = RichTextField(verbose_name='Текст заметки')

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
