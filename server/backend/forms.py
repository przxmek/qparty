from django import forms
from backend.models import Party


class JoinPartyForm(forms.Form):
    party_tag = forms.CharField(max_length=50, label='Party tag',
                                widget=forms.TextInput(attrs={'placeholder': 'Party tag..'}))
    admin_password = forms.CharField(widget=forms.PasswordInput, label='Host password', required=False)

    def clean(self):
        party_tag = super(JoinPartyForm, self).clean().get("party_tag")
        party = Party.objects.filter(tag=party_tag)
        if party.count() == 0:
            raise forms.ValidationError("Party with given tag does not exists.")

        admin_password = super(JoinPartyForm, self).clean().get("admin_password")
        if admin_password != '' and admin_password != party[0].password:
            raise forms.ValidationError("Incorrect admin password.")


class SetPasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), required=False)
    password_confirmation = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Repeat password'}), required=False)

    def clean(self):
        password = super(SetPasswordForm, self).clean().get("password")
        password_confirmation = super(SetPasswordForm, self).clean().get("password_confirmation")
        if not password:
            raise forms.ValidationError("Password can't be empty.")
        if password != password_confirmation:
            raise forms.ValidationError("Passwords are not identical.")