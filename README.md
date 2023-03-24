# Rasberry pi PICO

Ce projet est un exemple d'application web créée avec le framework JavaScript Nuxt.js et le CMS Strapi. Il s'agit d'un site simple présentant des projets personnels, chacun avec une image, une description et des technologies utilisées.

Ce projet consiste en un capteur d'accélération qui communique avec un serveur en local via un Raspberry Pi Pico. Le serveur est géré par un fichier Python nommé main.py et le client est développé en utilisant npm pour lancer le projet et une page index.html.

Pour faire fonctionner le Raspberry Pi Pico, il suffit de lancer le fichier main.py côté serveur. Cela permettra d'établir une connexion avec le client et de commencer à envoyer les données du capteur d'accélération.

Bien sur il faudra installer les packages avec la commande :
```npm i```

Le client peut être lancé en utilisant la commande :
```npm start```

Une fois le client lancé, accédez à la page index.html pour interagir avec le capteur d'accélération. Appuyez sur le bouton pour commencer à envoyer les données du capteur, et utilisez le bouton de la page web pour actualiser les scores que vous avez obtenus.

N'oubliez pas de connecter correctement votre Raspberry Pi Pico à votre ordinateur avant de lancer le serveur. Vous devrez également installer les dépendances requises pour le projet en utilisant npm.

Ce projet a été développé pour une utilisation en local uniquement. Assurez-vous que votre environnement de développement est correctement configuré avant de lancer le projet.

### Test sans server
    
<https://youtu.be/fVHhYoNw5x4>

### Test avec server

<https://youtu.be/t3BgHYDhlmg>

### Cablage

<https://youtu.be/L-GzW126JnM>