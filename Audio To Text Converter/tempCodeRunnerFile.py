import requests
from api_communication import *

filename = "shourav.wav"
audio_url = upload(filename)

save_transcript(audio_url, filename)