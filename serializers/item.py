
def convert_item_dict(item:any) -> dict:
    return {
        "_id" : str(item["_id"]),
        "name" : item["name"],
        "email" : item["email"],
        "item_name" : item["item_name"],
        "quantity" : item["quantity"],
        "expiry_date" : item["expiry_date"],
        "created_at" : item["created_at"],
    }


def convert_items_dict_list(items:list[dict]) -> list[dict]:
    return [ convert_item_dict(item) for item in items]