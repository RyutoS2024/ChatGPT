import requests
import json

# APIキーの設定
openai_api_key = ''  # 実際のAPIキーに置き換える

# ヘッダーの設定
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {openai_api_key}'
}

# リクエストボディの設定
data = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Say this is a test!"}],
    "temperature": 0.7
}

# APIリクエストの実行
response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, data=json.dumps(data))

# レスポンスの確認
print(response.text)
