from tool_exec.tools import BaseTool
from tool_exec.utils import find_bin, clean_n
import json


class Nuclei(BaseTool):
    def __init__(self, arguments: str):
        super().__init__(arguments)
        self._arguments = self.arguments
        self._bin = find_bin("nuclei")

    def run(self):
        output, error = self._run(f"{self._bin} {self._arguments}")
        if error:
            return self._parse_stderr(error)
        return self._parse_stdout(output)

    def _parse_stderr(self, stderr: str) -> dict:
        stderr = stderr.split('[0m]')[1]
        error = clean_n(stderr.strip())
        return self.fail_response(error, self._arguments)

    def _parse_stdout(self, stdout: str) -> dict:
        result = stdout.splitlines()
        data = [json.loads(r) for r in result]
        return self.success_response(data, self._arguments)
