from typing import Dict
import subprocess
import re


def dict_to_list(dict: Dict):
    to_return = []
    for key in dict.keys():
        to_return.append(key)
        if dict.get(key) != '':
            to_return.append(dict.get(key))
    return to_return


def find_bin(bin_name: str) -> str:
    """
    To find bin path location
    @param bin_name: terminal command
    @return: command binary full path

    Example:
        find_bin("nmap") -> "/usr/local/bin/nmap"
    """
    command = f"type {bin_name}"
    p = subprocess.Popen(args=command,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         stdin=subprocess.PIPE,
                         shell=True)

    (output, error) = p.communicate()
    _output, _error = bytes.decode(output), bytes.decode(error)
    if _error:  # TODO
        print("Error")
    if isinstance(_output, str):
        # TODO aliascheck
        array = _output.split("is")
        bin_path = array[-1]
        bin_path = clean_eof_tabs(bin_path)
        return bin_path
    else:  # TODO [']
        print("undefined")
        return ""


def clean_eof_tabs(string: str)-> str:
    return re.sub(r"[\n\t\s]*", "", string)

def clean_n(string: str) -> str:
    return ' '.join(string.split())