from fastapi import APIRouter, HTTPException
from config.db import item_collection
from models.item import Item, UpdateItem
from serializers.item import convert_item_dict, convert_items_dict_list
from datetime import datetime
from bson import ObjectId
from fastapi import status
from fastapi import responses


items_router = APIRouter()


@items_router.post("/")
def create_item(item:Item):
    item_data = item.dict()
    _id = item_collection.insert_one({
        **item_data,
        "expiry_date" : datetime.combine(item_data["expiry_date"], datetime.min.time()),
        "created_at" : datetime.now(),
    }).inserted_id
    return {
        **item_data,
        "_id" : str(_id)
    }


@items_router.get("/")
def get_items():
    items_list = item_collection.find()
    return convert_items_dict_list(items_list)


@items_router.get("/{_id}")
def get_item(_id:str):
    item = item_collection.find_one({"_id" : ObjectId(_id)})
    if item:
        return convert_item_dict(item)
    raise HTTPException(status_code=404, detail=f"Item with ID {_id} not found")


@items_router.put("/{_id}")
def update_item(_id:str, item:UpdateItem):
    update_data = {k: v for k, v in item.dict().items() if v is not None}
    if update_data.get("expiry_date"):
        update_data["expiry_date"] = datetime.combine(update_data["expiry_date"], datetime.min.time())
    if update_data:
        updated_item = item_collection.update_one({"_id": ObjectId(_id)}, {"$set": update_data})
        if updated_item.modified_count == 1:
            item =  item_collection.find_one({"_id": ObjectId(_id)})
            return convert_item_dict(item)
        raise HTTPException(status_code=404, detail=f"Item with ID {_id} not found")
    raise HTTPException(status_code=400, detail=f"Fields not Provided")


@items_router.delete("/{_id}")
def delete_item(_id:str):
    deleted_item = item_collection.delete_one({"_id" : ObjectId(_id)})
    if deleted_item.deleted_count == 1:
        return {"message": "Item deleted"}
    raise HTTPException(status_code=404, detail=f"Item with ID {_id} not found")


@items_router.get("/filter/")
def filter_items(email: str = None, expiry_date: str = None, created_at: str = None, quantity: int = None):
    q = {}
    if email:
        q["email"] = email
    if expiry_date:
        q["expiry_date"] =  {"$gt": datetime.strptime(expiry_date, "%Y-%m-%d")}
    if created_at:
        q["created_at"] = {"$gt": datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%S.%f")}
    if quantity:
        q["quantity"] = {"$gte": quantity}
    if q:
        items_list = item_collection.find(q)
        return convert_items_dict_list(items_list)
    return []


@items_router.get("/items/aggregate/",)
async def aggregate_items():
    pipeline = [
        {"$group": {"_id": "$email", "count": {"$sum": 1}}}
    ]
    aggregation_result = item_collection.aggregate(pipeline).to_list(1000)
    return aggregation_result