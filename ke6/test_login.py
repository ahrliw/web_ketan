import requests


def test_login_success_1():
    url = "http://49.235.92.12:7005/api/v1/login"

    body = {
        "username": "test",
        "password": "123456"
        }
    r = requests.post(url, json=body)
    print(r.text)
    print(r.json())
    assert r.json()["code"] == 0
    assert r.json()["msg"] == "login success!"
    assert len(r.json()["token"]) == 40


def test_login_fail_2():
    url = "http://49.235.92.12:7005/api/v1/login"

    body = {
        "username": "testxxwww",
        "password": "123456"
        }
    r = requests.post(url, json=body)
    print(r.text)
    print(r.json())
    assert r.json()["code"] == 3003
    assert r.json()["msg"] == "账号或密码不正确"
    assert len(r.json()["token"]) == 0


def test_login_fail_3():
    url = "http://49.235.92.12:7005/api/v1/login"

    body = {
        "username": "test1",
        "password": "123456xx"
        }
    r = requests.post(url, json=body)
    print(r.text)
    print(r.json())
    assert r.json()["code"] == 3003
    assert r.json()["msg"] == "账号或密码不正确"
    assert len(r.json()["token"]) == 0

    


