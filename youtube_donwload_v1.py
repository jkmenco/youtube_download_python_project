from pytube import YouTube
import os
import whisper
print()
print()
print()
video_url = 'https://www.youtube.com/watch?v=jUuqBZwwkQw&t=1s'
download_path = os.path.abspath("file_download")
whisper_model = whisper.load_model("base")
video_youtube_name = YouTube(video_url).title

def download_youtube_video(url, folder):
    try:    
        youtube_video = YouTube(url)
        video_stream = youtube_video.streams.filter(progressive=True, file_extension="mp4").order_by('resolution').desc().first()
        video_stream.download(folder)
        print(f"Descarga finalizada = {folder}")
    except Exception as errorYoutube:
        print(f'Ha ocurrido un error al descargar el video: {errorYoutube}')
print()
print()
print()
# descargar video        
download_youtube_video(video_url, download_path)
# Audio para usar
audio_file_path = os.path.join(download_path, video_youtube_name + '.mp4')
print()
print()
print()

def audio_transcribe_whisper(file_path, file_name):
    try:
        # Ruta del audio
        audio_file_path = os.path.join(file_path, file_name + '.mp4')
        # Transcribir audio
        audio_transcription = whisper_model.transcribe(audio_file_path)
        trascription_text = audio_transcription["text"]
        return trascription_text
    except Exception as errorWhisper:
        print(f'An exception occurred ----- >        , {errorWhisper}')

def create_file_text_transcription(transcrition, file_path, file_name):
    try:
        # Ruta de la transcripcion
        transcription_file_path = os.path.join(file_path, file_name + '_transcription.txt')
        # escribir texto
        with open(transcription_file_path, 'w') as f:
            f.write(transcrition)
        print('Transcripción finalizada')
    except Exception as errorCreateFile:
        print(f"Ha ocurrido un error en crear el archivo de texto -----> {errorCreateFile}")

video_youtube_transcribe = audio_transcribe_whisper(download_path, video_youtube_name)

create_file_text_transcription(video_youtube_transcribe, download_path, video_youtube_name)

print()
print()
print()