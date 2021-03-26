from tool_exec.tools.nmap import Nmap
import pytest

def test_http_wordpress_enum():
    nmap = Nmap("")
    xml_finding = '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE nmaprun>\n<?xml-stylesheet href="file:///usr/local/bin/../share/nmap/nmap.xsl" type="text/xsl"?>\n<!-- Nmap 7.91 scan initiated Fri Mar 26 10:30:57 2021 as: /usr/local/bin/nmap -oX - -p443,80 -oX - -sV -&#45;script http-wordpress-enum localhost -->\n<nmaprun scanner="nmap" args="/usr/local/bin/nmap -oX - -p443,80 -oX - -sV -&#45;script http-wordpress-enum localhost" start="1616765457" startstr="Fri Mar 26 10:30:57 2021" version="7.91" xmloutputversion="1.05">\n<scaninfo type="connect" protocol="tcp" numservices="2" services="80,443"/>\n<verbose level="0"/>\n<debugging level="0"/>\n<hosthint><status state="up" reason="unknown-response" reason_ttl="0"/>\n<address addr="127.0.0.1" addrtype="ipv4"/>\n<hostnames>\n<hostname name="localhost" type="user"/>\n</hostnames>\n</hosthint>\n<host starttime="1616765457" endtime="1616765583"><status state="up" reason="syn-ack" reason_ttl="0"/>\n<address addr="127.0.1" addrtype="ipv4"/>\n<hostnames>\n<hostname name="localhost" type="user"/>\n<hostname name="server-00-000.eze.r.cloudfront.net" type="PTR"/>\n</hostnames>\n<ports><port protocol="tcp" portid="80"><state state="open" reason="syn-ack" reason_ttl="0"/><service name="http" product="Amazon CloudFront httpd" method="probed" conf="10"/><script id="http-server-header" output="CloudFront"><elem>CloudFront</elem>\n</script></port>\n<port protocol="tcp" portid="443"><state state="open" reason="syn-ack" reason_ttl="0"/><service name="http" product="Amazon CloudFront httpd" tunnel="ssl" method="probed" conf="10"/><script id="http-server-header" output="&#xa;  CloudFront&#xa;  Tengine/2.2.1"><elem>CloudFront</elem>\n<elem>Tengine/2.2.1</elem>\n</script><script id="http-wordpress-enum" output="&#xa;Search limited to top 100 themes/plugins&#xa;  themes&#xa;    point&#xa;  plugins&#xa;    wordpress-seo 14.1&#xa;    wordpress-importer 0.7&#xa;"><table key="point">\n<elem key="name">point</elem>\n<elem key="path">/wp-content/themes/point/</elem>\n<elem key="category">themes</elem>\n</table>\n<table key="wordpress-seo">\n<elem key="name">wordpress-seo</elem>\n<elem key="path">/wp-content/plugins/wordpress-seo/</elem>\n<elem key="installation_version">14.1</elem>\n<elem key="category">plugins</elem>\n</table>\n<table key="wordpress-importer">\n<elem key="name">wordpress-importer</elem>\n<elem key="path">/wp-content/plugins/wordpress-importer/</elem>\n<elem key="installation_version">0.7</elem>\n<elem key="category">plugins</elem>\n</table>\n<elem key="title">Search limited to top 100 themes/plugins</elem>\n</script></port>\n</ports>\n<times srtt="15109" rttvar="8997" to="100000"/>\n</host>\n<runstats><finished time="1616765583" timestr="Fri Mar 26 10:33:03 2021" summary="Nmap done at Fri Mar 26 10:33:03 2021; 1 IP address (1 host up) scanned in 126.46 seconds" elapsed="126.46" exit="success"/><hosts up="1" down="0" total="1"/>\n</runstats>\n</nmaprun>\n'
    parse = nmap.xml_parser(xml_finding)
    assert parse.get('params') == "/usr/local/bin/nmap -oX - -p443,80 -oX - -sV --script http-wordpress-enum localhost"
    assert parse.get('start_at') == "Fri Mar 26 10:30:57 2021"
    assert len(parse.get('results')) == 2
    assert parse.get('results')[0].get('port') == "80"
    assert parse.get('results')[0].get('protocol') == "tcp"
    assert parse.get('results')[0].get('state') == "open"
    assert parse.get('results')[0].get('service') == "http"
    assert parse.get('results')[0].get('product') == "Amazon CloudFront httpd"
    assert parse.get('results')[0].get('scripts')[0]['name'] == "http-server-header"
    assert parse.get('results')[0].get('scripts')[0]['output'] == "CloudFront"
    assert parse.get('results')[1].get('port') == "443"
    assert parse.get('results')[1].get('protocol') == "tcp"
    assert parse.get('results')[1].get('state') == "open"
    assert parse.get('results')[1].get('service') == "http"
    assert parse.get('results')[1].get('product') == "Amazon CloudFront httpd"
    assert parse.get('results')[1].get('scripts')[0].get('name') == "http-server-header"
    assert parse.get('results')[1].get('scripts')[0].get('output') == "CloudFront Tengine/2.2.1"
    assert parse.get('results')[1].get('scripts')[1].get('name') == "http-wordpress-enum"
    assert parse.get('results')[1].get('scripts')[1].get('results')[0].get('name') == "point"
    assert parse.get('results')[1].get('scripts')[1].get('results')[0].get('path') == "/wp-content/themes/point/"
    assert parse.get('results')[1].get('scripts')[1].get('results')[0].get('category') == "themes"

    assert parse.get('results')[1].get('scripts')[1].get('results')[1].get('name') == "wordpress-seo"
    assert parse.get('results')[1].get('scripts')[1].get('results')[1].get('path') == "/wp-content/plugins/wordpress-seo/"
    assert parse.get('results')[1].get('scripts')[1].get('results')[1].get('installation_version') == "14.1"
    assert parse.get('results')[1].get('scripts')[1].get('results')[1].get('category') == "plugins"

    assert parse.get('results')[1].get('scripts')[1].get('results')[2].get('name') == "wordpress-importer"
    assert parse.get('results')[1].get('scripts')[1].get('results')[2].get('path') == "/wp-content/plugins/wordpress-importer/"
    assert parse.get('results')[1].get('scripts')[1].get('results')[2].get('installation_version') == "0.7"
    assert parse.get('results')[1].get('scripts')[1].get('results')[2].get('category') == "plugins"