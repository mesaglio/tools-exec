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

    def _parse_stderr(self, stderr: str) -> dict:
        return self.fail_response(stderr, self._arguments)

    def _parse_stdout(self, stdout: str) -> dict:
        result = stdout.splitlines()
        data = []
        is_data = '^\/(.*)$'
        for line in result:
            if re.search(is_data, line):
                data.append(" ".join(line.split()))
        return self.success_response(data, self._arguments)
