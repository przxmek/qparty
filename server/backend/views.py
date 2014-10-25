from django.contrib.sessions.models import Session
from django.shortcuts import render, redirect
from backend.forms import JoinPartyForm
from backend.models import Party, User


def is_party_assigned(request):
    user = get_user(request)
    return user and user.party


def get_user(request):
    try:
        return User.objects.filter(session=request.session.session_key)[0]
    except IndexError:
        return None


def index(request):
    if is_party_assigned(request):
        return redirect('player')

    return render(request, 'party/index.html')


def host_party(request):
    if is_party_assigned(request):
        return redirect('player')

    party = Party()
    party.init_party()
    user = get_user(request)
    if not user:
        user = User(session=Session.objects.get(session_key=request.session.session_key), party=party)
    else:
        user.party = party
    user.save()

    return render(request, 'party/player.html', {'user': user})


def join_party(request):
    if is_party_assigned(request):
        return redirect('player')

    if request.method == 'POST':
        form = JoinPartyForm(request.POST)
        if form.is_valid():
            party_tag = form.cleaned_data['party_tag']
            party = Party.objects.get(tag=party_tag)
            user = get_user(request)
            if not user:
                user = User(session=Session.objects.get(session_key=request.session.session_key), party=party)
            else:
                user.party = party
            user.save()
            return render(request, 'party/player.html', {'user': user})
    else:
        form = JoinPartyForm()

    return render(request, 'party/join_party.html', {'join_party_form': form})


def player(request):
    if not is_party_assigned(request):
        return redirect('index')

    return render(request, 'party/player.html', {'user': get_user(request)})


def logout(request):
    if not is_party_assigned(request):
        return redirect('index')

    user = get_user(request)
    user.party = None
    user.save()
    return redirect('index')