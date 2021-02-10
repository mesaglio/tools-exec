import subprocess
from typing import Dict
from sherlock.tools import BaseTool
import re


class Gobuster(BaseTool):
    def __init__(self, arguments: str):
        super().__init__(arguments)
        self._arguments = self.arguments

    def run(self):
        output, error = self._run(self.get_module_name(__name__))
        if 'error' in error.lower():
            return self._parse_stderr(error)
        return self._parse_stdout(output)

    @staticmethod
    def _parse_stderr(stderr: str):
        return {'Success': False, 'Error': stderr}

    def _parse_stdout(self, stdout: str):
        result = stdout.splitlines()
        data = []
        is_data = '^\/(.*)$'
        for line in result:
            if re.search(is_data, line):
                data.append(" ".join(line.split()))
        return {'Success': True, 'Params': self._arguments, 'Data': data}
