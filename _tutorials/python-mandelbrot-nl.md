---
classes: wide
title: "Een eerste (maar diepe) duik in Python met Mandelbrot"
tags: python dutch
author_profile: false
#toc: true
sidebar:
  - title: "Python Mandelbrot (WORK IN PROGRESS)"
    image: assets/python_mandelbrot/sidebar_image.png
    image_alt: "image"
    text: "Een eerste (maar diepe) duik in Python."
    nav: python-mandelbrot
---

DIT IS WORK IN PROGRESS. DEZE PAGINA IS NOG NIET AF.

In deze les ga je met Python een Mandelbrot explorer maken. Je hebt geen programmeerkennis nodig om deze cursus te
kunnen volgen. Aan de andere kant duiken we wel meteen een beetje de diepte in omdat we wel wat moois willen maken.
Vraag gerust om hulp of zoek op internet als je iets niet begrijpt.

# Mandelbrot

En fractal is een wiskundige of geometrische vorm die zichzelf herhaalt op steeds kleinere schaal, hoever je ook
inzoomt.
Bij de meeste fractals zie je bij het inzoomen steeds dezelfde vorm terugkomen. Bij de Mandelbrot fractal zie je steeds
een subtiel andere vorm terugkomen. Het resultaat is een oneindig complexe vorm die er steeds weer anders uitziet en
waar je uren naar kunt kijken.

De basis van de Mandelbrot is een eenvoudige formule. Het tekenen van de Mandelbrot met een computer programma is dan
ook niet zo moeilijk. Bovendien is het een leuk projectje als je ook wat van wiskunde houdt en/of wilt leren.

Ook al is de Mandelbrot in de basis eenvoudig, je zult zien dat er toch wel wat bij komt kijken om een mooie Mandelbrot
app te maken waarbij je kunt inzoomen en uitzoomen en als je meer functies wilt toevoegen. Deze hele tutorial zal dus
wel wat tijd kosten. Maar het resultaat is dan ook wel heel mooi!

# Installeren van Python en PyCharm

## Python installeren

