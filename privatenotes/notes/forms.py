from ckeditor import widgets
from django import forms


class NoteForm(forms.Form):
    content = forms.CharField(widget=widgets.CKEditorWidget())

    class Meta:
        fields = ['content']
