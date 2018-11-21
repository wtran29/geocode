from django import forms

from distance.status.models import Status


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = [
            'user',
            'content',
        ]

    def clean(self, *args, **kwargs):
        data = self.cleaned_data
        content = data.get('content', None)
        if content == "":
            content = None
        if content is None:
            raise forms.ValidationError('Content is required.')
        return super().clean(*args, **kwargs)

