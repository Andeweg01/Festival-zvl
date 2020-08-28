from django import forms
from .models import Concert, Edition, Location


class ConcertForm(forms.ModelForm):

    class Meta:
        model = Concert
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        editions = Edition.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in editions]

        self.fields['edition'].choices =friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-top'
