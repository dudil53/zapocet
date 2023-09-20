# DOKUMENTACE

# GUI
K vytvoření Graphical User Interface jsem používal knihovnu Tkinter a PILLOW na vkládání obrázků



# třídy
1. START()
   
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
   



# funkce


# 
