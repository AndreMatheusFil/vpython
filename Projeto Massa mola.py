from vpython import *
import numpy as np

def f(r):
    global k, m
    x= r[0]
    Vx = r[1]

    dx = Vx
    dVx = -k.value * x/m.value

    return np.array([dx,dVx],float)

def passo_rk4(r,h):
    k1 = h*f(r)
    k2 = h *f(r + 0.5 * k1)
    k3 = h * f(r + 0.5 * k2)
    k4 = h * f(r + k3)
    return (k1 + 2 *(k2+k3)+k4)/6

def Rodar():
    global running
    running = not running
    if running:
        pausar.text = "Pausar"
    else:
        pausar.text = "Continuar"


def Massa(c):
    if c.checked:
        leg_caixa.visible = True
    else:
        leg_caixa.visible = False


def Mola(c):
    if c.checked:
        leg_mola.visible = True
    else:
        leg_mola.visible = False


def muda_original():
    global original, azul, vermelho, amarelo
    azul.checked = False
    vermelho.checked = False
    amarelo.checked = False
    caixa.color = color.cyan

def muda_azul():
    global original, azul, vermelho, amarelo
    original.checked = False
    vermelho.checked = False
    amarelo.checked = False
    caixa.color = color.blue

def muda_vermelho():
    global original, azul, vermelho, amarelo
    original.checked = False
    azul.checked = False
    amarelo.checked = False
    caixa.color = color.red

def muda_amarelo():
    global original, azul, vermelho, amarelo
    original.checked = False
    vermelho.checked = False
    azul.checked = False
    caixa.color = color.yellow

scene.background = vector(0.955,0.949,0.767)
scene.width = 1400
running = False
scene.bind("click",Rodar)
pausar = button(text="Rodar",bind=Rodar)
scene.append_to_caption("\n Legendas\n")
check1 = checkbox(bind=Massa,text="Massa",checked=True)
check2 = checkbox(bind=Mola,text="Mola",checked=True)
scene.append_to_caption("\n \n Mudança de cores\n")
original = radio(bind=muda_original,text="Original",checked=True)
azul = radio(bind=muda_azul,text="Azul",checked=False)
vermelho = radio(bind=muda_vermelho,text="Vermelho",checked=False)
amarelo = radio(bind=muda_amarelo,text="Amarelo",checked=False)

scene.append_to_caption("\n\nOpções\n")

scene.append_to_caption("  Constante Elástica ")
def const_elast(k):
    wts.text = f'{k.value}'
k = slider(min = 1, max = 100, value = 10, bind = const_elast, stap = 1 , lenght=100,width=10)
wts=wtext(text=f'{k.value}')

scene.append_to_caption("\n Números de voltas da mola")
def num_voltas(voltas):
    wtm1.text = f'{voltas.value}'
n_volta = slider(min=5,max = 20,value = 8,bind=num_voltas,step=1,lenght=100,width=10)
wtm1=wtext(text=f"{n_volta.value}")

scene.append_to_caption("\n Massa do bloco:")
def massa_bloco(massa):
    wtm2.text =  f'{massa.value}'
m = slider(min=0.1,max=10,value=1,bind=massa_bloco,step=1,lenght=100,width=10)
wtm2=wtext(text=f'{m.value}')
scene.append_to_caption("\n\n\n")




parede = box(pos=vector(-4.8,0,0),size=vector(0.4,4,2.5),texture=textures.wood_old)
mesa=box(pos=vector(0,-2,0),size=vector(10,0.4,2.5),texture=textures.wood)


def main():
    global mola, caixa, leg_mola, leg_caixa
    mola = helix(pos=vector(-4.8,-1.3,0),axis=vector(3.5,0,0),radius=0.4,coils=8,color=color.orange)
    leg_mola = label(pos=vector(-2.5,-0.5,0),text="Mola",color=color.black)
    liga = cylinder(pos=vector(-1.3,-1.3,0),axis=vector(0,0,0.4),radius=0.02,color=color.orange)
    fio = cylinder(pos=vector(-1.3,-1.3,0),axis=vector(0.2,0,0),radius=0.02,color=color.orange)
    caixa = box(pos=vector(-0.7,-1.3,0),size=vector(1,1,1),color=color.cyan)
    leg_caixa = label(pos= caixa.pos + vector(0,1,0),text = "Massa", color=color.black)
    v0 = float(input('Digite o valor da velocidade inicial: '))
    ra = np.array([0,v0])
    r = ra

    h = 0.05

    while True:
        if running:
            rate(25)
            dr = passo_rk4(r, h)
            r = r + dr

            mola.axis = vector(3.5+dr[0],0,0)
            leg_mola.pos = vector(-2.5 +dr[0],-0.5,0)
            liga.pos = vector(-1.3 +dr[0],-1.3,0)
            fio.pos = vector(-1.3 + dr[0],-1.3,0)
            caixa.pos = vector(-0.7 + dr[0],-1.3,0)
            leg_caixa.pos = caixa.pos + vector(0,1,0)
            mola.coils = n_volta.value
            mola.thickness = k.value/500
            liga.radius = k.value/1000
            fio.radius = k.value/1000



main()