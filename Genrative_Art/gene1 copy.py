from p5 import *
def draw():
     background(255)
     no_stroke()

     # bright red
     fill(255, 0, 0)
     circle((72, 72), 58)

     # dark red
     fill(127, 0, 0)
     circle((144, 72), 58)

     # Pink (pale red)
     fill(255, 200, 200)
     circle((216, 72), 58)

if __name__ == '__main__':
    run()