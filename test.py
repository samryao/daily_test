import requests

if __name__ == '__main__':
    headers = {
        'Accept': 'application/vnd.apache.kylin-v2+json',
               'Content-Type': 'application/json;charset=utf-8',
               'authorization': 'Basic eXpkeHgwMDE6WXVtMTIzITE='
    }
    data = '{ "sql":"select count(*) from DWBI01.KY_KFC_CUBE_FACTCASH WHERE bizdate =\'2020-01-02\' ", "project":"KFC_CUBE" }'
    # print(data)
    url = "http://172.25.201.180:7170/kylin/api/query"
    # print(headers)
    response = requests.post(url=url, headers=headers, data=data)
    print(response)

