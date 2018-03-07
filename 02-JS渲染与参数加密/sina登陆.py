'''
1、进行正常功能的抓包（尽量要清理缓存，ctrl+F5强制刷新）
2、分析包
3、登录页面
https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.19)
登陆页post提交的参数关注点如下：
su：base64加密的字符串，通过分析得知，是由登陆账号进行base64得出
servertime：时间戳
nonce：未知
rsakv：未知
sp:猜测可能是密码进行ras加密后的参数
4、去寻找rsa加密的2个关键的key
5、在chrome浏览器中，F12打开调试窗口，如果选择一个js文件，然后找到event listener breakpoints，勾选mouse下的click事件
6、凡是赋值的代码行，都直接F10跳过就好，只有函数调用的地方，F11跟踪进入
7、注意window.postMessage
https://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=&rsakt=mod&client=ssologin.js(v1.4.19)&_=1518006926762

注意事项：
1、一定要记得清缓存
2、基本加密过的参数，都是需要关注的，实在破解不了，可以尝试提交空
3、浏览器端的加密，都不是针对客户端（即用户端），都是针对的传输过程，包括https
4、判断一个参数是否加密得来的，就是在这个抓包中进行查找，如果找到对应的response传到客户端的，那么就去访问对应的response请求得到这个参数
如果没有找到对应的response的传输，那么大概率就是js生成的，需要去调试js获取加密方法
5、不管get方法还是post方法，其实都是提交一些参数到服务器，请求一些资源
这两种方法，服务器都可能在response中传递一些关键的参数给客户端，用于之后的数据请求
这个之后的数据请求，有可能是post也有可能是get
'''

from urllib import parse
import base64
import rsa
import binascii
def user_encrypt(user):
    user = parse.quote(user)
    user = base64.b64encode(user.encode())
    return user.decode()

def rsa_encrypt(message,rsa_n,rsa_e='10001'):
    rsa_e = int(rsa_e,16)
    rsa_n = int(rsa_n,16)
    key = rsa.PublicKey(rsa_n,rsa_e)
    message = rsa.encrypt(message,key)
    message = binascii.b2a_hex(message)
    return message.decode()
def get_pwd(servertime,nonce,pwd):
    return servertime+'\t'+nonce+'\n'+pwd

if __name__ == '__main__':
    pwd = 'zx490336534'
    print(user_encrypt('15168230644'))
    servertime = 10
    nonce = ''
    rsa_n = ''
    rsa_e = '10001'
    pwd_encrypt = rsa_encrypt(get_pwd(servertime,nonce,pwd),rsa_n,rsa_e)