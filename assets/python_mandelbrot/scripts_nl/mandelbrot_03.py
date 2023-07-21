import pygame

clock = pygame.time.Clock()


def main():
    pygame.init()
    scherm = pygame.display.set_mode((800, 600))

    herteken = True
    midden = complex(-0.5, 0)
    schaal = 1.0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # linkermuisknop
                    schaal = schaal * 5
                    herteken = True
                elif event.button == 3:  # rechtermuisknop
                    schaal = schaal / 5
                    herteken = True

        if herteken:
            print("hertekenen")
            update(scherm, midden, schaal)
            herteken = False
        clock.tick(60)


def update(scherm, midden, schaal):
    scherm.fill((0, 0, 0))
    afstand_x = 2 / schaal
    afstand_y = afstand_x * scherm.get_height() / scherm.get_width()
    afstand = complex(afstand_x, afstand_y)
    teken_mandelbrot(scherm, midden - afstand, midden + afstand)
    pygame.display.flip()


def teken_mandelbrot(scherm, linksboven, rechtsonder):
    for y in range(scherm.get_height()):
        imag = vertaal(y, scherm.get_height(), 0, linksboven.imag, rechtsonder.imag)
        for x in range(scherm.get_width()):
            real = vertaal(x, 0, scherm.get_width(), linksboven.real, rechtsonder.real)
            positie = complex(real, imag)
            waarde = mandelbrot(positie, 100)
            kleur = (0, 0, 0)
            if waarde >= 0:
                kleur = (waarde * 3 % 256, waarde * 3 % 256, waarde * 2 % 256)
            scherm.set_at((x, y), kleur)


def vertaal(waarde, van_min, van_max, naar_min, naar_max):
    """Vertaalt een waarde van het ene bereik naar het andere bereik."""
    return naar_min + (waarde - van_min) * (naar_max - naar_min) / (van_max - van_min)


def mandelbrot(positie, max_iter):
    """
    Geeft het aantal iteraties om te bepalen of de positie in de verzameling ligt.
    Wanneer de positie niet deel is van de verzameling, wordt -1 teruggegeven."""
    z = 0j
    for i in range(max_iter):
        z = z * z + positie
        if abs(z) > 2:
            return i
    return -1


if __name__ == '__main__':
    main()
