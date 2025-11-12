from fastapi import FastAPI, HTTPException
import uvicorn
import json
from pydantic import BaseModel


class Price(BaseModel):
    new_price : int


app = FastAPI()
items = []

def load_data():

    with open("data.json", "r") as f:
         file_data = f.read()
         return json.loads(file_data)


def save_data(data):
    pass


@app.put("/items/{item_id}/")
def update_item_by_id(item_id : int, price : Price):
    data = load_data()
    for item in data:
        if item["id"] == item_id:
            item["price"] = price.new_price
            return {"message" : "Item updated", "item" : item}

    raise HTTPException(status_code = 404, detail="item not found")

@app.get("/items/")
def get_json_items():
    return load_data()


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)