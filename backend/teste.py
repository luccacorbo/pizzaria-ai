import requests

headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjUsImV4cCI6MTc3MjQ3ODYxMX0.jSCwpRTPEJYDh6Gp07eHFsGVQvW62gas91r4C31bWfQ"
}

requisicao = requests.get('http://127.0.0.1:8000/auth/refresh', headers=headers)
print(requisicao)

print(requisicao.json())