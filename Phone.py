class Phone():
    def __init__(self, phone_number):
        self.number = phone_number

    def call(self, other_number):
        print(f"calling {other_number} from {self.number}")

    def text(self, other_number, msg):
        print(f"sending text to {other_number} from {self.number}")
        print(msg)

    def open_app(self, app_name):
        print(f"opening {app_name}")


class iPhone(Phone):
    def __init__(self, phone_number):
        super().__init__(phone_number)
        self.fingerprint = None

    def set_fingerprint(self, new_fingerprint):
        self.fingerprint = new_fingerprint

    def unlock(self, fingerprint=None):
        if (fingerprint == self.fingerprint):
            print("phone is unlocked")
        else:
            print("phone is locked")


han_iPhone = iPhone(802353176)