Python is een programmeertaal. Ga naar [python.org](https://www.python.org/downloads/) en download en installeer Python op je laptop
als je dat niet al hebt gedaan.

## PyCharm installeren

PyCharm is een Integrated Development Environment (IDE). Je kunt Python schrijven met elke teksteditor, maar met een IDE
heb je heel veel hulp bij het programmeren. Ga naar [jetbrains.com](https://www.jetbrains.com/pycharm/download) en
download de gratis **Community** versie. Dus niet de Professional versie want daar is een licentie voor nodig! Voor de
community versie moet je iets naar beneden scrollen op de pagina.

# Een python project maken

1. Open PyCharm
2. Kies 'New Project'
3. De default instelling zijn prima, klik op 'Create'
4. Met de standaard instellingen maakt PyCharm ook een bestand `main.py` aan. Dit heb je niet nodig en mag je eventueel
   verwijderen. Maar je kunt het ook even openen en 'runnen' door op het groene pijltje naast de
   regel `if __name == '__main__':` te klikken. Je ziet dan onderin het scherm de uitvoer van het programma. Daar zou
   nu `Hi, PyCharm` moeten staan. Gefeliciteerd, je hebt je eerste Python programma uitgevoerd!

# Een python applicatie maken

## Een programma schrijven

Een programma is een tekstbestand met Python code. Een python programma heeft de volgende structuur:

```python

# We schrijven het programma van boven naar beneden. We beginnen met een functie met de naam `main` als startpunt. Het
# mag ook anders heten, maar `main` is wel gebruikelijk.
def main():
    print("Hello World!")


# Dit moet helemaal onderaan staan, en zorgt ervoor dat het programma
# start wanneer je het uitvoert.
if __name__ == "__main__":
    main()
```

Maak het bestand `zandbak.py` aan en kopieer de code hierboven erin. In dit zandbakje kun je spelen met Python code.

TIP: Gebruik de `tab`-toets om in te springen. Met `shift-tab` kun je een regel naar links laten springen.
{: .notice--info}

Om het programma uit te voeren kun je in PyCarm met de rechtermuisknop op het bestand klikken en kiezen
voor `Run 'zandbak'`. Wanneer je dit doet dan zal onder in het scherm een venster openen waarin de uitvoer van het
programma staat. Je ziet daar nu `Hello World!` staan.

Met `print` kun je dingen op het scherm printen. In het voorbeeld printen we een stuk tekst tussen aanhalingstekens. Dat
wordt een `string` genoemd. Maar je kunt ook andere dingen printen. Probeer bijvoorbeeld eens de volgende regels uit, je
kunt ze onder de `print` regel zetten en dan opnieuw het programma uitvoeren. Voor het opnieuw uitvoeren kun je ook op
de groene pijl links onderin het scherm of naast de regel `if __name__ == "__main__":` klikken.

```python
def main():
    print("Hello World!")
    print(1 + 2 * 3)
    print(2 / (1 + 2))
    x = 3.2
    print(x)
    x = x + 1
    print(f"x is nu {x}. En x+1 is {x + 1}")
    print(f"maar x is nog steeds {x}")
```

In deze code is `x` een variabele. Een variabele is een stukje geheugen waarin je een waarde kunt opslaan. Een variabele
kan uit een of meer letters of cijfers bestaan, maar mag niet met een cijfer beginnen.

In de laatste regel zie je een `f` voor de tekst staan. Dat is een `f-string`. Daarmee kun je variabelen of stukjes
python code tussen je tekst zetten.

Speel gerust met de code, en kijk wat er gebeurt als je iets verandert. Let op kringeltjes onder de code waarmee PyCharm
je helpt om fouten te voorkomen. Als je de muis boven zo'n kringeltje houdt dan zie je wat er aan de hand is.

## Een functie schrijven

Een functie is een stukje code dat je kunt hergebruiken. Je kunt een functie aanroepen met een naam en eventueel met een
aantal parameters. Een functie kan ook een waarde teruggeven, dat doe je met het `return` statement. Hieronder staat
bijvoorbeeld een functie die twee getallen bij elkaar optelt en het resultaat teruggeeft.

```python
def tel_op(waarde1, waarde2):
    return waarde1 + waarde2
```

Je kunt deze functie bijvoorbeeld aanroepen met:

```python
def main():
    print(tel_op(1, 2))  # dit print 3
    a = tel_op(3, 4)  # a is nu 7
    b = tel_op(a, 5)  # b is nu 12
    print(tel_op(a, b))  # dit print 19
```

Speel gerust met het maken van functies.

## Loops, if-statements en lijsten

Een loop is een stukje code dat een aantal keren wordt uitgevoerd. De meest gebruikte loop is de `for` loop. Hiermee kun
je een stukje code een aantal keren uitvoeren. Bijvoorbeeld:

```python
def main():
    # een for loop
    for i in range(10):
        print(i)
```

Dit print de getallen 0 tot en met 9. De `range` functie geeft een lijst van getallen terug. De `for` loop loopt door
deze lijst heen en voert de code uit voor elk getal in de lijst. De variabele `i` is een variabele die de waarde van het
huidige getal in de lijst bevat. Het is in bijna alle programmeertalen heel gebruikelijk om een numerieke loopvariabele
`i` te noemen.

Je kunt ook een lijst met waarden maken, en daar doorheen lopen. Bijvoorbeeld:

```python
def main():
    # een for loop
    mijn_lijst = ['aap', 'noot', 'mies']
    for waarde in mijn_lijst:
        print(waarde)
```

Je kunt ook een lijst maken in een loop. Bijvoorbeeld:

```python
def main():
    # een for loop
    even_getallen = []
    for i in range(10):
        if i % 2 == 0:
            even_getallen.append(i)
    print(even_getallen)
```

Hier gebruiken we een if-statement om te kijken of een getal even is. De `%` operator geeft de rest van een deling
terug. Als je een getal door 2 deelt dan is de rest 0 als het getal even is, en 1 als het getal oneven is. De `==`
operator
geeft `True` terug als de twee waarden gelijk zijn, en `False` als ze niet gelijk zijn. Met append voegen we een waarde
toe aan de lijst.

Naast `==` heb je ook nog `!=` (niet gelijk), `<` (kleiner dan), `>` (groter dan), `<=` (kleiner of gelijk) en `>=` om
waarden met elkaar te vergelijken.

Speel gerust met de code, en kijk wat er gebeurt als je iets veranderd. Hieronder zijn twee voorbeelden van functies
die je zou kunnen maken. Probeer ze eens te maken.

### Een functie het gemiddelde van een lijst getallen teruggeeft

```python
def gemiddelde(lijst):
    som = 0
    aantal = len(lijst)

    # jouw code hier
    return som / aantal
```

### Een functie die de *abc*-formule uitrekent

In python kun je een wortel berekenen met `math.sqrt`, bijvoorbeeld met `math.sqrt(4)`. Om deze functie te gebruiken
moet je eerst `import math` bovenaan je bestand zetten. Maak de functie `abc` af en test dit door bijvoorbeeld vanuit
je `main` functie `print(abc(1, 2, 3))` of `print(abc(-1, 2, 3))` aan te roepen.

```python
def abc(a, b, c):
    """Geeft de lijst met oplossingen terug. Dit kunnen er 0, 1 of 2 zijn."""
    discriminant =  # jouw code hier
    if discriminant < 0:
        return []
    elif discriminant == 0:  # elif is een afkorting van 'else if'
        return  # jouw code hier
    else:
        x1 =  # jouw code hier
        x2 =  # jouw code hier
        return [x1, x2]
```

### Vermoeden van Collatz

Nog een leuke opdracht is het vermoeden van Collatz. Dit is een vermoeden dat zegt dat als je een willekeurig getal
neemt, en je doet het volgende:

- als het getal even is, deel het door 2
- als het getal oneven is, vermenigvuldig het met 3 en tel er 1 bij op

Als je dit blijft herhalen dan kom je volgens het vermoeden uiteindelijk altijd uit op 1. Dit is nog nooit bewezen en
wie dat lukt of wie het lukt om het tegendeel te bewijzen zal wel beroemd worden.

Een voorbeeld van de reeks die je krijgt wanneer je begint bij 5: 5 -> 16 -> 8 -> 4 -> 2 -> 1

Maak een functie `collatz(n)` die de reeks print die je krijgt als je begint met `n`. Bijvoorbeeld `collatz(5)` geeft
dan:
```
5
16
8
4
2
1
```

Hiervoor kun je een `while`-loop gebruiken. While betekend 'zolang'. Je kunt een while loop gebruiken om een stukje code
te herhalen zolang een bepaalde voorwaarde waar is. Bijvoorbeeld:

```python
def main():
    i = 0
    while i < 10:
        print(i)
        i = i + 1
```


# Mandelbrot 01 - de mandelbrot functie

Nu je een beetje basiskennis Python hebt gaan we het eerste stukje van onze mandelbrot applicatie maken. Maak hiervoor
het bestand `mandelbrot.py` aan, en zet hierin de `main()` functie en de aanroep daarvan zoals we dat eerder ook in 
`zandbak.py` hebben gedaan.

Mandelbrot is gebaseerd op de functie

    `z = z² + c`

Hierbij zijn `z` en `c` complexe getallen. Dat zijn getallen die uit twee componenten bestaan. We gaan hier later meer
over uitleggen voor als je geïnteresseerd bent, maar voor nu is het voldoende om te weten dat je ze kunt gebruiken als
(x, y) coördinaten. In Python kun je complexe getallen maken met `complex(x, y)`. Bijvoorbeeld `complex(1, 2)` maakt
het complexe getal `1 + 2j`. Je kunt ook gewoon `1 + 2j` schrijven, dat is de gebruikelijke notatie voor complexe
getallen.

De grootte van een complex getal kun je berekenen met `abs`. Bijvoorbeeld `abs(1 + 2j)` geeft `2.23606797749979` terug.
Dit is eigenlijk gewoon de lengte van de lijn van `(0, 0)` naar `(x, y)`. Je kunt dit dus ook berekenen met de stelling van
Pythagoras.

Om van een complex getal de `x` en `y` component te krijgen kun je `.real` en `.imag` gebruiken. Hieronder zie je een paar
voorbeelden:

```python
def main():
    c = complex(1, 2)
    print(f"x = {c.real}")
    print(f"y = {c.imag}")
    print(f"lengte = {abs(c)}")
```

Om te bepalen of een punt `c` deel is van mandelbrot of niet, moet je de functie `z = z² + c` telkens herhalen. Als de
absolute waarde van `z` groter wordt dan 2, dan is het punt `c` niet onderdeel van mandelbrot. Als de waarde van `z` niet groter
dan 2, hoe vaak je ook herhaald, dan is het punt `c` wel onderdeel van mandelbrot. Omdat we niet oneindig lang willen
wachten geven we een maximaal aantal herhalingen (iteraties) op. Als `abs(z)` na zoveel herhalingen nog steeds
niet groter is dan 2, dan geven we `-1` terug. Als de waarde van `z` wel groter is dan 2, dan geven we het aantal
herhalingen terug dat nodig was om dat te bereiken. Dat doen we omdat het aantal herhalingen straks kan worden gebruikt
om een mooi kleurverloop te maken.

Omdat de mandelbrot functie een beetje moeilijk is om zonder al te veel kennis goed te implementeren krijg je hiervoor
de python code:

```python
def mandelbrot(positie, max_iter):
    z = 0j
    for i in range(max_iter):
        z = z * z + positie
        if abs(z) > 2:
            return i
    return -1
```

Hierbij is `positie` het punt `c` dat we willen testen, en `max_iter` het maximale aantal herhalingen dat we willen
doen. Ook al heb je deze functie niet zelf hoeven schrijven, probeer wel te begrijpen wat er gebeurt.

Voeg de mandelbrot functie toe aan `mandelbrot.py` onder de `main` functie. Voeg ook de
functie `mandelbrot_voorbeeld()`:

```python
def mandelbrot_voorbeeld(positie):
    print(f"mandelbrot({positie:.02f}, 100) = {mandelbrot(positie, 100)}")
```

Nu kun je vanaf je main functie `mandelbrot_voorbeeld` aanroepen met een complex getal als argument. Doe dit
bijvoorbeeld
met de waarden `0 + 0j`, `0.35 + 0.5j`, `0.5+0.5j`, `-3, 2j`. Hieraan zou je al een beetje moeten kunnen zien dat hoe
dichter je bij het punt (0, 0) komt, hoe meer herhalingen er nodig zijn om de waarde van `z` groter dan 2 te maken. Heel
dicht bij zijn 100 iteraties niet genoeg en wordt dus `-1` terug gegeven. Begin je met een complex getal dat verder van
`(0, 0)` af ligt, dan is de waarde van `z` al snel groter dan 2.

Als je er niet uit komt, kun je [mandelbrot_01.py](https://raw.githubusercontent.com/bertbaron/bertbaron.github.io/main/assets/python_mandelbrot/scripts_nl/mandelbrot_01.py){:target="_blank"}
bekijken. 

# Complexe getallen

Dit hoofdstuk kun je overslaan. Maar als je wat meer over complexe getallen wilt weten, lees dan verder.

Complexe getallen klinken meer complex dan dat ze zijn. Het zijn getallen die bestaan uit twee componenten, en kun je
schrijven als `a + bj`, oftewel `a` + `b` * `j`. Hierbij is `a` het reële (echte) deel. Dit is een gewoon getal zoals je
gewend
bent. `b` is het imaginaire (denkbeeldige) deel. De constante `j` is de imaginaire eenheid, en is gelijk aan `√-1`. In
plaats van
`j` wordt meestal `i` gebruikt, maar omdat Python `j` gebruikt doen wij dat hier ook.

Het lijkt misschien gek, maar je kunt hier gewoon me rekenen zoals je gewend bent. Bijvoorbeeld:

`2 * (2 + 3j) = 4 + 6j`  
`2j * 3j = 6 * j² = -6` (want `j²` is immers `-1`)

Zowel `a` als `b` kan `0` zijn. Als `b==0` dan heb je een gewoon getal.

Maak zelf de volgende berekeningen. Controleer ze door ze in `zandbak.py` te zetten:

`(2 + 3j)² =`  
`√-4 =` (gebruik de regel `√a * √b = √(a * b)`)

Werk ook de onderstaande berekeningen uit (de eerste is al gegeven).

`a + (bj)² = a + b²j² = a + b² * -1 = a - b²`  
`(a + bj)² =`  
`(a + bj)² + (c + dj) =`

Die laatste formule is de formule van Mandelbrot (`z = z² + c` waarbij `z` en `c` complexe getallen zijn). Zo zie je dat
je de mandelbrot ook prima kunt uitrekenen in een programmeertaal die geen complexe getallen kent.

Een complex getal heeft ook een grootte, die wordt weergegeven als `abs(v)`. Dit is gewoon de stelling van Pythagoras,
oftewel `√(a^2 + b^2)`.

# Mandelbrot 02 - Mandelbrot tekenen

Nu we weten hoe we kunnen bepalen of een punt onderdeel is van mandelbrot of niet, kunnen we een plaatje maken. We gaan
een plaatje maken van 800 bij 600 pixels. Elk punt in dit plaatje komt overeen met een complex getal. Om de mandelbrot
verzameling mooi in het midden te krijgen mappen we de linkerbovenhoek naar (-2.5, -1.5) (of `-2.5 - 1.5j`) en de
rechteronderhoek naar
(1.5, 1.5) (of `1.5 + 1.5j`).

## Vertalen van waarden naar een ander bereik

Voor we gaan tekenen maken we eerst een handige hulpfunctie om een waarde van het ene bereik naar het andere te
vertalen (mappen).
Probeer deze zelf te maken. Als je er niet uitkomt, kun je de functie `vertaal` in [mandelbrot_02.py](https://raw.githubusercontent.com/bertbaron/bertbaron.github.io/main/assets/python_mandelbrot/scripts_nl/mandelbrot_02.py){:target="_blank"} bekijken.

```python
def vertaal(waarde, van_min, van_max, naar_min, naar_max):
    return  # je code hier
```

Om je functie te testen kun je deze in je zandbak zetten en aanroepen met de volgende voorbeelden:

```python
def main():
    print(vertaal(0, 0, 100, 0, 1))  # 0
    print(vertaal(50, 0, 100, 0, 1))  # 0.5
    print(vertaal(100, 0, 100, 0, 1))  # 1
    print(vertaal(20, 0, 100, 5, -5))  # 3
    print(vertaal(80, 100, 0, 5, -5))  # -3
```

## Een scherm opzetten met `pygame`

Om te kunnen tekenen gebruiken we de `pygame` bibliotheek. Typ helemaal boven in je programma deze regel:

```python
import pygame
```

In PyCharm komen er nu rode kringeltjes onder het woord `pygame` te staan. Dit komt omdat PyCharm de library nog niet
heeft gedownload. Als je je muis even stil houdt boven `pygame`, dan verschijnt er een schermpje met iets als de melding
`No module named 'pygame'`, met daaronder de link `Install package 'pygame'`. Klik op die link om pygame te installeren.

Gebruik je geen PyCharm of werkt het niet, dan kun je ook in een terminalvenster het commando `pip install pygame`. Je
kunt een terminal openen door onder in het scherm op `Terminal` te klikken.

Pas nu je `main` functie aan zodat deze er als volgt uit ziet:

```python
clock = pygame.time.Clock()


def main():
    pygame.init()
    scherm = pygame.display.set_mode((800, 600))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        update(scherm)
        clock.tick(60)


def update(scherm):
    print("update")
```

In de eerste 2 regels van `main` zetten we `pygame` aan en maken we een scherm van 800 bij 600 pixels. Daarna starten we
een `while`
loop die blijft herhalen tot het programma wordt afgesloten. In de `while` loop roepen we eerst de functie `update` aan
die we nog moeten maken. Met `clock.tick(60)` zorgen we ervoor dat de loop maximaal 60 keer per seconde wordt
uitgevoerd.
Hiermee zorgen we er voor dat het programma niet heel veel CPU gebruikt wanneer de update heel kort duurt.

Elke keer dat we de loop beginnen halen we eerst alle events op. Dit zijn bijvoorbeeld toetsaanslagen of muisklikken.
Als we het event `QUIT` tegenkomen, dan sluiten we het programma af. Dit doen we door `pygame.quit()` aan te roepen en
met `return` uit de `main` functie te gaan.

## Het implementeren van de update functie

Nu we een scherm hebben, kunnen we de update functie implementeren. Deze functie moet het scherm leegmaken en daarna
alle pixels tekenen. Wanneer we klaar zijn met tekenen roepen we `pygame.display.flip()` aan om de nieuwe tekening op
het scherm te tonen. Dit gebeurt dus in 1x, zodat je niet ziet dat het scherm eerst zwart wordt en daarna wordt bijgewerkt.

```python
def update(scherm):
    scherm.fill((0, 0, 0))
    linksboven = complex(-2.5, -1.5)
    rechtsonder = complex(1.5, 1.5)

    for y in range(scherm.get_height()):
        imag = vertaal(y,..,.., .., ..)  # vul dit in, let op dat y=0 onder is, je moet dus omkeren
        for x in range(scherm.get_width()):
            real = vertaal(x,..,.., .., ..)  # vul dit in
            positie = complex(real, imag)
            waarde = mandelbrot(positie, 100)
            kleur = (0, 0, 0)
            if waarde >= 0:
                kleur = (255, 255, 255)
            scherm.set_at((x, y), kleur)

    pygame.display.flip()
```

Gebruik `linksboven.imag` en `linksboven.real` enz. om de imaginaire en reële delen (x en y) van een complex getal op te
vragen.
{: .notice--info}

Als je het programma nu uitvoert, zou je de klassieke mandelbrot moeten zien zoals in de afbeelding hieronder.

![Mandelbrot](/assets/python_mandelbrot/classic_mandelbrot.png)

Als het je echt niet lukt, kun je de code in [mandelbrot02.py](https://raw.githubusercontent.com/bertbaron/bertbaron.github.io/main/assets/python_mandelbrot/scripts_nl/mandelbrot_02.py){:target="_blank"}
bekijken. Probeer wel te begrijpen wat er gebeurt en waarom het bij jou niet werkte.

Het zal je misschien opvallen dat er heel veel CPU wordt gebruikt. Dit komt omdat we de mandelbrot nu telkens opnieuw
tekenen terwijl dat niet nodig is. Dit zullen we later oplossen.

### Een beetje kleur

Erg spectaculair is het nog niet. Laten we eens wat kleur toevoegen. We gaan de kleur bepalen aan de hand van de waarde
(het aantal iteraties dat nodig was om te bepalen dat een punt niet tot de mandelbrot verzameling behoort). Een kleur
op het scherm wordt bepaald door drie waarden, namelijk rood, groen en blauw. Deze waarden kunnen tussen 0 en 255
liggen.
Zijn ze alle drie 0 dan heb je zwart, zijn ze alle drie 255 dan heb je wit. Door deze waarden te combineren kun je alle
kleuren maken die op het scherm te tonen zijn.

Onze waarde ligt nu tussen 0 en 100 (voor -1 gebruiken we al zwarte pixels). We kunnen dus bijvoorbeeld dit als kleur
gebruiken:

```python
kleur = (waarde * 2, waarde * 2, waarde * 2)
```

Dit zou er al veel beter uit moeten zien. Doordat zowel de buitenkant donker is (0 iteraties wordt zwart) als
de binnenkant (-1 wordt ook zwart) krijg je een mooie rand met een lichte kleur. Doordat de helderheid verloopt geeft
dat bovendien een wat gloeiend effect.

We kunnen ook met 3 vermenigvuldigen, maar dan komen we over de 255 heen. Om dat te voorkomen kunnen we `% 256`
gebruiken.
Dit zorgt ervoor dat de waarde nooit hoger dan 255 wordt omdat de rest bij deling door 256 wordt gebruikt. Probeer
bijvoorbeeld dit eens:

```python
kleur = (waarde * 3 % 256, waarde * 3 % 256, waarde * 2 % 256)
```

Experimenteer met de kleuren en probeer een mooie kleurencombinatie te vinden. Later, wanneer we gaan inzoomen en kleur
belangrijker wordt, gaan we dit overigens nog veel mooier maken.

# Mandelbrot 03 - Inzoomen

Nu we een mandelbrot kunnen tekenen, kunnen we gaan inzoomen. Hiervoor gaan we de linkerbovenhoek en de rechteronderhoek
berekenen op basis van het midden en de schaal waarmee is ingezoomd.

Als eerste stap gaan we de update functie aanpassen zodat we de linkerbovenhoek en de rechteronderhoek kunnen opgeven.
Zo'n aanpassing waarbij de code wordt aangepast zonder dat de functionaliteit verandert noemen we een *refactoring*. Dit
is een belangrijk onderdeel van het ontwikkelen van software. Hiermee houd je de code leesbaar en overzichtelijk.

Maak onder de `update` functie de functie `teken_mandelbrot(scherm, linksboven, rechtsonder)` aan. Verplaats het
middelste
deel van de code uit de `update` functie naar de nieuwe functie en vervang de code in de `update` functie door een
aanroep van de nieuwe functie. De code zou er nu zo uit moeten zien:

```python
def update(scherm):
    scherm.fill((0, 0, 0))
    linksboven = complex(-2.5, -1.5)
    rechtsonder = complex(1.5, 1.5)
    teken_mandelbrot(scherm, linksboven, rechtsonder)
    pygame.display.flip()


def teken_mandelbrot(scherm, linksboven, rechtsonder):
# hier komt een deel van de code die eerst in update stond
```

Als je het goed hebt gedaan zou het programma nog steeds moeten werken. De volgende stap is om de linkerbovenhoek en
rechteronderhoek te berekenen op basis van het midden en de schaal. We beginnen met schaal 1. Met de linker muisknop
zoomen we in en met de rechter muisknop zoomen we uit. Pas je `main` functie aan zodat de loop er als volgt uit ziet:

```python
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
            elif event.button == 3:  # rechtermuisknop
                schaal = schaal / 5

    update(scherm, midden, schaal)
    clock.tick(60)
```

De update functie moeten we nu met de nieuwe parameters uitbreiden en dan de nieuwe linkerbovenhoek en rechteronderhoek
berekenen. Bij een schaal van 1 is de afstand van het midden tot de linkerkant 2. Bij een schaal van 2 moeten we dit
delen door 2, enz. Als we de afstand van het midden tot de linkerkant weten, kunnen we ook de afstand van het midden tot
de bovenkant berekenen. Dit doen we door de schermverhouding te gebruiken. In ons voorbeeld is de
verhouding `600 / 800`.
Is de horizontale afstand `2`, dan is de verticale afstand dus `2 * 600 / 800`. Hierdoor blijft de mandelbrot in
verhouding.

Maak nu de `update` functie af:

```python
def update(scherm, midden, schaal):
    scherm.fill((0, 0, 0))
    afstand_x =  # bereken de afstand van het midden tot de linkerkant
    afstand_y = afstand_x *  # de schermverhouding, gebruik scherm.get_height() en scherm.get_width()
    afstand = complex(afstand_x, afstand_y)
    teken_mandelbrot(scherm, midden - afstand, midden + afstand, 100)
    pygame.display.flip()
```

Als het goed is zul je nu nog steeds de mandelbrot op dezelfde manier zien getekend. Maar door op de linker muisknop te
drukken zou je moeten inzoomen en met de rechter muisknop weer uit moeten zoomen.

Zoals eerder gezegd wordt de mandelbrot nu telkens onnodig opnieuw getekend. Dit gaan we oplossen door alleen opnieuw
te tekenen wanneer de variabele `herteken` op `True` staat. Vervang dit:

```python
        update(scherm, midden, schaal)
```

door dit:

```python
        if herteken:
            print("hertekenen")
            update(scherm, midden, schaal)
            herteken = False
```

Zorg nu dat `herteken` op de juiste plekken op `True` wordt gezet, zodat de mandelbrot aan het begin 1x wordt getekend
en bij elke wijziging van de schaal ook weer opnieuw.

Met `midden = complex(-0.5, 0)` kun je maar 1 keer inzoomen voordat het hele scherm zwart wordt. Probeer eens een ander
midden te vinden waarbij je vaker kunt inzoomen.

Pas ook eens de schermgrootte aan, bijvoorbeeld naar 500 bij 600. Blijft de mandelbrot helemaal zichtbaar en in
verhouding?

Je kunt je oplossing vergelijken met [mandelbrot_03.py](https://raw.githubusercontent.com/bertbaron/bertbaron.github.io/main/assets/python_mandelbrot/scripts_nl/mandelbrot_03.py){:target="_blank"}.
Als jouw oplossing veel afwijkt, probeer dan de gegeven oplossing te begrijpen en gebruik die. Anders kan het zijn dat je
bij de volgende opdracht niet verder kunt.


# Mandelbrot 04 - Performance verbeteren

We willen het programma graag verder uitbreiden. Maar je zult merken dat het tekenen vrij lang duurt, en daardoor ook
het testen en spelen met de code. We gaan daarom eerst kijken of we de performance kunnen verbeteren.

Performance verbeteren is meestal niet nodig. Doe het dan ook niet. Je programma wordt vaak minder leesbaar en lastiger
te onderhouden. Als je wel de performance wilt proberen te verbeteren, zorg dan eerst dat je programma goed werkt. Meet
daarna waar de performance problemen zitten en verbeter alleen die punten.
{: .notice--warning}

Het berekenen van de mandelbrot is veel werk. Voor een scherm van 800 bij 600 pixels moeten we al 480.000 keer de
mandelbrot
berekenen. En voor elk punt kunnen wel 100 iteraties nodig zijn. Dat is al 48 miljoen berekeningen. Bovendien willen we
later
misschien wel 1000 iteraties doen en het scherm vergroten naar 1920 bij 1080 pixels. Dan hebben we het over 2 miljard
berekeningen. Het zal duidelijk zijn dat als we de berekeningen per pixel kunnen versnellen, we veel tijd kunnen
besparen.
Het zal ook duidelijk zijn dat het weinig helpt als we de loop in de `main` functie sneller maken. Elke loop worden er
misschien 2 miljard berekeningen uitgevoerd, dan maken de paar regels in de `main` functie niet veel uit.

## Rekentijd meten

Voor we beginnen, gaan we eerst de tijd printen die het tekenen kost. We gebruiken hiervoor de `time` module. Voeg boven
in je bestand `import time` toe en zet de volgende regels rond je aanroep naar `update`:

```python
            start = time.time()
update(scherm, midden, schaal)
print(f"Update duurde {time.time() - start:.2f} seconden")
```

Als je nu een paar keer inzoomt en weer uitzoomt, zul je zien dat het eerste scherm nog redelijk snel wordt getekend,
maar
dat het minder snel gaat wanneer het hele scherm zwart wordt. Dit komt omdat de mandelbrot daar veel meer iteraties
nodig
heeft. Doe dit een paar keer en onthoudt de getallen die je ziet of schrijf ze (afgerond) op. Bij mij duurt het tekenen
bijvoorbeeld ongeveer `1.8` seconden voor het eerste scherm en `7` seconden bij `2x` inzoomen. Merk op dat het niet elke
keer precies hetzelfde is. Herhaal het daarom eventueel een paar keer. En houdt je laptop aan de stroom, want anders
kan het zijn dat die in een zuiniger stand gaat wanneer de batterij bijna leeg is.

## Just-in-time compileren

Python is een taal die wordt geïnterpreteerd. Dat betekent dat de code tijdens het uitvoeren wordt omgezet naar
machinetaal
voordat deze kan worden uitgevoerd. Dit gebeurt elke keer weer opnieuw. Uiteraard optimaliseert de Python interpreter
dit
zoveel mogelijk, maar omdat de taal heel flexibel is, is het niet mogelijk om alles te optimaliseren.

Met de `numba` module kunnen we een functie laten compileren naar machinetaal. Dit heet just-in-time compileren. De code
wordt dan gecompileerd de eerste keer dat deze wordt aangeroepen. Dit kost tijd, maar elke volgende keer wordt de al
gecompileerde code rechtstreeks op de processor uitgevoerd. En dat kan veel sneller zijn. Er zijn wel een paar
beperkingen,
dus je kunt niet zomaar elke functie compileren. Maar voor de mandelbrot functie werkt het prima.

Installeer de `numba` module met `pip install numba`. Voeg daarna boven in je bestand `from numba import jit` toe. Nu
kun je `@jit(nopython=True)` direct boven de functie `mandelbrot` zetten. Daarmee wordt deze functie gecompileerd. Draai
het programma nu nog een keer en kijk of het sneller gaat. Bij mij gaat het eerste scherm nu ongeveer `3x` zo snel
(behalve de eerste keer). Bij `2x` inzoomen gaat het zelfs `10x` zo snel!

Als het niet werkt bij jou, kijk dan nog eens goed naar `mandelbrot03.py` om te kijken of je misschien verschillen ziet.

Wat zijn jouw resultaten?

Waarom is het eerste scherm de eerste keer minder snel?

Waarom is het verschijl groter wanneer er meer is ingezoomed?

### Nog een keer JIT

Een andere functie die voor elke pixel wordt uitgevoerd is `vertaal`. Gelukkig kan deze ook worden gecompileerd met
`@jit(nopython=True)`. Doe dit en kijk of het nog sneller gaat. Bij mij scheelt het eigenlijk maar een klein beetje.

### Het scherm tekenen met `numpy` en nog meer JIT

Wat we nu gaan doen is wel een beetje voor gevorderde programmeurs. Als je het wel gelooft, installeer dan de `numpy`
module met `pip install numpy`, neem de code over van `mandelbrot04.py` en ga verder met Mandelbrot 05.

Wil je het toch zoveel mogelijk zelf doen en proberen te begrijpen, ga dan verdr met deze opdracht.

Waar nog wat te winnen valt, is in de loop waarin de pixels worden getekend. We kunnen proberen om `@jit(nopython=True)`
boven `def teken_mandelbrot` zetten, maar als je dat probeert, zul je zien dat je een foutmelding krijgt. Dat komt omdat
we in deze functie een `pygame.Surface` (`scherm`) gebruiken. En dat is geen type dat `numba` kent. Om dit op te lossen
gaan we het scherm niet tekenen met heel veel aanroepen naar `scherm.set_at`, maar we de pixels eerst in een `numpy`
array zetten en daarna die array in één keer naar het scherm schrijven. Een array is een lijst of matrix met getallen.
`numpy` arrays zijn veel efficiënter (maar minder generiek) dan python lijsten. Maar de grootste winst zit hem er straks
in dat `numba` arrays wel kent en we dus weer `@jit` kunnen gebruiken.

#### Stap 1, het scherm tekenen met `numpy`

Installeer de `numpy` module met `pip install numpy`.

In `teken_mandelbrot` zit een (dubbele) loop over alle pixels. We gaan nu voor de loop de pixel buffer opvragen als een
`numpy` array, en na de loop deze buffer weer terugschrijven naar het scherm, met:

```python
    pixel_array = pygame.surfarray.pixels2d(scherm)  # toegang tot de pixel buffer

# hier zit de loop over y en x

pygame.surfarray.blit_array(scherm, pixel_array)  # schrijf de pixel buffer terug naar het scherm
```

Om op de array te tekenen vervangen we `scherm.set_at((x, y), kleur)` door `pixel_array[y, x] = kleur`. Let op dat de
volgorde van `x` en `y` is omgedraaid.

Als je het programma nu draait dan gaat er nog iets fout. Je zult iets als de volgende foutmelding zien:

```
    pixel_array[x, y] = kleur
ValueError: setting an array element with a sequence.
```

Op het scherm maakten we een kleur met een `(r, g, b)` tuple. Dit word door `pygame` omgezet naar een enkel getal. Maar
nu moeten we dat zelf doen. Voeg onderstaande functie toe aan je programma:

```python
@jit(nopython=True)
def rgb(r, g, b):
    return (r << 16) | (g << 8) | b
```     

Nu kun je `rgb(r, g, b)` gebruiken om een kleur te maken. Draai het programma nu nog een keer en kijk of het werkt. Is
het ook sneller? Misschien is dat niet zo omdat er nog wat onnodige berekeningen in zitten. Probeer die er niet uit te
halen, wanneer we straks `@jit` gebruiken zal de compiler zelf wel zo slim zijn om die er uit te halen.

We tekenen nu op de array, maar kunnen nog steeds geen `@jit` gebruiken. Daarvoor moeten we de loop verplaatsen naar een
functie. Maar in die functie willen we geen `scherm` gebruiken, enkel de `array`. Nu wordt `scherm` nog in de loop
gebruikt,
je kunt dat in PyCharm mooi zien als je er op klikt. Los dit op door voor de loop variabelen te maken en deze in de loop
te gebruiken. Bijvoorbeeld `breedte = scherm.get_width()`. En gebruik dan `breedte` in de loop. Doe dit ook
voor `hoogte`.

Verplaats de loop nu naar een functie en roep deze aan vanuit `teken_mandelbrot`:

```python
@jit(nopython=True)
def teken_mandelbrot_op_array(breedte, hoogte, linksboven, rechtsonder, pixel_array):
# je loop over x en y
```

Kijk of je programma nog werkt en of het sneller is geworden. Bij mij is dit eindresultaat ongeveer `30x` zo snel als
Mandelbrot 03!

# Mandelbrot 05

We willen natuurlijk graag het programma verder uitbreiden zodat we bijvoorbeeld overal kunnen inzoomen. Toch gaan we,
voordat we dat doen, eerst nog een keer refactoren.

Het punt is nu namelijk dat er in de main functie een paar variabelen zijn, zoals `herteken`, `midden` en `schaal`. En
als we het programma verder uitbreiden dan komen er nog meer bij. Op allemaal plekken in de code worden deze variabelen
dan gezet en gelezen, waardoor onze `main` functie onoverzichtelijk wordt. We willen de `main` functie juist zo schoon
mogelijk houden. Er moet zo weinig mogelijk code in die te maken heeft met het tekenen van de mandelbrot. Dit gaan we
doen door een `Mandelbrot` class te maken. In die `class` komen alle variabelen die nodig zijn. Classes in Python zijn
soms wat omslachtiger dan in veel andere talen. Daarom gebruiken we een `dataclass`, die maakt sommige dingen wat
makkelijker.

## Dataclasses

Een voorbeeld van een dataclass is:

```python
from dataclasses import dataclass


def main():


# je main


@dataclass
class Persoon:
    naam: str
    leeftijd: int
```

Je kunt nu een persoon maken met `jan = Persoon("Jan", 45)`. Vervolgens kun je dan bijvoorbeeld `print(jan.naam)`
doen of `jan.leeftijd = 46`. Speel hier even mee in je `zandbak.py`.

### types

Merk op dat er bij de velden `types` staan. Dit helpt de compiler om te controleren of je de class goed gebruikt. In
PyCharm krijg je dan vaak nog betere hulp en feedback als er iets fout is. Als je een type echt niet weet dan mag je
ook `...` invullen (bijvoorbeeld `naam: ...`)

### default waarde

Je kunt ook een default waarde opgeven. Bijvoorbeeld `leeftijd: int = 0`. Als je nu een persoon maakt zonder leeftijd
(`jan = Persoon('Jan')`) dan krijgt deze automatisch leeftijd `0`.

### functies

Je kunt aan een (data)class ook een functie toevoegen. Functies kunnen velden gebruiken of aanpassen. Bijvoorbeeld:

```python
@dataclass
class Persoon:
    naam: str
    leeftijd: int = 0

    def verjaar(self):
        self.leeftijd = self.leeftijd + 1
```

Elke functie in een class krijgt als eerste argument `self`. Dit is een verwijzing naar het object zelf. Je kunt dus
bijvoorbeeld `self.leeftijd` gebruiken om de leeftijd van het object te veranderen.

Probeer nu eens het volgende:

```python
def main():
    jan = Persoon("Jan")
    print(jan.leeftijd)
    jan.verjaar()
    print(jan.leeftijd)
```

Als je veel variabelen hebt dan is het handig om 'named variables' te gebruiken bij het aanmaken. Bijvoorbeeld:

```python
    jan = Persoon(naam="Jan", leeftijd=45)
```

Dit is iets wat je overigens ook bij gewone functies kunt doen.

## Mandelbrot class

Nu je wat gespeeld hebt met (data)classes gaan we de `Mandelbrot` class maken. Importeer `dataclass` en maak de volgende
class aan onder je `main` functie:

```python
@dataclass
class Mandelbrot:
    scherm: pygame.Surface
    midden: complex = complex(-0.5, 0)
    schaal: float = 1
    herteken: bool = True
```

Verplaats de functie `def update(scherm, midden, schaal)` naar de dataclass. Let er op dat je inspringt. In PyCharm
kun je dit doen door de hele functie te selecteren en op `tab` te drukken. Pas de functie aan zodat je `self` gebruikt.
Merk op dat de overige parameters nu niet meer nodig zijn, je moet enkel `def update(self)` overhouden.

Vervang de variabelen boven je loop in de `main` functie nu door `mb = Mandelbrot(scherm)`. Zorg dat de rest van de
code nu `mandelbrot.xxx` gebruikt in plaats van de variabelen die je had. Je programma zou nu weer gewoon moeten werken.
Wanneer het nog niet goed is, vergelijk dan met `mandelbrot_05a.py`

## Methodes gebruiken in plaats van class variabelen

In je `main` staan nu dingen als

```python
mb.schaal = mb.schaal * 5
mb.herteken = True
```

Dat is allemaal nog vrij omslachtig en specifiek. We willen eigenlijk dat de `Mandelbrot` class dit zelf kan doen.
Hieronder
zie je de loop uit de `main` functie zoals we die willen hebben.

```python
    mb = Mandelbrot(scherm)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # linkermuisknop
                mb.update_schaal(5)
            elif event.button == 3:  # rechtermuisknop
                mb.update_schaal(1 / 5)

    mb.update()
    clock.tick(60)
```

Dat ziet er toch een stuk netter uit. Pas nu zelf de mandelbrot class aan zodat dit werkt.

# Mandelbrot 06 - Verplaatsen bij zoomen

Nu zijn we klaar om weer functionaliteit toe te voegen. We willen zorgen dat bij het inzoomen en uitzoomen het punt
onder de cursor het nieuwe midden wordt.


[//]: # ([Voor vragen of opmerkingen over deze pagina kun je een hier Github issue maken]&#40;)

[//]: # (here: https://github.com/bertbaron/bertbaron.github.io/issues&#41;)