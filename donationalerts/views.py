from multiprocessing import Process

import requests
from django.shortcuts import render, redirect
from django.views import View
from .API import *

from .script import *

APP_ID = '7637'
API_KEY = 'Q1kfbkrr2FmHLBKbnGFSyKNTKNeyFvqnjqPRNquJ'
REDIRECT_URI = 'http://127.0.0.1:8000/donationalerts/'
SCOPE = 'oauth-donation-index+oauth-user-show'

class MainPageView(View):
    template_name = 'donationalerts.html'

    def get(self, request):
        code = request.GET['code']

        # 4. Getting Access Token
        data = {'grant_type': 'authorization_code', 'client_id': APP_ID, 'client_secret': API_KEY,
                'redirect_uri': REDIRECT_URI, 'code': code}
        r = requests.post('https://www.donationalerts.com/oauth/token', data=data).json()

        access_token = r['access_token']

        # Authorized Request
        headers = {'Authorization': 'Bearer {}'.format(access_token)}

        response = requests.get('https://www.donationalerts.com/api/v1/user/oauth', headers=headers)
        r = response.json()

        user = r['data']['name']
        response = requests.get('https://www.donationalerts.com/api/v1/alerts/donations', headers=headers)
        donations = response.json()

        process = Process(target=script, args=(access_token,))
        try:
            process.start()
        except Exception as e:
            error = str(e)

        return render(request, self.template_name, context={'user': user, 'donations': donations['data'], 'total': donations['meta']['total'], 'error': error})


class LoginView(View):

    def get(self, request):
        url = f'https://www.donationalerts.com/oauth/authorize?client_id={APP_ID}&redirect_uri={REDIRECT_URI}&response_type=code&scope={SCOPE}'
        return redirect(url)
