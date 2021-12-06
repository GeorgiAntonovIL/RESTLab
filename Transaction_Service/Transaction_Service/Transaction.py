from pydantic import BaseModel


class Transaction:
    transaction_id: int
    date_of_execution: str

    def __init__(self, trans_id, date):
        self.transaction_id = trans_id
        self.date_of_execution = date
