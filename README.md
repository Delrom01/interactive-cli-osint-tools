# interactive-cli-osint-tools
Create an interactive cli of OSINT tools

### Description
Pour mon projet d'UTC503 du CNAM, j'ai décidé de créer un CLI interactif d'outils OSINT. 
L'idée c'est d'avoir un seul outil à lancer (lors d'un CTF par exemple) pour ensuite accéder à d'autres, au lieu de tous les retenir.

On retrouve donc dans le CLI la liste des outils avec leur description. Leur utilisation est ensuite guidée est assistée.

### Organisation
Pour le moment, je 3 outils de @megadose et d'autres outils. Disponibles sur PyPi, je les ai installés avec la commande pip (comme toutes les bibliothèques utilisées dans le script). Ainsi, nous avons simplement qu'à récupérer les fichiers .py et lancer un pip install de requirement.txt pour que tout soit correctement installé.

2 fichiers sont nécessaires pour faire fonctionner le CLI :

  - commands.py : qui contient une classe Commands définissant toutes les fonctions du CLI. C'est dans ce fichier qu'on ajoutera le code d'un nouvel outil.
  - cli_list_exe.py ou cli_input_exe.py : qui contient le code de l'interface CLI à générer du fichier commands.py. Nous avons 2 types de CLI : l'un où les outils sont         
    appelés par saisie au clavier (avec système d'autocomplétion), et l'autre où les outils sont sélectionnés parmi une liste à l'aide des flèches du clavier.    
    
    Seulement quelques lignes de codes diverses entre ces 2 scripts python afin de changer le mode de sélection (saisie au clavier ou saisie par déplacement de 
    curseur)

### Autre 
