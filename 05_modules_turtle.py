import turtle            # permite usar as funções e objetos do módulo turtle
wn = turtle.Screen()     # cria uma janela gráfica
alex = turtle.Turtle()   # cria um turtle chamado alex
alex.forward(150)        # manda o alex se mover 150 unidades para frente
alex.left(90)            # roda de 90 graus para a esquerda
alex.forward(75)         # desenha o segundo lado do retângulo """

wn.bgcolor("green")         # define a cor de fundo da janela

tess = turtle.Turtle()
tess.color("blue")               # tess fica azul
tess.pensize(3)                  # define a espessura da caneta

tess.forward(50)
tess.left(120)
tess.forward(50)

wn.exitonclick()

""" import turtle
wn = turtle.Screen()             # Cria uma janela e define seus atributos
wn.bgcolor("lightgreen")


tess = turtle.Turtle()           # cria tess e define seus atributos
tess.color("hotpink")
tess.pensize(5)

alex = turtle.Turtle()           # cria alex

tess.forward(80)                 # tess desenha um triângulo equilátero
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)                   # complete o triângulo

tess.right(180)                  # tess muda de direção
tess.forward(80)                 # tess se move para longe da origem

alex.forward(50)                 # alex desenha um quadrado
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)

wn.exitonclick() """
