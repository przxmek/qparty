from django.contrib.sessions.models import Session
from django.shortcuts import render, redirect
from backend.forms import JoinPartyForm
from backend.models import Party, User
from backend.views import get_user, is_party_assigned


def index(request, template_name='webpage/index.html'):
    join_party_form = JoinPartyForm(request.POST or None)

    if is_party_assigned(request):
        return redirect('webparty:index')

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

    context = {
        'join_form': join_party_form,
    }

    return render(request, template_name, context)


def host_party(request):
    if not is_party_assigned(request):
        party = Party()
        party.init_party()
        user = get_user(request)
        if not user:
            user = User(session=Session.objects.get(session_key=request.session.session_key), party=party)
        else:
            user.party = party
        user.save()
        party.admins.add(user)
        party.save()

    return redirect('player')