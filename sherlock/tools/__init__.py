import subprocess
from typing import Dict
from sherlock.utils import dict_to_list
from sherlock.utils.exceptions import invalid_config


class BaseTool:
    def __init__(self, arguments: str):
        self.arguments = arguments

    @staticmethod
    def get_module_name(module_name: str):
        return module_name.split('.')[-1]

    def _run(self, command: str):
        custom_args = [command]
        custom_args.extend(self.arguments.split())
        p = subprocess.Popen(args=custom_args,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE)

        (output, error) = p.communicate()
        return bytes.decode(output), bytes.decode(error)
