# interactive-cli-osint-tools
Create an interactive CLI of OSINT tools

### Description
Pour mon projet d'UTC503 du CNAM, j'ai décidé de créer un CLI interactif d'outils OSINT. 
L'idée c'est d'avoir un seul outil à lancer (lors d'un CTF par exemple) pour ensuite accéder à d'autres (au lieu de retenir tous les différents outils OSINT et de les lancer individuellement).

On retrouve donc dans le CLI la liste des outils avec leur description. Leur utilisation est ensuite guidée et assistée.

### Organisation
À l'heure actuelle, le CLI compte 5 outils : 3 de @megadose et 2 autres basiques et communs dans le domaine de l'OSINT. 

2 fichiers sont nécessaires pour faire fonctionner le CLI :

  - ```commands.py``` : qui contient une classe ```Commands()``` définissant toutes les fonctions du CLI. C'est dans ce fichier qu'on ajoutera le code d'un nouvel outil.
  - ```cli_list_exe.py``` ou ```cli_input_exe.py``` : qui contient le code de l'interface CLI à générer du fichier ```commands.py```. 
    
    Nous avons 2 types de CLI : l'un où les outils sont appelés par saisie au clavier avec système d'autocomplétion (cli_input_exe), et l'autre où les outils sont   sélectionnés parmi une liste à l'aide des flèches du clavier (cli_list_exe).    
    
    Seulement quelques lignes de codes diverses entre ces 2 scripts python afin de changer le mode de sélection (saisie au clavier ou sélection graphique)

### Installation 
Les outils présents dans le CLI sont disponibles sur PyPi, je les ai donc installés avec la commande ```pip``` (comme toutes les bibliothèques utilisées dans ces scripts). 

Ainsi, pour l'installation du CLI, nous avons simplement qu'à :
1. Cloner le dépôt github pour récupérer les fichiers .py ainsi que la documentation : ```git@github.com:Delrom01/interactive-cli-osint-tools.git```
2. Se déplacer dans le dossier du projet : ```cd ./interactive-cli-osint-tools/```
3. Lancer ```pip install -r requirements.txt``` pour que tous les outils nécessaires au CLI s'installent

### Utilisation 
Pour lancer le CLI, il suffit d'exécuter la commande suivante : ```python3 cli_list_exe.py``` ou ```python3 cli_input_exe.py``` (suivant le type de CLI souhaité), et de se laisser guider. Exemple : 

![Exemple_1](relative/path/to/img.jpg?raw=true "Exemple d'utilisation (1)")

![Exemple_2](relative/path/to/img.jpg?raw=true "Exemple d'utilisation (2)")

Une [Documentation](https://github.com/Delrom01/interactive-cli-osint-tools/blob/main/Doc/_build/html/index.html) est également disponible. Une fois le dépôt cloné, on peut y accéder via le lien suivant : ```file://<path>/interactive-cli-osint-tools/Doc/_build/html/commands.html``` dans un navigateur comme Firefox.
