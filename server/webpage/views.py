from django.contrib.sessions.models import Session
from django import forms
from django.shortcuts import render, redirect

from backend.forms import JoinPartyForm, SetPasswordForm
from backend.models import Party, User
from backend.views import get_user, is_party_assigned


def index(request, template_name='webpage/index.html'):
    if is_party_assigned(request):
        return redirect('webparty:index')

    join_party_form = JoinPartyForm(request.POST or None)
    join_party_form.fields['admin_password'].widget = forms.HiddenInput()
    set_passwd_form = SetPasswordForm(request.POST or None)

    if join_party_form.is_valid():
        party_tag = join_party_form.cleaned_data['party_tag']

        try:
            party = Party.objects.get(tag=party_tag)
        except:
            party = None

        user = get_user(request)
        if not user:
            user = User(session=Session.objects.get(session_key=request.session.session_key), party=party)
        else:
            user.party = party
        user.save()

        return redirect('webparty:index')

    if set_passwd_form.is_valid():
        party = Party()
        party.init_party()
        user = get_user(request)
        if not user:
            user = User(session=Session.objects.get(session_key=request.session.session_key), party=party)
        else:
            user.party = party
        user.save()
        party.admins.add(user)
        party.password = set_passwd_form.cleaned_data['password']
        party.save()

        return redirect('player')


    context = {
        'join_form': join_party_form,
        'host_form': set_passwd_form,
    }

    return render(request, template_name, context)


def leave(request):
    if not is_party_assigned(request):
        return redirect('webpage:index')

    user = get_user(request)
    user.party = None
    user.save()

    return redirect('webpage:index')