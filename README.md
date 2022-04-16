# Virus

## Introduction et Bibliographie
Aujourd’hui, les virus sont très présents dans notre société, l’exemple le plus marquant reste celui de la covid-19. Ceux-ci se développent dans une société selon divers critères tels que le taux de contagion, le taux de mortalité, le nombre de personnes dans la population …
Nous avons donc cherché, au cours de ce travail, à modéliser la propagation d’un virus dit lambda.

Notre projet a été créé de façon à ce que chaque expérience dépende de paramètres principaux :
- Le taux de contagion
- Le taux de mortalité
- Le nombre d’individus composant la population
- La distance à laquelle une personne peut être contaminée
- Le temps d’immunité maximal
- Le temps de contagion maximal
- Le nombre de personnes infectées au début

Ainsi, notre modèle est assez simple, les individus se déplacent dans leur environnement et à chaque fois qu’ils sont assez proches d’un autre individu, il y a une certaine probabilité que l’autre individu soit contaminé. Puis, au cours de leur contamination, il y a une certaine probabilité pour qu’ils décèdent et à la fin de celle-ci, s'ils ont survécu, ils deviennent immunisés durant un certain temps. 

On peut dès lors remarquer des différences entre notre modèle et celui de Galvan A. et May R. qui se concentre sur le nombre de patients infectés à partir d'un individu unique au sein de la population. Ils utilisent d’ailleurs une règle qui stipule que certains individus peuvent contaminer plus de personnes que d’autres.

Gabriel Guilsou Kolaye, Clive Mbuge, J-C Kamgang et S. Bowong s'intéressent quant à eux à l’impact de l’environnement sur la propagation d’une épidémie et à l’impact des caractéristiques personnelles d’un individu telles que la religion pratiquée, le métier, le genre, la classe sociale…

## Problématique
Un virus peut-il disparaître de lui-même dans une population ?

## Hypothèse principale
Le virus disparaît de lui-même si le taux de contagion est très important et si le taux de mortalité est faible.
Il disparaît également de lui-même si les taux de contagion et de mortalité sont élevés.

## Objectifs
Montrer, avec une simulation informatique, qu'à partir de certains seuils du taux de contagion et du taux de mortalité, le virus en vient à
disparaître complètement au sein de la population.

 
 ## Expériences et résultats
 Pour répondre à notre problématique, nous avons réalisé diverses expériences grâce à notre outil de simulation.

 - Test 1<br/>
 Population: 400<br/>
 Taux de contagion: 100%<br/>
 Taux de mortalité: 100%<br/>
 
<img src="https://user-images.githubusercontent.com/50793868/163190353-59bbb477-7b5c-4215-a285-2596c69e05eb.png" height="384" width="512">
<img src="https://user-images.githubusercontent.com/50793868/163190361-6ee696f9-a411-4937-b628-3150695e18cc.png" height="384" width="512">

 Toute la population a disparu.

 - Test 2<br/>
 Population: 400<br/>
 Taux de contagion: 100%<br/>
 Taux de mortalité: 30%<br/>
 
 <img src="https://user-images.githubusercontent.com/50793868/163190362-730624fe-d2b2-4f41-831c-81df1ccedd1d.png" height="384" width="512">
 <img src="https://user-images.githubusercontent.com/50793868/163190365-db659680-c114-46bc-aca0-fa4cc96385e0.png" height="384" width="512">
 
 Toute la population a disparu.

 - Test 3<br/>
 Population: 400<br/>
 Taux de contagion: 60%<br/>
 Taux de mortalité: 30%<br/>
 
 <img src="https://user-images.githubusercontent.com/50793868/163190367-96ce27c0-e957-4ed5-a3e8-206af76ac38e.png" height="384" width="512">
 <img src="https://user-images.githubusercontent.com/50793868/163190370-c8de16e1-f201-45c9-a312-0ec37538d817.png" height="384" width="512">

 Nombre de survivants: 16

 - Test 4<br/>
 Population: 400<br/>
 Taux de contagion: 20%<br/>
 Taux de mortalité: 80%<br/>
 
 <img src="https://user-images.githubusercontent.com/50793868/163190375-e6e99df8-827e-433e-84a0-baa7effcd095.png" height="384" width="512">
 <img src="https://user-images.githubusercontent.com/50793868/163190378-52e34913-c64a-4a5b-995c-222e37b156a7.png" height="384" width="512">
 
 Nombre de survivants: 21

 - Test 5<br/>
 Population: 400<br/>
 Taux de contagion: 50%<br/>
 Taux de mortalité: 50%<br/>
 
