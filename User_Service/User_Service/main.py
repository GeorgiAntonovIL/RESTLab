import uvicorn as uvicorn
from fastapi import FastAPI, HTTPException
import requests
from UpdateUserDTO import UpdateUserDTO
from User import User

app = FastAPI()

user_dict = {}


@app.get("/")
def home_page():
    return "Hello from User_Service"


@app.get("/get/user/{user_id}")
def get_id(user_id: int):
    if user_id not in user_dict:
        raise HTTPException(status_code=204, detail="no context")
    req = requests.get(f"http://127.0.0.1:8002/get/address/{user_id}")
    trans_req = requests.get(f"http://127.0.0.1:8003/get/{user_id}")
    return user_dict[user_id], req.json(), trans_req.json()


@app.post("/create/{user_id}")
def create_user(user_id: int, user: User):
    if user_id in user_dict:
        return {"Error": "user already exists"}
    user_dict[user_id] = user
    requests.post(f"http://127.0.0.1:8002/create/{user_id}")
    return user_dict[user_id]


@app.delete("/delete/{user_id}")
def delete_user(user_id: int):
    if user_id not in user_dict:
        return {"Error": "User does not exist"}
    requests.delete(f"http://127.0.0.1:8002/delete/{user_id}")
    del user_dict[user_id]
    return {"Response": "User has been deleted"}


@app.put("/update/{user_id}")
def update_user(user_id: int, user: UpdateUserDTO):
    if user_id not in user_dict:
        return {"Error": "User does not exist"}
    user_dict.update({user_id: user})
    requests.post(f"http://127.0.0.1:8002/create/{user_id}")
    return user_dict[user_id]


@app.get("/get/all")
def get_id():
    return user_dict


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8001)
