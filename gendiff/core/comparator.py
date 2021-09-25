REMOVED = 'removed'
UPDATED = 'updated'
ADDED = 'added'


def compare(dict1: dict, dict2: dict) -> dict:
    for key, val in dict1.items():
        if isinstance(val, dict):
            pass
