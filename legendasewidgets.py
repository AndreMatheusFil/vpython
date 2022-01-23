from vpython import *
terra = sphere(texture=textures.earth,radius=10)
legenda = label(pos=terra.pos,
                text='Terra',
                xoffset=120,
                yoffset=120,
                box=True,
                border=1,
                color=color.blue,
                height=50,
                background=color.magenta,
                line=True,
                linecolor=color.cyan,
                linewidht=0.5
                )


def Botao(b):
    print('Olá!')

button(bind=Botao, text="Clique",color=color.white,background=color.black)

def Radio(r):
    print(r.text)

radio(bind=Radio, text='Azul')
radio(bind=Radio, text='Amarelo')
radio(bind=Radio, text='Vermelho')

def Check(c):
    if c.checked == True:
        terra.texture = textures.metal
    else:
        terra.texture = textures.earth

checkbox(bind=Check, text='Metal')

def Sld(s):
    print(s.value)

slider(bind=Sld, min=0, max=100, step=1, vertical=True, value= 50 )

def Menu(m):
    print(m.selected, m.index)
menu(bind=Menu, choices=['Macarrão','Pizza','Yakissoba','Sushi'])
def Texto(t):
    print(t.text,t.number)

winput(bind=Texto,text='Entre com um dado',width=130)

while True:
    a= scene.waitfor('mousedown')
    if a.event == 'mousedown':
        scene.delete()