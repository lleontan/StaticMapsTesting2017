import pygame
import sys
from io import BytesIO
import urllib.request
screen = pygame.display.set_mode((700,300))



baseUrl="http://dev.virtualearth.net/REST/V1/"
apiKey="&key=AuAaQIpuk55T4X2UIhXfXitbUHHzIJNHlQLK-Y5v5Na_tx5cAz9Fvmw-xUR5oW8T"
callType="Imagery/Map/Road/"
sampleLocation="Bellevue%20Washington?mapLayer=TrafficFlow"


def getImage(location):
    queryString= baseUrl+callType+location+apiKey
    print(queryString)
    urllib.request.urlretrieve(queryString, "helloWorld.jpg")
    image1=pygame.image.load("helloWorld.jpg")
    return img
newQuery=getImage(sampleLocation)
while True:
    clock.tick(fps)
    coord=pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0,0,0))   
    screen.blit(newQuery,(0,0))
    pygame.display.flip()
    pygame.event.pump()

