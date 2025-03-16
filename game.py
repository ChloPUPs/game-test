import pygame
import sys

# Make textbox opacity low

pygame.init()

screen = pygame.display.set_mode((640, 480))
surface = pygame.Surface((640, 480), pygame.SRCALPHA)

clock = pygame.time.Clock()

font = pygame.font.Font("freesansbold.ttf", 25)

textbox = pygame.Rect(0, 0, screen.width, 100)

textbox_pos = 0

class Player:
        def __init__(self, velocity, speed):
                self.velocity = velocity
                self.rect = pygame.Rect(60, 60, 30, 30)
                self.speed = speed

        def draw(self):
                pygame.draw.rect(screen, (255, 0, 0), self.rect)

class NonPlayerChar:
        def __init__(self, pos, color, width, height, text):
                self.color = color
                self.text = text
                self.pos = pos
                self.width = width
                self.height = height
                self.rect = pygame.Rect(self.pos[0], self.pos[1], self.width, self.height)
        
        def draw(self):
                pygame.draw.rect(screen, self.color, self.rect)

# Create player
player = Player([0, 0], 2)

# NPC #1
npc1_text = [
        "Hello! This is a test. Press space.",
        "Text 2!!",
        "Wow",
        "sers",
        "I like toothpaste",
        ""
]
npc1 = NonPlayerChar([540, 400], (0, 50, 255), 30, 30, npc1_text)

def draw_textbox(str):
        text = font.render(str, True, (255, 255, 255))
        pygame.draw.rect(surface, (0, 0, 0, 125), textbox)
        screen.blit(text, (50, 25))
def undraw_textbox():
        pygame.draw.rect(surface, (0, 0, 0, 0), textbox)
def text_pos_change(str, textbox_pos_len):
        global textbox_pos
        if textbox_pos_len < len(str) - 1:
                textbox_pos += 1

while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                        
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                                player.velocity[0] += player.speed
                        if event.key == pygame.K_LEFT:
                                player.velocity[0] += player.speed * -1
                        if event.key == pygame.K_DOWN:
                                player.velocity[1] += player.speed
                        if event.key == pygame.K_UP:
                                player.velocity[1] += player.speed * -1
                        if event.key == pygame.K_SPACE:
                                text_pos_change(npc1_text, textbox_pos)
                if event.type == pygame.KEYUP:
                        if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                                player.velocity[0] = 0
                        if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                                player.velocity[1] = 0

        player.rect.x += player.velocity[0]
        player.rect.y += player.velocity[1]
        screen.fill((0, 200, 255))
        screen.blit(surface, (0, 0))
        npc1.draw()
        player.draw()

        if player.rect.colliderect(npc1.rect):
                draw_textbox(npc1_text[textbox_pos])
        else:
                textbox_pos = 0
                undraw_textbox()

        clock.tick(60)
        pygame.display.update()