# Tennis Ball Collector

Ceci est un template de dépôt Git pour le cours d'ingénierie système et modélisation robotique à l'ENSTA Bretagne en 2023.


## Lancer la simulation

### Dépendences

- Import sam_bot model :

```bash
cd ~/ros2_ws/src
git clone https://github.com/ros-planning/navigation2_tutorials.git
cd navigation2_tutorials/
rm -r nav2_*
cd ../..
colcon build
```


### Démarrer la simulation

###### A compléter avec la/les commande(s) à lancer.
```bash
# TODO
```


## Groupe

### Membres

Thomas TACHERON

Jonas SOUEIDAN

Rémi POREE

Simon GERVAISE

### Gestion de projet

[Taiga](https://tree.taiga.io/project/thomastacheron-collecteballe/timeline)



## Structure du dépôt

Ce dépôt doit être cloné dans le dossier `src` d'un workspace ROS 2.

### Package `tennis_court`

Le dossier `tennis_court` est un package ROS contenant le monde dans lequel le robot ramasseur de balle devra évoluer ainsi qu'un script permettant de faire apparaître des balles dans la simulation.
Ce package ne doit pas être modifié.
Consulter le [README](tennis_court/README.md) du package pour plus d'informations.


### Documents

Le dossier `docs` contient tous les documents utiles au projet:
- Des [instructions pour utiliser Git](docs/GitWorkflow_fork.md)
- Un [Mémo pour ROS 2 et Gazebo](docs/Memo_ROS2.pdf)
- Les [slides de la présentation Git](docs/GitPresentation.pdf)


### Rapports

Le dossier `reports` doit être rempli avec les rapports d'[objectifs](../reports/GoalsTemplate.md) et de [rétrospectives](../reports/DebriefTemplate.md) en suivant les deux templates mis à disposition. Ces deux rapports doivent être rédigés respectivement au début et à la fin de chaque sprint.

### Package `tennis_bot_description`

Le dossier `tennis_bot_description` est un package ROS permettant de 

Lancer le terrain avec le model sam_bot :

```bash
ros2 launch tennis_bot_description spawner_sam.launch.py 
```

Lancer le terrain avec le model tennis_bot :

```bash
ros2 launch tennis_bot_description spawner.launch.py 
```