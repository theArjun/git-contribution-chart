import requests
from bs4 import BeautifulSoup
from django.shortcuts import render


def index(request):
    username = request.POST['username'] if request.method == 'POST' else 'thearjun'
    url = 'https://github.com/{}'.format(username)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    data = soup.findAll('rect')
    username = soup.select_one("span.p-name").text
    if str(username) == '':
        username = soup.select_one("span.p-nickname").text

    year_contribution = [int(el.get('data-count')) for el in data]
    year_date = [el.get('data-date') for el in data]
    month_contribution = [int(el.get('data-count')) for el in data][-30:]
    month_date = [el.get('data-date') for el in data][-30:]
    week_contribution = [int(el.get('data-count')) for el in data][-7:]
    week_date = [el.get('data-date') for el in data][-7:]

    return render(
        request,
        'chart/index.html',
        {
            'username': username,
            'year_date': year_date,
            'year_contribution': year_contribution,
            'month_date': month_date,
            'month_contribution': month_contribution,
            'week_date': week_date,
            'week_contribution': week_contribution,
        }
    )
