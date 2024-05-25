from openai import OpenAI

# APIキーの設定
client = OpenAI(api_key='xxxxxxxxxxxxxxxx')

# Whisper APIを使用して音声をテキストに変換
# 音声ファイル
audio_file_path = f"MP3/LR_black_phrase_E_01.mp3"
# テキストファイル（マークダウン）
text_file_path = f"MD/LR_black_phrase_E_01.md"

# ファイルを読み取る
with open(audio_file_path, "rb") as audio_file:
    transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file,
        language="en"
    )

# テキストファイルに書き出し
with open(text_file_path, "w", encoding="utf-8") as text_file:
    text_file.write(transcription.text)

# ログを出力する
print(f"Transcription for {audio_file_path} saved to {text_file_path}")
