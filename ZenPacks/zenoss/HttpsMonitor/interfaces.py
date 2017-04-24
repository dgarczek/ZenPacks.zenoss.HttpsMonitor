##############################################################################
# 
# Copyright (C) Zenoss, Inc. 2010, all rights reserved.
# 
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
# 
##############################################################################


from Products.Zuul.interfaces import IRRDDataSourceInfo
from Products.Zuul.form import schema
from Products.Zuul.utils import ZuulMessageFactory as _t


class IHttpsMonitorDataSourceInfo(IRRDDataSourceInfo):
    timeout = schema.Int(title=_t(u'Timeout (seconds)'))
    cycletime = schema.Int(title=_t(u'Cycle Time (seconds)'))
    hostname = schema.TextLine(title=_t(u'Host Name'), group=_t('HTTPS Monitor'))
    port = schema.Int(title=_t(u'Port'), group=_t('HTTPS Monitor'))
    ipAddress = schema.TextLine(title=_t(u'IP Address or Proxy Address'), group=_t('HTTPS Monitor'))
    url = schema.TextLine(title=_t(u'URL'), group=_t('HTTPS Monitor'))
    regex = schema.TextLine(title=_t(u'Regular Expression'), group=_t('HTTPS Monitor'))
    basicAuthUser = schema.TextLine(title=_t(u'Basic Auth User'), group=_t('HTTPS Monitor'))
    basicAuthPass = schema.Password(title=_t(u'Basic Auth Password'), group=_t('HTTPS Monitor'))
    onRedirect = schema.Choice(title=_t(u'Redirect Behavior'),
                             vocabulary='httpsMonitorRedirectVocabulary', group=_t('HTTPS Monitor'))
    useSsl = schema.Bool(title=_t(u'Use SSL?'), group=_t('HTTPS Monitor'))
    useSni = schema.Bool(title=_t(u'Use SNI?'), group=_t('HTTPS Monitor'))
    caseSensitive = schema.Bool(title=_t(u'Case Sensitive'), group=_t('HTTPS Monitor'))
    invert = schema.Bool(title=_t(u'Invert Expression'), group=_t('HTTPS Monitor'))
    proxyAuthUser = schema.TextLine(title=_t(u'Proxy User'), group=_t('Proxy Credentials'))
    proxyAuthPassword = schema.Password(title=_t(u'Proxy Password'), group=_t('Proxy Credentials'))
