from abc import ABC, abstractmethod
import subprocess
from typing import Dict
from tool_exec.utils import dict_to_list
from tool_exec.utils.exceptions import invalid_config


class BaseTool(ABC):
    def __init__(self, arguments: str):
        self.arguments = arguments

    @staticmethod
    def get_module_name(module_name: str):
        return module_name.split('.')[-1]

    @staticmethod
    def _run(command: str):
        command_list = command.split()
        p = subprocess.Popen(command_list,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE,
                             bufsize=100000)

        (output, error) = p.communicate()
        return bytes.decode(output), bytes.decode(error)

    @abstractmethod
    def _parse_stderr(stderr: str) -> dict:
        ...
    
    @abstractmethod
    def _parse_stdout(self, stdout: str):
        ...

    @staticmethod
    def fail_response(error, arguments):
        return {'Success': False, 'Parmas': arguments, 'Erorr': error}

    @staticmethod
    def success_response(data, arguments):
        return {'Success': True, 'Params': arguments, 'Data': data}