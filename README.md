# ZenPacks.zenoss.HttpsMonitor
HTTPS Monitor Zenpack for Zenoss Core 4.x

This ZenPack is an extended version of the stock HttpMonitor and supports polling websites that require Server Name Indication (SNI) extension in the request.

It is configured based on the manual check_http Nagios Plugin request:

/usr/lib64/nagios/plugins/check_http -H www.mywebsite.com --onredirect=follow --ssl --sni



