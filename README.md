# zapocet
Zápočtový program z předmětu Programování 2 na MFF UK Praha. Autor: Adam Fürstenzeller

**PROGRAM ZAPNETE SPUŠTĚNÍM poker.py**
**ve složce cards jsou všechny POTŘEBNÉ obrázky**

# Obecně
Můj zápočtový program je hra Poker Texas Hold'em. Je to hra pro více hráčů a funguje stylem pass and play - jednotlivý hráči si mezi sebou po každém tahu posílají zařízení, na kterém hrají. Při předání hry dalšímu hráči se zakryjí všechny karty v ruce. Pravidla hry jsou klasická pravidla Pokeru Texas Hold'em (případně k přečtení například zde: https://www.fyft.cz/hry-clanky/texas-holdem-poker-pravidla/)


# Start hry
Spuštěním programu se dostaneme do hlavního menu, kde si můžeme vybrat počet hráčů a počáteční stav peněz / small a big blindů. Jednotlivý hráči si mohou určit jména/přezdívky a po zapnutí hry bude každému hráči přiřazen 'avatar'. Po tom, co si hráči vyberou možnosti hry, které chtějí můžou zmáčknout tlačítko 'Start Game' a tím začne samotná hra s vybraným počtem hráčů.

# Průběh hry
Tlačítko 'Start Game' nás přesune do herního rozhraní, kde před sebou vidíme pouze jedno tlačítko 'NEXT'. Prvním stisknutím tohoto tlačítka se rozdají hráčům karty. Druhým stisknutím začne první kolo sázek tzv. pre-flop. V této fázi hry se po směru hodinových ručiček v sázení prostřídají všichni hráči - jak je tomu klasicky při pokeru - small a big blind se automaticky vsadí a tedy první kolo se sázením začíná hráč po big blindovi. Hráč, který je právě na tahu je zvýrazněn tím, že jeho jméno se na obrazovce rozsvítí zeleně. Po tom co hráč odehraje svůj tah, zneviditelní se jeho karty, zmizí 'akční/tahová' tlačítka a na obrazovce zůstane pouze tlačítko 'NEXT'. Zároveň se rozsvítí jméno následujícího hráče. V tento moment by si zařízení měl převzít hráč jehož jméno se rzsvítilo - tedy hráč, který teď bude na tahu. Ten si stisknutím tlačítka 'NEXT' odkryje své karty a může hrát.

Po tom, co je odehráno celé první kolo, zůstane na obrazovce opět pouze tlačítko 'NEXT'. Stisknutím tohoto tlačítka se objeví nová karta na stole - tzv. turn. Následným stisknutím tlačítka 'NEXT' se spustí další kolo sázek - tentokrát se začína od prvního hráče po 'dealerovi', tedy od small blinda.

Po dalším kole sázek zůstane opět pouze tlačítko 'NEXT', stisknutím se na stole objeví poslední karta - tzv. river. Další stisknutím tlačítka 'NEXT' se spustí poslední kolo sázek.

Po posledním kole sázek se vyhodnotí situace na stole a program určí vítěze - jejich jména se objeví na obrazovce dohromady s obnosem peněz, které vyhrál a s kombinací, kterou výherci měli. Vyhrané peníze se připíší vítězům, karty zmizí ze stolu a rukou jednotlivých hráčů a začne nové kolo.

# Konec hry
Hra se dá kdykoliv ukončit stisknutím tlačítka na zavření okna, ve kterém se hra hraje.

