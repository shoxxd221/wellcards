import requests

from .models import Card
from .models import ApiToken
from wellcards.celery import app
from wellcards.settings import CLIENT_ID, API_KEY

domain = 'https://api.spenxy.com'


@app.task
def get_api_token():
    """"Send POST request to Spenxy to get API Token"""
    token = requests.post(
        'https://api.spenxy.com/api/v1/authentication/login',
        headers={
            'Content-Type': 'application/json',
            'x-api-key': API_KEY,
            'x-client-id': CLIENT_ID},
        data=''
    ).json()['access_token']
    token_model = ApiToken.objects.get(id=1)
    token_model.token = token
    token_model.save()
    return token


def get_request_to_spenxy(endpoint: str, params=None):
    """"Send GET request to Spenxy"""
    if params is None:
        params = {}
    return requests.get(domain + endpoint,
                        headers={'Authorization': f'Bearer {ApiToken.objects.get(id=1).token}'},
                        params=params).json()


@app.task
def update_card_balance():
    """"Task that update balances of all cards every 5 minutes"""
    response = get_request_to_spenxy('/api/v1/cards/all')
    for i in response:
        card = Card.objects.filter(card_id=i['card_id']).first()
        if card is not None and i['balance']['available'] != card.balance.available:
            card.balance.available = i['balance']['available']
