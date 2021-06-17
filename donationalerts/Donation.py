
class Donation:

    def __init__(self, donat: dict):
        self.dictinary = donat
        if donat == None:
            self.id = None
            self.name = None
            self.username = None
            self.recipient_name = None
            self.message = None
            self.message_type = None
            self.payin_system = None
            self.amount = None
            self.currency = None
            self.is_shown = None
            self.created_at = None
        else:
            self.id = donat['id']
            self.name = donat['name']
            self.username = donat['username']
            self.recipient_name = donat['recipient_name']
            self.message = donat['message']
            self.message_type = donat['message_type']
            self.payin_system = donat['payin_system']
            self.amount = donat['amount']
            self.currency = donat['currency']
            self.is_shown = donat['is_shown']
            self.created_at = donat['created_at']


    def __str__(self):
        return str(self.id)

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name and self.username == other.username and \
               self.recipient_name == other.recipient_name and self.message == other.message and \
                self.message_type == other.message_type and self.payin_system == other.payin_system and \
                self.amount == other.amount and self.currency == other.currency and self.is_shown == other.is_shown and \
                self.created_at == other.created_at



    def __ne__(self, other):
        return self.id != other.id or self.name != other.name or self.username != other.username or \
               self.recipient_name != other.recipient_name or self.message != other.message or \
               self.message_type != other.message_type or self.payin_system != other.payin_system or \
               self.amount != other.amount or self.currency != other.currency or self.is_shown != other.is_shown or \
               self.created_at != other.created_at

