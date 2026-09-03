import httpx

response = httpx.get('https://httpbin.org/get')
response2 = httpx.post('https://httpbin.org/post')

print(response.json())
print(response.text)
print(response.content)

print(response2.headers)
print(response2.cookies)
print(response2.status_code)