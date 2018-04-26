from json import dumps, loads


def dict_to_json(_dict):
    return dumps(_dict)


def json_to_dict(_json):
    return loads(_json)
