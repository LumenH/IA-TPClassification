TP de classification - Debrot Aurélie

Il faut créer les dossiers suivants :
  train/pos
  train/neg
  test/pos
  test/neg

Puis, le script machinLearning.py peut être lancé. Il n'a besoin d'aucun argument.
Ce script permet de préparer les données. Il va les séparer en dans les dossiers test et train suivant les ratios donnés en cours.
Si ce script est exécuté sur Windows, il y a des lignes à décommenter dans la méthode process. Cela concerne l'encodage des fichiers. Après des tests, sous Windows, il
est nécessaire de préciser l'encodage, tandis que sur une machine virutelle avec Ubuntu, ce paramètre d'encodage n'est pas accepté. La ligne sans encodage est celle
actuellement exécutée par le script, la ligne avec encodage est commentée juste en dessous. Il suffira de faire l'échange pour que cela fonctionne sous Windows.

Ensuite, le script classification.py peut être lancé. Il n'a besoin d'aucun argument.
Ce script permet d'effectuer la classification à proprement parler. Il s'inspire du tutoriel vu en cours.
Si ce script est executé sur Windows, la partie Optimisation ne va pas fonctionner.
