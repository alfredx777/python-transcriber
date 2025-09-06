# Python Audio Transcriber

A simple audio transcription app built in **Python** using [OpenAI Whisper](https://github.com/openai/whisper).  
It allows you to select an audio file via a **Windows file dialog**, transcribes it, and saves the result as a text file.

## Features
- Transcribes audio files (`.mp3`, `.wav`, `.m4a`)
- Saves transcript in a `transcripts/` folder
- Transcript file uses the same name as the audio (e.g., `Meeting1_transcript.txt`)
- Runs locally, no paid subscription required

## Requirements
- Python 3.9+
- [ffmpeg](https://ffmpeg.org/download.html) installed and added to PATH
- Dependencies:
  ```bash
  pip install -r requirements.txt
