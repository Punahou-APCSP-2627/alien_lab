# IMPORTS

import py5
import py5_tools
import jpype
import time

count = 0

jpype.isJVMStarted() # allows py5 to use underlying Java

# SKETCH

def setup():
  py5.size(500, 500)
  

def draw():
  global count
  py5.background('#0B1033') #background

  py5.no_stroke()
  py5.fill(255, 255, 200)
  py5.circle(420, 80, 60) # making the moon


  py5.fill(255)
  if count < 30000:
    py5.circle(py5.random(0, 500), py5.random(0, 300), 2)
    py5.circle(py5.random(0, 500), py5.random(0, 300), 2)
    py5.circle(py5.random(0, 500), py5.random(0, 300), 2)
    py5.circle(py5.random(0, 500), py5.random(0, 300), 2)
    py5.circle(py5.random(0, 500), py5.random(0, 300), 2)
    py5.circle(py5.random(0, 500), py5.random(0, 300), 2)
    py5.circle(py5.random(0, 500), py5.random(0, 300), 2)
    py5.circle(py5.random(0, 500), py5.random(0, 300), 2)
    py5.circle(py5.random(0, 500), py5.random(0, 300), 2)
    py5.circle(py5.random(0, 500), py5.random(0, 300), 2)
    py5.circle(py5.random(0, 500), py5.random(0, 300), 2)
    py5.circle(py5.random(0, 500), py5.random(0, 300), 2)
    py5.circle(py5.random(0, 500), py5.random(0, 300), 2) # stars
    count += 1
  else:
    pass

  py5.ellipse(250, 250, 60, 200)

  py5.fill(120, 60, 160)
  py5.quad(0, 400, 500, 380, 500, 500, 0, 500) # ground

  py5.stroke(0, 100, 0)
  py5.stroke_weight(3)
  py5.fill(0, 255, 0)
  py5.ellipse(250, 300, 100, 160) # body

  py5.line(230, 370, 210, 420)
  py5.line(270, 370, 290, 420) # legs

  py5.fill(0, 200, 0) # head
  py5.circle(250, 170, 120)

  py5.fill(255, 150, 0) # antenna
  py5.triangle(230, 120, 220, 70, 245, 115)
  py5.triangle(270, 120, 280, 70, 255, 115)

  py5.fill(255)
  py5.circle(225, 160, 30) # eye shape
  py5.circle(275, 160, 30)
  py5.fill(0)
  py5.circle(225 + (py5.mouse_x - 250)/40, 160 + (py5.mouse_y - 250)/40, 12) # pupils
  py5.circle(275 + (py5.mouse_x - 250)/40, 160 + (py5.mouse_y - 250)/40, 12)

  py5.fill(255, 150, 100)
  py5.text_size(24)
  py5.text("Lebron James from the Philadelphia 76ers", 50, 470) # name

  py5.text_size(40)
  py5.text("🚀", py5.mouse_x - 20, py5.mouse_y + 15)
  py5.line(250, 175, py5.mouse_x, py5.mouse_y)
  py5.no_stroke

#run
py5.run_sketch()
py5_tools.screenshot()  