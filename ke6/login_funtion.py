import requests

def login(username="test", password="123456"):
    url = "http://49.235.92.12:7005/api/v1/login"

    body = {
        "username": username,
        "password": password
        }
    response = requests.post(url, json=body)
    print(response.text)
    return response

if __name__ == '__main__':
    # 调试的代码，自测
    r = login("test", "123456")
    print(r)   # <Response [200]>
    print(r.json()["token"])