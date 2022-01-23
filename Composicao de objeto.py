from vpython import *
cabo = cylinder(size=vector(1.3,0.2,0.2),color=color.orange, pos=vector(0,0,0))
cabeca = box(size=vector(0.2,0.6,0.2), pos=vector(1.1,0,0),color=color.blue)

martelo = compound([cabo,cabeca])
martelo.axis=vector(-3,-2,4)