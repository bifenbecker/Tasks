import json, socket
import time
from json import JSONDecodeError

import requests
from .Donation import Donation
from .SerializerDonation import SerializerDonation

APP_ID = '7637'
API_KEY = 'Q1kfbkrr2FmHLBKbnGFSyKNTKNeyFvqnjqPRNquJ'
REDIRECT_URI = 'http://127.0.0.1:8000/donationalerts/'
SCOPE = 'oauth-donation-index+oauth-user-show'

SAVE_PATH = 'donationalerts/last_donation.json'

def script(access_token):
    while True:
        headers = {'Authorization': 'Bearer {}'.format(access_token)}
        try:
            response = requests.get('https://www.donationalerts.com/api/v1/alerts/donations', headers=headers)
        except Exception:
            raise Exception("Не удалось получить донаты")

        donations = response.json()

        last_donation_api = Donation(donations['data'][0])
        last_donation_json = SerializerDonation.open(SAVE_PATH)

        if last_donation_api != last_donation_json:
            SerializerDonation.save(SAVE_PATH, last_donation_api)
            try:
                send_message_to_server(last_donation_api)
            except Exception as e:
                raise Exception(str(e))

        time.sleep(5)


def send_message_to_server(donation: Donation):
    send_data = SerializerDonation.get_donation_bytes(donation)
    HOST = '109.194.67.119'
    PORT = 9000
    try:
        sock = socket.socket()
        sock.connect((HOST, PORT))
        sock.send(send_data)
    except Exception:
        raise Exception(f"Не удалось отправить данные на сервер {HOST}:{PORT}")
    data = sock.recv(1024)
    sock.close()