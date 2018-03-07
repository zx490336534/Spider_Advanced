# -*- coding: utf-8 -*-
import hashlib
#import http.client
#import urllib.request
import urllib2
import urllib
import json
import base64
import user1

def md5str(str): #md5加密字符串
		m=hashlib.md5(str.encode(encoding = "utf-8"))
		return m.hexdigest()
		
def md5(byte): #md5加密byte
		return hashlib.md5(byte).hexdigest()
		
class DamatuApi():
	
	ID = '49755'
	KEY = '39b98d2cfe4aaa039c239b98254aadc1'
	HOST = 'http://api.dama2.com:7766/app/'

	def __init__(self,username,password):
		self.username=username
		self.password=password
		
	def getSign(self,param=b''):
		return (md5(bytes(self.KEY) + bytes(self.username) + param))[:8]
		
	def getPwd(self):
		return md5str(self.KEY +md5str(md5str(self.username) + md5str(self.password)))
		
	def post(self,path,params={}):
		data = urllib.urlencode(params).encode('utf-8')
		url = self.HOST + path
		response = urllib2.Request(url,data)
		return urllib2.urlopen(response).read()
	
	#查询余额 return 是正数为余额 如果为负数 则为错误码
	def getBalance(self):
		data={'appID':self.ID,
			'user':self.username,
			'pwd':dmt.getPwd(),
			'sign':dmt.getSign()
		}
		res = self.post('d2Balance',data)
		res = str(res)
		jres = json.loads(res)
		if jres['ret'] == 0:
			return jres['balance']
		else:
			return jres['ret']
    
	#上传验证码 参数filePath 验证码图片路径 如d:/1.jpg type是类型，查看http://wiki.dama2.com/index.php?n=ApiDoc.Pricedesc  return 是答案为成功 如果为负数 则为错误码
	def decode(self,filePath,type):
		f=open(filePath,'rb')
		fdata=f.read()
		filedata=base64.b64encode(fdata)
		f.close()
		data={'appID':self.ID,
			'user':self.username,
			'pwd':dmt.getPwd(),
			'type':type,
			'fileDataBase64':filedata,
			'sign':dmt.getSign(fdata)
		}		
		res = self.post('d2File',data)
		res = str(res)
		jres = json.loads(res)
		if jres['ret'] == 0:
			#注意这个json里面有ret，id，result，cookie，根据自己的需要获取
			return(jres['result'])
		else:
			return jres['ret']
		
	#url地址打码 参数 url地址  type是类型(类型查看http://wiki.dama2.com/index.php?n=ApiDoc.Pricedesc) return 是答案为成功 如果为负数 则为错误码
	def decodeUrl(self,url,type):
		data={'appID':self.ID,
			'user':self.username,
			'pwd':dmt.getPwd(),
			'type':type,
			'url':urllib.quote(url),
			'sign':dmt.getSign(url.encode(encoding = "utf-8"))
		}
		res = self.post('d2Url',data)
		res = str(res)
		jres = json.loads(res)
		if jres['ret'] == 0:
			#注意这个json里面有ret，id，result，cookie，根据自己的需要获取
			return(jres['result'])
		else:
			return jres['ret']
	
	#报错 参数id(string类型)由上传打码函数的结果获得 return 0为成功 其他见错误码
	def reportError(self,id):
		#f=open('0349.bmp','rb')
		#fdata=f.read()
		#print(md5(fdata))
		data={'appID':self.ID,
			'user':self.username,
			'pwd':dmt.getPwd(),
			'id':id,
			'sign':dmt.getSign(id.encode(encoding = "utf-8"))
		}	
		res = self.post('d2ReportError',data)
		res = str(res, encoding = "utf-8")
		jres = json.loads(res)
		return jres['ret']

		
#调用类型实例：
#1.实例化类型 参数是打码兔用户账号和密码	
dmt=DamatuApi(user1.user,user1.pwd)
#2.调用方法：
#print(dmt.getBalance()) #查询余额
#code = dmt.decode('code/code.png',287) #上传打码,第二个参数为验证码类型
#print(dmt.decodeUrl('http://captcha.qq.com/getimage?aid=549000912&r=0.7257105156128585&uin=3056517021',200)) #上传打码
#print(dmt.reportError('894657096')) #上报错误
def calcCode():
	code = dmt.decode('code/code.png',287)
	#print code
	code = code.replace('|',',')
	code = code.split(',')
	x_list = code[0::2]
	y_list = code[1::2]
	s = ''
	for i in zip(x_list,y_list):
		y = int(i[1]) - 30
		s += '%s,%s,' %(i[0],y)
		#1,2,3,4
	return s[:-1]