# Definicje:
Przekształcenie funkcji podstawowej f(x) do funkcji złożonej g(x) można wyrazić jako 2 oddzielne przekształcenia: na argumencie (PRZEKSZTAŁCENIA X) 
i na funkcji (PRZEKSZTAŁCENIA Y):

funkcja poszukiwana g(x) = PRZEKSZTAŁCENIA Y [  f( PRZEKSZTAŁCENIA X( x ) ]

Podstawowe przekształcenia opisane są na tej stronie:
[https://pl.wikibooks.org/wiki/Matematyka_dla_liceum/Funkcje_i_ich_w%C5%82asno%C5%9Bci/Przekszta%C5%82canie_wykresu_funkcji]

Z czysto artmetycznego znaczenia kolejność tych przekształceń nie ma znaczenia:
n.p. funkcję złożoną g(x) = f(-x+1) możemy z powodzeniem otrzymać na 2 sposoby:
```f(x) -> f(-x) -> f(-x+1)```
oraz
```f(x) -> f(x+1) -> f(-x+1)```

Jednakże jeśli chcemy **WYZNACZYĆ GRAFICZNIE** wykres funkcji g(x) na drodze kolejnych przekształceń podstawowych, **MUSIMY** stosować określoną kolejność, 
w przeciwnym razie nasze graficzne przekształcenia będą błędne! Przykładowo przekształcenie:

```f(-x) -> f(-x+1)```

nie będzie proatą translacją, co widać ma wykresie:

Dlatego w przeciwieństwie do operacji artmetycznych takich, jak dodawanie i mnożenie, przekształcenia funkcji w tym wypadku nie są przemienne.

# Kolejność
Zasady ustalające właściwą kolejność przekształceń są całkowicie różne dla przekształceń na argumencie i na funkcji.

### PRZEKSZTAŁCENIA X

Przy przekształceniach X (na argumencie) obowiązuje zasada, **"ostatni będą pierwszymi"**.

Wprowadźmy następujące rozróżnienie:
x bez minusa i wartości bezwzględnej nazwijmy czystym x
-x lub |x| nazwijmy przekształconym x

Aby poprawnie przekształcić argument, każde kolejne przekształcenie musi być wykonane na czystym x. Mówiąc obrazowo dodany operator (tj. +, -, ×, | |) musi stykać się z czystym symbolem x. I tak:
```
f(x) -> f(-x) -> f(-x+1)
'''
jest błędne, bo +1 dodane jest do przekształconego -x

```
f(x) -> f(x+1) -> f(-x+1) 
```
jest poprawne, bo mnożenie przez -1 (czyli dodanie minusa) wykonane jest na czystym x

Stąd wynika wspomniana zasada "ostatni będą pierwszymi":
```
f(x) 
f(x+1)      - dodajemy +1 do czystego x
f(-x+1)     - mnożymy czysty x przez -1
f(-|x|+1)   - wyciągamy wartość bezwzg. z czystego x
f(-|x+3|+1) - dodajemy +3 do czystego x
```
Jak widać, operacja +1 stojąca niejako na końcu musi być wykonana jako pierwsza.

### PRZEKSZTAŁCENIA Y

Tu obowiązuje zasada **"jednej kuli śnieżnej"** -  kolejne przekształcenia muszą być wykonane na całej funkcji, a nietylko na jej części, mówiąc obrazowo przyklejają się one do stopniowo coraz większej kuli śnieżnej, ale musi to być ciągle jedna kula:
```
f(x)+1 -> -f(x)+1
```
jest błędne bo mnożenie przez -1 wykonaliśmy tylko na częci funkcji, a wyraz +1 pozostał niezmieniony

```
-f(x)  -> -f(x)+1 
```
jest poprawne, bo dodajemy +1 do jednego wyrazu.

Podobnie jest z modułem ( wartością bezwzg.):
```
f(x)+1  ->  -f(x)+1 -1 -> |-f(x)+1| -1 
```
jest błedne, bo po dodaniu modułu, wyraz -1 pozostaje "poza" ostatnim przekształceniem (modułem), mówiąc obrazowo dzielimy kulę śnieżną na dwie mniejsze.

```
f(x)+1  ->  |-f(x)+1|  -> |-f(x)+1| -1
```
jest poprawne, bo każde kolejne przekształcenie modyfikuje całą funkcję - nasza kula śnieżna rośnie jako jeden wyraz


### PRZEKSZTAŁCENIA XY

Niektóre przekształcenia na argumencie i funkcji można wykonać równocześnie pod warunkiem , że przestrzegamy odpowiednio obu zasad **"ostatni będą pierwszymi"** 
i **"jednej kuli śnieżnej"**:
- translacja T o wektor [a, b] funkcji f(x) -> f(x - a) + b
- symetria względem środka układu współrzędnych S[0,0] funkcji f(x) -> -f(-x)


