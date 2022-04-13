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
 ![test_1_a](https://user-images.githubusercontent.com/50793868/163190353-59bbb477-7b5c-4215-a285-2596c69e05eb.png) ![test_1_b](https://user-images.githubusercontent.com/50793868/163190361-6ee696f9-a411-4937-b628-3150695e18cc.png)
![test_2_a](https://user-images.githubusercontent.com/50793868/163190362-730624fe-d2b2-4f41-831c-81df1ccedd1d.png)
![test_2_b](https://user-images.githubusercontent.com/50793868/163190365-db659680-c114-46bc-aca0-fa4cc96385e0.png)
![test_3_a](https://user-images.githubusercontent.com/50793868/163190367-96ce27c0-e957-4ed5-a3e8-206af76ac38e.png)
![test_3_b](https://user-images.githubusercontent.com/50793868/163190370-c8de16e1-f201-45c9-a312-0ec37538d817.png)
![test_4_a](https://user-images.githubusercontent.com/50793868/163190375-e6e99df8-827e-433e-84a0-baa7effcd095.png)
![test_4_b](https://user-images.githubusercontent.com/50793868/163190378-52e34913-c64a-4a5b-995c-222e37b156a7.png)
![test_5_a](https://user-images.githubusercontent.com/50793868/163190382-310c1e79-52d0-4a05-8f8f-72876ee89c11.png)
![test_5_b](https://user-images.githubusercontent.com/50793868/163190388-7f87bf37-c42e-4ba0-b046-031d8d6e175a.png)
![test_6_a](https://user-images.githubusercontent.com/50793868/163190389-db7377db-8d03-441e-af90-78e5419e3d8d.png)
![test_6_b](https://user-images.githubusercontent.com/50793868/163190392-033aeaf5-b1bd-4f1b-81ad-3b8a02430389.png)

 ## Conclusion
 
 ## Souces principales
- A., Galvani, et May R. « Comment se propage une épidémie ». Revue Francophone 	des Laboratoires, vol. 2006, no 379, février 2006, p. 16‑17. ScienceDirect, 		https://doi.org/10.1016/S1773-035X(06)80075-4.

- KOLAYE, Gabriel Guilsou, et al. Modélisation et simulation multi-agent de la 		propagation d’une épidémie de choléra: cas de la ville de Ngaoundéré. janvier 		2020. HAL Archives Ouvertes, https://hal.archives-ouvertes.fr/hal-02460282. 
 
 ## Prérequis
 - Python 3
 - Pygame
 - Matplotlib
 - Datetime

