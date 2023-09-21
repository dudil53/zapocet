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

TKTABLE() je třída reprezentující hrací stůl. Při zavolání zadáme počet hráčů u stolu - stůl pak vytvoří spojový seznam hráčů a dealera uloží do self.dealer, zároveň jim rozdá zadaná jména a peníze

Třídové funkce:

   **refresh**


   **blinds**

   **deal**

   **ready_to_bet**

   **bet**

   **flop**

   **turn_river**

   **check_table**

   **just_one_player**

   **clear_table**

   **close**

   **check_for_winners**



# funkce


# 
