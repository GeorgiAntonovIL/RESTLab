import uvicorn as uvicorn
from fastapi import FastAPI
from AddressDTO import AddressDTO

app = FastAPI()

address_dict = {}


@app.get("/")
def home_page():
    return "Hello from Address_Service"


@app.get("/get/address/{user_id}")
def get_address(user_id: int):
    return address_dict[user_id]


@app.post("/create/{user_id}")
def create_address(user_id: int):
    if user_id not in address_dict:
        address_dict[user_id] = []
    address = AddressDTO()
    address_dict[user_id].append(address)
    return address_dict[user_id]


@app.delete("/delete/{user_id}")
def delete_address(user_id: int):
    if user_id not in address_dict:
        return {"Error": "User does not exist"}
    del address_dict[user_id]


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8002)
