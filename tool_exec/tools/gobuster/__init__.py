import subprocess
from typing import Dict
from tool_exec.tools import BaseTool
import re
from tool_exec.utils import find_bin


class Gobuster(BaseTool):
    def __init__(self, arguments: str):
        super().__init__(arguments)
        self._arguments = self.arguments
        self._bin = find_bin("gobuster")

    def run(self):
        output, error = self._run(f"{self._bin} {self._arguments}")
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
