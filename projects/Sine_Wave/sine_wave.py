from turtle import *
from math import *


A = 50      # Amplitude
B = 100     # WaveLength
C = 0       # Horizontal Shift
D = 0       # Vertical Shift

penup()
# As x increases y increases and decreases as it is evaluated.
for x in range(-200, 200):
    # Sine Wave Equation
    y = A * sin((2 * pi / B) * (x + C)) + D
    goto(x, y)
    pendown()

hideturtle()
mainloop()
