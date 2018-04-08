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
    	Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cache-Control: max-age=0
Connection: keep-alive
Cookie: ll="118172"; bid=pNb-tilKHGo; gr_user_id=bcb86895-719b-4a8f-91de-e923bc31bf25; __yadk_uid=j7AukO9dfGxMyPj3B84egHnziLjk37Db; _vwo_uuid_v2=DFF85F209BFA09280545204792E54229|7c9fe8bd07c67511ab8950ba7362dcbf; UM_distinctid=1629ab30fe6317-0266efee2ef2ce-b34356b-1fa400-1629ab30fe74cc; __utmz=81379588.1523013852.3.3.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmc=30149280; __utma=81379588.840243717.1510755424.1523016391.1523066997.5; __utmc=81379588; _pk_ref.100001.3ac3=%5B%22%22%2C%22%22%2C1523066997%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.3ac3=*; gr_cs1_b727a2e9-e6e8-4646-8ff9-feacc7ec8419=user_id%3A0; CNZZDATA1272964020=1133262041-1523013203-https%253A%252F%252Fwww.douban.com%252F%7C1523067061; viewed="25862578_26892808_1400705_27154065"; ps=y; __utma=30149280.1863945187.1510151677.1523066997.1523067730.10; __utmz=30149280.1523067730.10.9.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; __utmt_douban=1; push_noty_num=0; push_doumail_num=0; dbcl2="78608593:7tzsR3/IJ38"; ck=LzfU; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03=3dbd8d46-202c-4f79-b852-f2ee398bc84f; gr_cs1_3dbd8d46-202c-4f79-b852-f2ee398bc84f=user_id%3A1; __utmb=30149280.9.10.1523067730; __utmb=81379588.17.10.1523066997; _pk_id.100001.3ac3=e403aeab4497a81b.1510755425.5.1523067821.1523017536.; ap=1
Host: book.douban.com
Referer: https://www.douban.com/accounts/login?redir=https://book.douban.com/subject/25862578/&source=None&login_type=sms
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'''
    print_dict_from_copy_headers(text)


