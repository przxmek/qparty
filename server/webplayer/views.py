from django.shortcuts import render


def player(request, template_name='webplayer/player.html'):
    context = {

    }

    return render(request, template_name, context)