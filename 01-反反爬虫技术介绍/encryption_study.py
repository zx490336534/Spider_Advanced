#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Terry'


'''
    任何加密都是针对的bytes： b'\xB3\X3B'


    URL编码解码：
    用于url的参数提交
    中文、特殊字符 转换为 %B3%3B%53。。。。。。
'''
# from urllib import parse
# s = '测试url编码=%@#$%^&*()'
# # 默认编码为UTF-8
# s1 = parse.quote(s) # 编码
# print(s1)
# s2 = parse.unquote(s1) # 解码
# print(s2)
# 对一个的js，是 URLEncode()

'''
    base64：
    是网络上最常见的用于传输8Bit字节码的编码方式之一，
    Base64就是一种基于64个可打印字符来表示二进制数据的方法，用于在HTTP环境下传递较长的标识信息
    后一两位可能有“=”
    防君子不防小人，很容易解密

    输出为 A-Z、a-z、0-9和"+"、"/" 字符组成的字符串
    很多时候字符串尾部为 1个或2个  "="
    把3个字节的二进制拼接， 24位， 按6位分割，变成4个字节，每个字节小于64
    最后留下1个字节的时候，会在尾部添加 2个 '='
    最后留下2个字节的时候，会在尾部添加 1个 '='
'''

# import base64
# s = '测试base12'

# #  会按57个字节的长度为间隔 加入 \n
# s1 = base64.encodebytes(s.encode())
# print(s1)
# s3 = base64.decodebytes(s1).decode()
# print(s3)
#
# 最常用的base64 加密，可以自定义替换 + 和 /
# s2 = base64.b64encode(s.encode())
# print(s2)
# s4 = base64.b64decode(s2).decode()
# print(s4)

# # 标准base64加密，等同于不带额外参数的 b64encode
# s5 = base64.standard_b64encode(s.encode())
# print(s5)
# s6 = base64.standard_b64decode(s5)
# print(s6.decode())

# url安全的，会把 + 替换为 - ， 把 / 替换为 _
# 等同于 base64.b64encode(s.encode(), b'-_') base64.b64decode(s2, b'-_')
# s7 = base64.urlsafe_b64encode(s.encode())
# print(s7)
# s8 = base64.urlsafe_b64decode(s7)
# print(s8.decode())


'''
    MD5:
    Message-Digest Algorithm 5（摘要算法5）
    1、压缩性：任意长度的数据，算出的MD5值长度都是固定的。
    2、容易计算：从原数据计算出MD5值很容易。
    3、抗修改性：对原数据进行任何改动，哪怕只修改1个字节，所得到的MD5值都有很大区别。
    4、强抗碰撞：已知原数据和其MD5值，想找到一个具有相同MD5值的数据（即伪造数据）是非常困难的。

    输出为 128 bit，  每4位二进制组合一个十六进制字符，一般输出为 长度 32 个16进制字符串
'''

# import hashlib
#
# s = 'this is a md5 test.'
# m = hashlib.md5()
# m.update(s.encode())
# print(m.hexdigest())

# # 一般的简便写法
# print(hashlib.md5(s.encode()).hexdigest())


'''
    DES:
    全称为Data Encryption Standard，即数据加密标准，是一种使用密钥加密的块算法
    入口参数有三个：Key、Data、Mode
    Key为7个字节共56位，是DES算法的工作密钥；
    Data为8个字节64位，是要被加密或被解密的数据；
    Mode为DES的工作方式,有两种:加密或解密

    3DES（即Triple DES）是DES向AES过渡的加密算法，
    使用两个密钥，执行三次DES算法，
    加密的过程是加密-解密-加密
    解密的过程是解密-加密-解密

    pycrypto安装指南：帮助文档（https://www.dlitz.net/software/pycrypto/api/current/）
    要先安装VC2015：microsoft visual studio 2015(14)
    1、http://blog.csdn.net/a624806998/article/details/78596543
        在执行 python setup.py install 之前，运行
        set CL=/FI"%VCINSTALLDIR%\\INCLUDE\\stdint.h" %CL%
    2、出现ImportError: No module named 'winrandom'错误
        处理：修改python3安装目录下的 lib/Crypto/Random/OSRNG/nt.py 文件中找到
        import winrandom
        修改为
        from Crypto.Random.OSRNG import winrandom
'''

