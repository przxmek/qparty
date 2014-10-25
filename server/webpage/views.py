from django.contrib.sessions.models import Session
from django.shortcuts import render, redirect
from backend.models import Party, User
from backend.views import get_user


def index(request, template_name='webpage/index.html'):
    party_tag = request.POST.get('party_tag', None)
    try:
        party = Party.objects.get(tag=party_tag)
    except:
        party = None

    if party:
        user = get_user(request)
        if not user:
            user = User(session=Session.objects.get(session_key=request.session.session_key), party=party)
        else:
            user.party = party
        user.save()

        return redirect('dashboard')

    context = {
        'party_tag': party_tag,
    }

    return render(request, template_name, context)