import requests
import json


def send_request_to_login():
    url = "https://gw.l004-stg.com/api/v2/auth/login"

    payload = json.dumps({
      "username": "taystg001",
      "password": "123456789aA"
    })
    headers = {
      'accept': 'application/json, text/plain, */*',
      'accept-language': 'en-US,en;q=0.9',
      'content-type': 'application/json',
      'origin': 'https://fe.l004-stg.com',
      'referer': 'https://fe.l004-stg.com/',
      'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"macOS"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-site',
      'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response




if __name__ == '__main__':
  response = send_request_to_login()
  print(response.status_code)
  print(response.content)

