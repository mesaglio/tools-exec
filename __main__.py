import logging
import json
from sherlock.logger import logger
from sherlock.tools.gobuster import Gobuster
from sherlock.tools.ls import Ls

if __name__ == "__main__":
    args = 'dir -w SecLists-master/Discovery/Web-Content/common.txt --wildcard -u 131.255.4.19'
    gb = Gobuster(args)
    result = gb.run()
    print(json.dumps(result,indent=4))
    ls = Ls('-la')
    print(ls.run())
