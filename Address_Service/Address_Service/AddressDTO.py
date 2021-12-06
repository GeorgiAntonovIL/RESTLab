import random


class AddressDTO:
    address: str

    def __init__(self):
        self.address = str(f"{random.randint(1, 500)} Street")
