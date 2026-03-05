# 测试后端api是否可用

import requests
card_key = ""      #卡密
domain = "https://web.datarisk8.com"

def test_key_api():
    print("测试余额检查接口")
    url = f"{domain}/api/v1/card_key/balance"
    data = {
        "card_key": card_key
    }
    response = requests.post(url, json=data)
    print(response.text)


def test_detect_facebook_risk_api():
    print("测试facebook检测接口：输入手机号或者邮箱，输出是否注册、是否被ban")
    url = f"{domain}/api/v1/detect"
    data = {
        "platform": "facebook",
        "check_type": "risk",
        "phone_numbers": [ "8613900139601","8613800138301","8613922991169"], # 新、老、冻结
        "card_key": card_key
    }
    response = requests.post(url, json=data)
    print(response.text)


def test_detect_facebook_uid_api():
    print("测试facebook检测接口：输入uid，输出是否注册、注册时间")
    url = f"{domain}/api/v1/detect"
    data = {
        "platform": "facebook",
        "check_type": "uid",
        "phone_numbers": ["100024001607849","61571013000001","61587089372111"],
        "card_key": card_key
    }
    response = requests.post(url, json=data)
    print(response.text)

def test_detect_facebook_ck_api():
    print("测试facebook检测接口：输入ck，输出是否存活")
    url = f"{domain}/api/v1/detect"

    ck1 = "c_user=100024001607849; xs=22%3AchxGhLd1CeW6MWBd0qZY7BG5ww" # 有效ck

    ck2 = "c_user=61587089372313; xs=33%3A2AnEEISL0ea2wmZ5f1111Pw;" # 需要人脸验证的ck

    ck3 = "c_user=61587089372111; xs=33%3AAOLLAf72AnEEISL0ea2wmZ5f1111Pw;" # 无效ck


    data = {
        "platform": "facebook",
        "check_type": "ck",
        "phone_numbers": [ck1, ck2, ck3],
        "card_key": card_key
    }
    response = requests.post(url, json=data)
    print(response.text)

def test_detect_ins_isnew_api():
    print("测试instagram检测接口：输入手机号或者邮箱或者昵称，输出是否注册")
    url = f"{domain}/api/v1/detect"
    account_numbers = [
    '8618100138006',  # 原始号码
    '8618100138007',  # 新增号码
    '8618100138008',  # 新增号码
    '8618100138009',  # 新增号码
    '8618100138010',  # 新增号码
    '8618100138011',  # 新增号码
    '61493731470',  # 新增老号码
    '8618100138013',  # 新增号码
    '61493548355',  # 新增老号码
    '8618100138015',  # 新增号码
    '8618100138016',  # 新增号码
]
    data = {
        "platform": "instagram",
        "check_type": "isnew",
        "phone_numbers": account_numbers,
        "card_key": card_key
    }
    response = requests.post(url, json=data)
    print(response.text)

def test_detect_ins_userinfo_byname_api():
    print("测试instagram检测接口：检测账号基本信息：订阅量，发帖量，是否是正式账号等，以及是否被风控。")
    url = f"{domain}/api/v1/detect"
    username_list = [
    "pavitramurthy",
    "vina.ykumar7698__",
    "misrasarvesh3_465",
    "wldrdylhshmy",
    "omnoon516"
]
    data = {
        "platform": "instagram",
        "check_type": "risk",
        "phone_numbers": username_list,
        "card_key": card_key
    }
    response = requests.post(url, json=data)
    print(response.text)


def test_detect_ins_extract_cookies_api():
    print("测试instagram检测接口：输入账号、密码，输出cookie")
    url = f"{domain}/api/v1/detect"

    username_pwd_list = [
    "pavitramurthy;12345678",
    #"vina.ykumar7698;ewyusuis;3279",
    # "misrasarvesh3_46;dui78201a"
    ]
    data = {
        "platform": "instagram",
        "check_type": "extract_cookies",
        "phone_numbers": username_pwd_list, 
        "card_key": card_key
    }
    response = requests.post(url, json=data)
    print(response.text)

def test_detect_wa_isnew_api():
    print("测试whatsapp检测接口：输入手机号，输出是否注册")
    url = f"{domain}/api/v1/detect"
    data = {
        "platform": "whatsapp",
        "check_type": "isnew",
        "phone_numbers": ["8618356960091", "8618356960092", "8613916915997"],
        "card_key": card_key
    }
    response = requests.post(url, json=data)
    print(response.text)


if __name__ == "__main__":  
    # test_key_api()

    # test_detect_facebook_risk_api()
    # test_detect_facebook_uid_api()
    # test_detect_facebook_ck_api()
    # test_detect_ins_isnew_api()
    # test_detect_ins_userinfo_byname_api() 
    # test_detect_ins_extract_cookies_api()
    test_detect_wa_isnew_api()
