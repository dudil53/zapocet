# DOKUMENTACE

# GUI
K vytvoření Graphical User Interface jsem používal knihovnu Tkinter a PILLOW na vkládání obrázků



# třídy
**1. START()**
   
   'START' je třída, kterou volám na začátku programu. Má pouze jeden parametr root - okno tkinteru které vytvoříme.
   
   Třídové funkce:
   
   **__init__**
   
   ve funkci init vytvářím GUI hlavního menu: tlačítka 'START GAME' a 'QUIT GAME' (ty spouští jiné funkce při stisknutí), boxy pro jména hráčů, posuvné volení počtu hráčů a dropdown menu na volbu peněz
   tlačítka ukládám jako atributy třídy - self.button, abych na ně mohl jednoduše odkazovat v ostatních třídových funkcích

   **player_nr_update**

   tato funkce slouží k aktualizaci počtu hráčů, zobrazení nových boxů na jména popřípadě odstranění nadbytečných. Počet hráčů funkce uloží do proměnné self.nr_of_players pro další práci

   **buy_in_update**

   podobně jako předchozí funkce, tato funkce aktualizuje dropdown menu možností buy-inů a ukládá vybranou možnost do proměnné self.blinds_var

   **start_game**

   poslední a nejdůležitější třídová fce start_game - tato funkce posbírá informace o počtu a jménech hráčů a buy-inu. Potom vytvoří objekt self.table = TKTABLE() -- zavolá třídu samotného 'hracího stolu'. Zároveň odevzdá všechny informace potřebné ke hře a zničí úvodní menu.

**2. PLAYER()**

Objekt PLAYER() používám jako nody cyklického spojového seznamu znázorňující to, jak za sebou hráči u stolu hrají. Konec i začátek je v objektu DEALER() - tak poznáme, že už hráli všichni. Při odehrávání sázek potom procházím skrz tento spojový seznam a v každé nodě se zastavím a zeptám se hráče na tah, který chce odehrát.

Tato třída je velice jednoduchá - opravdu se jedná jen o nody spojového seznamu s pár specialními prvky:

   self.hand - karty hráče

   self.cash - peníze hráče

   self.position - pozice hráče. funkuje k identifikaci hráčů

   a další atributy, které jsou vesměs podobné self.hand - mají hráčovi karty a karty na stole atd.

**4. DEALER()**

Objekt DEALER() slouží jako konečná a záchytná noda spojového seznamu hráčů. Je vytvořen pouze jeden a uložen v TKTABLE.dealer
   
**6. TKTABLE()**

TKTABLE() je třída reprezentující hrací stůl. Při zavolání zadáme počet hráčů u stolu - stůl pak vytvoří spojový seznam hráčů a dealera uloží do self.dealer, zároveň jim rozdá zadaná jména a peníze. V funkci __init__ je zároveň hodně práce s GUI.

Třídové funkce:

   **refresh**

Tato funkce slouží k aktualizaci toho co vidíme na obrazovce - schování a zviditelnění karet hráčů.

   **blinds**

Tato funkce se spustí na začátku každé nové hry. Projde hráče a od dvou prvních, kteří mají peníze, vybere small a big blind.

   **deal**

Tato funkce projde spojový seznam hráčů a rozdá každému do ruky dvě karty - z balíčku, který je uložený jako atribut stolu. Na začátku každého kola se vytvoří a zamíchá nový balíček karet pomocí dalších funkcí.

   **ready_to_bet**

Funkce, která proběhne spojový seznam hráčů a připraví je do pozice, ve které můžou sázet. (změní self.played na False). Funkce se volá vždy před funkcí bet.

   **bet**

Funkce na sázení. Prochází postupně celý spojový seznam hráčů a každého se ptá na tah: všechna tlačítka na obrazovce mění stejnou proměnnou self.action_var, na tuto změnu program čeká pomocí .wait_variable(self.action_var) - každé tlačítko tuto proměnnou změní na jiný string, podle toho jaká akce má být vykonána. 

Funkci řekneme jestli je preflop nebo ne - podle toho sázení buď přeskočí small a big blinda nebo ne

Když funkce projde celý spojový seznam, zkontroluje, jestli každý hráč má vsazeno stejně - nebo nejvíc co může. Pokud ne, spustí druhé kolo sázek dokud se situace neopraví.

   **flop**

Tato funkce rozdá karty na flop - první tři.

   **turn_river**
   
Tato funkce přidá vždy jednu kartu na stůl - buď čtvrtou turn a nebo pátou river.

   **check_table**

Tato funkce kontroluje stůl a kolik hráčů je ve hře. Pokud zbývá pouze jeden, skončí kolo a nechá posledního hráče vyhrát
   **just_one_player**

Tato funkce funguje párově s funkcí check_table.

   **clear_table**

Tato funkce projde stůl a vyčistí/připraví ho na další hru - zbaví se karet, vynuluje peníze v potu atd.

   **close**

Tato funkce řeší problém, který nastal při psaní programu - při zavření okna se zasekl celý loop a v cmd pořád běžel. Tato funkce funguje jako callback a vše ukončí při zavření okna.

   **check_for_winners**



# funkce


# 
