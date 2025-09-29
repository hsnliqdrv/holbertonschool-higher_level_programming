#!/usr/bin/python3
"""3-to_json_string
"""


def to_json_string(my_obj):
    """Return JSON of object

    Arguments:
        my_obj (object): an object

    Returns:
        (str): serialized object
    """
    with json.dumps(my_obj) as json_repr:
        return json_repr
