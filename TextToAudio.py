import os
from elevenlabs import generate, set_api_key,save
import subprocess
from mutagen.wave import WAVE 
from mutagen.mp3 import MP3
import creds


set_api_key(creds.ELEVEN_API)


def GenerateAudio_2D(text,name):
  global audio
  audio = generate(text=text,voice="7fmH2g8AST4iUSgzMb2m",model="eleven_multilingual_v2")
  dir_path_mp3 = "AudioConvert"
  os.makedirs(dir_path_mp3, exist_ok=True)
  AudioName_MP3 = name + ".mp3"
  file_path_MP3 = os.path.join(dir_path_mp3, AudioName_MP3)
  save(audio, file_path_MP3)
  audio_mp3 = MP3(file_path_MP3)
  lenth = audio_mp3.info.length
  return file_path_MP3, lenth
  
