import json
from typing import Dict


def format(difference: Dict[str, list]) -> str:
    return json.dumps(difference)
