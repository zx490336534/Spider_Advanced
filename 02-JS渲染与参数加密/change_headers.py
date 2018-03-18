from urllib.parse import parse_qsl

def print_headers_raw_to_dict(headers_raw_l):
    print("{\n    '" + ",\n    ".join(map(lambda s: "'" +
        "': '".join(s.strip().split(': ')) + "'", headers_raw_l))[1:-1] + "'\n}")

def print_headers_raw_to_dict_space(headers_raw_l):
    print("{\n    '" + ",\n    ".join(map(lambda s: "'" + "': '".join(s.strip().split('\t')) + "'", headers_raw_l))[1:-1] + "'\n}")

def print_dict_from_copy_headers(headers_raw):
    headers_raw = headers_raw.strip()
    headers_raw_l = headers_raw.splitlines()

    if 'HTTP/1.1' in headers_raw_l[0]:
        headers_raw_l.pop(0)
    if headers_raw_l[0].startswith('Host'):
        headers_raw_l.pop(0)
    if headers_raw_l[-1].startswith('Cookie'):
        headers_raw_l.pop(-1)

    if ':' in headers_raw_l[0]:
        print_headers_raw_to_dict(headers_raw_l)
    else:
        print_headers_raw_to_dict_space(headers_raw_l)

def print_url_params(url_params):
    s = str(parse_qsl(url_params.strip(), 1))
    print("OrderedDict(\n    " + "),\n    ".join(map(lambda s: s.strip(), s.split("),")))[1:-1] + ",\n)")


if __name__ == '__main__':
    text='''
    	staticpage	https://www.baidu.com/cache/user/html/v3Jump.html
charset	UTF-8
token	a6e8d1f982edb13d2089267d40b05134
tpl	mn
subpro	
apiver	v3
tt	1521204077122
codestring	
safeflg	0
u	https://www.baidu.com/
isPhone	false
detect	1
gid	EEB1251-BFF1-4901-B6B4-F302BCEBBC7E
quick_user	0
logintype	dialogLogin
logLoginType	pc_loginDialog
idc	
loginmerge	true
splogin	rate
username	490336534
password	QwgZ4U2M6BRKnchQ3Ombs+Gyk2if7MC40ak7WB++HjArhmJvVWMrgzQf/wrh7gvdxSzykDhIFzOc82y6CGWBuqMRYHVZFy+uLXPtlwfWuEHW3eXh+oNEjgqdC+DOpTtrh0nX6slHUGH9hNpd7Cu57sv5qCi8Ls8xlKFaRv5CygY=
mem_pass	on
rsakey	K5jfYdYXuNx7sFY1wWRVsXsDusbkZ71x
crypttype	12
ppui_logintime	6188
countrycode	
fp_uid	7640c01633d892cd899a345681f9e0fb
fp_info	7640c01633d892cd899a345681f9e0fb002~~~gxggpJnz2WyFvVp_kggGAnwvXlUv10jvm0znnwvXlUv10jvmBzvgl0sagl0srggsSglqqCn0VgbnzPo1xz4kBzvV9zokbx4XCwbnjV4lvV4XtNoVtxvXZxYlSVoXGM4XtVvmlxYybUokBNoXZN4XywbWzP6-3RbW9_IkgtykgtHkgtRkgsMn0vl9nhU5n3~In2ZIWodIr2F5Z6gb-df5qj3I-3~In2V2Wyl676eI-2RcroyIJoybW6gbJsRG7y~GroOIW6p2ZdvG72lcrEg5-yl6rhkIWxM6rxMu~fW678VcrhF4kZFoqSxukZzoVte-n0dA6n2-G72R51xkIWdD5rxeGW3McrhFbNx~vktMv-Ck4X8l4mBVvn9joVBSonCfvXBW6kyl6-BVvm9jvnZNGVtSvk8yGrBWvmlzvktUG-vd4XZNvn9UvV2-Y-GVvX0V6kZS6nGM6n9x6nBUG-BVvX0MGX6-4nBS6XZWvnZVoWGjGr9M6nZzokyf4mvU6mlzo-ok4m2l6Xo~4X5w6n2-G72R51xkIWdD5rxeGW3McrhFbNSM6rZSomfl6rvMok9zGX0Wv-ZzGklVvV8l4m3yvWvjoWoy6mZMoktd4r9MoV3lvnpj4n3fvXo-om2-oXvWorClYk9W6rZWGVof4m2y6XlzGrBMokbjoVZW6mGNGkfy4r9MomZxo-Cy6-6k6kbWvn9U6mbSGk6~oVCy4r8-4mlSvW9_Kkgs~kgstkgswkgsFggpEnzQ-0DBMS_znw5rxOI-hNI0__gkgsLggtVkgtOkgtjkgtZkgthkgtfnvuXZFompjomBS4mpV4mbMoVpMoB__
loginversion	v4
dv	tk0.08641891848382711521204071086@sun0ol9m~-8kMY8kIb8k6d8k6b8k3z8k2~7t~-7UEf9B6a8k2bCt~Y9UMf9U9d8knzCm~YCknf9U6S8knbCm~S9kJf9Snx8k9d9m~S7S6_sn0vC7k3f9m-JEJb0J3u7KdOEJdhG9BhGKzhQIz7zPz538kEb7UIf9SILGkJY8kqfr2uCod5hBrOGJu7EKS2~KdO~MK7SNaOY4m~d9kEb8k9zC0~d9m~~8uohB3NtEJdGKdhBJuw-9uOGIsuSIzNjIVEf7Bna9Y~S7SQw7B2f9m-JEJb0J3u7KdOEJdhG9BhGKzhQIz7zPz538kJS9B2f9SILGkJS8kqfr2uCod5hBrOGJu7EKS2~KdO~MK7SNaOY4m~d7kqz8k9zC0~_rn0or7BE-8kJYCm~b7BEf8k2L7W~x9BIf7kEd8k2zCk6f8k9d90~S7Uqf7BE~8kna7BMfIsuSIYd~DsOZPVZL8H-j4aZe8k9zC0~SCk6f9UJa8k9b9UEfr2uCod5hBrOGJu7EKS2~KdOdIarYBVug4t~S7SQw7kn-8k9z71~d7UEY8uohB3NtEJdGKdhBJuw-9uOGIzr1PHZx8k9zC0~_Cll4wlIWglcDhInh9t~Y8kMd-npNsf~8UqL7UE-Ck3-CkEL9S6Y7S2-7Bn-9Uqx9kI-9k6ahnpD0oxI09F8YOzNzIeMVuT40JeMaOg8Y-dPVoZ4VZe4HE_Fnv9Uqd8kM-71~L7Uqf7U6L8k2b9Uqf9BqL9m~-CBn~8k6z71~zCk2_
traceid	DD618F01
callback	parent.bd__pcbs__jfkibx'''
    print_dict_from_copy_headers(text)


