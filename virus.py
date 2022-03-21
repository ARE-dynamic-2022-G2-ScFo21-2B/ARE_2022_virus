import pygame, random
from math import sqrt

pygame.init()

WINDOW_RESOLUTION = (900, 900)
NB_POPULATION = 100

TAUX_MORTALITE = 0
TAUX_INFECTION = 0
TAUX_IMMUNITE = 0

TEMPS_INFECTION_MAX = 0
TEMPS_IMMUNITE_MAX = 0




screen = pygame.display.set_mode(WINDOW_RESOLUTION)
pygame.display.set_caption("Propagation épidémie")
power = True
clock = pygame.time.Clock()
blanc = (255, 255, 255)
rose = (240, 180, 195)
rouge = (255, 0, 0)

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
    return dico

# Fonction permettant d'initialiser la population avec NB_POPUATION agents
def initialisation_population():
    dico = {}
    for i in range(NB_POPULATION):
        dico = creation_agent()
        liste_agents.append(dico)

# Fonction permettant de modifier les coordonnées selon un mouvement prédéfini
def modifier_coordonnees():
    for i in range(int((80/100)*NB_POPULATION)):
        n = random.randint(0, len(liste_agents)-1)
        #nx = random.randint(liste_agents[n]['x']-2, liste_agents[n]['x']+2)
        #ny = random.randint(liste_agents[n]['y']-2, liste_agents[n]['y']+2)
        if(liste_agents[n]['wait'] > 0):
            liste_agents[n]['wait'] -= 1
        else:
            nx = (liste_agents[n]['dest'][0] - liste_agents[n]['x'])/200 + liste_agents[n]['x']
            ny = (liste_agents[n]['dest'][1] - liste_agents[n]['y'])/150 + liste_agents[n]['y']
            if(sqrt((nx - liste_agents[n]['dest'][0])**2 + (ny - liste_agents[n]['dest'][1])**2) < 10):
                liste_agents[n]['dest'] = (random.randint(0, WINDOW_RESOLUTION[0]), random.randint(0, WINDOW_RESOLUTION[1]))
                liste_agents[n]['wait'] = random.randint(10, 100)
            liste_agents[n]['x'] = nx
            liste_agents[n]['y'] = ny


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
    screen.fill(blanc)
    modifier_coordonnees()
    liste_x, liste_y = actualisation_coordonnees()
    for i in range(len(liste_agents)):
        pygame.draw.circle(screen, rose, (int(liste_x[i]), int(liste_y[i])), 5)

def main():
    global power
    initialisation_population()
    while power:
        actualisation()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                power = False
        pygame.display.flip()
        clock.tick(60)

main()