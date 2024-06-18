import pygame
import os

pygame.init()

screen_width = 700
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

def load_frames(path: str, frames_number: int, fps: int = 30):
    """
    Pega as imagens de uma pasta com seu caminho (path)
    em seguda carrega uma a uma na tela do pygame com o dado fps
    """
    frames_animation = []
    frame_duration = 1000//fps
    
    for i in range(frames_number):
        frame = pygame.image.load(os.path.join(path, f'frame{i}.png')).convert_alpha()
        frames_animation.append(frame)
    
    for i in range(frames_number):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        screen.fill((1,1,1))
        screen.blit(frames_animation[i], (0,0))
        pygame.display.flip()
        pygame.time.delay(frame_duration)

