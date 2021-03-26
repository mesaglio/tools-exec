import subprocess
from typing import Dict
from tool_exec.utils import dict_to_list
from tool_exec.utils.exceptions import invalid_config


class BaseTool:
    def __init__(self, arguments: str):
        self.arguments = arguments

    @staticmethod
    def get_module_name(module_name: str):
        return module_name.split('.')[-1]

    @staticmethod
    def _run(command: str):
        p = subprocess.Popen(args=command,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE,
                             shell=True)

        (output, error) = p.communicate()
        return bytes.decode(output), bytes.decode(error)
