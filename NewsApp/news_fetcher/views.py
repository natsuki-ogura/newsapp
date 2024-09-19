import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings


def fetch_news(request):
    try:
        newsapi_key = settings.NEWSAPI_KEY
        url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi_key}'
        response = requests.get(url)
        news_data = response.json()
        articles = news_data['articles']
        context = {'articles': articles}

        return render(request, 'news_fetcher/fetch_news.html', context)

    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}")
