from typing import Dict


def dict_to_list(dict: Dict):
    to_return = []
    for key in dict.keys():
        to_return.append(key)
        if dict.get(key) != '':
            to_return.append(dict.get(key))
    return to_return
