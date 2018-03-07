'''
url编码解码
例子：%E6%B5%8B%E8%AF%95
'''
from urllib import parse
s = '测试'
s1 = parse.quote(s)
print(s1)
s2 = parse.unquote(s1)
print(s2)
#js:URLEncode()



'''
base64
最常见的编码
'''
import base64
s = '测试'
s1 = base64.encodebytes(s.encode())
print(s1)
s2 = base64.decodebytes(s1).decode()
print(s2)


'''
MD5(摘要算法)

'''