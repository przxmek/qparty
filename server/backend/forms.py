from django import forms
from backend.models import Party


class JoinPartyForm(forms.Form):
    party_tag = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput, required=False)

    def clean(self):
        party_tag = super(JoinPartyForm, self).clean().get("party_tag")
        if Party.objects.filter(tag=party_tag).count() == 0:
            raise forms.ValidationError("Party with given tag does not exists.")