from httpx import Client



with Client(base_url='https://httpbin.org') as client:
    response = client.get('/get')

    print(response.json())
    print()
    print(response.text)
    print()
    print(response.content)
    print()

    # response2 = client.post('https://httpbin.org/post')

    # print(response2.text)
    # print()
    # print(response2.headers)
    # print()
    # print(response2.cookies)

    response2 = client.get(
        '/redirect/10',
        follow_redirects= True
    )

    print(response2.history)
