# ZenPacks.zenoss.HttpsMonitor
HTTPS Monitor Zenpack for Zenoss Core 4.x

This ZenPack is an extended version of the stock HttpMonitor and supports polling websites that require Server Name Indication (SNI) extension in the request.

It is configured based on the manual check_http Nagios Plugin command:

/usr/lib64/nagios/plugins/check_http -H www.mywebsite.com --onredirect=follow --ssl --sni

Configuration Properties Changes: \
zPingMonitorIgnore is set to True 

Data Source Changes: \
Cycle Time (seconds) is set to 150 ( Default: 300 ) \
Severity is set to Criticial ( Default: Warning ) \
Port is set to 443 ( Default: 80 ) \
Use SSL? is checked ( Default: unchecked ) \
Use SNI? is checked ( Default: N/A ) 

Graph Definitions Changes: \
Time Line Type is set to Area ( Default: Line ) \
Size Line Type is set to Area ( Default: Line ) 

Install Instructions: \
Git clone (url) \
cd ZenPacks.zenoss.HttpsMonitor \
python setup.py bdist_egg

ZenPack Installation: \
zenpack --install zenpack --install ZenPacks.zenoss.HttpsMonitor-1.1.0-py2.7.egg \
zopectl restart \
zenhub restart
