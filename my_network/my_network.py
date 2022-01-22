import json

import requests


def main():
    # j = {
    #     'employee': [
    #         {'id': 111, 'name': 'Mike'},
    #         {'id': 222, 'name': 'Nancy'}
    #     ]
    # }
    # print(j)
    # print('############')
    # print(json.dumps(j))
    #
    # with open('output/test.json', 'w') as f:
    #     json.dump(j, f)
    #
    # print('############')
    # with open('output/test.json', 'r') as f:
    #     print(json.load(f))

    payload = {'key1': 1, 'key2': 2}
    # r = requests.get('http://httpbin.org/get', params=payload)
    # r = requests.post('http://httpbin.org/post', data=payload)
    # r = requests.put('http://httpbin.org/put', data=payload)
    # r = requests.delete('http://httpbin.org/delete', data=payload)

    r = requests.get('http://httpbin.org/get', params=payload, timeout=0.01)
    print(r.status_code)
    print(r.text)
    print(r.json())
