from django.shortcuts import render
from youtube.forms import SearchForm
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup


def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            encoded_query = urllib.parse.urlencode({'search_query': query})
            response = urllib.request.urlopen('https://www.youtube.com/results?' + encoded_query)
            page_src = response.read()
            response.close()
            parsed = BeautifulSoup(page_src)

            send_data = []

            div_results = parsed.body.find('div', attrs={'id': 'results'})
            songs_divs = div_results.find_all('div', attrs={'class': 'yt-lockup-content'})
            for div in songs_divs:
                link = div.find('a')
                send_data.append((link.get('href')[9:], link.text))

            return render(request, 'youtube/search_results.html', {'query': query, 'src': send_data})
    else:
        form = SearchForm()

    return render(request, 'youtube/index.html', {'search_form': form})