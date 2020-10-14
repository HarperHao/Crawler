from urllib import request, parse
import time, json, random, hashlib

content = input("请输入要翻译的内容：")
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
data = {}
u = 'fanyideskweb'
d = content
f = str(int(time.time() * 1000) + random.randint(1, 10))
c = 'rY0D^0\'nM0}g5Mm1z%1G4'
sign = hashlib.md5((u + d + f + c).encode('utf-8')).hexdigest()
data['i'] = content
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = f
data['sign'] = sign
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_REALTlME'
data['typoResult'] = 'true'

data = parse.urlencode(data).encode('utf-8')
req = request.Request(url, data=data)
response = request.urlopen(req)

res = response.read().decode('utf-8')
res = json.loads(res)
res = res["translateResult"]
# print(res)
print('result:', res[0][0]['tgt'])