# # DES 加密
# from Crypto.Cipher import DES
# from Crypto.Util import Counter
# from Crypto import Random
# import binascii
#
# key = '-8B key-' # 长度为8
# msg = 'We are no longer the knights who say ni!'
# nonce = Random.new().read(int(DES.block_size/2))
#
# def des_encrypt(key, msg):
#     ctr = Counter.new(int(DES.block_size*8/2), prefix=nonce)
#     cipher = DES.new(key, DES.MODE_CTR, counter=ctr)
#     msg = nonce + cipher.encrypt(msg)
#     msg = binascii.b2a_hex(msg)
#     return msg.decode()
#
# print(des_encrypt(key.encode(), msg.encode()))

# 3DES 加密
# from Crypto.Cipher import DES3
# from Crypto import Random
# import binascii
#
# key = 'Sixteen byte key'
# msg = 'sona si latine loqueris '
# iv = Random.new().read(DES3.block_size)
# print(iv)
# def des3_encrypt(key, msg):
#     cipher = DES3.new(key, DES3.MODE_OFB, iv)
#     msg = iv + cipher.encrypt(msg)
#     msg = binascii.b2a_hex(msg)
#     return msg.decode()
#
# s = des3_encrypt(key.encode(), msg.encode())
# print(s)

'''
    AES：
    高级加密标准（英语：Advanced Encryption Standard，缩写：AES），这个标准用来替代原先的DES
    AES的区块长度固定为128 比特，密钥长度则可以是128，192或256比特 （16、24和32字节）
    大致步骤如下：
    1、密钥扩展（KeyExpansion），
    2、初始轮（Initial Round），
    3、重复轮（Rounds），每一轮又包括：SubBytes、ShiftRows、MixColumns、AddRoundKey，
    4、最终轮（Final Round），最终轮没有MixColumns。
'''

# from Crypto.Cipher import AES
# from Crypto import Random
# import binascii
#
# # 加密
# key = b'Sixteen byte key'
# msg = b'Attack at dawn'
# iv = Random.new().read(AES.block_size) # 16字节长度
# cipher = AES.new(key, AES.MODE_CFB, iv)
# msg = iv + cipher.encrypt(msg)
# print(binascii.b2a_hex(msg))
#
# # 解密
# cipher = AES.new(key, AES.MODE_CFB, iv)
# msg1 = cipher.decrypt(msg)
# print(msg1[16:])

'''
    RSA:
    公钥加密算法，一种非对称密码算法
    公钥加密，私钥解密

    3个参数：
    rsa_n， rsa_e，message
    rsa_n, rsa_e  用于生成公钥
    message： 需要加密的消息
'''
# import rsa
# import binascii
#
# def rsa_encrypt(rsa_n, rsa_e, message):
#     key = rsa.PublicKey(rsa_n, rsa_e)  # 创建公钥
#     message = rsa.encrypt(message, key)  # 加密
#     message = binascii.b2a_hex(message)  # 将加密信息转换为16进制
#     return message.decode()
# #
# pubkey='EB2A38568661887FA180BDDB5CABD5F21C7BFD59C090CB2D245A87AC253062882729293E5506350508E7F9AA3BB77F4333231490F915F6D63C55FE2F08A49B353F444AD3993CACC02DB784ABBB8E42A9B1BBFFFB38BE18D78E87A0E41B9B8F73A928EE0CCEE1F6739884B9777E4FE9E88A1BBE495927AC4A799B3181D6442443'
# print("pubkey length：%s"  % len(pubkey))
# rsa_n = int(pubkey, 16)
# rsa_e = int('10001', 16) # js里面一般是 parseInt('10001', 16)
# s = '需要加密的字符串'
# print(rsa_encrypt(rsa_n, rsa_e, s.encode()))
# print(len(rsa_encrypt(rsa_n, rsa_e, s.encode())))


'''
    还要很多网站有自定义的加密算法，不是通用的算法，处理方式：
    1、破解js，写对应的python算法。优点：执行快，缺点：复杂，难度高，有可能随时需要更新
    2、selenium 进行浏览器模拟
    3、pyV8，下载这个JS，用pyV8调用这个js的方法

    有一些参数很复杂，但是你可以尝试不提交，就是提交 ""，是有可能通过的
'''
