from fastapi import APIRouter, HTTPException
from models.clockin import ClockIn, UpdateClockIn
from datetime import datetime
from config.db import clockin_collection
from serializers.clockin import convert_clockin_dict, convert_clockins_dict_list
from bson import ObjectId


clockin_router = APIRouter()


@clockin_router.post("/")
def create_clockin(clockin: ClockIn):
    clockin_data = clockin.dict()
    _id = clockin_collection.insert_one({
        **clockin_data,
        "created_at" : datetime.now(),
    }).inserted_id
    return {
        **clockin_data,
        "_id" : str(_id)
    }


@clockin_router.get("/")
def get_clockins():
    clockins = clockin_collection.find()
    return convert_clockins_dict_list(clockins)


@clockin_router.get("/{_id}")
def get_clockin(_id:str):
    clockin = clockin_collection.find_one({"_id":ObjectId(_id) })
    if clockin:
        return convert_clockin_dict(clockin)
    raise HTTPException(status_code=404, detail=f"Clock-in with ID {id} not found")


@clockin_router.put("/{_id}")
def get_clockin(_id:str, clockin: UpdateClockIn):
    update_data = { k : v for k, v in clockin.dict().items() if v is not None}
    if update_data:
        updateed_record = clockin_collection.update_one({"_id" : ObjectId(_id)}, {"$set" : update_data})
        if updateed_record.modified_count == 1:
            clockin = clockin_collection.find_one({"_id" : ObjectId(_id)})
            return convert_clockin_dict(clockin)
        raise HTTPException(status_code=404, detail=f"Clock-in with ID {id} not found")
    raise HTTPException(status_code=400, detail=f"Fields not Provided")
    

@clockin_router.delete("/{_id}")
def delete_clockin(_id:str):
    deleted_clockin = clockin_collection.delete_one({"_id" : ObjectId(_id)})
    if deleted_clockin.deleted_count == 1:
        return {"message": "Clock-in deleted"}
    raise HTTPException(status_code=404, detail=f"Clock-in with ID {_id} not found")


@clockin_router.get("/filter/")
def filter_clockins(email : str = None, location: str = None,created_at : str = None ):
    q = {}
    if email:
        q["email"] = email
    if location:
        q["location"] = location
    if created_at:
        q["created_at"] = {"$gt": datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%S.%f")}

    if q:
        clockins = clockin_collection.find(q)
        return convert_clockins_dict_list(clockins)
    return []
