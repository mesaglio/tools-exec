import logging
import json
from tool_exec.logger import logger
from tool_exec.tools.gobuster import Gobuster
from tool_exec.tools.nmap import Nmap

if __name__ == "__main__":#TODO to test in local
    nmap = Nmap("-p8001,80 -oX - -sV --script http-wordpress-enum,vulners localhost")
    output = nmap.run()
    print(json.dumps(output,indent=4))
