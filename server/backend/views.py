from django.shortcuts import render, redirect
from backend.forms import JoinPartyForm
from backend.models import Party, User


def get_user(request):
    try:
        return User.objects.filter(session=request.session)[0]
    except IndexError:
        return None


def index(request):
    if get_user(request):
        return player(request)

    return render(request, 'party/index.html')


def host_party(request):
    if get_user(request):
        return player(request)

    party = Party()
    party.init_party()
    user = User(session=request.session, party=party)
    user.save()

    return render(request, 'party/player.html', {'party_tag': party.tag})


def join_party(request):
    if get_user(request):
        return player(request)

    if request.method == 'POST':
        form = JoinPartyForm(request.POST)
        party_tag = form.cleaned_data['party_tag']
        party = Party.objects.get(tag=party_tag)
        user = User(session=request.session, party=party)
        user.save()
        if form.is_valid():
            return render(request, 'party/player.html', {'user': user})
    else:
        form = JoinPartyForm()

    return render(request, 'party/join_party.html', {'join_party_form': form})


def player(request):
    user = get_user(request)
    if not user:
        return redirect('index')

    return render(request, 'party/player.html', {'user': user})