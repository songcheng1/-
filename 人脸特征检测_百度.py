
import requests
import json

API_KEY = "xxxxxx"
SECRET_KEY = "xxxxxx"


def main():
    url = "https://aip.baidubce.com/rest/2.0/face/v1/landmark?access_token=" + get_access_token()

    # image 可以通过 get_file_content_as_base64("C:\fakepath\part.jpg",False) 方法获取
    payload = json.dumps({
        "image": "https://ns-strategy.cdn.bcebos.com/ns-strategy/upload/fc_big_pic/part-00764-2257.jpg",
        "image_type": "URL",
        "max_face_num": "1"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))


if __name__ == '__main__':
    main()
