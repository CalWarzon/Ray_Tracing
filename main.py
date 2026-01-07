import math as m
import os
import time as t
from readchar import readchar
map = [
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
  [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
  [0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1, 1, 0, 0, 1, 0],
  [0, 0, 0, 0, 1, 1, 0, 0, 1, 1],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
screenwidth = 44
screenlength = 22
brightness = 15
stepsize = 0.1
size = 40
brightness_levels1 = [' ','-','+','*','=','&','$','#','%','@']
brightness_levels2 = [' ',' ','░','░','▒','▒','▓','▓','█','█']
brightness_levels3 = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
brightness_levels = brightness_levels2
def printscreen(cords,direction,fov):
  x = cords[0]
  y = cords[1]
  screenx = []
  screeny = []
  for i in range(screenwidth):
    adjustdirection = direction - (fov/2) + ((fov/screenwidth) * i)
    distance = castray(x,y,adjustdirection)
    brighnessofpixel = round(brightness/distance)
    lengthofpixel = round(size/distance)
    if brighnessofpixel > 9:
      brighnessofpixel = 9
    if brighnessofpixel < 1:
      brighnessofpixel = 1
    if lengthofpixel > screenlength:
      lengthofpixel = screenlength
    screenx.append(brightness_levels[brighnessofpixel])
    screeny.append(lengthofpixel)
  distfromcenter = round(screenlength/2)
  for i in range(screenlength):
    screenrow = ''
    for i in range(screenwidth):
      if screeny[i]/2 > abs(distfromcenter):
        screenrow += screenx[i]
      else:
        screenrow += ' '
    print(screenrow)
    distfromcenter -= 1
def castray(playerx,playery,direction):
  xstep = m.cos(m.radians(direction))*stepsize
  ystep = m.sin(m.radians(direction))*stepsize
  x = playerx
  y = playery
  while True:
    x += xstep
    y += ystep
    testx = int(round(x))
    testy = int(round(y))
    if testx < 0 or testx > 9 or testy < 0 or testy > 9 or map[testy][testx] == 1:
      return m.sqrt((x - playerx) ** 2 + (y - playery) ** 2)
def attemptmove(xy,direction,speed):
  attemptmoveto = [xy[0] + (m.cos(m.radians(direction)) * speed), xy[1] + (m.sin(m.radians(direction)) * speed)]
  if attemptmoveto[0] < 0 or attemptmoveto[0] > 9 or attemptmoveto[1] < 0 or attemptmoveto[1] > 9 or map[round(attemptmoveto[1])][round(attemptmoveto[0])] == 1:
    return xy 
  else:
    return attemptmoveto
def normalize(angle):
  while angle > 360:
    angle -= 360
  while angle < 0:
    angle += 360
  return angle
def sfloat(num):
  try:
    return float(num)
  except:
    return 0
playercords = [0,0]
playerdirection = 0
fov = 80
turnspeed = 10
speed = 0.5
printscreen(playercords,playerdirection,fov)
while True:
  print(playercords)
  print(playerdirection)
  responce = readchar()
  nplayercords = playercords
  nplayerdirection = playerdirection
  if responce == 'w':
    nplayercords = attemptmove(playercords, playerdirection,speed)
  elif responce == 'd':
    nplayercords = attemptmove(playercords, normalize(playerdirection + 90),turnspeed)
  elif responce == 's':
    nplayercords = attemptmove(playercords, normalize(playerdirection + 180),speed)
  elif responce == 'a':
    nplayercords = attemptmove(playercords, normalize(playerdirection + 270),speed)
  elif responce == ',':
    nplayerdirection = normalize(playerdirection - turnspeed)
  elif responce[:10] == '.':
    nplayerdirection = normalize(playerdirection + turnspeed)
  frames = 1
  fulltime = 0.2
  for i in range(frames):
    framexy = [playercords[0] + (((nplayercords[0] - playercords[0])/frames) * i + 1),playercords[1] + ((nplayercords[1] - playercords[1])/frames) * i + 1]
    framed = playerdirection + (((nplayerdirection - playerdirection)/frames) * i + 1)
    os.system('clear')
    printscreen(framexy, framed, fov)
    t.sleep(fulltime/frames)
  playercords = nplayercords
  playerdirection = nplayerdirection