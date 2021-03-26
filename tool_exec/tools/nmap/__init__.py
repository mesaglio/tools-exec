from tool_exec.tools import BaseTool
from tool_exec.utils import find_bin
import os
import xmltodict


class Nmap(BaseTool):
    def __init__(self, arguments: str):
        super().__init__(arguments)
        self._arguments = self.arguments
        self._bin = find_bin("nmap")

    def run(self):
        full_command = f"{self._bin} -oX - {self._arguments}"
        output, error = self._run(full_command)
        if 'error' in error.lower():
            return self._parse_stderr(error)
        return self._parse_stdout(output)

    def _parse_stdout(self, stdout: str) -> dict:
        parser = self._xml_parser(stdout)
        return {'Success': True, 'Params': self._arguments, 'Data': parser}

    @staticmethod
    def _xml_parser(output: str) -> dict:
        to_return = {}
        parse = xmltodict.parse(output).get('nmaprun')
        to_return['params'] = parse.get('@args')
        to_return['start_at'] = parse.get('@startstr')
        to_return['results'] = []
        for port in parse.get('host').get('ports').get('port'):
            port_info = {'port': port.get('@portid'),
                         'protocol': port.get('@protocol'),
                         'state': port.get('state').get('@state'),
                         'service': port.get('service').get('@name'),
                         'product': port.get('service').get('@product', ''),
                         'version': port.get('service').get('@version', ''),
                         'more_info': port.get('service').get('@extrainfo', ''),
                         'scripts': []}
            if port.get('script'):
                for script in port.get('script'):
                    script_info = {'name': script.get('@id')}
                    if script.get('table'):
                        script_info['results'] = []
                        if script.get('table').get('elem'):
                            for info in script.get('table').get('elem'):
                                result_info = {info.get('@key'): info.get('#text')}
                                script_info['results'].append(result_info)
                        elif script.get('table').get('table'):
                            for cve_info in script.get('table').get('table'):
                                cve = {}
                                for elem in cve_info.get('elem'):
                                    cve[elem.get('@key')] = elem.get('#text')
                                script_info['results'].append(cve)
                        else:
                            script_info['output'] = script.get('@output')
                    port_info['scripts'].append(script_info)
            to_return['results'].append(port_info)
        return to_return
