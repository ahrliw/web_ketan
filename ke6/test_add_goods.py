from ke6.login_funtion import login
import requests

def test_add_goods_success():
    """商品添加成功"""
    # step1 登录
    url2 = "http://49.235.92.12:7005/api/v2/goods"
    r = login("test", "123456")
    token = r.json()["token"]
    h = {
        "Authorization": "Token %s"%token
    }
    body = {
               "goodscode": "sp_10088"
            }
    r2 = requests.post(url2, headers=h, json=body)
    print(r2.text)
    # assert r2.json()["code"] == 0


def test_goods_2():
    """session会话管理"""
    s = requests.session()
    print(s.headers)

    r = login("test", "123456")
    token = r.json()["token"]
    h = {
        "Authorization": "Token %s"%token
    }

    # 更新session会话的头部，加token
    s.headers.update(h)

    # s.token = token

    url2 = "http://49.235.92.12:7005/api/v2/goods"
    body = {
               "goodscode": "sp_10088"
            }
    r2 = s.post(url2, json=body)
    print(r2.text)

    # print(s.token)




