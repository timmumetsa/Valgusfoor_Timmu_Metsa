import pygame  # Impordib pygame'i mooduli.

# Algseadistused.
pygame.init()  # Initsialiseerib pygame'i.

# Akna suurus ja nimi
WIDTH, HEIGHT = 300, 300  # Määrab akna laiuse ja kõrguse.
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Loob akna.
pygame.display.set_caption("Valgusfoor - Timmu Metsa")  # Määrab akna nime.

# Värvid.
BLACK = (0, 0, 0)  # Must värv.
WHITE = (255, 255, 255)  # Valge värv.
RED = (255, 0, 0)  # Punane värv.
YELLOW = (255, 255, 0)  # Kollane värv.
GREEN = (0, 255, 0)  # Roheline värv.

# Valgusfoori mõõtmed ja asukoht.
foor_x = WIDTH // 2 - 50  # Valgusfoori X-koordinaat (keskjoonest vasakule nihutatud).
foor_y = HEIGHT // 2 - 140  # Valgusfoori Y-koordinaat, et see oleks täpses kohas.
foor_width = 100  # Valgusfoori laius.
foor_height = 270  # Valgusfoori kõrgus.

# Ringi mõõtmed.
ring_radius = 40  # Tulede raadius.
ring_spacing = 5  # Vahe tulede vahel.

# Peamine tsükkel.
running = True  # Muutuja tsükli käimas hoidmiseks.
while running:
    screen.fill(BLACK)  # Taust mustaks.

    # Joonistab valgusfoori kasti.
    pygame.draw.rect(screen, WHITE, (foor_x, foor_y, foor_width, foor_height), 2)  # Valgusfoori kontuur.

    # Joonistab tuled.
    pygame.draw.circle(screen, RED, (WIDTH // 2, foor_y + ring_radius + 10), ring_radius)  # Ülemine punane tuli.
    pygame.draw.circle(screen, YELLOW, (WIDTH // 2, foor_y + 3 * ring_radius + ring_spacing + 10),
                       ring_radius)  # Keskmine kollane tuli.
    pygame.draw.circle(screen, GREEN, (WIDTH // 2, foor_y + 5 * ring_radius + 2 * ring_spacing + 10),
                       ring_radius)  # Alumine roheline tuli.

    # Värskendab ekraani.
    pygame.display.flip()  # Uuendab ekraanil kuvatavat pilti.

    # Väljumise kontroll.
    for event in pygame.event.get():  # Kontrollib Pygame'i sündmusi.
        if event.type == pygame.QUIT:  # Kui vajutatakse sulgemisnuppu.
            running = False  # Lõpetab tsükli ja sulgeb programmi.

pygame.quit()  # Lõpetab pygame'i töö.