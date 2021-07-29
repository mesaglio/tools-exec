# Tools-exec

To execute seg-inf tools from python3 and get the result in json.

### Examples

```python
#Nmap example
nmap = Nmap("-p8001,80 -oX - -sV --script http-wordpress-enum,vulners localhost")
output = nmap.run()
'''
{
    "Success": true,
    "Params": "-p8001,80 -oX - -sV --script http-wordpress-enum,vulners localhost",
    "Data": {
        "params": "/usr/local/bin/nmap -oX - -p8001,80 -oX - -sV --script http-wordpress-enum,vulners localhost",
        "start_at": "Fri Mar 26 01:47:46 2021",
        "results": [
            {
                "port": "80",
                "protocol": "tcp",
                "state": "closed",
                "service": "http",
                "product": "",
                "version": "",
                "more_info": "",
                "scripts": []
            },
            {
                "port": "8001",
                "protocol": "tcp",
                "state": "open",
                "service": "http",
                "product": "Apache httpd",
                "version": "2.4.38",
                "more_info": "(Debian)",
                "scripts": [
                    {
                        "name": "http-server-header"
                    },
                    {
                        "name": "http-wordpress-enum",
                        "results": [
                            {
                                "category": "plugins",
                                "path": "/wp-content/plugins/akismet/",
                                "name": "akismet"
                            }
                        ]
                    },
                    {
                        "name": "vulners",
                        "results": [
                            {
                                "cvss": "7.5",
                                "type": "cve",
                                "id": "CVE-2020-11984",
                                "is_exploit": "false"
                            },
                            {
                                "cvss": "7.2",
                                "type": "exploitpack",
                                "id": "EXPLOITPACK:44C5118F831D55FAF4259C41D8BDA0AB",
                                "is_exploit": "true"
                            }
                        ]
                    }
                ]
            }
        ]
    }
}
'''
#Gobuster example
args = 'dir -w /Users/jmesaglio/SecLists-master/Discovery/Web-Content/common.txt --wildcard -u 127.0.0.1'
gb = Gobuster(args)
result = gb.run()
print(json.dumps(result, indent=4))
'''
{
    "Success": true,
    "Params": "dir -w /Users/jmesaglio/SecLists-master/Discovery/Web-Content/common.txt --wildcard -u 131.255.4.19",
    "Data": [
        "/.cache (Status: 200) [Size: 1019]",
        "/.bash_history (Status: 200) [Size: 1019]",
        "/.bashrc (Status: 200) [Size: 1019]",
        "/.history (Status: 200) [Size: 1019]",
        "/.hta (Status: 200) [Size: 1019]",
        "/.git/HEAD (Status: 200) [Size: 1019]",
        "/.cvs (Status: 200) [Size: 1019]"
        ]
}
'''
```

### To run tests

```
# In local
-> poetry install && poetry run make local-test
```