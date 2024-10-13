
def convert_clockin_dict(clockin:any) -> dict:
    return {
        "_id" : str(clockin["_id"]),
        "email" : clockin["email"],
        "location" : clockin["location"],
        "created_at" : clockin["created_at"],
    }


def convert_clockins_dict_list(clockins:list[dict]) -> list[dict]:
    return [ convert_clockin_dict(clockin) for clockin in clockins]