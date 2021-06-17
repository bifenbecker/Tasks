import json
from json import JSONDecodeError

from .Donation import Donation

class SerializerDonation:

    @staticmethod
    def get_json(donation: Donation) -> dict:
        res = {
            'id': donation.id,
            'name': donation.name,
            'username': donation.username,
            'recipient_name': donation.recipient_name,
            'message': donation.message,
            'message_type': donation.message_type,
            'payin_system': donation.payin_system,
            'amount': donation.amount,
            'currency': donation.currency,
            'is_shown': donation.is_shown,
            'created_at': donation.created_at,
        }
        return res

    @staticmethod
    def get_donation(json: dict) -> Donation:
        donation = Donation(json)
        return donation

    @staticmethod
    def save(path: str, donation: Donation):
        data = SerializerDonation.get_json(donation)
        with open(path, 'w', encoding='utf-8') as fp:
            json.dump(data, fp)

    @staticmethod
    def open(path: str):
        with open(path, 'r', encoding='utf-8') as fp:
            try:
                donation_json = json.load(fp)
            except JSONDecodeError:
                donation_json = None

        return SerializerDonation.get_donation(donation_json)

    @staticmethod
    def get_donation_bytes(donation: Donation) -> bytes:
        encode_data = json.dumps(SerializerDonation.get_json(donation), indent=2).encode('utf-8')
        return encode_data