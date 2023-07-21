def main():
    print('Testing mandlebrot!')
    # print('mandelbrot(0.5 + 0.5j, 100) =', mandelbrot(0.5 + 0.5j, 100))
    # print('mandelbrot(0 + 0j, 100) =', mandelbrot(0 + 0j, 100))
    # print('mandelbrot(-10 - 10j, 100) =', mandelbrot(-10 - 10j, 100))
    # for c in [0, 1, 1 + 1j, 1 + 2j, 2 + 1j, 2 + 2j]:
    #     mandelbrot_voorbeeld(c)
    mandelbrot_voorbeeld(0 + 0j)
    mandelbrot_voorbeeld(0.35 + 0.5j)
    mandelbrot_voorbeeld(0.5 + 0.5j)
    mandelbrot_voorbeeld(-3 + 2j)
    # print()
    # for i in range(10):
    #     mandelbrot_voorbeeld(i * 0.1 + 0.5j)


def mandelbrot_voorbeeld(positie):
    print(f"mandelbrot({positie:.02f}, 100) = {mandelbrot(positie, 100)}")


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
