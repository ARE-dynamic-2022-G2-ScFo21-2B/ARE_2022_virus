# Virus

## Introduction et Bibliographie
Aujourd’hui, les virus sont très présents dans notre société, l’exemple le plus marquant reste celui de la covid-19. Ceux-ci se développent dans une société selon divers critères tels que le taux de contagion, le taux de mortalité, le nombre de personnes dans la population…
Nous avons donc cherché, au cours de ce travail, à modéliser la propagation d’un virus dit lambda.

Notre projet a été créé de façon à ce que chaques expériences dépendent de paramètres principaux :
- Le taux de contagiosité
- Le taux de mortalité
- Le nombre d’individus composants la population
- La distance à laquelle une personne peut être contaminée
- Le temps d’immunité maximal
- Le temps de contagion maximal
- Le nombre de personnes infectées au début

Ainsi, notre modèle est assez simple, les individus se déplacent dans leur environnement et à chaque fois qu’ils sont assez proches d’un autre individu, il y a une certaine probabilité que l’autre individu soit contaminé. Puis au cours de lors contamination, il y a une certaine probabilité pour qu’ils décèdent et à la fin de celle-ci, s'ils ont survécu, ils deviennent immunisés durant un certain temps. 

On peut dès lors remarquer des différences entre notre modèle et celui de Galvan A. et May R. qui se concentre sur le nombre de patients infectés à partir d'un individu unique au sein de la population. Ils utilisent d’ailleurs une règle qui stipule que certains individus peuvent contaminer plus de personnes que d’autres.

Gabriel Guilsou Kolaye, Clive Mbuge, J-C Kamgang et S. Bowong s'intéressent quant à eux à l’impact de l’environnement sur la propagation d’une épidémie et à l’impact des caractéristiques personnelles d’un individu telles que la religion pratiquée, le métier, le genre, la classe sociale…

## Problématique
Un virus peut-il disparaître de lui-même dans une population ?

## Hypothèse principale
Le virus disparaît de lui-même si le taux de contagiosité est très important et si le taux de mortalité est faible.
Il disparaît également de lui-même si les taux de contagiosité et de mortalité sont élevés.

## Objectifs
Montrer, avec une simulation informatique, qu'à partir de certains seuils du taux de contagiosité et du taux de mortalité, le virus en vient à
disparaître complètement au sein de la population.

 
 ## Expériences et résultats
 
 ## Conclusion
 
 ## Prérequis
 - Python 3
 - Pygame
 - Matplotlib
 - Datetime

