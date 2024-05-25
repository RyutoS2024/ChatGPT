from openai import OpenAI

# APIキーの設定
client = OpenAI(api_key='xxxxxxxxxxxxxxxx')

# Whisper APIを使用して音声をテキストに変換
# 処理するMP3ファイルの番号のリスト
file_numbers = range(0, 14)  # 0~13

# 各ファイルを処理
for num in file_numbers:
    # ファイル名を生成 (例: 1.mp3, 2.mp3, 3.mp3)
    audio_file_path = f"MP3/{num}.mp3"
    text_file_path = f"MD/{num}.md"
    
    with open(audio_file_path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file,
            language="en"
        )
    
    # テキストファイルに書き出し
    with open(text_file_path, "w", encoding="utf-8") as text_file:
        text_file.write(transcription.text)
    
    print(f"Transcription for {audio_file_path} saved to {text_file_path}")
