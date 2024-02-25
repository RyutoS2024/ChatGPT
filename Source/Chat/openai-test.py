from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "あなたはダイエットの知識が豊富なアシスタントです"
    },
    {
      "role": "user",
      "content": "これからお昼ご飯を食べようと思います。ダイエットに適したお昼ご飯を教えてください"
    }
  ],
  temperature=0.7, # テキストの多様性を制御
  # max_tokens=100, # 生成するトークンの最大数
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

print(completion.choices[0].message.content)