<img src="https://user-images.githubusercontent.com/50793868/163190382-310c1e79-52d0-4a05-8f8f-72876ee89c11.png" height="384" width="512">
<img src="https://user-images.githubusercontent.com/50793868/163190388-7f87bf37-c42e-4ba0-b046-031d8d6e175a.png" height="384" width="512">

 Nombre de survivants: 15

 - Test 6<br/>
 Population: 400<br/>
 Taux de contagion: 90%<br/>
 Taux de mortalité: 30%<br/>
 
 <img src="https://user-images.githubusercontent.com/50793868/163190389-db7377db-8d03-441e-af90-78e5419e3d8d.png" height="384" width="512">
 <img src="https://user-images.githubusercontent.com/50793868/163190392-033aeaf5-b1bd-4f1b-81ad-3b8a02430389.png" height="384" width="512">

 Nombre de survivants: 28

Interprétation de ces résultats: <br/>
Nous pouvons déjà observer que lorsque le taux de contagion est à son maximum (100%), toute
la population en vient à disparaître, que le virus soit très mortel (100%) ou moins mortel (30%).<br/>
Sur les test 3 et 4, nous avons diminué le taux de mortalité, respectivement à 30% et 80% en faisant également varier
le taux de contagion (60% puis 20%). Nous pouvons alors observé que dans le cas d'un faible taux de mortalité et 
d'un fort taux de contagion, ainsi que dans le cas d'un fort taux de mortalité et d'un faible taux de contagion,
le virus en vient à disparaître de lui-même, avant d'avoir éliminé la totalité de la population. <br/>
On peut également noter que le temps avant disparition du virus et bien plus élevé (de l'ordre du double) dans le test 4 que dans le test 3.<br/>
Pour le test 5, nous avons réalisé une simulation équilibrée (50% de taux de contagion, 50% de taux de mortalité), et nous
avons également pu observer que le virus en vient à disparaître de lui-même, après plusieurs vagues épidémiques.<br/>
Enfin, le test 6 permet de montrer que lorsque le taux de contagion est extrêmement élevé (90%) mais que le taux de mortalité
est bien moins important (30%), le virus disparaît de lui même très rapidement (en l'occurence après une seule vague).

 ## Conclusion
 Nous pouvons alors invalider la première hypothèse, qui dit que le virus en vient à disparaître lorsque le taux de contagion est très
 élevé. En effet, nous avons remarqué que pour un taux de mortalité à son maximum (100%), comme pour un taux beaucoup plus bas (30%), toute la
 population a disparu à la fin de la simulation. En revanche, le deuxième hypothèse peut être considérée comme validée, cas nous
 avons observé que dans toutes les autres situations, le virus en est venu à disparaître complètement avant que toute la population n'ait disparu.
 
 
 ## Souces principales
- A., Galvani, et May R. « Comment se propage une épidémie ». Revue Francophone 	des Laboratoires, vol. 2006, no 379, février 2006, p. 16‑17. ScienceDirect, 		https://doi.org/10.1016/S1773-035X(06)80075-4.

- KOLAYE, Gabriel Guilsou, et al. Modélisation et simulation multi-agent de la 		propagation d’une épidémie de choléra: cas de la ville de Ngaoundéré. janvier 		2020. HAL Archives Ouvertes, https://hal.archives-ouvertes.fr/hal-02460282. 
 
 ## Prérequis
 - Python 3
 - Pygame
 - Matplotlib
 - Datetime
