from vpython import *
cena = canvas(width=500, height=300, align='center', background=color.cyan)
box()
while True:
    a = cena.waitfor('keydown')
    print(a.key)
    if a.event == 'keydown':
        cena.delete()
    if a.key == 'up':
        scene.delete()
        cena = canvas(width=500, height=300, align='center', background=color.cyan)
        sphere(texture=textures.earth)
    if a.key == 'down':
        scene.delete()
        cena = canvas(width=500, height=300, align='center', background=color.red)
        box(pos=vector(-3,0,0),
            color=color.magenta,
            emissive=True,
            )
    if a.key == 'right':
        scene.delete()
        cena = canvas(width=500, height=300, align='center', background=color.red)
        arrow(pos=vector(0,0,0),
              axis=vector(10,4,6),
              color=color.orange,
              oppacity=0.1,
              )
    if a.key == 'left':
        scene.delete()
        cena = canvas(width=500, height=300, align='center', background=color.red)
        cone(pos=vector(0,-10,0),
              radius=3,
              texture=textures.metal,
             axis=vector(10,4,6)
              )
    if a.key == 'shift':
        scene.delete()
        cena = canvas(width=500, height=300, align='center', background=color.red)
        pyramid(pos=vector(2,7,-1),
                axis=vector(0,-2,1),
                shiness=1,
                texture=textures.rock,

                )
    if a.key == 'tab':
        scene.delete()
        cena = canvas(width=500, height=300, align='center', background=color.red)
        cylinder(pos=vector(0, 3, -2),
                axis=vector(7, 7, 1),
                radius=2.8,
                shiness=1,
                color=vector(0.87,0.45,0.932),
                 )
    if a.key == 'ctrl':
        scene.delete()
        cena = canvas(width=500, height=300, align='center', background=color.red)
        ellipsoid(pos=vector(0, 0, 0),
                 size=vector(10,1,5),
                 shiness=1,
                 color=vector(0.875, 0.730, 0.980),
                 )
        ring(pos=vector(-2, -2, 0),
             thickness=0.5,
             radius=3,
             shiness=1,
             color=vector(0.875, 0.730, 0.980),
             )
        helix(pos=vector(0,0,0),
              axis=vector(-2,-2,0),
              radius=1,
              coils=20,
              color=color.black
              )
