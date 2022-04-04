import pygame, random
from math import sqrt
from datetime import datetime

pygame.init()

WINDOW_RESOLUTION = (900, 900)
NB_POPULATION = 400

TAUX_MORTALITE = 90
TAUX_INFECTION = 70


TEMPS_INFECTION_MAX = 25
TEMPS_IMMUNITE_MAX = 25

NOMBRE_INFECTE_DEBUT = 5
DISTANCE_CONTAMINATION = 50



nb_mort = 0
nb_infecte = NOMBRE_INFECTE_DEBUT
screen = pygame.display.set_mode(WINDOW_RESOLUTION)
pygame.display.set_caption("Propagation épidémie")
power = True
clock = pygame.time.Clock()
blanc = (255, 255, 255)
rose = (240, 180, 195)
rouge = (255, 0, 0)
bleu = (0, 0, 250)
vert = (0, 255, 25)
seconde = int(datetime.now().strftime("%S"))

liste_agents = []
liste_x = []
liste_y = []

# Fonction permettant la création d'un agent
def creation_agent():
    dico = {}
    x = random.randint(0, WINDOW_RESOLUTION[0])
    y = random.randint(0, WINDOW_RESOLUTION[1])
    dico['x'] = x
    dico['y'] = y
    dico['dest'] = (random.randint(0, WINDOW_RESOLUTION[0]), random.randint(0, WINDOW_RESOLUTION[1]))
    dico['wait'] = random.randint(10, 100)
    dico["infection"] = 0
    dico["immunite"] = 0
    dico["test_mortalite"] = 0
    return dico

# Fonction calculant la distance entre deux agents
def distance(agent1, agent2):
    return sqrt((agent1['x'] - agent2['x'])**2 + (agent1['y'] - agent2['y'])**2)

# Fonction permettant d'initialiser la population avec NB_POPULATION agents
def initialisation_population():
    dico = {}
    for i in range(NB_POPULATION):
        dico = creation_agent()
        liste_agents.append(dico)
    for i in range(NOMBRE_INFECTE_DEBUT):
        n = random.randint(0, NB_POPULATION-1)
        liste_agents[n]["infection"] = random.randint(5, TEMPS_INFECTION_MAX)
        liste_agents[n]["immunite"] = random.randint(5, TEMPS_IMMUNITE_MAX)
        liste_agents[n]["test_mortalite"] = 1

# Fonction permettant de modifier les coordonnées selon un mouvement prédéfini
def modifier_coordonnees():
    for i in range(int((80/100)*NB_POPULATION)):
        n = random.randint(0, len(liste_agents)-1)
        if(liste_agents[n]['wait'] > 0):
            liste_agents[n]['wait'] -= 1
        else:
            nx = (liste_agents[n]['dest'][0] - liste_agents[n]['x'])/150 + liste_agents[n]['x']
            ny = (liste_agents[n]['dest'][1] - liste_agents[n]['y'])/150 + liste_agents[n]['y']
            if(sqrt((nx - liste_agents[n]['dest'][0])**2 + (ny - liste_agents[n]['dest'][1])**2) < 50):
                liste_agents[n]['dest'] = (random.randint(0, WINDOW_RESOLUTION[0]), random.randint(0, WINDOW_RESOLUTION[1]))
                liste_agents[n]['wait'] = random.randint(10, 100)
            liste_agents[n]['x'] = nx
            liste_agents[n]['y'] = ny

# Fonction gérant les contaminations et l'immunité
def contamination():
    for i in liste_agents:
        if i["infection"] > 0:
            for j in liste_agents:
                if ((j["infection"] == 0) and (j["immunite"] == 0) and (distance(i, j) < DISTANCE_CONTAMINATION)):
                    n = random.randint(1, 100)
                    if n <= TAUX_INFECTION:
                        j["infection"] = random.randint(5, TEMPS_INFECTION_MAX)
                        j["immunite"] = random.randint(5, TEMPS_IMMUNITE_MAX)
                        j["test_mortalite"] = 1
        if ((i["infection"] == 0) and (i["immunite"] > 0)):
            i["immunite"] -= 1

# Fonction gérant la mortalité
def mortalite():
    global nb_mort, NB_POPULATION, nb_infecte
    nb_infecte = 0
    for i in liste_agents:
       if i["infection"] > 0:
            nb_infecte += 1
            i["infection"] -= 1
            if i["test_mortalite"] == 1:
                n = random.randint(1, i["infection"])
                if (n == 1):
                    i["test_mortalite"] = 0
                    p = random.randint(1, 100)
                    if p <= TAUX_MORTALITE:
                        liste_agents.remove(i)
                        NB_POPULATION -= 1
                        nb_mort += 1
                        print(nb_mort)
        

            

# Fonction permettant d'actualiser les coordonnées dans les deux listes x et y afin de pouvoir tracer un point
def actualisation_coordonnees():
    liste_x = []
    liste_y = []
    for i in liste_agents:
        liste_x.append(i['x'])
        liste_y.append(i['y'])
    return liste_x, liste_y


# Fonction permettant d'actualiser le programme et de tracer les nouveaux points
def actualisation():
    global seconde
    screen.fill(blanc)
    if ((int(datetime.now().strftime("%S")) - seconde >= 1) or (int(datetime.now().strftime("%S")) - seconde < 0)):
        seconde = int(datetime.now().strftime("%S"))
        contamination()
        mortalite()
    modifier_coordonnees()
    liste_x, liste_y = actualisation_coordonnees()
    for i in range(len(liste_agents)):
        if (liste_agents[i]["infection"] > 0):
            point_couleur = rouge
        elif (liste_agents[i]["immunite"] > 0):
            point_couleur = vert
        else:
            point_couleur = bleu
        pygame.draw.circle(screen, point_couleur, (int(liste_x[i]), int(liste_y[i])), 5)

def test_fin():
    global nb_mort, nb_infecte
    if NB_POPULATION == 0:
        print("Toute la population est morte")
        print(f"Nombre de morts: {nb_mort}")
        return 0
    if nb_infecte == 0:
        print("Le virus a disparu")
        print(f"Nombre de survivant: {NB_POPULATION}")
        return 0
    return 1

def main():
    global power
    initialisation_population()
    while power:
        actualisation()
        power = test_fin()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                power = False
        pygame.display.flip()
        clock.tick(60)

main()