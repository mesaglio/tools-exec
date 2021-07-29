import json
from tool_exec.logger import logger
from tool_exec.tools.gobuster import Gobuster
from tool_exec.tools.nmap import Nmap
from tool_exec.tools.nuclei import Nuclei

if __name__ == "__main__":  # TODO to test in local
    args = "-u http://localhost:8000 http://localhost:8081 -ud /Users/jmesaglio/Documents/Repos/meli-nuclei-template -t test/ -silent -json"
    nuclei = Nuclei(args)
    output = nuclei.run()
    print(json.dumps(output, indent=4))
