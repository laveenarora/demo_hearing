from flask import Flask, render_template
from gtts import gTTS
import pygame
import time
import os

app = Flask(__name__)

def text_to_speech():
    text = "Hello, I am here!"
    language = 'en'
    tts = gTTS(text=text, lang=language, slow=False)

    # Save the synthesized speech to a temporary file
    temp_file = "temp.mp3"
    tts.save(temp_file)

    # Play the speech using Pygame
    pygame.mixer.init()
    pygame.mixer.music.load(temp_file)
    pygame.mixer.music.play()

    # Wait for the speech to finish playing
    clock = pygame.time.Clock()
    while pygame.mixer.music.get_busy():
        clock.tick(30)

    # Clean up by removing the temporary file
    pygame.mixer.quit()
    os.remove(temp_file)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/text_to_speech')
def text_to_speech_route():
    text_to_speech()
    return "Text-to-speech completed."

if __name__ == "__main__":
    app.run(debug=True)
