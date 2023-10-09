import speech_recognition as sr
from flask import  request, jsonify

recognizer = sr.Recognizer()

def get_audio_transcript(audio_file):
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        transcript = recognizer.recognize_google(audio_data, language='pt-BR')
        return transcript

def audio_verify():
    # Verificando se o usuário enviou um arquivo de áudio
    if 'audio' in request.files:
        audio_file = request.files['audio']
        
        try:
            audio_content = get_audio_transcript(audio_file)
            if audio_content:
                return jsonify({"audio_transcript": audio_content})
        except sr.UnknownValueError:
            return jsonify({"error": "Não foi possível reconhecer a fala no áudio."})
        except sr.RequestError:
            return jsonify({"error": "Houve um erro ao processar o áudio."})