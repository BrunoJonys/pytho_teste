import turtle

bruno = turtle.Turtle()
def poligono(t,n,linha):
    angulo = 360 / n
    for i in range(n):
        t.fd(linha)
        t.lt(angulo)
poligono(bruno,7,70)
turtle.mainloop()