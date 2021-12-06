from http.client import HTTPException

import uvicorn as uvicorn
from fastapi import FastAPI
import requests
import json
from Transaction import Transaction

app = FastAPI()

transaction_dict = {}


@app.get("/")
def home_page():
    return "Hello from Transaction_Service"


@app.get("/get/{user_id}")
def get_transactions(user_id: int):
    if user_id not in transaction_dict:
        return {"Error": "Transaction does not exist"}
    return transaction_dict[user_id]


@app.post("/create/{user_id}")
def create_transaction(user_id: int):
    request = requests.get(f"http://127.0.0.1:8001/get/user/{user_id}")
    if request.status_code == 204:
        return {"Error": "User does not exist"}

    for x in range(0, 10):
        req = requests.get(f"http://127.0.0.1:8000/info/generate/id")
        if req.status_code == 200:
            if user_id not in transaction_dict:
                transaction_dict[user_id] = []
            dictionary = json.loads(req.content)
            trans_id = dictionary.get("id")
            trans_date = dictionary.get("dateOfExecution")
            transaction = Transaction(trans_id, trans_date)
            transaction_dict[user_id].append(transaction)
            return transaction_dict[user_id]
        else:
            print("Status code 500.Will retry")

    return {"Error": "retried 10 times and still got status code 500"}


@app.delete("/delete/{user_id}")
def delete_user(user_id: int):
    if user_id not in transaction_dict:
        return {"Error": "Transaction does not exist"}
    del transaction_dict[user_id]
    return {"Response": "Transactions have been deleted"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8003)
