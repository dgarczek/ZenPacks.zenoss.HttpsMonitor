# ZenPacks.zenoss.HttpsMonitor
HTTPS Monitor Zenpack for Zenoss Core 4.x

This ZenPack is an extended version of the stock HttpMonitor and supports polling websites that require Server Name Indication (SNI). SNI is an extension to TLS that allows multiple SSL/TLS certificates on a single IP address.

Although the Nagios Plugin check_http supports SNI, the user cannot enable SNI within the Zenoss Dashboard by default.

We can run check_http tests on the command line to better understand the request parameters that Zenoss needs to handle in order to successfully poll websites requiring SNI. In the example below, we try polling a website that requires the client to specify an SNI name during the SSL/TLS negotiation. Note: www.mywebsite.com is not an actual website requiring SNI, just an example.

Without SNI: \
/usr/lib64/nagios/plugins/check_http -H www.mywebsite.com --onredirect=follow --ssl \
CRITICAL - Cannot make SSL connection.

With SNI: \
/usr/lib64/nagios/plugins/check_http -H www.mywebsite.com --onredirect=follow --ssl --sni \
HTTP OK: HTTP/1.1 200 OK - 316717 bytes in 0.980 second response time |time=0.980466s;;;0.000000 size=316717B;;;0 \ 

Notice the extra --sni option.\\

This HttpsMonitor ZenPack allows the user to put a "check" next to UseSSL? and UseSNI? in the HttpsMonitor Data Source. Zenoss then generates the check_http command with all required options.

Some changes I made to the default settings. Adjust to suit your needs.

Configuration Properties Changes: \
zPingMonitorIgnore is set to True ( Default: False)

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
zenpack --install ZenPacks.zenoss.HttpsMonitor-1.1.0-py2.7.egg \
zopectl restart \
zenhub restart
