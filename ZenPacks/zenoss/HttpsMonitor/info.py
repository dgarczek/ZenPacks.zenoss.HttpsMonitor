##############################################################################
# 
# Copyright (C) Zenoss, Inc. 2010, all rights reserved.
# 
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
# 
##############################################################################


from zope.interface import implements
from zope.schema.vocabulary import SimpleVocabulary
from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.template import RRDDataSourceInfo
from ZenPacks.zenoss.HttpsMonitor.interfaces import IHttpsMonitorDataSourceInfo
from ZenPacks.zenoss.HttpsMonitor.datasources.HttpsMonitorDataSource import HttpsMonitorDataSource

def httpsMonitorRedirectVocabulary(context):
    return SimpleVocabulary.fromValues(HttpsMonitorDataSource.onRedirectOptions)


class HttpsMonitorDataSourceInfo(RRDDataSourceInfo):
    implements(IHttpsMonitorDataSourceInfo)
    timeout = ProxyProperty('timeout')
    cycletime = ProxyProperty('cycletime')
    hostname = ProxyProperty('hostname')
    ipAddress = ProxyProperty('ipAddress')
    port = ProxyProperty('port')
    url = ProxyProperty('url')
    regex = ProxyProperty('regex')
    basicAuthUser = ProxyProperty('basicAuthUser')
    basicAuthPass = ProxyProperty('basicAuthPass')
    onRedirect = ProxyProperty('onRedirect')
    useSsl = ProxyProperty('useSsl')
    useSni = ProxyProperty('useSni')
    caseSensitive = ProxyProperty('caseSensitive')
    invert = ProxyProperty('invert')
    proxyAuthUser = ProxyProperty('proxyAuthUser')
    proxyAuthPassword = ProxyProperty('proxyAuthPassword')
    
    @property
    def testable(self):
        """
        We can NOT test this datsource against a specific device
        """
        return False
