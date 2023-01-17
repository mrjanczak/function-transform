# Wstęp:
Przekształcenie funkcji podstawowej f(x) do funkcji złożonej g(x) można traktować jako dwa oddzielne przekształcenia przeprowadzone na argumencie i na funkcji. 
Podstawowe przekształcenia opisane są na stronie:

[https://pl.wikibooks.org/wiki/Matematyka_dla_liceum/Funkcje_i_ich_w%C5%82asno%C5%9Bci/Przekszta%C5%82canie_wykresu_funkcji]

Z czysto artmetycznego punktu widzenia kolejność tych przekształceń nie ma znaczenia: n.p. funkcję złożoną g(x) = f(|x|+1) możemy z powodzeniem otrzymać na 2 sposoby:

```f(x) -> f(|x|) -> f(|x|+1)```

oraz

```f(x) -> f(x+1) -> f(|x|+1)```

Na koniec otrzymujemy przecież tę samą funkcję.

Jednakże jeśli chcemy **WYZNACZYĆ GRAFICZNIE** wykres funkcji g(x) na drodze kolejnych przekształceń podstawowych, **MUSIMY** stosować określoną **KOLEJNOŚĆ**, 
w przeciwnym razie nasze graficzne przekształcenia będą błędne! Przykładowo przekształcenie:

```f(x) -> f(|x|) -> f(|x|+1)```

nie będzie translacją, co widać na wykresie (załóżmy f(x) = x**2 (2-ga potęga x)):

![Figure_1](https://user-images.githubusercontent.com/6569984/212870332-2760f47e-ccb3-4f11-ab06-bdd263118e4c.png)

# Kolejność
Zasady ustalające właściwą kolejność przekształceń są całkowicie różne dla przekształceń na argumencie i na funkcji.

### PRZEKSZTAŁCENIA NA ARGUMENCIE

Przy przekształceniach na argumencie obowiązuje zasada **"działań tylko na czystym x"**.

Wprowadźmy następujące rozróżnienie:
- x bez minusa i wartości bezwzględnej nazwijmy **czystym x**
- -x lub |x| nazwijmy **przekształconym x**

Aby poprawnie przekształcić argument, każde kolejne przekształcenie musi być wykonane na czystym x. Mówiąc obrazowo dodany operator (tj. +, -, ×, | |) musi stykać się z czystym symbolem x. I tak:

```f(x) -> f(|x|) -> f(|x|+1)```

jest błędne, bo +1 dodane jest do **przekształconego |x|**

```f(x) -> f(x+1) -> f(|x|+1)```

jest poprawne, bo operacja *wartość bezwzględna* wykonana jest na **czystym x**

Można zauważyć, że operacje najbardziej oddalone od x muszą być wykonane jako pierwsze. Na poniższym przykładzie:

```
f(x)        - funkcja podstawowa, gdzie np. f(x) = x**2 (2-ga potęga)
f(x+1)      - dodajemy +1 do czystego x - **T[-1,0]**
f(-x+1)     - mnożymy czysty x przez -1 - **S.OY**
f(-|x|+1)   - wyciągamy wartość bezwzg. z czystego x - **S.cz.OY**
f(-|x+3|+1) - dodajemy +3 do czystego x - **T[-3,0]**
```

widać, że operacja +1 stojąca niejako na końcu musi być wykonana jako pierwsza, aby wszytkie przekształcenia na wykresie były poprawne:

![Figure_3](https://user-images.githubusercontent.com/6569984/212886355-d198f9ac-ea32-44ee-a42c-f4cb794210c3.png)

### PRZEKSZTAŁCENIA NA FUNKCJI

Przy przekształceniach na funkcji obowiązuje zasada **"operacji tylko na całej funkcji"** - 
kolejne przekształcenia muszą być wykonane na całej funkcji, a nie tylko na jej części, 
mówiąc obrazowo przyłączają się one do funkcji, stopniowo coraz bardziej ją wydłużając. 
Poniższe przekształcenie:

```f(x)+1 -> -f(x)+1```

jest błędne, bo mnożenie przez -1 wykonaliśmy tylko na części funkcji, 
a wyraz +1 pozostał niejako pominięty - w efekcie symetria całkowita na wykresie nie jest wzg. osi OX:

![Figure_4](https://user-images.githubusercontent.com/6569984/212887645-907c1f6d-b812-4d7a-9b42-ef081e3588bf.png)

```-f(x)  -> -f(x)+1 ```

jest poprawne, bo dodawanie (+1) wykonane jest na całej funkcji (-f(x)).

Podobnie jest z modułem ( wartością bezwzg.). Przekształcenia:

```f(x)+1  ->  f(x)+1 -2 -> |f(x)+1| -2```

są błedne, bo po dodaniu modułu, 
wyraz -2 pozostaje "poza" ostatnim przekształceniem (modułem), 
mówiąc obrazowo dzielimy wtedy funkcję na dwie mniejsze - 
symetria częściowa na wykresie nie jest wzg. osi OX:

![Figure_5](https://user-images.githubusercontent.com/6569984/212888822-16dc6370-f3d9-4d4d-be9c-6d3034e03bf5.png)

```f(x)+1  ->  |f(x)+1|  -> |f(x)+1| -2```

jest poprawne, bo każde kolejne przekształcenie modyfikuje **całą** funkcję.


### PRZEKSZTAŁCENIA NA ARGUMENCIE I FUNKCJI

Niektóre przekształcenia na argumencie i funkcji można wykonać równocześnie pod warunkiem, że przestrzegamy odpowiednio obu powyższych zasad:
- translacja T o wektor [a, b] funkcji f(x) -> f(x - a) + b
- symetria względem środka układu współrzędnych S[0,0] funkcji f(x) -> -f(-x)

Przeanalizujmy poniższy przykład:
```
f(x)
f(x+1)              - dodajemy +1 do czystego x - T[-1,0]
-f(-x+1)            - mnożymy przez -1 argument i funkcjię - Symetria wzg. początku uk. współ. S[0,0]
-f(-|x|+1)          - wyciągamy wartość bezwgl. z czystego argumentu - S.cz.OY
-f(-|x+2|+1)+1      - dodajemy +2 do czystego argumentu i +1 do całej funkcji - T[-2,1]
|-f(-|x+2|+1)+1|    - wart. bezwg. z całej funkcji - S.cz.OX
|-f(-|x+2|+1)+1|-1  - odejmujemy -1 od całej funkcji - T[0,-1]
```
![Figure_6](https://user-images.githubusercontent.com/6569984/212892374-48da9d34-7b26-472e-8e17-071361607f10.png)

Przekształcenia **S[0,0]** i **T[-2,1]** zawierają operacje zarówno na argumencie, jak i funkcji. Jednak w obu wypadkach 
zachowane są zasady odpowiednio operacji na **czystym x** i **na całej funkcji**.
