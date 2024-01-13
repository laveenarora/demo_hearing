from gtts import gTTS
import pygame
import time
import os


def initialize_pygame():
    # Initialize Pygame
    pygame.init()


def text_to_speech(text, language='en'):
    tts = gTTS(text=text, lang=language, slow=False)

    # Save the synthesized speech to a temporary file
    temp_file = "temp.mp3"
    tts.save(temp_file)

    # Set up the display
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Text-to-Speech Demo")

    # Delay before displaying the text and playing the speech
    time.sleep(1)

    # Display the text on the Pygame window
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, (255, 255, 255))
    screen.blit(text_surface,
                (width // 2 - text_surface.get_width() // 2, height // 2 - text_surface.get_height() // 2))
    pygame.display.flip()

    # Play the speech using Pygame
    pygame.mixer.init()
    pygame.mixer.music.load(temp_file)
    pygame.mixer.music.play()

    # Wait for the speech to finish playing
    clock = pygame.time.Clock()
    while pygame.mixer.music.get_busy():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        clock.tick(30)

    # Clean up by removing the temporary file
    pygame.mixer.quit()
    os.remove(temp_file)


if __name__ == "__main__":
    initialize_pygame()

    # Convert text to speech and play it
    text_to_speech("Hi, I am here")

    # Quit Pygame
    pygame.quit()
