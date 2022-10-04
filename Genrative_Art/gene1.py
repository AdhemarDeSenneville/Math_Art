from p5 import *
from random import randint
import math

alfa = 45
w_ = 300
max_w = 100
min_w = 10


def setup():
    size(1000, 1000)
    no_stroke()
    background(0,0,0)
    colorMode("HSB")

def draw():
    rotate(alfa)
    rect_width = int(min_w + (max_w-min_w)*(math.sin()+1)//2)
    
    strokeWeight(randint(1,10))
    stroke(100,50,randint(0,255))
    line(randint(0,width), 0, randint(0,width), height)


run()