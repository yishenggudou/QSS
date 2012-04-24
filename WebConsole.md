###签名Api
+ 数据格式
-----------------------------------------
    In [28]: data={'payload':{}}

    In [29]: data['payload']['url'] = '/haibo/'

    In [30]: data['payload']['secretkey'] = 'A367481FC5752C7805248C5AEDCD1484'

    In [31]: data['payload']['Date'] = '201204241035'

    In [32]: data['payload']['Htto-Verb'] = 'GET'

    In [33]: data['payload']['Http-Verb'] = 'GET'

    In [34]: data['payload']['Content-Type'] = ''

    In [35]: data['payload']['Content-MD5'] = ''

    In [39]: data
    Out[39]: 
    {'payload': {'Content-MD5': '',
      'Content-Type': '',
      'Date': '201204241035',
      'Htto-Verb': 'GET',
      'Http-Verb': 'GET',
      'secretkey': 'A367481FC5752C7805248C5AEDCD1484',
      'url': '/haibo/'}}

    In [40]: 

    In [105]: print requests.post('http://10.11.50.187:9999/web/sign/',data={'payload':json.dumps({'headers':data['payload']})}).content
    {"signature": "a7OyytGJnirO5KZxDFmUBNm7hME="}

    In [106]: print requests.get('http://10.11.50.187:9999/web/sign/',params={'payload':json.dumps({'headers':data['payload']})}).content
    {"signature": "a7OyytGJnirO5KZxDFmUBNm7hME="}
-----------------------------------------



