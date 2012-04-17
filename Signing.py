#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
    Copyright 2011 timger
    
    +Author timger
    +Gtalk&Email yishenggudou@gmail.com
    +Msn yishenggudou@msn.cn
    +Twitter http://twitter.com/yishenggudou  @yishenggudou
    +Weibo http://t.sina.com/zhanghaibo @timger
    @qiyi
'''

import os
import base64
import time
import hmac

try:
    from hashlib import sha1  # for python2.4     
    from hashlib import sha256 as sha256
  
    if sys.version[:3] == "2.4":
    # we are using an hmac that expects a .new() method.
        class Faker:
            def __init__(self, which):
                 self.which = which
                 self.digest_size = self.which().digest_size
 
             def new(self, *args, **kwargs):
                return self.which(*args, **kwargs)

    sha = Faker(sha)
    sha256 = Faker(sha256)

except:
    import sha as sha1

__author__ = 'timger & yishenggudou@gmail.com'
__license__ = '@qiyi'
__version__ = (0,0,0)


def create_signature(accesskey_id='', accesskey_secret='', header={}, url=''):
    u"""
    accesskey_id:
    accesskey_secret:
    headers:{}
    url:the request url like '/qss/'
    --------------------------------------------------------------------------------------------
    StringToSign =
    HTTP-Verb + "\n" +
    Content-MD5 + "\n" +
    Content-Type + "\n" +
    Date + "\n" +
    CanonicalizedAmzHeaders +
    CanonicalizedResource;
    see detail http://docs.amazonwebservices.com/AmazonS3/latest/dev/RESTAuthentication.html
    其后面描述有很多复杂的签名,为自定义域名和其他复杂使用而准备的，此处只做简单实现
    --------------------------------------------------------------------------------------------
    """

    headers = dict([(i[0].upper(),i[1]) for i in header.copy().items()])
    url = url or headers.get('path'.upper())
    HTTP_Verb = headers.get('HTTP-Verb'.upper(),'')
    Content_Type = headers.get('Content-Type'.upper(),'')
    Content_MD5 = headers.get('Content-MD5'.upper(),'')
    Date = headers.get('Date'.upper(),'')
    CanonicalizedAmzHeaders = ''
    CanonicalizedResource = url
    StringToSign = '\n'.join([HTTP_Verb,Content_Type,Content_MD5,Date,CanonicalizedAmzHeaders+CanonicalizedResource])
    Signature = base64.encodestring(hmac.new(accesskey_secret,StringToSign,sha1).digest()).strip()
    return Signature




